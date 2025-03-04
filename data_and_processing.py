import numpy as np
from typing import Callable
from pandas import DataFrame, Series, concat
from scipy import ndimage
from scipy.ndimage import label, uniform_filter1d
from scipy.interpolate import interp1d
from sklearn.neural_network import MLPClassifier
from scipy.signal import savgol_filter
from sklearn.preprocessing import StandardScaler
from scipy.signal import butter, sosfilt
from functools import wraps

ABSORPTION_LINE_WIDTH = 30


def scale_data_with_standard_scaler(data):
    """
    Масштабирует массив данных с помощью StandardScaler.
    """
    # Проверка входного массива
    if len(data.shape) == 1:  # Если данные одномерные, преобразуем в двумерные
        data = data.reshape(-1, 1)

    # Создание и применение StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    return scaled_data.flatten()


def normalize_energy(arr):
    """Нормализовать массив так, чтобы его энергия была равна 1."""
    norm = np.sqrt(np.sum(np.abs(arr) ** 2))
    # Добавляем проверку на нули, чтобы избежать деления на нуль
    return arr / norm if norm != 0 else arr


def split_into_windows(input_list: list, window_width: int) -> np.ndarray:
    """Разбивает список на перекрывающиеся окна заданной ширины и нормализует каждое окно."""
    # Проверяем, чтобы длина input_list была больше или равна window_width
    if len(input_list) < window_width:
        return np.array([])  # Возврат пустого массива, если список слишком мал
    windows = [input_list[i:i + window_width] for i in range(len(input_list) - window_width + 1)]
    return np.array(windows)


def interpolate_values(frequency, values, step=0.06):
    """
    Интерполирует значения (например, without_gas или with_gas) по частотам.

    :param frequency: Исходные значения частот (список или Series).
    :param values: Исходные значения (например, without_gas или with_gas).
    :param step: Шаг интерполяции, по умолчанию 1.

    :return: Интерполированные значения.
    """
    # Преобразуем входные данные в numpy массивы
    frequency = np.asarray(frequency)
    values = np.asarray(values)
    # Проверка, чтобы частоты и значения не были пустыми
    if len(frequency) == 0 or len(values) == 0:
        raise ValueError("Частоты и значения не могут быть пустыми.")
    # Вычисляем новый диапазон частот
    min_freq, max_freq = frequency.min(), frequency.max()
    new_frequencies = np.arange(min_freq, max_freq + step, step)
    # Создаем интерполятор
    interpolator = interp1d(frequency, values, kind="linear", fill_value="extrapolate")
    # Интерполируем данные для нового диапазона частот
    new_gamma = interpolator(new_frequencies)
    return new_frequencies, new_gamma


def spectra_will_be_changed(method):
    """Декоратор для вызова __spectra_interceptor после выполнения метода"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        interceptor_attr = '_DataAndProcessing__spectra_interceptor'
        if hasattr(self, interceptor_attr) and callable(getattr(self, interceptor_attr)):
            getattr(self, interceptor_attr)(method.__name__, *args, **kwargs)
        return result
    return wrapper


def absorption_will_be_changed(method):
    """Декоратор для вызова __absorption_interceptor после выполнения метода"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        interceptor_attr = '_DataAndProcessing__absorption_interceptor'
        if hasattr(self, interceptor_attr) and callable(getattr(self, interceptor_attr)):
            getattr(self, interceptor_attr)(method.__name__, *args, **kwargs)
        return result
    return wrapper


class DataAndProcessing:
    # __slots__ это механизм, ограничивающий объекту возможность динамически добавлять новые атрибуты. По умолчанию dict
    # переопределив __slots__, удаляется __dict__, и объект может иметь только строго заданные атрибуты.
    # Защита от изменений полей вне методов класса (изменять значение полей можно только через методы данного класса)
    __slots__ = (
        '__spectra_interceptor', '__spectra', '__point_absorption', '__neural_network', '__smoothed_noise',
        '__absorption_interceptor'
    )
    # Константы для инициализации пустых DataFrame
    DEFAULT_SPECTROMETER_DATA = DataFrame(columns=["frequency", "without_gas", "with_gas"])
    DEFAULT_POINT_ABSORPTION = DataFrame(columns=["frequency", "gamma", "status", "source_neural_network"])

    def __init__(self):
        # Функция-перехватчик, вызываемая после выполнения метода
        self.__spectra_interceptor: Callable = lambda method_name, *args, **kwargs: None
        self.__absorption_interceptor: Callable = lambda method_name, *args, **kwargs: None
        # Данные со спектрометра
        self.__spectra = self.DEFAULT_SPECTROMETER_DATA.copy()
        # Точки, соответствующие линиям поглощения
        self.__point_absorption = self.DEFAULT_POINT_ABSORPTION.copy()
        # Нейронная сеть
        self.__neural_network: MLPClassifier | None = None
        self.__smoothed_noise = None

    # ---------------------------------------------------------------------------
    #   Функция-перехватчик, вызываемая после выполнения методов класса.
    # ---------------------------------------------------------------------------
    def set_spectra_interceptor(self, func: Callable) -> None:
        """Устанавливает функцию, которая будет вызываться при вызове метода изменяющего спектр."""
        self.__spectra_interceptor = func

    def set_absorption_interceptor(self, func: Callable) -> None:
        """Устанавливает функцию, которая будет вызываться при вызове метода изменяющего частоты поглощения."""
        self.__absorption_interceptor = func

    # ---------------------------------------------------------------------------
    #   Очистка данных
    # ---------------------------------------------------------------------------
    @spectra_will_be_changed
    def clear_data_from_spectrometer(self):
        """Очищает данные спектрометра."""
        self.__spectra = self.DEFAULT_SPECTROMETER_DATA.copy()

    @spectra_will_be_changed
    def clear_point_absorption(self):
        """Очищает таблицу точек поглощения."""
        self.__point_absorption = self.DEFAULT_POINT_ABSORPTION.copy()

    @spectra_will_be_changed
    def clear_data(self):
        """Очищает все данные (оставляя нейронную сеть)"""
        self.clear_data_from_spectrometer()
        self.clear_point_absorption()

    # ---------------------------------------------------------------------------
    #   Setters - запись данных
    # ---------------------------------------------------------------------------
    @spectra_will_be_changed
    def set_spectrum_with_substance(self, frequency: list | Series, gamma: list | Series):
        """Добавляет данные в колонку 'with_gas' таблицы спектрометра."""
        if len(frequency) != len(gamma):
            raise ValueError("Количество частот не совпадает с количеством гамм")

        # Преобразуем входные данные
        frequency, gamma = interpolate_values(frequency, gamma)

        cutoff_frequency = 0.1
        sos = butter(3, cutoff_frequency, btype="highpass", analog=False, output="sos")
        noise = sosfilt(sos, gamma)
        self.__smoothed_noise = np.std(uniform_filter1d(noise, size=3)) * 5
        print(self.__smoothed_noise)
        # self.__spectra["with_gas"] = self.__smoothed_noise

        gamma = savgol_filter(gamma, window_length=10, polyorder=2)
        # Интерполяция значений без газа
        interpolated_frequencies, interpolated_gamma = interpolate_values(frequency, gamma)
        # Частота пуста - данных не было - задаем
        if self.__spectra["frequency"].empty:
            self.__spectra["frequency"] = interpolated_frequencies
            self.__spectra["with_gas"] = interpolated_gamma
        else:
            # Частота задана, проверяем что они совпадают
            if len(self.__spectra["frequency"].values) != len(interpolated_frequencies):
                raise ValueError("Частоты старых значений и новых не совпадают")
            self.__spectra["with_gas"] = interpolated_gamma

    @spectra_will_be_changed
    def set_spectrum_without_substance(self, frequency: list | Series, gamma: list | Series):
        """Добавляет данные в колонку 'without_gas' таблицы спектрометра."""
        if len(frequency) != len(gamma):
            raise ValueError("Количество частот не совпадает с количеством гамм")
        # Преобразуем входные данные
        gamma = savgol_filter(gamma, window_length=10, polyorder=2)
        frequency, gamma = interpolate_values(frequency, gamma)
        # Интерполяция значений без газа
        interpolated_frequencies, interpolated_gamma = interpolate_values(frequency, gamma)
        # Частота пуста - данных не было - задаем
        if self.__spectra["frequency"].empty:
            self.__spectra["frequency"] = interpolated_frequencies
            self.__spectra["without_gas"] = interpolated_gamma
        else:
            # Частота задана, проверяем что они совпадают
            if len(self.__spectra["frequency"].values) != len(interpolated_frequencies):
                raise ValueError("Частоты старых значений и новых не совпадают")
            self.__spectra["without_gas"] = interpolated_gamma

    @spectra_will_be_changed
    def set_neural_network(self, neural_network: MLPClassifier) -> None:
        self.__neural_network: MLPClassifier = neural_network

    # ---------------------------------------------------------------------------
    #   Getters - получение данных
    # ---------------------------------------------------------------------------
    def get_neural_network(self) -> DataFrame | None:
        return self.__neural_network

    def get_neural_network_info(self) -> tuple[int, int]:
        """
        Возвращает информацию о количестве входов и скрытых слоев нейронной сети.

        Returns
        -------
        tuple[int, int]
            Кортеж, содержащий:
            - Количество входов
            - Количество скрытых слоев
        """
        num_inputs = self.__neural_network.n_features_in_
        hidden_layer_sizes = self.__neural_network.hidden_layer_sizes
        return num_inputs, hidden_layer_sizes

    def get_spectra(self) -> DataFrame:
        return self.__spectra

    def get_point_absorption(self) -> DataFrame:
        return self.__point_absorption

    # ---------------------------------------------------------------------------
    #   Обработка данных
    # ---------------------------------------------------------------------------
    @spectra_will_be_changed
    @absorption_will_be_changed
    def processing(self, filling_blanks=True):
        # Проверка наличия данных и нейронной сети
        if self.__spectra["with_gas"].empty:
            raise ValueError("Для обработки отсутствуют данные с веществом")
        if self.__neural_network is None:
            raise ValueError("Для обработки отсутствует нейронная сеть")

        # Очистка прошлых результатов
        self.clear_point_absorption()

        # Определение количества входов в нейронную сеть
        num_inputs = self.__neural_network.n_features_in_

        # Подготовка окон для нейронной сети
        gamma = scale_data_with_standard_scaler(self.__spectra["with_gas"].values)
        windows = split_into_windows(gamma, num_inputs)

        # Проверка наличия окон
        if len(windows) == 0:
            raise ValueError(
                "Недостаточно данных для анализа нейронной сетью. Проверьте параметры окон или количество данных."
            )

        # Предсказание нейронной сети
        result = self.__neural_network.predict(windows)

        # Добавление нулей на края для выравнивания длины
        result = np.pad(result, (len(self.__spectra["with_gas"]) - len(result)) // 2, mode="constant")

        # Устранение "дыр" в результатах, если требуется
        if filling_blanks:
            result = ndimage.binary_erosion(
                ndimage.binary_dilation(result, iterations=ABSORPTION_LINE_WIDTH // 2),
                iterations=ABSORPTION_LINE_WIDTH // 4,
            )

        # Обработка групп подряд идущих единиц
        labeled_array, num_features = label(result)
        indices = []

        for group_label in range(1, num_features + 1):
            # Находим индексы текущей группы
            group_indices = np.where(labeled_array == group_label)[0]
            # Выбираем индекс элемента с максимальным значением 'with_gas'
            max_index = group_indices[np.argmax(self.__spectra.loc[group_indices, "with_gas"].values)]
            indices.append(max_index)

        # Проверка разницы между with_gas и without_gas
        # хай пас фильтр на 5 точек, с очень большой частотой отсечки
        if not self.__spectra["without_gas"].empty and not self.__spectra["without_gas"].isna().all():
            # Фильтрация точек, где разница положительна и превышает отклонение
            indices = [
                idx for idx in indices
                if self.__spectra.loc[idx, "with_gas"] - self.__spectra.loc[idx, "without_gas"] > self.__smoothed_noise
            ]

        # Формирование результата
        self.__point_absorption = DataFrame({
            "frequency": self.__spectra.loc[indices, "frequency"].values,
            "gamma": self.__spectra.loc[indices, "with_gas"].values,
            "status": None,
            "source_neural_network": True
        })

    # ---------------------------------------------------------------------------
    #   Методы для работы с графиком
    # ---------------------------------------------------------------------------
    def get_status_point_absorption(self, frequency: float, gamma: float):
        """Возвращает индекс, статус и источник точки поглощения с заданными координатами."""
        mask = (self.__point_absorption["frequency"] == frequency) & (self.__point_absorption["gamma"] == gamma)
        result = self.__point_absorption.loc[mask, ["status", "source_neural_network"]]
        if not result.empty:
            index = result.index[0]
            status = result.iloc[0]["status"]
            source_neural_network = result.iloc[0]["source_neural_network"]
            return index, status, source_neural_network
        return None, None, None

    @absorption_will_be_changed
    def set_status_point_absorption_by_index(self, index: int, new_status: bool):
        """Обновляет статус для точки поглощения по индексу."""
        if 0 <= index < len(self.__point_absorption):
            self.__point_absorption.loc[index, "status"] = new_status

    @absorption_will_be_changed
    def set_status_point_absorption_by_coordinates(self, frequency: float, gamma: float, new_status: bool):
        """Обновляет статус для точки поглощения по координатам."""
        mask = (self.__point_absorption["frequency"] == frequency) & (self.__point_absorption["gamma"] == gamma)
        self.__point_absorption.loc[mask, "status"] = new_status

    @absorption_will_be_changed
    def add_new_point_absorption(self, frequency: float, gamma: float):
        """Метод добавляет новую точку поглощения с заданными координатами."""
        new_point = DataFrame({
            "frequency": [frequency],
            "gamma": [gamma],
            "status": [True],
            "source_neural_network": [False]
        })
        self.__point_absorption = concat([self.__point_absorption, new_point], ignore_index=True)
        self.__point_absorption.sort_values(by="frequency", inplace=True, ignore_index=True)

    @absorption_will_be_changed
    def del_point_absorption(self, frequency: float, gamma: float):
        """Удаляет точку поглощения, если она была добавлена в ручную"""
        mask = (self.__point_absorption["frequency"] == frequency) & (self.__point_absorption["gamma"] == gamma)
        to_delete = self.__point_absorption[mask & (self.__point_absorption["source_neural_network"] == False)]
        if not to_delete.empty:
            self.__point_absorption = self.__point_absorption.drop(to_delete.index).reset_index(drop=True)

    @absorption_will_be_changed
    def del_point_absorption_by_index(self, index: int):
        """Удаляет точку поглощения по индексу, если она была добавлена вручную"""
        if 0 <= index < len(self.__point_absorption):
            if not self.__point_absorption.loc[index, "source_neural_network"]:
                self.__point_absorption = self.__point_absorption.drop(index).reset_index(drop=True)
