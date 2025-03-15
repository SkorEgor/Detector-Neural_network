import sys

from pyqtgraph.Qt.QtCore import Qt
from pyqtgraph.Qt.QtWidgets import (
    QApplication,
    QCheckBox,
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
)


class CustomHeader(QHeaderView):
    def __init__(self, orientation, parent):
        super().__init__(orientation, parent)
        self.checkbox = QCheckBox(self)
        # Позиционируем чекбокс в третьем столбце (индекс 2)
        self.checkbox.setGeometry(self.sectionPosition(2) + 10, 5, 20, 20)
        self.checkbox.stateChanged.connect(self.checkbox_toggled)

    def checkbox_toggled(self, state):
        table = self.parent()
        for row in range(table.rowCount()):
            item = table.item(row, 2)  # Третий столбец (индекс 2)
            if item:
                item.setCheckState(
                    Qt.CheckState.Checked if state else Qt.CheckState.Unchecked
                )

    def resizeEvent(self, event):
        # Перемещаем чекбокс при изменении размера заголовка
        self.checkbox.setGeometry(self.sectionPosition(2) + 10, 5, 20, 20)
        super().resizeEvent(event)


class MyWindow(QTableWidget):  # Предполагается, что ваша таблица в классе окна
    def __init__(self, parent=None):
        super().__init__(parent, 5, 3)  # Устанавливаем начальные размеры таблицы
        self.tableWidget_frequency_absorption = None
        self.initialize_table()
        self.resize(400, 300)

    def initialize_table(self):
        """Инициализация: Пустая таблица с чекбоксом в заголовке третьего столбца"""
        self.tableWidget_frequency_absorption = (
            self  # Предполагаем, что это ваша таблица
        )
        self.tableWidget_frequency_absorption.clear()
        self.tableWidget_frequency_absorption.setColumnCount(3)

        # Устанавливаем кастомный заголовок
        custom_header = CustomHeader(Qt.Orientation.Horizontal, self)
        self.tableWidget_frequency_absorption.setHorizontalHeader(custom_header)
        self.tableWidget_frequency_absorption.setHorizontalHeaderLabels(
            ["Частота МГц", "Гамма", ""]
        )

        # Настраиваем размеры столбцов
        self.tableWidget_frequency_absorption.resizeColumnToContents(2)

        # Для примера добавим несколько строк
        for row in range(5):
            self.tableWidget_frequency_absorption.insertRow(row)
            self.tableWidget_frequency_absorption.setItem(
                row, 0, QTableWidgetItem(f"{row + 1} МГц")
            )
            self.tableWidget_frequency_absorption.setItem(
                row, 1, QTableWidgetItem(f"Гамма {row}")
            )
            # Добавляем чекбокс в ячейки третьего столбца
            item = QTableWidgetItem()
            item.setFlags(item.flags() | Qt.ItemFlags.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.tableWidget_frequency_absorption.setItem(row, 2, item)


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
