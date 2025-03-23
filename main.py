import sys
import ctypes
import traceback
from functools import partial

from PySide6.QtWidgets import QApplication, QMessageBox

import resources_rc  # noqa: F401
from app_exception import AppException
from gui_logic import GuiProgram


def handle_exception(app, exc_type, exc_value, exc_traceback):
    """Глобальный обработчик исключений."""
    print("Произошла необработанная ошибка:", file=sys.stderr)
    traceback.print_exception(exc_type, exc_value, exc_traceback)
    parent = app.activeWindow()
    if isinstance(exc_value, AppException):
        QMessageBox.warning(parent, exc_value.title, exc_value.message)
    else:
        QMessageBox.critical(parent, "Необработанная ошибка", str(exc_value))


def main():
    # Установка ID приложения для Windows
    my_app_id = "company.my-product.subproject.version"
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
    # Инициализация приложения
    app = QApplication(sys.argv)
    # Установка обработчика исключений ДО запуска диалога
    sys.excepthook = partial(handle_exception, app)
    # Запуск диалога
    dialog = GuiProgram(None)
    # Используем только один event loop и передаем результат в sys.exit
    sys.exit(dialog.exec())


if __name__ == "__main__":
    main()
