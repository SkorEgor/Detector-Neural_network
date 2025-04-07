import pkg_resources

from detector_neural_network.app_exception import AppException


class ColorTheme:
    """Класс темной и светлой темы приложения"""

    light_style_sheet: str
    dark_style_sheet: str

    def __init__(self, light_file: str = "light_style_sheet.qss", dark_file: str = "dark_style_sheet.qss"):
        """Инициализация с указанием путей к файлам стилей"""
        # Получение пути к директории данного модуля (theme.py)
        package = "detector_neural_network.color_theme"
        self.light_style_sheet = self._load_styles(package, light_file)
        self.dark_style_sheet = self._load_styles(package, dark_file)

    @staticmethod
    def _load_styles(package: str, resource: str) -> str:
        """Чтение содержимого файла стилей через pkg_resources"""
        try:
            # Получаем содержимое файла как строку
            return pkg_resources.resource_string(package, resource).decode("utf-8")
        except FileNotFoundError:
            raise AppException("""Ошибка "Цветовой темы" """, f"""Файл с цветовой темой "{resource}" не найден""")
        except Exception as error:
            raise AppException("""Ошибка "Цветовой темы" """, f"""Ошибка при загрузке "{resource}": {error}""")


color_theme = ColorTheme()
