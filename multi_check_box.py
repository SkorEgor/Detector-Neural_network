from pyqtgraph.Qt import QtSvg
from pyqtgraph.Qt.QtCore import Qt
from pyqtgraph.Qt.QtGui import QPixmap, QPainter
from pyqtgraph.Qt.QtCore import pyqtSignal
from pyqtgraph.Qt.QtWidgets import QApplication, QHBoxLayout, QLabel, QVBoxLayout, QWidget


def load_svg_icon(svg_path, size=24):
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)

    renderer = QtSvg.QSvgRenderer(svg_path)
    painter = QPainter(pixmap)
    renderer.render(painter)
    painter.end()

    return pixmap


class BaseMultiCheckBox(QWidget):
    clicked = pyqtSignal(object)

    def __init__(self, initial_state: bool | None = None, icon_size: int = 24, allow_none: bool = True):
        super().__init__()

        self.icon_size = icon_size
        self.allow_none = allow_none
        self.state = initial_state if (initial_state is not None or allow_none) else False
        self.icon_status = {}  # Пустой словарь, будет заполнен в дочерних классах

        self.label = QLabel()
        self.label.setFixedSize(self.icon_size, self.icon_size)
        self.label.setAlignment(Qt.Alignment.AlignCenter)
        self.label.mousePressEvent = self.on_click

        layout = QVBoxLayout()
        layout.addWidget(self.label, alignment=Qt.Alignment.AlignHCenter | Qt.Alignment.AlignVCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)

    def on_click(self, event):
        if self.allow_none:
            self.state = {None: True, True: False, False: None}[self.state]
        else:
            self.state = not self.state
        self.label.setPixmap(self.icon_status[self.state])
        self.clicked.emit(self.state)
        event.accept()

    def set_initial_pixmap(self):
        """Метод для установки начального состояния пиксмапы после инициализации icon_status"""
        if self.icon_status:  # Проверяем, что словарь не пустой
            self.label.setPixmap(self.icon_status[self.state])


class GreenRedYellowCheckBox(BaseMultiCheckBox):
    def __init__(self, initial_state: bool | None = None, icon_size: int = 24, allow_none: bool = True):
        super().__init__(initial_state, icon_size, allow_none)  # Сначала вызываем базовый конструктор
        # определяем icon_status
        self.icon_status = {
            False: load_svg_icon('resource/multi_check_box_svg/no_24dp.svg', icon_size),
            None: load_svg_icon('resource/multi_check_box_svg/undefined_24dp.svg', icon_size),
            True: load_svg_icon('resource/multi_check_box_svg/yes_green_24dp.svg', icon_size)
        }
        self.set_initial_pixmap()


class BlueRedYellowCheckBox(BaseMultiCheckBox):
    def __init__(self, initial_state: bool | None = None, icon_size: int = 24, allow_none: bool = True):
        super().__init__(initial_state, icon_size, allow_none)  # Сначала вызываем базовый конструктор
        # определяем icon_status
        self.icon_status = {
            False: load_svg_icon('resource/multi_check_box_svg/no_24dp.svg', icon_size),
            None: load_svg_icon('resource/multi_check_box_svg/undefined_24dp.svg', icon_size),
            True: load_svg_icon('resource/multi_check_box_svg/yes_blue_24dp.svg', icon_size)
        }
        self.set_initial_pixmap()


# Локальная отладка элементов
if __name__ == "__main__":
    def main():
        app = QApplication([])

        green_checkbox = GreenRedYellowCheckBox()
        blue_checkbox = BlueRedYellowCheckBox()


        def handle_green_click(state):
            print(f"Green checkbox state: {state}")


        def handle_blue_click(state):
            print(f"Blue checkbox state: {state}")


        green_checkbox.clicked.connect(handle_green_click)
        blue_checkbox.clicked.connect(handle_blue_click)

        window = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(green_checkbox)
        layout.addWidget(blue_checkbox)
        window.setLayout(layout)
        window.show()

        app.exec()

    main()
