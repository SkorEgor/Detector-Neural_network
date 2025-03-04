import sys
import ctypes
import traceback
from functools import partial
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox, QApplication
from PyQt5.QtCore import Qt
from gui_logic import GuiProgram
from app_exception import AppException


def handle_exception(app, exc_type, exc_value, exc_traceback):
    """Глобальный обработчик исключений."""
    # Выводим трассировку ошибки в консоль
    print("Произошла необработанная ошибка:", file=sys.stderr)
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    parent = app.activeWindow()
    if isinstance(exc_value, AppException):
        QMessageBox.warning(parent, exc_value.title, exc_value.message)
        return
    QMessageBox.critical(parent, "Необработанная ошибка", str(exc_value))
    # sys.exit(1)


if __name__ == '__main__':
    # Решает проблему не правильного масштабирования интерфейса и осей графика PyQtGraph на разных мониторах
    # https://github.com/pyqtgraph/pyqtgraph/issues/756#issuecomment-1023182391
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    # Установка значка приложения на панели задач
    # https://stackoverflow.com/a/1552105
    my_app_id = 'company.my-product.subproject.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
    # Инициализации и запуск приложения
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    program = GuiProgram(dialog)
    dialog.show()
    # Устанавливаем глобальный обработчик исключений, c передачей app для подгрузки иконки приложения
    sys.excepthook = partial(handle_exception, app)
    sys.exit(app.exec_())
