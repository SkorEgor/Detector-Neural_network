import sys

import numpy as np
import pandas as pd
from pandas import DataFrame
from pyqtgraph.Qt.QtCore import Qt, pyqtSignal
from pyqtgraph.Qt.QtGui import QPixmap, QColor
from pyqtgraph.Qt.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
)
from pyqtgraph import PlotWidget, mkPen, setConfigOptions, ScatterPlotItem
from data_and_processing import DataAndProcessing


def clearer_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        widget = item.widget()
        # Удаляем виджет
        if widget:
            widget.deleteLater()
        # Рекурсивно очищаем вложенный layout
        elif item.layout():
            clearer_layout(item.layout())


class SpectrometerPlotWidget(PlotWidget):
    title_data = "График №1. Данные с исследуемым веществом и без вещества"
    horizontal_axis_name_data = "Частота [МГц]"
    vertical_axis_name_data = "Гамма [усл.ед.]"
    name_without_gas = "Без вещества"
    color_without_gas = "#515151"
    name_with_gas = "C веществом"
    color_with_gas = "#DC7C02"
    list_absorbing = "Участок с линией поглощения"
    color_absorbing = "#36F62D"
    color_status = {
        True: "#36F62D",  # Зеленый
        False: "#FF0000",  # Красный
        None: "#FFA500",  # Оранжевый
    }
    # Объявляем сигнал обновления легенды (для кастомной легенды)
    dataUpdated = pyqtSignal(list)

    def __init__(
        self,
        absorption_click_callback=None,
        with_gas_click_callback=None,
        *args,
        **kwargs,
    ):
        setConfigOptions(
            background="w",  # Белый фон
            foreground="k",  # Черный цвет текста
        )
        super().__init__(*args, **kwargs)
        self.showGrid(x=True, y=True)
        self.setLabel("left", self.vertical_axis_name_data)
        self.setLabel("bottom", self.horizontal_axis_name_data)
        self.setTitle(self.title_data)
        self.absorption_click_callback = absorption_click_callback
        self.with_gas_click_callback = with_gas_click_callback

    def plot_spectrometer_data(self, data_obj: DataAndProcessing):
        """
        Метод для отрисовки данных со спектрометра, используя объект DataAndProcessing.

        :param data_obj: Объект DataAndProcessing с данными для отрисовки.
        """
        # Очищаем предыдущие данные
        self.clear()
        legend_data = []

        # Извлекаем данные для отрисовки из data_obj
        spectrometer_data = data_obj.get_spectra()
        absorption_points = data_obj.get_point_absorption()

        # Проверка на наличие данных "без вещества" и их отрисовка
        if (
            isinstance(spectrometer_data, DataFrame)
            and not spectrometer_data.empty
            and "without_gas" in spectrometer_data.columns
            and not spectrometer_data["without_gas"].dropna().empty
        ):
            self.plot(
                spectrometer_data["frequency"],
                spectrometer_data["without_gas"],
                pen=mkPen(color=self.color_without_gas, width=2),
                symbol="o",
                symbolSize=4,
                symbolBrush=self.color_without_gas,
                name=self.name_without_gas,
            )
            legend_data.append((self.color_without_gas, self.name_without_gas))

        # Проверка на наличие данных "с веществом" и их отрисовка
        if (
            isinstance(spectrometer_data, DataFrame)
            and not spectrometer_data.empty
            and "with_gas" in spectrometer_data.columns
            and not spectrometer_data["with_gas"].dropna().empty
        ):
            # Рисуем линию
            self.plot(
                spectrometer_data["frequency"],
                spectrometer_data["with_gas"],
                pen=mkPen(color=self.color_with_gas, width=2),
                name=self.name_with_gas,
            )
            # Добавляем точки поверх линии с обработкой нажатий
            with_gas_scatter = ScatterPlotItem(
                x=spectrometer_data["frequency"],
                y=spectrometer_data["with_gas"],
                symbol="o",
                pen=mkPen("k"),
                size=5,
                brush=self.color_with_gas,
            )
            self.addItem(with_gas_scatter)
            with_gas_scatter.sigClicked.connect(
                lambda plot, points: self.with_gas_click_callback(self, plot, points)
            )
            legend_data.append((self.color_with_gas, self.name_with_gas))

        # Отрисовка точек поглощения
        if isinstance(absorption_points, DataFrame) and not absorption_points.empty:
            # Цвета для раскраски точек
            conditions = [
                # status=False
                (not absorption_points["status"]),
                # status=None
                (absorption_points["status"].isna()),
                # status=True и source_neural_network=True
                (absorption_points["status"])
                & (absorption_points["source_neural_network"]),
                # status=True и source_neural_network=False
                (absorption_points["status"])
                & (not absorption_points["source_neural_network"]),
            ]
            choices = [
                "#FF0000",  # Красный
                "#FFA500",  # Оранжевый
                "#36F62D",  # Зеленый
                "#2854C5",  # Синий
            ]
            self.absorption_scatter = ScatterPlotItem(
                x=absorption_points["frequency"],
                y=absorption_points["gamma"],
                pen=mkPen("k"),
                symbol="o",
                brush=np.select(conditions, choices, default="#FFA500"),
                symbolBrush="b",
                size=8,
            )
            self.addItem(self.absorption_scatter)
            # Подключаем callback если он задан
            if self.absorption_click_callback:
                self.absorption_scatter.sigClicked.connect(
                    lambda plot, points: self.absorption_click_callback(
                        self, plot, points
                    )
                )
            legend_data.append((self.color_absorbing, self.list_absorbing))

        # Испускаем сигнал с обновленными данными для легенды
        self.dataUpdated.emit(legend_data)

    def update_absorption_point_color(self, status: list[bool]):
        """Метод для обновления цвета конкретной точки поглощения по индексу"""
        if self.absorption_scatter:
            self.absorption_scatter.setBrush([self.color_status[s] for s in status])

    def zoom_to_region(self, x_min, x_max, y_min, y_max, padding_factor=0.1):
        """
        Метод для зума к указанной области графика с заданными границами.
        """
        # Устанавливаем диапазон отображения с использованием встроенного padding
        self.setXRange(x_min, x_max, padding=padding_factor)
        self.setYRange(y_min, y_max, padding=padding_factor)

        # Отключаем авто-шкалу, чтобы сохранить заданный зум
        self.enableAutoRange(x=False, y=False)


class LegendWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

    def update_legend(self, legend_items):
        # Очистка предыдущих элементов легенды
        clearer_layout(self.layout)
        print(f"{legend_items=}")
        print(f"{self.layout.itemAt(0)=}")
        # Добавляем новые элементы в легенду
        for color, label in legend_items:
            item_layout = QHBoxLayout()

            # Цветной квадратик для обозначения цвета данных
            color_label = QLabel()
            pixmap = QPixmap(20, 20)
            pixmap.fill(QColor(color))
            color_label.setPixmap(pixmap)
            item_layout.addWidget(color_label)

            # Текстовое описание
            text_label = QLabel(label)
            item_layout.addWidget(text_label)

            self.layout.addLayout(item_layout)


class SpectrometerPlotAndLegendWidget(QWidget):
    def __init__(self, absorption_click_callback=None, with_gas_click_callback=None):
        super().__init__()
        # Устанавливаем цвет фона
        # self.setStyleSheet("background-color: #FFFFFF;")

        # Создаем и добавляем график
        layout = QVBoxLayout()
        self.plot_widget = SpectrometerPlotWidget(
            absorption_click_callback=absorption_click_callback,
            with_gas_click_callback=with_gas_click_callback,
        )
        layout.addWidget(self.plot_widget)

        # Создаем и добавляем легенду под графиком
        self.legend_widget = LegendWidget()
        layout.addWidget(self.legend_widget, alignment=Qt.AlignmentFlag.AlignCenter)

        # Подключаем сигнал dataUpdated к методу update_legend
        self.plot_widget.dataUpdated.connect(self.legend_widget.update_legend)

        self.setLayout(layout)


# Пример использования
if __name__ == "__main__":
    app = QApplication(sys.argv)

    data_processing = DataAndProcessing()
    data_processing._DataAndProcessing__spectra = pd.DataFrame(
        {
            "frequency": [1, 2, 3, 4, 5],
            "without_gas": [10, 15, 13, 18, 20],
            "with_gas": [8, 14, 12, 17, 19],
        }
    )
    data_processing._DataAndProcessing__point_absorption = pd.DataFrame(
        {"frequency": [2, 4], "gamma": [14, 17], "status": ["absorption", "absorption"]}
    )

    main_window = SpectrometerPlotAndLegendWidget()
    main_window.plot_widget.plot_spectrometer_data(data_processing)
    main_window.show()

    sys.exit(app.exec_())
