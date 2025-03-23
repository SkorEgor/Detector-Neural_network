import os

from app_exception import AppException


class ColorTheme:
    """Класс темной и светлой темы приложения"""

    light_style_sheet: str
    dark_style_sheet: str

    def __init__(
            self, light_file: str = "light_style_sheet.qss", dark_file: str = "dark_style_sheet.qss"
    ):
        """Инициализация с указанием путей к файлам стилей"""
        # Получение пути к директории данного модуля (theme.py)
        base_path = os.path.dirname(__file__)
        self.light_style_sheet = self._load_styles(os.path.join(base_path, light_file))
        self.dark_style_sheet = self._load_styles(os.path.join(base_path, dark_file))

    @staticmethod
    def _load_styles(file_path: str) -> str:
        """Чтение содержимого файла стилей"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise AppException("""Ошибка "Цветовой темы" """, f"""Файл с цветовой темой "{file_path}" не найден""")
        except Exception as error:
            raise AppException("""Ошибка "Цветовой темы" """, f"""Ошибка при загрузке "{file_path}": {error} """)


color_theme = ColorTheme()
