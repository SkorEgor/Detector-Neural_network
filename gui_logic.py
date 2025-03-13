import os
import setting
from joblib import load
from functools import partial
from pyqtgraph.Qt.QtWidgets import QFileDialog, QTableWidgetItem
from app_exception import AppException
from custom_dialog import CustomDialog
from multi_check_box import GreenRedYellowCheckBox, BlueRedYellowCheckBox
from parser import parser, parser_all_data
from plot_spectrometer_data import (
    SpectrometerPlotAndLegendWidget,
    SpectrometerPlotWidget,
)


class GuiProgram(CustomDialog):
    """
    Класс логики приложения
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Обработчики нажатий кнопок интерфейса
        # - Загрузка нейронной сети
        self.pushButton_reading_file_neural_network.clicked.connect(
            self.loading_neural_network
        )
        # - Загрузка данных без вещества
        self.pushButton_reading_file_no_gas.clicked.connect(
            self.reading_and_plotting_data_without_substance
        )
        # - Загрузка данные с веществом
        self.pushButton_reading_file_with_gas.clicked.connect(
            self.reading_and_plotting_data_with_substance
        )
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
        self.pushButton_save_table_to_file.clicked.connect(self.saving_data)
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
        if setting.DEBUG:
            self.file_name_neural_network = setting.DEFAULT_FILE_PATH_NEURAL_NETWORK
        else:
            self.file_name_neural_network, _ = QFileDialog.getOpenFileName(
                self,
                """Выбрать файл "Нейронной сети" """,
                ".",
                "Neural network(*.joblib);;All Files(*)",
            )
        # Если имя файла не получено, сброс
        if not self.file_name_neural_network:
            raise AppException(
                "Ошибка при загрузке нейронной сети",
                """Путь к файлу "нейронной сети" не найден""",
            )
        # 2. Загрузка модели
        self.data.set_neural_network(load(self.file_name_neural_network))
        # 3. Получение количества входов и скрытых слоев, отображение в UI
        num_inputs, hidden_layer_sizes = self.data.get_neural_network_info()
        self.label_parameters_neural_network.setText(
            f"Кол-во вх: {num_inputs}\nРазмеры слоев: {hidden_layer_sizes}"
        )

    def reading_and_plotting_data_without_substance(self, skip_read=False):
        """Чтение и построение сигнала без вещества"""
        # 1. Чтения файла (если файл тот же - пропускаем)
        if not skip_read:
            # Получение имени файла из диалогового окна (в режиме DEBUG используется путь по умолчанию)
            if setting.DEBUG:
                self.file_name_without_substance = (
                    setting.DEFAULT_FILE_PATH_WITHOUT_SUBSTANCE
                )
            else:
                self.file_name_without_substance, _ = QFileDialog.getOpenFileName(
                    self,
                    "Выбрать файл 'Данные без вещества'",
                    ".",
                    "Spectrometer Data(*.csv);;All Files(*)",
                )
            # Если имя файла не получено, сброс
            if not self.file_name_without_substance:
                raise AppException(
                    """Ошибка при загрузке файла "данных без вещества" """,
                    """Путь к файлу "данных без вещества" - не найден """,
                )
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
            frequency, gamma = parser(
                self.lines_file_without_gas, start_frequency, end_frequency
            )
        else:
            # Парс данных
            frequency, gamma = parser_all_data(self.lines_file_without_gas)
        # 3. Сохраняем данных
        self.data.set_spectrum_without_substance(frequency, gamma)
        # 4. Отображаем данные на графике
        self.update_graphics()

    def reading_and_plotting_data_with_substance(self, skip_read=False):
        """Чтение и построение сигнала с веществом"""
        # 1. Чтения файла (если файл тот же - пропускаем)
        if not skip_read:
            # Получение имени файла из диалогового окна (в режиме DEBUG используется путь по умолчанию)
            if setting.DEBUG:
                self.file_name_with_substance = setting.DEFAULT_FILE_PATH_WITH_SUBSTANCE
            else:
                self.file_name_with_substance, _ = QFileDialog.getOpenFileName(
                    self,
                    "Выбрать файл 'Данные c веществом'",
                    ".",
                    "Spectrometer Data(*.csv);;All Files(*)",
                )
            # Если имя файла не получено, сброс
            if not self.file_name_with_substance:
                raise AppException(
                    """Ошибка при загрузке файла "данных с веществом" """,
                    """Путь к файлу "данных с веществом" - не найден """,
                )
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
            frequency, gamma = parser(
                self.lines_file_with_gas, start_frequency, end_frequency
            )
        else:
            # Парс данных
            frequency, gamma = parser_all_data(self.lines_file_with_gas)
        # 3. Сохраняем данных
        self.data.set_spectrum_with_substance(frequency, gamma)
        # 4. Отображаем данные на графике
        self.update_graphics()

    def change_spectrum_range(self):
        """Вызов при обновлении диапазона спектра - Очищает, отображает данные в актуальном диапазоне"""
        spectra = self.data.get_spectra()
        update_with_gas = not (
            spectra["with_gas"].empty or spectra["with_gas"].isna().all()
        )
        update_without_gas = not (
            spectra["without_gas"].empty or spectra["without_gas"].isna().all()
        )
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
            raise AppException(
                """Ошибка при "Вычислении" """, """Нет данных с веществом """
            )
        if not self.data.get_neural_network():
            raise AppException(
                """Ошибка при "Вычислении" """, """Нет нейронной сети """
            )
        # обработка
        self.data.processing()
        # Отрисовка
        self.update_graphics()
        # Отображение в таблице
        self.table()

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
            index, status, source_neural_network = (
                self.data.get_status_point_absorption(x, y)
            )
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
                self.update_graphics()
                self.table()

    # ---------------------------------------------------------------------------
    #   Методы для работы с таблицей
    # ---------------------------------------------------------------------------
    def initialize_table(self):
        """Инициализация: Пустая таблица"""
        self.tableWidget_frequency_absorption.clear()
        self.tableWidget_frequency_absorption.setColumnCount(4)
        self.tableWidget_frequency_absorption.setHorizontalHeaderLabels(
            ["Частота МГц", "Гамма", ""]
        )
        self.tableWidget_frequency_absorption.setColumnHidden(
            3, True
        )  # Скрываем столбец с индексом
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
            self.tableWidget_frequency_absorption.setItem(
                visible_row, 0, QTableWidgetItem(f"{frequency:.3f}")
            )
            self.tableWidget_frequency_absorption.setItem(
                visible_row, 1, QTableWidgetItem(f"{gamma:.7E}")
            )
            self.tableWidget_frequency_absorption.setItem(
                visible_row, 3, QTableWidgetItem(str(index))
            )
            # Создаем и настраиваем чекбокс для столбца статуса
            checkbox_class = GreenRedYellowCheckBox if source else BlueRedYellowCheckBox
            check_box = checkbox_class(
                initial_state=status, icon_size=22, allow_none=source
            )
            check_box.clicked.connect(
                partial(self.frequency_selection, check_box, index, source)
            )
            self.tableWidget_frequency_absorption.setCellWidget(
                visible_row, 2, check_box
            )
            # Устанавливаем высоту текущей строки
            self.tableWidget_frequency_absorption.setRowHeight(visible_row, 26)
            visible_row += 1

        # Устанавливаем окончательное количество видимых строк
        self.tableWidget_frequency_absorption.setRowCount(visible_row)

        # Настраиваем внешний вид таблицы
        self.tableWidget_frequency_absorption.setColumnWidth(
            2, 30
        )  # Ширина столбца с чекбоксом
        self.tableWidget_frequency_absorption.resizeColumnsToContents()  # Масштабируем по содержимому

    def frequency_selection(
        self, sender: GreenRedYellowCheckBox | BlueRedYellowCheckBox, index, source
    ):
        """Клик по чекбоксу в таблице"""
        # Нет точек поглощения - сброс
        point_absorption = self.data.get_point_absorption()
        if point_absorption.empty:
            return
        # Точка от нейронной сети -> меняем состояние в данных и обновляем график
        if source:
            self.data.set_status_point_absorption_by_index(index, sender.state)
        # Точка поставленная руками -> удаляем из данных, обновляем график
        else:
            self.data.del_point_absorption_by_index(index)

    def get_clicked_cell(self, row):
        """Клик по строке таблице - zoom к указанной области графика или к зоне с линиями поглощения"""
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
        self.plot_widget_1.plot_widget.zoom_to_region(
            x_min=x_min, x_max=x_max, y_min=y_min, y_max=y_max
        )

    # ---------------------------------------------------------------------------
    #   Методы для сохранения в файл
    # ---------------------------------------------------------------------------
    def saving_data(self):
        """Сохранение результатов/таблицы в файл"""
        # 0. Проверка, что данные для сохранения есть
        spectra = self.data.get_spectra()
        point_absorption = self.data.get_point_absorption()
        if spectra.empty:
            raise AppException("""Ошибка "Сохранения" """, """Нет данных""")

        # 1. Выбор места для сохранения
        # 1.1. Рекомендуемое название файла (WARNING)
        name_with_substance, _ = os.path.splitext(self.file_name_with_substance)
        recommended_file_name = f"{spectra['frequency'].iloc[0]}-{spectra['frequency'].iloc[-1]}_{name_with_substance}"
        # 1.2. Вызов окна с выбором места для сохранения
        file_name, file_type = QFileDialog.getSaveFileName(
            self,
            "Сохранение",
            recommended_file_name,
            "Text(*.txt);;Spectrometer Data(*.csv);;All Files(*)",
        )
        # 1.3. Если имя не получено, прервать
        if not file_name:
            return

        # 2. Запись
        with open(file_name, "w", encoding="utf-8") as file:
            # Заголовок/Название столбцов
            file.write("FREQUENCY:\tGAMMA:\n")
            # Перебираем по парно частоты и гаммы пиков; Записываем по строчно в файл
            for i in range(self.tableWidget_frequency_absorption.rowCount()):
                if self.tableWidget_frequency_absorption.cellWidget(i, 2).state:
                    f = self.tableWidget_frequency_absorption.item(i, 0).text()
                    g = self.tableWidget_frequency_absorption.item(i, 1).text()
                    file.write(f"{f}\t{g}\n")
            # Конец файла
            file.write(
                """***********************************************************\n"""
            )
            # Фильтр строк, где source_neural_network=True
            filtered = point_absorption[point_absorption["source_neural_network"]]
            # 1. Количество строк, где source_neural_network=True
            dots_found = filtered.shape[0]
            # 2. Количество строк, где source_neural_network=True и status=True
            points_confirmed = filtered[filtered["status"]].shape[0]
            # 3. Количество строк, где source_neural_network=True и status=False
            points_rejected = filtered[not filtered["status"]].shape[0]
            # 4. Всего точек
            dots_all = point_absorption.shape[0]
            # 5. Точек добавлено
            dots_add = point_absorption[
                not point_absorption["source_neural_network"]
            ].shape[0]
            print(dots_found, points_confirmed, points_rejected, dots_all, dots_add)
            file.write(
                f"Точек обнаружено: {dots_found}\n"
                f"Обнаруженных точек подтверждено: {points_confirmed} \n"
                f"Обнаруженных точек  не утверждено: {points_rejected} \n"
                f"Всего точек: {dots_all} \n"
                f"Точек добавлено: {dots_add}\n"
            )

    # ---------------------------------------------------------------------------
    #   Методы для работы со статистикой
    # ---------------------------------------------------------------------------
    def update_statistics(self):
        """Метод агрегирует данные статистики и отображает под таблицей в UI"""
        point_absorption = self.data.get_point_absorption()
        if point_absorption.empty:
            return

        # Фильтр строк, где source_neural_network=True
        filtered_neuron_found = point_absorption[
            point_absorption["source_neural_network"]
        ]
        # Количество строк, где source_neural_network=True
        points_neuron_found = filtered_neuron_found.shape[0]
        # Количество строк, где source_neural_network=True и status=True
        points_confirmed = filtered_neuron_found[filtered_neuron_found["status"]].shape[
            0
        ]
        # Процент выбранных
        percent_chosen = (
            0 if points_neuron_found == 0 else points_confirmed / points_neuron_found
        )
        # Фильтр строк, где status=True
        filtered_absorption_lines = point_absorption[point_absorption["status"]]
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
