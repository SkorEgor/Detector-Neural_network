import os

from joblib import load
from functools import partial
from pyqtgraph.Qt.QtCore import QSettings
from pyqtgraph.Qt.QtWidgets import QFileDialog, QTableWidgetItem

from detector_neural_network import setting
from detector_neural_network.app_exception import AppException
from detector_neural_network.custom_dialog import CustomDialog
from detector_neural_network.parser import parser, parser_all_data
from detector_neural_network.multi_check_box import BlueRedYellowCheckBox, GreenRedYellowCheckBox
from detector_neural_network.plot_spectrometer_data import SpectrometerPlotAndLegendWidget, SpectrometerPlotWidget
from detector_neural_network.setting import (
    DEFAULT_FILE_PATH_WITHOUT_SUBSTANCE,
    DEFAULT_FILE_PATH_WITH_SUBSTANCE,
    DEFAULT_FILE_PATH_NEURAL_NETWORK,
)

settings = QSettings(setting.ORGANIZATION, setting.APPLICATION)


class GuiProgram(CustomDialog):
    """
    Класс логики приложения
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Обработчики нажатий кнопок интерфейса
        # - Загрузка нейронной сети
        self.pushButton_reading_file_neural_network.clicked.connect(self.loading_neural_network)
        # - Загрузка данных без вещества
        self.pushButton_reading_file_no_gas.clicked.connect(self.reading_and_plotting_data_without_substance)
        # - Загрузка данные с веществом
        self.pushButton_reading_file_with_gas.clicked.connect(self.reading_and_plotting_data_with_substance)
        # - Смена режима чтения и отображения файлов
        self.radioButton_all_range.clicked.connect(self.change_spectrum_range)
        self.radioButton_selected_range.clicked.connect(self.change_spectrum_range)
        # - Очистка данных спектров
        self.pushButton_reset_spectrum_data.clicked.connect(self.reset_spectrum_data)
        # - Обработка нейронной сетью
        self.pushButton_menu_calculate.clicked.connect(self.processing)

        # Объект графика №1 для отображения данных DataAndProcessing
        self.plot_widget_1 = SpectrometerPlotAndLegendWidget(
            absorption_click_callback=self.absorption_point_handler,
            with_gas_click_callback=self.with_gas_point_handler,
        )
        self.layout_plot_1.addWidget(self.plot_widget_1)
        # Устанавливаем метод вызываемый при обновлении частот поглощения
        self.data.set_absorption_interceptor(self.update_ui_on_absorption_change)

        # Таблица
        # - Фильтр
        self.comboBox_select_table_view.currentIndexChanged.connect(self.table)
        # - Инициализация пустой таблицы с заголовками
        self.initialize_table()
        # - Сохранить данные из таблицы в файл
        self.pushButton_save_table_to_file.clicked.connect(self.saving_result_data)
        # - Загрузить данные в таблицу из файла
        self.pushButton_load_result.clicked.connect(self.load_result_data)
        # - Выбрана строка таблицы zoom
        self.tableWidget_frequency_absorption.cellClicked.connect(self.get_clicked_cell)
        self.comboBox_select_table_view.currentIndexChanged.connect(self.table)
        # # - Выбран заголовок таблицы
        # self.tableWidget_frequency_absorption.horizontalHeader().sectionClicked.connect(self.click_handler)

    # ---------------------------------------------------------------------------
    #   Алгоритм работы приложения
    # ---------------------------------------------------------------------------
    def loading_neural_network(self):
        """Загрузка нейронной сети"""
        # 1. Получение имени файла из диалогового окна (в режиме DEBUG используется путь по умолчанию)
        if setting.DEBUG_ALL or setting.USE_DEFAULT_FILE_PATH_NEURAL_NETWORK:
            self.file_name_neural_network = setting.DEFAULT_FILE_PATH_NEURAL_NETWORK
        else:
            # - Загружаем последнюю успешную директорию, если она есть, иначе используем текущую (".")
            last_dir = settings.value("last_neural_network_dir", DEFAULT_FILE_PATH_NEURAL_NETWORK, type=str)
            self.file_name_neural_network, _ = QFileDialog.getOpenFileName(
                self,
                """Выбрать файл "Нейронной сети" """,
                last_dir,
                "Neural network(*.joblib);;All Files(*)",
            )
        # - Если диалог закрыт через крестик или отменён, просто выходим
        if not self.file_name_neural_network:
            return
        # 2. Загрузка модели
        self.data.set_neural_network(load(self.file_name_neural_network))
        # 3. Получение количества входов и скрытых слоев, отображение в UI
        num_inputs, hidden_layer_sizes = self.data.get_neural_network_info()
        self.label_parameters_neural_network.setText(f"Кол-во вх: {num_inputs}\nРазмеры слоев: {hidden_layer_sizes}")
        # - Сохранение директории для следующего открытия диалога
        settings.setValue("last_neural_network_dir", os.path.dirname(self.file_name_neural_network))

    def reading_and_plotting_data_without_substance(self, skip_read=False):
        """Чтение и построение сигнала без вещества"""
        # 1. Чтения файла (если файл тот же - пропускаем)
        if not skip_read:
            # Получение имени файла из диалогового окна (в режиме DEBUG используется путь по умолчанию)
            if setting.DEBUG_ALL or setting.USE_DEFAULT_FILE_PATH_WITHOUT_SUBSTANCE:
                self.file_name_without_substance = setting.DEFAULT_FILE_PATH_WITHOUT_SUBSTANCE
            else:
                # - Загружаем последнюю успешную директорию, если она есть, иначе используем текущую (".")
                last_dir = settings.value("last_without_substance_dir", DEFAULT_FILE_PATH_WITHOUT_SUBSTANCE, type=str)
                self.file_name_without_substance, _ = QFileDialog.getOpenFileName(
                    self,
                    "Выбрать файл 'Данные без вещества'",
                    last_dir,
                    "Spectrometer Data(*.csv);;All Files(*)",
                )
            # - Если диалог закрыт через крестик или отменён, просто выходим
            if not self.file_name_without_substance:
                return
            # Чтение данных
            with open(self.file_name_without_substance) as file:
                self.lines_file_without_gas = file.readlines()
        # - Если файл не прочитан - скип
        if not self.lines_file_without_gas:
            return
            # 2. В зависимости от режима - парсим
        if self.radioButton_selected_range.isChecked():
            # Запрашиваем начало и конец диапазона спектра, из UI с валидацией
            start_frequency, end_frequency = self.get_spectrum_frequency_range()
            # Парс данных в заданных частотах
            frequency, gamma = parser(self.lines_file_without_gas, start_frequency, end_frequency)
        else:
            # Парс данных
            frequency, gamma = parser_all_data(self.lines_file_without_gas)
        # 3. Сохраняем данных
        self.data.set_spectrum_without_substance(frequency, gamma)
        # 4. Отображаем данные на графике
        self.update_graphics()
        # - Сохранение директории для следующего открытия диалога
        settings.setValue("last_without_substance_dir", os.path.dirname(self.file_name_without_substance))

    def reading_and_plotting_data_with_substance(self, skip_read=False):
        """Чтение и построение сигнала с веществом"""
        # 1. Чтения файла (если файл тот же - пропускаем)
        if not skip_read:
            # Получение имени файла из диалогового окна (в режиме DEBUG используется путь по умолчанию)
            if setting.DEBUG_ALL or setting.USE_DEFAULT_FILE_PATH_WITH_SUBSTANCE:
                self.file_name_with_substance = setting.DEFAULT_FILE_PATH_WITH_SUBSTANCE
            else:
                # - Загружаем последнюю успешную директорию, если она есть, иначе используем текущую (".")
                last_dir = settings.value("last_with_substance_dir", DEFAULT_FILE_PATH_WITH_SUBSTANCE, type=str)
                self.file_name_with_substance, _ = QFileDialog.getOpenFileName(
                    self,
                    "Выбрать файл 'Данные c веществом'",
                    last_dir,
                    "Spectrometer Data(*.csv);;All Files(*)",
                )
            # - Если диалог закрыт через крестик или отменён, просто выходим
            if not self.file_name_with_substance:
                return
            # Чтение данных
            with open(self.file_name_with_substance) as file:
                self.lines_file_with_gas = file.readlines()
        # - Если файл не прочитан - скип
        if not self.lines_file_with_gas:
            return
        # 2. В зависимости от режима - парсим
        if self.radioButton_selected_range.isChecked():
            # Запрашиваем начало и конец диапазона спектра, из UI с валидацией
            start_frequency, end_frequency = self.get_spectrum_frequency_range()
            # Парс данных в заданных частотах
            frequency, gamma = parser(self.lines_file_with_gas, start_frequency, end_frequency)
        else:
            # Парс данных
            frequency, gamma = parser_all_data(self.lines_file_with_gas)
        # 3. Сохраняем данных
        self.data.set_spectrum_with_substance(frequency, gamma)
        # 4. Отображаем данные на графике
        self.update_graphics()
        # - Сохранение директории для следующего открытия диалога
        settings.setValue("last_with_substance_dir", os.path.dirname(self.file_name_with_substance))

    def change_spectrum_range(self):
        """Вызов при обновлении диапазона спектра - Очищает, отображает данные в актуальном диапазоне"""
        spectra = self.data.get_spectra()
        update_with_gas = not (spectra["with_gas"].empty or spectra["with_gas"].isna().all())
        update_without_gas = not (spectra["without_gas"].empty or spectra["without_gas"].isna().all())
        self.data.clear_data()
        if update_with_gas:
            self.reading_and_plotting_data_with_substance(True)
        if update_without_gas:
            self.reading_and_plotting_data_without_substance(True)
        self.table()

    def reset_spectrum_data(self):
        """Сброс данных спектра"""
        self.data.clear_data()
        self.update_graphics()
        self.table()

    def processing(self):
        """Поиск линий поглощения"""
        spectra = self.data.get_spectra()
        if spectra["with_gas"].empty or spectra["with_gas"].isna().all():
            raise AppException("""Ошибка при "Вычислении" """, """Нет данных с веществом """)
        if not self.data.get_neural_network():
            raise AppException("""Ошибка при "Вычислении" """, """Нет нейронной сети """)
        # обработка
        self.data.processing()

    # ---------------------------------------------------------------------------
    #   Методы для работы с графиком
    # ---------------------------------------------------------------------------
    def update_graphics(self):
        """Обновить график."""
        self.plot_widget_1.plot_widget.plot_spectrometer_data(self.data)

    def absorption_point_handler(self, widget: SpectrometerPlotWidget, plot, points):
        """Обработчик клика по точкам поглощения"""
        for point in points:
            x, y = point.pos()
            # Получаем текущий статус
            index, status, source_neural_network = self.data.get_status_point_absorption(x, y)
            if index is None:
                return
            # Если точку поставили в ручную - удаляем
            if not source_neural_network:
                self.data.del_point_absorption_by_index(index)
                return
            # Если точку от нейронной сети - определяем новый статус и цвет
            if status is None:
                new_status = True
            elif status:
                new_status = False
            else:
                new_status = None
            # Обновляем статус в данных
            self.data.set_status_point_absorption_by_index(index, new_status)

    def with_gas_point_handler(self, widget: SpectrometerPlotWidget, plot, points):
        """Обработчик клика по точкам 'with_gas'."""
        for point in points:
            x, y = point.pos()
            # Проверяем, есть ли точка в точках поглощения
            index, _, _ = self.data.get_status_point_absorption(x, y)
            # Точки нет – добавляем
            if index is None:
                self.data.add_new_point_absorption(x, y)

    # ---------------------------------------------------------------------------
    #   Методы для работы с таблицей
    # ---------------------------------------------------------------------------
    def initialize_table(self):
        """Инициализация: Пустая таблица"""
        self.tableWidget_frequency_absorption.clear()
        self.tableWidget_frequency_absorption.setColumnCount(4)
        self.tableWidget_frequency_absorption.setHorizontalHeaderLabels(["Частота МГц", "Гамма", ""])
        self.tableWidget_frequency_absorption.setColumnHidden(3, True)  # Скрываем столбец с индексом
        self.tableWidget_frequency_absorption.resizeColumnToContents(2)

    def table(self):
        """Отобразить точки поглощения в таблице с фильтрацией и форматированием."""
        # Получаем данные точек поглощения
        point_absorption = self.data.get_point_absorption()
        if point_absorption.empty:
            # Если данных нет - очищаем таблицу
            self.tableWidget_frequency_absorption.setRowCount(0)
            return

        # Устанавливаем начальное количество строк
        self.tableWidget_frequency_absorption.setRowCount(len(point_absorption))

        # Получаем текущий выбранный фильтр
        filter_index = self.comboBox_select_table_view.currentIndex()

        # Счетчик видимых строк
        visible_row = 0

        # Обрабатываем каждую строку данных
        for frequency, gamma, status, source, index in zip(
            point_absorption["frequency"],
            point_absorption["gamma"],
            point_absorption["status"],
            point_absorption["source_neural_network"],
            point_absorption.index.to_list(),
        ):
            # Применяем фильтр отображения
            # - Все
            if filter_index == 0:  # Все
                pass
            # - Под вопросом
            elif filter_index == 1 and status is None:
                pass
            # - Отклоненные
            elif filter_index == 2 and status is False:
                pass
            # - Подтвержденные
            elif filter_index == 3 and status is True and source:
                pass
            # - Добавленные вручную
            elif filter_index == 4 and status is True and not source:
                pass
            else:
                continue

            # Заполняем ячейки частоты, гаммы, индекса
            self.tableWidget_frequency_absorption.setItem(visible_row, 0, QTableWidgetItem(f"{frequency:.3f}"))
            self.tableWidget_frequency_absorption.setItem(visible_row, 1, QTableWidgetItem(f"{gamma:.7E}"))
            self.tableWidget_frequency_absorption.setItem(visible_row, 3, QTableWidgetItem(str(index)))
            # Создаем и настраиваем чекбокс для столбца статуса
            checkbox_class = GreenRedYellowCheckBox if source else BlueRedYellowCheckBox
            check_box = checkbox_class(initial_state=status, icon_size=22, allow_none=source)
            check_box.clicked.connect(partial(self.frequency_selection, check_box, index, source))
            self.tableWidget_frequency_absorption.setCellWidget(visible_row, 2, check_box)
            # Устанавливаем высоту текущей строки
            self.tableWidget_frequency_absorption.setRowHeight(visible_row, 26)
            visible_row += 1

        # Устанавливаем окончательное количество видимых строк
        self.tableWidget_frequency_absorption.setRowCount(visible_row)

        # Настраиваем внешний вид таблицы
        self.tableWidget_frequency_absorption.setColumnWidth(2, 30)  # Ширина столбца с чекбоксом

    def frequency_selection(self, sender: GreenRedYellowCheckBox | BlueRedYellowCheckBox, index, source, checked):
        """Клик по чекбоксу в таблице"""
        # Нет точек поглощения - сброс
        if self.data.get_point_absorption().empty:
            return
        # Точка от нейронной сети -> меняем состояние в данных и обновляем график
        if source:
            self.data.set_status_point_absorption_by_index(index, sender.state)
        # Точка поставленная руками -> удаляем из данных, обновляем график
        else:
            self.data.del_point_absorption_by_index(index)

    def get_clicked_cell(self, row):
        """Клик по строке таблице - zoom к указанной области графика или к зоне с линиями поглощения"""
        # Нет исходных данных - сброс
        if self.data.get_spectra().empty:
            return
        # Получаем необходимые данные
        # * Спектр
        spectra = self.data.get_spectra()
        # * Точки поглощения
        point_absorption = self.data.get_point_absorption()
        # * Индекс точки к которой необходим zoom
        index_data = int(self.tableWidget_frequency_absorption.item(row, 3).text())
        # * Ширина окна просмотра
        window_width: float = self.get_window_width()
        frequency_left_or_right = window_width / 2

        # Находим границы области
        # * По x
        frequency_peak = point_absorption["frequency"].loc[index_data]
        x_min = frequency_peak - frequency_left_or_right
        x_max = frequency_peak + frequency_left_or_right
        # * По y
        mask = spectra["frequency"].between(x_min, x_max)
        y_values = spectra["with_gas"][mask]
        if not y_values.empty:
            y_min = y_values.min()
            y_max = y_values.max()
        # Если данных в диапазоне нет, берем общий min/max для "with_gas"
        else:
            y_min = spectra["with_gas"].min()
            y_max = spectra["with_gas"].max()

        # zoom
        self.plot_widget_1.plot_widget.zoom_to_region(x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max)

    # ---------------------------------------------------------------------------
    #   Методы для сохранения и загрузки результата в файл
    # ---------------------------------------------------------------------------
    def saving_result_data(self):
        """Сохранение результатов/таблицы в файл"""
        point_absorption = self.data.get_point_absorption()
        if self.data.get_spectra().empty:
            raise AppException("Ошибка 'Сохранения'", "Нет данных")

        # Загружаем последнюю успешную директорию, если она есть, иначе используем текущую (".")
        last_dir = settings.value("result_dir", ".", type=str)
        # - Формируем имя файла и добавляем путь
        base_name = os.path.splitext(os.path.basename(self.file_name_with_substance))[0]
        recommended_file_name = os.path.join(last_dir, f"Result_for_{base_name}")
        # - Загрузка
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Сохранение", recommended_file_name, "Text(*.txt);;Spectrometer Data(*.csv);;All Files(*)"
        )
        # - Если диалог закрыт через крестик или отменён, просто выходим
        if not file_name:
            return

        # Запись
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                # Заголовок
                file.write("FREQUENCY:\tGAMMA:\tSOURCE_NEURAL_NETWORK:\n")
                # Запись только подтвержденных данных (status=True)
                filtered_data = point_absorption[point_absorption["status"] == True]
                for row in filtered_data[["frequency", "gamma", "source_neural_network"]].itertuples(index=False):
                    file.write(f"{row.frequency}\t{row.gamma}\t{row.source_neural_network}\n")
                # Разделитель и статистика
                file.write("***********************************************************\n")
                nn_data = point_absorption[point_absorption["source_neural_network"] == True]
                stats = {
                    "RESULTS_FORMATTER_VERSION": setting.RESULTS_FORMATTER_VERSION,
                    "Обнаружено": nn_data.shape[0],
                    "Подтверждено": nn_data[nn_data["status"] == True].shape[0],
                    "Отклонено": nn_data[nn_data["status"] == False].shape[0],
                    "Непроверенно": nn_data[nn_data["status"].isna()].shape[0],
                    "Добавлено вручную": point_absorption[point_absorption["source_neural_network"] == False].shape[0],
                    "Всего": point_absorption.shape[0],
                }
                file.write("\n".join(f"{key}: {value}" for key, value in stats.items()) + "\n")
            # Сохраняем директорию выбранного файла как последнюю успешную
            settings.setValue("result_dir", os.path.dirname(file_name))
        except IOError as e:
            raise AppException("Ошибка записи файла", str(e))

    def load_result_data(self):
        """Чтение данных из файла результата и загрузка в точки поглощения"""
        if self.data.get_spectra().empty:
            raise AppException("Ошибка 'Загрузки'", "Нет исходных данных спектров.")
        # Загружаем последнюю успешную директорию, если она есть, иначе текущую
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Открыть файл результата",
            settings.value("result_dir", ".", type=str),
            "Text(*.txt);;Spectrometer Data(*.csv);;All Files(*)",
        )
        # - Если файл не выбран, выходим
        if not file_name:
            return

        try:
            with open(file_name, "r", encoding="utf-8") as file:
                data = [
                    (float(freq), float(gam), src.lower() == "true")
                    for line in file
                    if "\t" in line and not line.startswith(("FREQ", "*"))
                    for freq, gam, src in [line.strip().split("\t")]
                ]
                if not data:
                    raise AppException("Ошибка чтения", "Нет данных точек поглощения")

                freq, gamma, src_nn = zip(*data)
                self.data.set_point_absorption(freq, gamma, [True] * len(freq), src_nn)
                settings.setValue("result_dir", os.path.dirname(file_name))

        except (IOError, ValueError) as error:
            raise AppException("Ошибка файла", str(error))

    # ---------------------------------------------------------------------------
    #   Методы для работы со статистикой
    # ---------------------------------------------------------------------------
    def update_statistics(self):
        """Метод агрегирует данные статистики и отображает под таблицей в UI"""
        point_absorption = self.data.get_point_absorption()
        if point_absorption.empty:
            return

        # Фильтр строк, где source_neural_network=True
        filtered_neuron_found = point_absorption[point_absorption["source_neural_network"] == True]
        # Количество строк, где source_neural_network=True
        points_neuron_found = filtered_neuron_found.shape[0]
        # Количество строк, где source_neural_network=True и status=True
        points_confirmed = filtered_neuron_found[filtered_neuron_found["status"] == True].shape[0]
        # Процент выбранных
        percent_chosen = 0 if points_neuron_found == 0 else points_confirmed / points_neuron_found
        # Фильтр строк, где status=True
        filtered_absorption_lines = point_absorption[point_absorption["status"] == True]
        # Всего найденных частот поглощения
        number_absorption_lines = filtered_absorption_lines.shape[0]
        # Строки статистики
        text_statistics = (
            f"Одобрено {points_confirmed} из {points_neuron_found} ( {percent_chosen:.2%} ) \n"
            f"Всего частот поглощения: {number_absorption_lines}"
        )
        # Вывод в label под таблицей
        self.label_statistics_on_selected_frequencies.setText(text_statistics)

    # ---------------------------------------------------------------------------
    #   Методы вызываемый при обновлении частот поглощения
    # ---------------------------------------------------------------------------
    def update_ui_on_absorption_change(self, *args, **kwargs):
        """Метод вызываемый при обновлении частот поглощения."""
        self.table()
        self.update_graphics()
        self.update_statistics()
