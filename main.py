import sys
import ctypes
import traceback
from functools import partial

from pyqtgraph.Qt.QtCore import QCoreApplication, Qt, qVersion
from pyqtgraph.Qt.QtWidgets import QApplication, QMessageBox

from app_exception import AppException
from gui_logic import GuiProgram


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


if __name__ == "__main__":

    def main():
        # Решает проблему не правильного масштабирования интерфейса и осей графика PyQtGraph на разных мониторах
        # https://github.com/pyqtgraph/pyqtgraph/issues/756#issuecomment-1023182391
        QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
        if int(qVersion().split(".")[0]) < 6:
            QCoreApplication.setAttribute(Qt.ApplicationAttribute.AA_EnableHighDpiScaling, True)
        # Установка значка приложения на панели задач
        # https://stackoverflow.com/a/1552105
        my_app_id = "company.my-product.subproject.version"
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
        # Инициализации и запуск приложения
        app = QApplication(sys.argv)
        dialog = GuiProgram()
        dialog.show()
        # Устанавливаем глобальный обработчик исключений, c передачей app для подгрузки иконки приложения
        sys.excepthook = partial(handle_exception, app)
        sys.exit(app.exec())

    main()
