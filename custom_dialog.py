import os
from pyqtgraph.Qt.QtCore import Qt
from gui import Ui_Dialog
from color_theme import ColorTheme
from app_exception import AppException
from validators import get_float_and_positive
from data_and_processing import DataAndProcessing


class CustomDialog(Ui_Dialog):
    """Класс для добавления доп. логики UI компонентов (валидация полей (get))"""

    def __init__(self, dialog, *args, **kwargs):
        # 1. Создание окна
        # - Инициализация UI из дизайна
        super().__init__(*args, **kwargs)
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        # - Инициализация окна
        Ui_Dialog.__init__(self)
        dialog.setWindowFlags(  # Передаем флаги создания окна
            Qt.WindowType.CustomizeWindowHint |        # must be set to allow the other flags to be changed
            Qt.WindowType.WindowCloseButtonHint |      # Кнопка закрытия
            Qt.WindowType.WindowMaximizeButtonHint |   # Кнопка развернуть
            Qt.WindowType.WindowMinimizeButtonHint     # Кнопка свернуть
        )
        # - Устанавливаем пользовательский интерфейс
        self.setupUi(dialog)

        # 3. Мета данные для данных
        # 3.1 Нейронная сеть
        self.file_name_neural_network: str | None = None
        # 3.2 Спектр без вещества
        self.lines_file_without_gas: list[str] | None = None
        self.file_name_without_substance: str | None = None
        # 3.3 Спектр с веществом
        self.lines_file_with_gas: list[str] | None = None
        self.file_name_with_substance: str | None = None

        # 2. Объект данных (данные со спектрометра и нейронная сеть) их обработки
        self.data = DataAndProcessing()
        # - Устанавливаем метод, который синхронизирует данные и ui
        self.data.set_spectra_interceptor(self.update_ui_on_spectra_change)

        # Обработчики нажатий кнопок интерфейса
        # - Переключение цветовой темы
        self.checkBox_color_theme.toggled.connect(self.update_color_theme)

    def update_color_theme(self, state):
        """Смена цветового стиля интерфейса. Смена с темной темы на светлую и обратно."""
        self.widget_style_sheet.setStyleSheet(ColorTheme.dark_style_sheet if state else ColorTheme.light_style_sheet)

    def update_ui_on_spectra_change(self, *args, **kwargs):
        """Метод вызываемый при обновлении данных для изменения соответствующих индикаторов UI"""
        print("update_ui_on_data_change")
        # Проверка наличия "нейронной сети" (выставляем соответсвующий статус и имя файла)
        if self.data.get_neural_network():
            self.label_text_neural_network.setText(self.file_name_neural_network)
            self.checkBox_download_neural_network.setCheckState(Qt.CheckState.Checked)
        else:
            self.label_text_neural_network.setText("Нет файла")
            self.checkBox_download_neural_network.setCheckState(Qt.CheckState.Unchecked)

        spectra = self.data.get_spectra()
        # Проверяем наличие "Спектра без вещества" (выставляем соответсвующий статус и имя файла)
        if not (spectra["without_gas"].empty or spectra["without_gas"].isna().all()):
            self.label_text_file_name_no_gas.setText(os.path.basename(self.file_name_without_substance))
            self.checkBox_download_no_gas.setCheckState(Qt.CheckState.Checked)
        else:
            self.label_text_file_name_no_gas.setText("Нет файла")
            self.checkBox_download_no_gas.setCheckState(Qt.CheckState.Unchecked)
        # Проверяем наличие "Спектра с веществом"
        if not (spectra["with_gas"].empty or spectra["with_gas"].isna().all()):
            self.label_text_file_name_with_gas.setText(os.path.basename(self.file_name_with_substance))
            self.checkBox_download_with_gas.setCheckState(Qt.CheckState.Checked)
        else:
            self.label_text_file_name_with_gas.setText("Нет файла")
            self.checkBox_download_with_gas.setCheckState(Qt.CheckState.Unchecked)

    # ---------------------------------------------------------------------------
    #   Getters - получение данных из интерфейса
    # ---------------------------------------------------------------------------
    def get_start_range(self) -> float:
        """Получение из UI частоты с которой начинается диапазон спектра"""
        return get_float_and_positive(
            val=self.lineEdit_start_range.text(),
            field_name="Начало диапазона частот",
            call_raise=True
        )

    def get_end_range(self) -> float:
        """Получение из UI частоты которой заканчивается диапазон спектра"""
        return get_float_and_positive(
            val=self.lineEdit_end_range.text(),
            field_name="Конец диапазона частот",
            call_raise=True
        )

    def get_spectrum_frequency_range(self) -> tuple[float, float]:
        """Получение из UI интервала частот спектра"""
        start: float = self.get_start_range()
        end: float = self.get_end_range()
        if end < start:
            raise AppException("Ошибка диапазона частот", "Частота 'от' больше 'до', в фильтре на чтение.")
        return start, end

    def get_window_width(self) -> float:
        """Получение из UI ширину окна просмотра выбранной линии поглощения"""
        return get_float_and_positive(
            val=self.lineEdit_window_width.text(),
            field_name="Ширина окна просмотра",
            call_raise=True
        )
