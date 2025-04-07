# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QDialog, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1281, 610)
        icon = QIcon()
        icon.addFile(u":/application_picture/resource/application_picture/app_icon-round.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.layout_dialog_main = QHBoxLayout(Dialog)
        self.layout_dialog_main.setSpacing(0)
        self.layout_dialog_main.setObjectName(u"layout_dialog_main")
        self.layout_dialog_main.setContentsMargins(0, 0, 0, 0)
        self.widget_style_sheet = QWidget(Dialog)
        self.widget_style_sheet.setObjectName(u"widget_style_sheet")
        self.widget_style_sheet.setStyleSheet(u"QWidget {\n"
"    font: 10pt \"MS Shell Dlg 2\";				/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0440\u0430\u0437\u043c\u0435\u0440\u0430 \u0438 \u0441\u0435\u043c\u0435\u0439\u0441\u0442\u0432\u043e \u0448\u0440\u0438\u0444\u0442\u0430*/\n"
"    color: rgb(208, 208, 208);						/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    background-color: rgb(33, 37, 43);	/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 */\n"
"}\n"
"\n"
"/*------------------------------------------------*/\n"
"/*   ScrollBars															*/\n"
"/*------------------------------------------------*/\n"
"QScrollBar {\n"
"    border: none;													/* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u043f\u043e\u043b\u043e\u0441 \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a"
                        "\u0438 */\n"
"    border-right: 5px solid rgb(211, 211, 211); 	/* \u0417\u0430\u0434\u0430\u0435\u0442 \u043f\u0440\u0430\u0432\u043e\u0439 \u0433\u0440\u0430\u043d\u0438\u0446\u0435 \u0446\u0432\u0435\u0442 \u0438 \u0442\u043e\u043b\u0449\u0438\u043d\u0443 */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;									/* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u043b\u044f \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"    background: rgb(52, 59, 72);			/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u043e\u043b\u043e\u0441\u044b */\n"
"    width: 8px;											/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 \u043f\u043e\u043b\u043e\u0441\u044b \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 */\n"
"    "
                        "margin: 21px 0 21px 0;					/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0441\u0432\u0435\u0440\u0445\u0443 \u0438 \u0441\u043d\u0438\u0437\u0443 */\n"
"    border-radius: 0px;							/* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043f\u043e\u043b\u043e\u0441\u044b */\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u0437\u0443\u043d\u043e\u043a \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e\u0439 \u043f\u043e\u043b\u043e\u0441\u044b */\n"
"QScrollBar::handle:vertical {	\n"
"    background: rgb(255, 255, 255);	/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    min-height: 25px;								/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0443\u044e \u0432"
                        "\u044b\u0441\u043e\u0442\u0443 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"    border-radius: 4px;							/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u0430 */\n"
"}\n"
"\n"
"/* \u041d\u0438\u0436\u043d\u044f\u044f \u0441\u0442\u0440\u0435\u043b\u043a\u0430 */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;									/* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u043d\u0438\u0436\u043d\u0435\u0439 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    background: rgb(55, 63, 77);			/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043d\u0438\u0436\u043d\u0435\u0439 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    height: 20px;										/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 \u043e\u0431\u043b\u0430"
                        "\u0441\u0442\u0438 \u043d\u0438\u0436\u043d\u0435\u0439 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    subcontrol-position: bottom;			/* \u0420\u0430\u0441\u043f\u043e\u043b\u0430\u0433\u0430\u0435\u0442 \u0441\u0442\u0440\u0435\u043b\u043a\u0443 \u0432\u043d\u0438\u0437\u0443 \u043f\u043e\u043b\u043e\u0441\u044b */\n"
"    subcontrol-origin: margin;				/* \u041e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442 \u043d\u0430\u0447\u0430\u043b\u043e \u043e\u0442\u0441\u0447\u0435\u0442\u0430 \u043f\u043e\u0437\u0438\u0446\u0438\u0438 \u0438\u0437 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u043e\u0442\u0441\u0442\u0443\u043f\u043e\u0432 */\n"
"}\n"
"\n"
"/* \u0412\u0435\u0440\u0445\u043d\u044f\u044f \u0441\u0442\u0440\u0435\u043b\u043a\u0430 */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;									/* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0432\u0435\u0440\u0445\u043d\u0435\u0439 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    backgrou"
                        "nd: rgb(55, 63, 77);			/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u0435\u0440\u0445\u043d\u0435\u0439 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    height: 20px;										/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u0432\u0435\u0440\u0445\u043d\u0435\u0439 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    subcontrol-position: top;					/* \u0420\u0430\u0441\u043f\u043e\u043b\u0430\u0433\u0430\u0435\u0442 \u0441\u0442\u0440\u0435\u043b\u043a\u0443 \u0432\u0432\u0435\u0440\u0445\u0443 \u043f\u043e\u043b\u043e\u0441\u044b */\n"
"    subcontrol-origin: margin;				/* \u041e\u043f\u0440\u0435\u0434\u0435\u043b\u044f\u0435\u0442 \u043d\u0430\u0447\u0430\u043b\u043e \u043e\u0442\u0441\u0447\u0435\u0442\u0430 \u043f\u043e\u0437\u0438\u0446\u0438\u0438 \u0438\u0437 \u043e\u0431\u043b\u0430\u0441\u0442\u0438 \u043e\u0442\u0441\u0442\u0443\u043f"
                        "\u043e\u0432 */\n"
"}\n"
"\n"
"/* \u0426\u0432\u0435\u0442\u0430 \u0432\u0435\u0440\u0445\u043d\u0435\u0439 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"QScrollBar::up-arrow:vertical {\n"
"    border-top-left-radius: 4px;			/* \u0421\u043a\u0440\u0443\u0433\u043b\u044f\u0435\u0442 \u0432\u0435\u0440\u0445\u043d\u0438\u0439 \u043b\u0435\u0432\u044b\u0439 \u0443\u0433\u043e\u043b \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    border-top-right-radius: 4px;			/* \u0421\u043a\u0440\u0443\u0433\u043b\u044f\u0435\u0442 \u0432\u0435\u0440\u0445\u043d\u0438\u0439 \u043f\u0440\u0430\u0432\u044b\u0439 \u0443\u0433\u043e\u043b \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    background: rgb(255, 255, 255);	/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u0435\u0440\u0445\u043d\u0435\u0439 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"}\n"
"\n"
"/* \u0426\u0432\u0435\u0442\u0430 \u043d\u0438\u0436\u043d\u0435\u0439 \u0441\u0442\u0440\u0435\u043b\u043a\u0438"
                        " */\n"
"QScrollBar::down-arrow:vertical {\n"
"    border-bottom-left-radius: 4px;		/* \u0421\u043a\u0440\u0443\u0433\u043b\u044f\u0435\u0442 \u043d\u0438\u0436\u043d\u0438\u0439 \u043b\u0435\u0432\u044b\u0439 \u0443\u0433\u043e\u043b \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    border-bottom-right-radius: 4px;	/* \u0421\u043a\u0440\u0443\u0433\u043b\u044f\u0435\u0442 \u043d\u0438\u0436\u043d\u0438\u0439 \u043f\u0440\u0430\u0432\u044b\u0439 \u0443\u0433\u043e\u043b \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"    background: rgb(255, 255, 255); 	/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0431\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u043d\u0438\u0436\u043d\u0435\u0439 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 */\n"
"}\n"
"\n"
"/* \u041e\u0431\u043b\u0430\u0441\u0442\u0438 \u043d\u0430\u0434 \u0438 \u043f\u043e\u0434 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u043e\u043c */\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;"
                        " 							/* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0444\u043e\u043d \u0434\u043b\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u0435\u0439 \u043d\u0430\u0434 \u0438 \u043f\u043e\u0434 \u043f\u043e\u043b\u0437\u0443\u043d\u043a\u043e\u043c */\n"
"}\n"
"\n"
"/*------------------------------------------------*/\n"
"/*   RadioButton													*/\n"
"/*------------------------------------------------*/\n"
"/* \u0418\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u0430\u0434\u0438\u043e\u043a\u043d\u043e\u043f\u043a\u0438 \u0432 \u043e\u0431\u044b\u0447\u043d\u043e\u043c \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0438 */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);	/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    width: 15px;										/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440\u0430 */\n"
"    hei"
                        "ght: 15px;										/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440\u0430 */\n"
"    border-radius: 10px;							/* \u0421\u043a\u0440\u0443\u0433\u043b\u044f\u0435\u0442 \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440 */\n"
"    background: rgb(44, 49, 60);			/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0444\u043e\u043d \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440\u0430 */\n"
"}\n"
"\n"
"/* \u0418\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u0430\u0434\u0438\u043e\u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u0438 */\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);	/* \u041c\u0435\u043d\u044f\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"/* \u0418\u043d"
                        "\u0434\u0438\u043a\u0430\u0442\u043e\u0440 \u0440\u0430\u0434\u0438\u043e\u043a\u043d\u043e\u043f\u043a\u0438 \u0432 \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u043c \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0438 */\n"
"QRadioButton::indicator:checked {\n"
"    border: 3px solid rgb(52, 59, 72); 	/* \u0421\u043e\u0445\u0440\u0430\u043d\u044f\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    background: rgb(255, 255, 255);	/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0444\u043e\u043d \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440\u0430 \u043f\u0440\u0438 \u0432\u044b\u0431\u043e\u0440\u0435 */\n"
"}\n"
"\n"
"/* \u0420\u0430\u0434\u0438\u043e\u043a\u043d\u043e\u043f\u043a\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u0438 */\n"
"QRadioButton:hover {\n"
"    background-color: rgb(40, 44, 52);		 /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0444\u043e\u043d \u043a\u043d\u043e\u043f\u043a\u0438"
                        " \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"/* \u0420\u0430\u0434\u0438\u043e\u043a\u043d\u043e\u043f\u043a\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"QRadioButton:pressed {\n"
"    background-color: rgb(170, 170, 170);	/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0444\u043e\u043d \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    color: rgb(0, 0, 0);										/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: none;											/* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}\n"
"\n"
"/* \u0421\u043f\u0435\u0446\u0438\u0444\u0438\u0447\u043d\u044b\u0439 \u0441\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0440\u0430\u0434\u0438\u043e\u043a\u043d\u043e\u043f\u043e\u043a \u0418\u0437\u043c"
                        "\u0435\u043d\u0435\u043d\u0438\u044f \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u043e\u0432*/\n"
"#radioButton_selected_range {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/cycle1_24dp_white.svg); /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441\u043f\u0440\u0430\u0432\u0430 */\n"
"    image-position: right center;			/* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0435\u0442 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 */\n"
"    padding-top: 3px;								/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"    padding-bottom: 3px;						/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043d\u0438\u0437\u0443 */\n"
"    padding-right: 4px;							/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442"
                        "\u0441\u0442\u0443\u043f \u0441\u043f\u0440\u0430\u0432\u0430 */\n"
"}\n"
"#radioButton_selected_range:pressed {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/cycle2_24dp_white.svg); /* \u041c\u0435\u043d\u044f\u0435\u0442 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    image-position: right center;			/* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0435\u0442 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 */\n"
"    padding-top: 3px;								/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"    padding-bottom: 3px;						/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043d\u0438\u0437\u0443 */\n"
"    padding-right: 4px;							/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043f"
                        "\u0440\u0430\u0432\u0430 */\n"
"}\n"
"\n"
"/*------------------------------------------------*/\n"
"/*   CheckBox															*/\n"
"/*------------------------------------------------*/\n"
"/* \u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\u043d\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 */\n"
"QCheckBox {\n"
"    padding-left: 0px;				/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043b\u0435\u0432\u0430 */\n"
"    padding-right: -8px;        /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u043e\u0442\u0440\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u044b\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043f\u0440\u0430\u0432\u0430 */\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 - \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e */\n"
"QCheckBox::indicator:unchecked {\n"
"	/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0438\u0437\u043e"
                        "\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u043d\u0435\u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    image: url(:/multi_check_box/resource/multi_check_box_svg/no_24dp.svg);\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 - \u0432\u044b\u0431\u0440\u0430\u043d\u043e */\n"
"QCheckBox::indicator:checked {\n"
"	/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"    image: url(:/multi_check_box/resource/multi_check_box_svg/yes_green_24dp.svg); \n"
"}\n"
"\n"
"/*------------------------------------------------*/\n"
"/*   PushButton														*/\n"
"/*------------------------------------------------*/\n"
"\n"
"/* \u0421\u0442\u0430\u043d\u0434\u0430\u0440"
                        "\u0442\u043d\u043e\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"QPushButton {\n"
"    font-size: 12pt;												/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    background-color: rgb(37, 41, 48);			/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0444\u043e\u043d */\n"
"    border: 1px solid rgb(52, 59, 72);				/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    background-position: left center;				/* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0435\u0442 \u0444\u043e\u043d\u043e\u0432\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 */\n"
"    background-repeat: no-repeat;					/* \u041e\u0442\u043a\u043b\u044e\u0447\u0430\u0435\u0442 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0435 \u0444"
                        "\u043e\u043d\u043e\u0432\u043e\u0433\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f */\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043c\u044b\u0448\u0438 */\n"
"QPushButton:hover {\n"
"    background-color: rgb(40, 44, 52);			/* \u041c\u0435\u043d\u044f\u0435\u0442 \u0444\u043e\u043d */\n"
"    border: none;												/* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"QPushButton:pressed {\n"
"    background-color: rgb(170, 170, 170);		/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0444\u043e\u043d */\n"
"    color: rgb(181, 181, 181);								/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: non"
                        "e;												/* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 \"\u041d\u0435\u0439\u0440\u043e\u043d\u043d\u0430\u044f \u0441\u0435\u0442\u044c\" */\n"
"#pushButton_neural_network_heade {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/network_24dp_white.svg);/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    image-position: left center;							/* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    padding-top: 2px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"    padding-bottom: 2px;									/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043d\u0438\u0437\u0443 */\n"
"    padding-left: 4px;											/"
                        "* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043b\u0435\u0432\u0430 */\n"
"}\n"
"#pushButton_neural_network_heade:hover {\n"
"    border-left: 4px solid rgb(208, 208, 208);	/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 \u0441\u043b\u0435\u0432\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u0444\u0430\u0439\u043b\u0430 \u0434\u043b\u044f \u043d\u0435\u0439\u0440\u043e\u043d\u043d\u043e\u0439 \u0441\u0435\u0442\u0438 */\n"
"#pushButton_reading_file_neural_network {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/download_24dp_white.svg);/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 \"\u0414\u0430\u043d\u043d\u044b\u0435"
                        "\" */\n"
"#pushButton_data_header {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/data_24dp_white.svg);/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    image-position: left center;							/* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    padding-top: 2px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"    padding-bottom: 2px;									/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043d\u0438\u0437\u0443 */\n"
"    padding-left: 4px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043b\u0435\u0432\u0430 */\n"
"}\n"
"#pushButton_data_header:hover {\n"
"    border-left: 4px solid rgb(208, 208, 208);	/* \u0414\u043e\u0431\u0430\u0432"
                        "\u043b\u044f\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 \u0441\u043b\u0435\u0432\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0438 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u0444\u0430\u0439\u043b\u043e\u0432 */\n"
"#pushButton_reading_file_no_gas {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/download_24dp_white.svg);/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"}\n"
"#pushButton_reading_file_with_gas {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/download_24dp_white.svg);/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u0441\u0431\u0440\u043e\u0441\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0441\u043f\u0435\u043a\u0442\u0440\u0430 */\n"
"#pushButton_reset_sp"
                        "ectrum_data {\n"
"    font-size: 10pt;												/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f/\u0437\u0430\u043a\u0440\u044b\u0442\u0438\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u044b */\n"
"#pushButton_close_open_table {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/table_24dp_white.svg);/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    image-position: left center;							/* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    padding-top: 2px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"    padding-bottom: 2px;									/* \u0414\u043e"
                        "\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043d\u0438\u0437\u0443 */\n"
"    padding-left: 4px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043b\u0435\u0432\u0430 */\n"
"}\n"
"#pushButton_close_open_table:hover {\n"
"    border-left: 4px solid rgb(208, 208, 208);	/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 \u0441\u043b\u0435\u0432\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u0440\u0430\u0441\u0447\u0435\u0442\u0430 */\n"
"#pushButton_menu_calculate {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/launch_24dp_white.svg);/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    image-position: left center;							/* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430"
                        "\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    padding-top: 2px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"    padding-bottom: 2px;									/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043d\u0438\u0437\u0443 */\n"
"    padding-left: 4px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043b\u0435\u0432\u0430 */\n"
"}\n"
"#pushButton_menu_calculate:hover {\n"
"    border-left: 4px solid rgb(208, 208, 208);	/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 \u0441\u043b\u0435\u0432\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u0437\u0430\u0433\u0440\u0443\u0437\u043a\u0438 \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u0430"
                        " */\n"
"#pushButton_load_result {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/download_24dp_white.svg);/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    image-position: left center;							/* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    padding-top: 2px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"    padding-bottom: 2px;									/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043d\u0438\u0437\u0443 */\n"
"    padding-left: 4px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043b\u0435\u0432\u0430 */\n"
"}\n"
"#pushButton_load_result:hover {\n"
"    border-left: 4px solid rgb(208, 208, 208);	/* \u0414\u043e\u0431\u0430\u0432"
                        "\u043b\u044f\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 \u0441\u043b\u0435\u0432\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u0441\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0432 \u0444\u0430\u0439\u043b */\n"
"#pushButton_save_table_to_file {\n"
"    image: url(:/general_black_ui/resource/general_black_ui/save_24dp_white.svg);/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    image-position: left center;							/* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0435\u0442 \u0438\u043a\u043e\u043d\u043a\u0443 */\n"
"    padding-top: 2px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"    padding-bottom: 2px;									/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435"
                        "\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043d\u0438\u0437\u0443 */\n"
"    padding-left: 4px;											/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u043e\u0442\u0441\u0442\u0443\u043f \u0441\u043b\u0435\u0432\u0430 */\n"
"}\n"
"#pushButton_save_table_to_file:hover {\n"
"    border-left: 4px solid rgb(208, 208, 208);	/* \u0414\u043e\u0431\u0430\u0432\u043b\u044f\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 \u0441\u043b\u0435\u0432\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"/*------------------------------------------------*/\n"
"/*   LineEdit															*/\n"
"/*------------------------------------------------*/\n"
"QLineEdit:enabled {\n"
"    background-color: rgb(44, 49, 58);				/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0444\u043e\u043d */\n"
"    border: 1px solid rgb(255, 255, 255);				/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
""
                        "}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043e\u0442\u043a\u043b\u044e\u0447\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f */\n"
"QLineEdit:disabled {\n"
"    background-color: rgba(67, 74, 88, 0);			/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1px solid rgb(255, 255, 255);				/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    color: rgb(67, 74, 88);										/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"\n"
"/*------------------------------------------------*/\n"
"/*   GroupBox														*/\n"
"/*------------------------------------------------*/\n"
"QGroupBox {\n"
"    color: rgb(255, 255, 255);									/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0446\u0432"
                        "\u0435\u0442 \u0448\u0440\u0438\u0444\u0442\u0430 \u0434\u043b\u044f \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 \u0433\u0440\u0443\u043f\u043f\u044b */\n"
"}\n"
"\n"
"/*------------------------------------------------*/\n"
"/*   TableWidget													*/\n"
"/*------------------------------------------------*/\n"
"QTableWidget {	\n"
"    gridline-color: rgb(136, 136, 136);					/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0446\u0432\u0435\u0442 \u043b\u0438\u043d\u0438\u0439 \u0441\u0435\u0442\u043a\u0438 */\n"
"    border-top: 1px solid rgb(54, 60, 74);			/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0432\u0435\u0440\u0445\u043d\u044e\u044e \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-bottom: 1px solid rgb(54, 60, 74);	/* \u0417\u0430\u0434\u0430\u0435\u0442 \u043d\u0438\u0436\u043d\u044e\u044e \u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(72, 81, 94);				/* \u0423\u0441\u0442"
                        "\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0444\u043e\u043d \u0434\u043b\u044f \u0432\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0445 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 */\n"
"}\n"
"\n"
"QHeaderView { \n"
"    qproperty-defaultAlignment: AlignCenter;	/* \u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0435\u0442 \u0441\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u0441\u0435\u043a\u0446\u0438\u0439 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u044b */\n"
"QHeaderView::section {\n"
"    background-color: rgb(37, 41, 48);				/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0444\u043e\u043d \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u0432 */\n"
"    border: 1px solid rgb(136, 136, 136);				/* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 "
                        "\u0433\u0440\u0430\u043d\u0438\u0446\u0443 */\n"
"    border-style: none;											/* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u0441\u0442\u0438\u043b\u044c \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 \u0432 \u0432\u0435\u0440\u0445\u043d\u0435\u043c \u043b\u0435\u0432\u043e\u043c \u0443\u0433\u043b\u0443 \u0442\u0430\u0431\u043b\u0438\u0446\u044b */\n"
"QTableCornerButton::section {\n"
"    background-color: rgb(33, 37, 43);				/* \u0417\u0430\u0434\u0430\u0435\u0442 \u0444\u043e\u043d \u0443\u0433\u043b\u043e\u0432\u043e\u0439 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"}")
        self.layout_style_sheet = QHBoxLayout(self.widget_style_sheet)
        self.layout_style_sheet.setSpacing(0)
        self.layout_style_sheet.setObjectName(u"layout_style_sheet")
        self.layout_style_sheet.setContentsMargins(0, 0, 0, 0)
        self.widget_menu = QWidget(self.widget_style_sheet)
        self.widget_menu.setObjectName(u"widget_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_menu.sizePolicy().hasHeightForWidth())
        self.widget_menu.setSizePolicy(sizePolicy)
        self.widget_menu.setMinimumSize(QSize(225, 0))
        self.widget_menu.setMaximumSize(QSize(215, 16777215))
        self.widget_menu.setStyleSheet(u"")
        self.layout_menu = QVBoxLayout(self.widget_menu)
        self.layout_menu.setSpacing(0)
        self.layout_menu.setObjectName(u"layout_menu")
        self.layout_menu.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout_menu.setContentsMargins(0, 0, 0, 0)
        self.widget_menu_title = QWidget(self.widget_menu)
        self.widget_menu_title.setObjectName(u"widget_menu_title")
        self.widget_menu_title.setMinimumSize(QSize(0, 50))
        self.widget_menu_title.setMaximumSize(QSize(16777215, 50))
        self.widget_menu_title.setStyleSheet(u"")
        self.layout_menu_title = QHBoxLayout(self.widget_menu_title)
        self.layout_menu_title.setSpacing(0)
        self.layout_menu_title.setObjectName(u"layout_menu_title")
        self.layout_menu_title.setContentsMargins(0, 0, 0, 0)
        self.label_imag_app = QLabel(self.widget_menu_title)
        self.label_imag_app.setObjectName(u"label_imag_app")
        self.label_imag_app.setMinimumSize(QSize(40, 40))
        self.label_imag_app.setMaximumSize(QSize(54, 40))
        self.label_imag_app.setSizeIncrement(QSize(0, 0))
        self.label_imag_app.setStyleSheet(u"padding-left: 7px;\n"
"padding-right: 7px;\n"
"border: none;\n"
"")
        self.label_imag_app.setPixmap(QPixmap(u":/application_picture/resource/application_picture/app_icon-round.png"))
        self.label_imag_app.setScaledContents(True)
        self.label_imag_app.setMargin(0)
        self.label_imag_app.setIndent(-1)

        self.layout_menu_title.addWidget(self.label_imag_app)

        self.label_text_app_name = QLabel(self.widget_menu_title)
        self.label_text_app_name.setObjectName(u"label_text_app_name")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label_text_app_name.setFont(font)
        self.label_text_app_name.setStyleSheet(u"font-size: 14pt;")
        self.label_text_app_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_menu_title.addWidget(self.label_text_app_name)

        self.checkBox_color_theme = QCheckBox(self.widget_menu_title)
        self.checkBox_color_theme.setObjectName(u"checkBox_color_theme")
        self.checkBox_color_theme.setMinimumSize(QSize(0, 0))
        self.checkBox_color_theme.setMaximumSize(QSize(55, 16777215))
        self.checkBox_color_theme.setStyleSheet(u"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 - \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d*/\n"
"QCheckBox::indicator:unchecked {\n"
"	/* \u0412\u044b\u0431\u043e\u0440 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438*/\n"
"	image: url(:/toggle_color_theme/resource/toggle_color_theme/off_black.svg);\n"
"\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 -  \u0432\u044b\u0431\u0440\u0430\u043d*/\n"
"QCheckBox::indicator:checked {\n"
"	/* \u0412\u044b\u0431\u043e\u0440 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438*/\n"
"	image: url(:/toggle_color_theme/resource/toggle_color_theme/on_white.svg);\n"
"}\n"
"")
        self.checkBox_color_theme.setText(u"")

        self.layout_menu_title.addWidget(self.checkBox_color_theme)


        self.layout_menu.addWidget(self.widget_menu_title)

        self.widget_menu_body = QWidget(self.widget_menu)
        self.widget_menu_body.setObjectName(u"widget_menu_body")
        self.widget_menu_body.setStyleSheet(u" .QWidget{\n"
"\n"
"}")
        self.layout_menu_body = QVBoxLayout(self.widget_menu_body)
        self.layout_menu_body.setSpacing(0)
        self.layout_menu_body.setObjectName(u"layout_menu_body")
        self.layout_menu_body.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.layout_menu_body.setContentsMargins(0, 0, 3, 0)
        self.scrollArea_menu_body = QScrollArea(self.widget_menu_body)
        self.scrollArea_menu_body.setObjectName(u"scrollArea_menu_body")
        self.scrollArea_menu_body.setTabletTracking(False)
        self.scrollArea_menu_body.setStyleSheet(u"")
        self.scrollArea_menu_body.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_menu_body.setFrameShadow(QFrame.Shadow.Sunken)
        self.scrollArea_menu_body.setLineWidth(1)
        self.scrollArea_menu_body.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.scrollArea_menu_body.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_menu_body.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea_menu_body.setWidgetResizable(True)
        self.scrollArea_menu_body.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 222, 480))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.Layout_scroll_menu = QVBoxLayout(self.scrollAreaWidgetContents)
        self.Layout_scroll_menu.setSpacing(5)
        self.Layout_scroll_menu.setObjectName(u"Layout_scroll_menu")
        self.Layout_scroll_menu.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.Layout_scroll_menu.setContentsMargins(0, 0, 0, 0)
        self.widget_neural_network = QWidget(self.scrollAreaWidgetContents)
        self.widget_neural_network.setObjectName(u"widget_neural_network")
        self.widget_neural_network.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_neural_network.sizePolicy().hasHeightForWidth())
        self.widget_neural_network.setSizePolicy(sizePolicy1)
        self.widget_neural_network.setMinimumSize(QSize(0, 0))
        self.widget_neural_network.setStyleSheet(u"")
        self.layout_menu_neural_network = QVBoxLayout(self.widget_neural_network)
        self.layout_menu_neural_network.setSpacing(0)
        self.layout_menu_neural_network.setObjectName(u"layout_menu_neural_network")
        self.layout_menu_neural_network.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout_menu_neural_network.setContentsMargins(0, 0, 0, 5)
        self.widget_neural_network_header = QWidget(self.widget_neural_network)
        self.widget_neural_network_header.setObjectName(u"widget_neural_network_header")
        self.widget_neural_network_header.setStyleSheet(u"")
        self.layout_neural_network_header = QHBoxLayout(self.widget_neural_network_header)
        self.layout_neural_network_header.setSpacing(0)
        self.layout_neural_network_header.setObjectName(u"layout_neural_network_header")
        self.layout_neural_network_header.setContentsMargins(0, 0, 0, 0)
        self.pushButton_neural_network_heade = QPushButton(self.widget_neural_network_header)
        self.pushButton_neural_network_heade.setObjectName(u"pushButton_neural_network_heade")
        sizePolicy1.setHeightForWidth(self.pushButton_neural_network_heade.sizePolicy().hasHeightForWidth())
        self.pushButton_neural_network_heade.setSizePolicy(sizePolicy1)
        self.pushButton_neural_network_heade.setMinimumSize(QSize(0, 40))
        self.pushButton_neural_network_heade.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.pushButton_neural_network_heade.setFont(font1)
        self.pushButton_neural_network_heade.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_neural_network_heade.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_neural_network_heade.setAutoFillBackground(False)
        self.pushButton_neural_network_heade.setStyleSheet(u"")
        self.pushButton_neural_network_heade.setIconSize(QSize(25, 25))
        self.pushButton_neural_network_heade.setCheckable(True)
        self.pushButton_neural_network_heade.setChecked(True)
        self.pushButton_neural_network_heade.setAutoRepeat(False)
        self.pushButton_neural_network_heade.setAutoExclusive(False)
        self.pushButton_neural_network_heade.setFlat(False)

        self.layout_neural_network_header.addWidget(self.pushButton_neural_network_heade)


        self.layout_menu_neural_network.addWidget(self.widget_neural_network_header)

        self.widget_neural_network_body = QWidget(self.widget_neural_network)
        self.widget_neural_network_body.setObjectName(u"widget_neural_network_body")
        self.widget_neural_network_body.setEnabled(True)
        self.widget_neural_network_body.setStyleSheet(u"")
        self.layout_neural_network_body = QVBoxLayout(self.widget_neural_network_body)
        self.layout_neural_network_body.setSpacing(0)
        self.layout_neural_network_body.setObjectName(u"layout_neural_network_body")
        self.layout_neural_network_body.setContentsMargins(5, 5, 5, 5)
        self.widget = QWidget(self.widget_neural_network_body)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label_text_neural_network = QLabel(self.widget)
        self.label_text_neural_network.setObjectName(u"label_text_neural_network")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_text_neural_network.sizePolicy().hasHeightForWidth())
        self.label_text_neural_network.setSizePolicy(sizePolicy2)
        self.label_text_neural_network.setMinimumSize(QSize(0, 30))
        self.label_text_neural_network.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_text_neural_network.setFont(font2)
        self.label_text_neural_network.setStyleSheet(u"")
        self.label_text_neural_network.setTextFormat(Qt.TextFormat.AutoText)
        self.label_text_neural_network.setScaledContents(False)

        self.horizontalLayout_2.addWidget(self.label_text_neural_network)

        self.pushButton_reading_file_neural_network = QPushButton(self.widget)
        self.pushButton_reading_file_neural_network.setObjectName(u"pushButton_reading_file_neural_network")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_reading_file_neural_network.sizePolicy().hasHeightForWidth())
        self.pushButton_reading_file_neural_network.setSizePolicy(sizePolicy3)
        self.pushButton_reading_file_neural_network.setMinimumSize(QSize(30, 30))
        self.pushButton_reading_file_neural_network.setMaximumSize(QSize(16777215, 30))
        self.pushButton_reading_file_neural_network.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reading_file_neural_network.setStyleSheet(u"")
        self.pushButton_reading_file_neural_network.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButton_reading_file_neural_network)

        self.checkBox_download_neural_network = QCheckBox(self.widget)
        self.checkBox_download_neural_network.setObjectName(u"checkBox_download_neural_network")
        self.checkBox_download_neural_network.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.checkBox_download_neural_network.sizePolicy().hasHeightForWidth())
        self.checkBox_download_neural_network.setSizePolicy(sizePolicy3)
        self.checkBox_download_neural_network.setMinimumSize(QSize(0, 30))
        self.checkBox_download_neural_network.setMaximumSize(QSize(16777215, 30))
        self.checkBox_download_neural_network.setStyleSheet(u"")
        self.checkBox_download_neural_network.setChecked(False)
        self.checkBox_download_neural_network.setTristate(False)

        self.horizontalLayout_2.addWidget(self.checkBox_download_neural_network)


        self.layout_neural_network_body.addWidget(self.widget)

        self.label_parameters_neural_network = QLabel(self.widget_neural_network_body)
        self.label_parameters_neural_network.setObjectName(u"label_parameters_neural_network")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_parameters_neural_network.sizePolicy().hasHeightForWidth())
        self.label_parameters_neural_network.setSizePolicy(sizePolicy4)

        self.layout_neural_network_body.addWidget(self.label_parameters_neural_network)


        self.layout_menu_neural_network.addWidget(self.widget_neural_network_body)


        self.Layout_scroll_menu.addWidget(self.widget_neural_network)

        self.widget_data = QWidget(self.scrollAreaWidgetContents)
        self.widget_data.setObjectName(u"widget_data")
        sizePolicy1.setHeightForWidth(self.widget_data.sizePolicy().hasHeightForWidth())
        self.widget_data.setSizePolicy(sizePolicy1)
        self.widget_data.setMinimumSize(QSize(0, 0))
        self.widget_data.setStyleSheet(u"")
        self.layout_menu_data = QVBoxLayout(self.widget_data)
        self.layout_menu_data.setSpacing(0)
        self.layout_menu_data.setObjectName(u"layout_menu_data")
        self.layout_menu_data.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout_menu_data.setContentsMargins(0, 0, 0, 5)
        self.widget_data_header = QWidget(self.widget_data)
        self.widget_data_header.setObjectName(u"widget_data_header")
        self.widget_data_header.setStyleSheet(u"")
        self.layout_data_header = QHBoxLayout(self.widget_data_header)
        self.layout_data_header.setSpacing(0)
        self.layout_data_header.setObjectName(u"layout_data_header")
        self.layout_data_header.setContentsMargins(0, 0, 0, 0)
        self.pushButton_data_header = QPushButton(self.widget_data_header)
        self.pushButton_data_header.setObjectName(u"pushButton_data_header")
        sizePolicy1.setHeightForWidth(self.pushButton_data_header.sizePolicy().hasHeightForWidth())
        self.pushButton_data_header.setSizePolicy(sizePolicy1)
        self.pushButton_data_header.setMinimumSize(QSize(0, 40))
        self.pushButton_data_header.setMaximumSize(QSize(16777215, 42))
        self.pushButton_data_header.setFont(font1)
        self.pushButton_data_header.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_data_header.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_data_header.setAutoFillBackground(False)
        self.pushButton_data_header.setStyleSheet(u"")
        self.pushButton_data_header.setIconSize(QSize(20, 20))
        self.pushButton_data_header.setCheckable(True)
        self.pushButton_data_header.setChecked(True)
        self.pushButton_data_header.setAutoRepeat(False)
        self.pushButton_data_header.setAutoExclusive(False)
        self.pushButton_data_header.setFlat(False)

        self.layout_data_header.addWidget(self.pushButton_data_header)


        self.layout_menu_data.addWidget(self.widget_data_header)

        self.widget_data_body = QWidget(self.widget_data)
        self.widget_data_body.setObjectName(u"widget_data_body")
        self.widget_data_body.setStyleSheet(u"")
        self.layout_data_body = QVBoxLayout(self.widget_data_body)
        self.layout_data_body.setSpacing(5)
        self.layout_data_body.setObjectName(u"layout_data_body")
        self.layout_data_body.setContentsMargins(5, 5, 5, 5)
        self.groupBox_no_gas = QGroupBox(self.widget_data_body)
        self.groupBox_no_gas.setObjectName(u"groupBox_no_gas")
        self.groupBox_no_gas.setMinimumSize(QSize(0, 50))
        self.groupBox_no_gas.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_no_gas.setSizeIncrement(QSize(0, 0))
        self.groupBox_no_gas.setBaseSize(QSize(0, 0))
        self.groupBox_no_gas.setFont(font2)
        self.groupBox_no_gas.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.groupBox_no_gas.setMouseTracking(False)
        self.groupBox_no_gas.setTabletTracking(False)
        self.groupBox_no_gas.setStyleSheet(u"")
        self.groupBox_no_gas.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_no_gas.setFlat(True)
        self.groupBox_no_gas.setCheckable(False)
        self.layout_no_gas = QHBoxLayout(self.groupBox_no_gas)
        self.layout_no_gas.setSpacing(5)
        self.layout_no_gas.setObjectName(u"layout_no_gas")
        self.layout_no_gas.setContentsMargins(5, 5, 5, 5)
        self.label_text_file_name_no_gas = QLabel(self.groupBox_no_gas)
        self.label_text_file_name_no_gas.setObjectName(u"label_text_file_name_no_gas")
        sizePolicy2.setHeightForWidth(self.label_text_file_name_no_gas.sizePolicy().hasHeightForWidth())
        self.label_text_file_name_no_gas.setSizePolicy(sizePolicy2)
        self.label_text_file_name_no_gas.setMinimumSize(QSize(0, 30))
        self.label_text_file_name_no_gas.setMaximumSize(QSize(16777215, 30))
        self.label_text_file_name_no_gas.setFont(font2)
        self.label_text_file_name_no_gas.setStyleSheet(u"")
        self.label_text_file_name_no_gas.setTextFormat(Qt.TextFormat.AutoText)
        self.label_text_file_name_no_gas.setScaledContents(False)

        self.layout_no_gas.addWidget(self.label_text_file_name_no_gas)

        self.pushButton_reading_file_no_gas = QPushButton(self.groupBox_no_gas)
        self.pushButton_reading_file_no_gas.setObjectName(u"pushButton_reading_file_no_gas")
        self.pushButton_reading_file_no_gas.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_reading_file_no_gas.sizePolicy().hasHeightForWidth())
        self.pushButton_reading_file_no_gas.setSizePolicy(sizePolicy3)
        self.pushButton_reading_file_no_gas.setMinimumSize(QSize(30, 30))
        self.pushButton_reading_file_no_gas.setMaximumSize(QSize(16777215, 30))
        self.pushButton_reading_file_no_gas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reading_file_no_gas.setStyleSheet(u"")
        self.pushButton_reading_file_no_gas.setIconSize(QSize(25, 25))

        self.layout_no_gas.addWidget(self.pushButton_reading_file_no_gas)

        self.checkBox_download_no_gas = QCheckBox(self.groupBox_no_gas)
        self.checkBox_download_no_gas.setObjectName(u"checkBox_download_no_gas")
        self.checkBox_download_no_gas.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.checkBox_download_no_gas.sizePolicy().hasHeightForWidth())
        self.checkBox_download_no_gas.setSizePolicy(sizePolicy3)
        self.checkBox_download_no_gas.setMinimumSize(QSize(0, 30))
        self.checkBox_download_no_gas.setMaximumSize(QSize(16777215, 30))
        self.checkBox_download_no_gas.setStyleSheet(u"")
        self.checkBox_download_no_gas.setChecked(False)
        self.checkBox_download_no_gas.setTristate(False)

        self.layout_no_gas.addWidget(self.checkBox_download_no_gas)


        self.layout_data_body.addWidget(self.groupBox_no_gas)

        self.groupBox_with_gas = QGroupBox(self.widget_data_body)
        self.groupBox_with_gas.setObjectName(u"groupBox_with_gas")
        self.groupBox_with_gas.setMinimumSize(QSize(0, 50))
        self.groupBox_with_gas.setSizeIncrement(QSize(0, 0))
        self.groupBox_with_gas.setBaseSize(QSize(0, 0))
        self.groupBox_with_gas.setFont(font2)
        self.groupBox_with_gas.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.groupBox_with_gas.setMouseTracking(False)
        self.groupBox_with_gas.setTabletTracking(False)
        self.groupBox_with_gas.setStyleSheet(u"")
        self.groupBox_with_gas.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_with_gas.setFlat(True)
        self.groupBox_with_gas.setCheckable(False)
        self.layout_with_gas = QHBoxLayout(self.groupBox_with_gas)
        self.layout_with_gas.setSpacing(5)
        self.layout_with_gas.setObjectName(u"layout_with_gas")
        self.layout_with_gas.setContentsMargins(5, 5, 5, 5)
        self.label_text_file_name_with_gas = QLabel(self.groupBox_with_gas)
        self.label_text_file_name_with_gas.setObjectName(u"label_text_file_name_with_gas")
        sizePolicy2.setHeightForWidth(self.label_text_file_name_with_gas.sizePolicy().hasHeightForWidth())
        self.label_text_file_name_with_gas.setSizePolicy(sizePolicy2)
        self.label_text_file_name_with_gas.setMinimumSize(QSize(0, 30))
        self.label_text_file_name_with_gas.setMaximumSize(QSize(16777215, 30))
        self.label_text_file_name_with_gas.setFont(font2)
        self.label_text_file_name_with_gas.setStyleSheet(u"")
        self.label_text_file_name_with_gas.setTextFormat(Qt.TextFormat.AutoText)
        self.label_text_file_name_with_gas.setScaledContents(False)

        self.layout_with_gas.addWidget(self.label_text_file_name_with_gas)

        self.pushButton_reading_file_with_gas = QPushButton(self.groupBox_with_gas)
        self.pushButton_reading_file_with_gas.setObjectName(u"pushButton_reading_file_with_gas")
        sizePolicy3.setHeightForWidth(self.pushButton_reading_file_with_gas.sizePolicy().hasHeightForWidth())
        self.pushButton_reading_file_with_gas.setSizePolicy(sizePolicy3)
        self.pushButton_reading_file_with_gas.setMinimumSize(QSize(0, 30))
        self.pushButton_reading_file_with_gas.setMaximumSize(QSize(16777215, 30))
        self.pushButton_reading_file_with_gas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_reading_file_with_gas.setStyleSheet(u"")
        self.pushButton_reading_file_with_gas.setIconSize(QSize(25, 25))

        self.layout_with_gas.addWidget(self.pushButton_reading_file_with_gas)

        self.checkBox_download_with_gas = QCheckBox(self.groupBox_with_gas)
        self.checkBox_download_with_gas.setObjectName(u"checkBox_download_with_gas")
        self.checkBox_download_with_gas.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.checkBox_download_with_gas.sizePolicy().hasHeightForWidth())
        self.checkBox_download_with_gas.setSizePolicy(sizePolicy3)
        self.checkBox_download_with_gas.setMinimumSize(QSize(0, 30))
        self.checkBox_download_with_gas.setMaximumSize(QSize(16777215, 30))
        self.checkBox_download_with_gas.setStyleSheet(u"")
        self.checkBox_download_with_gas.setChecked(False)
        self.checkBox_download_with_gas.setTristate(False)

        self.layout_with_gas.addWidget(self.checkBox_download_with_gas)


        self.layout_data_body.addWidget(self.groupBox_with_gas)

        self.pushButton_reset_spectrum_data = QPushButton(self.widget_data_body)
        self.pushButton_reset_spectrum_data.setObjectName(u"pushButton_reset_spectrum_data")
        self.pushButton_reset_spectrum_data.setMinimumSize(QSize(148, 25))
        self.pushButton_reset_spectrum_data.setMaximumSize(QSize(148, 16777215))
        self.pushButton_reset_spectrum_data.setFont(font2)
        self.pushButton_reset_spectrum_data.setStyleSheet(u"QPushButton:hover {\n"
"	border: none;												/* \u0431\u0435\u0437 \u0433\u0440\u0430\u043d\u0438\u0446 */\n"
"}")

        self.layout_data_body.addWidget(self.pushButton_reset_spectrum_data, 0, Qt.AlignmentFlag.AlignHCenter)

        self.groupBox_frequency_range = QGroupBox(self.widget_data_body)
        self.groupBox_frequency_range.setObjectName(u"groupBox_frequency_range")
        self.groupBox_frequency_range.setMinimumSize(QSize(0, 100))
        self.groupBox_frequency_range.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_frequency_range.setSizeIncrement(QSize(0, 0))
        self.groupBox_frequency_range.setBaseSize(QSize(0, 0))
        self.groupBox_frequency_range.setFont(font2)
        self.groupBox_frequency_range.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.groupBox_frequency_range.setMouseTracking(False)
        self.groupBox_frequency_range.setTabletTracking(False)
        self.groupBox_frequency_range.setStyleSheet(u"")
        self.groupBox_frequency_range.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_frequency_range.setFlat(True)
        self.groupBox_frequency_range.setCheckable(False)
        self.layout_frequency_range = QVBoxLayout(self.groupBox_frequency_range)
        self.layout_frequency_range.setSpacing(0)
        self.layout_frequency_range.setObjectName(u"layout_frequency_range")
        self.layout_frequency_range.setContentsMargins(5, 5, 5, 5)
        self.radioButton_all_range = QRadioButton(self.groupBox_frequency_range)
        self.radioButton_all_range.setObjectName(u"radioButton_all_range")
        self.radioButton_all_range.setMinimumSize(QSize(0, 30))
        self.radioButton_all_range.setFont(font2)
        self.radioButton_all_range.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_all_range.setStyleSheet(u"")
        self.radioButton_all_range.setChecked(True)

        self.layout_frequency_range.addWidget(self.radioButton_all_range)

        self.radioButton_selected_range = QRadioButton(self.groupBox_frequency_range)
        self.radioButton_selected_range.setObjectName(u"radioButton_selected_range")
        self.radioButton_selected_range.setMinimumSize(QSize(0, 30))
        self.radioButton_selected_range.setFont(font2)
        self.radioButton_selected_range.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.radioButton_selected_range.setStyleSheet(u"")
        self.radioButton_selected_range.setChecked(False)

        self.layout_frequency_range.addWidget(self.radioButton_selected_range)

        self.widget_start_range = QWidget(self.groupBox_frequency_range)
        self.widget_start_range.setObjectName(u"widget_start_range")
        sizePolicy2.setHeightForWidth(self.widget_start_range.sizePolicy().hasHeightForWidth())
        self.widget_start_range.setSizePolicy(sizePolicy2)
        self.widget_start_range.setMinimumSize(QSize(0, 30))
        self.widget_start_range.setStyleSheet(u"")
        self.layout_start_range = QHBoxLayout(self.widget_start_range)
        self.layout_start_range.setSpacing(0)
        self.layout_start_range.setObjectName(u"layout_start_range")
        self.layout_start_range.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout_start_range.setContentsMargins(0, 0, 0, 0)
        self.label_text_start_range = QLabel(self.widget_start_range)
        self.label_text_start_range.setObjectName(u"label_text_start_range")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_text_start_range.sizePolicy().hasHeightForWidth())
        self.label_text_start_range.setSizePolicy(sizePolicy5)
        self.label_text_start_range.setMinimumSize(QSize(0, 30))
        self.label_text_start_range.setFont(font2)

        self.layout_start_range.addWidget(self.label_text_start_range)

        self.lineEdit_start_range = QLineEdit(self.widget_start_range)
        self.lineEdit_start_range.setObjectName(u"lineEdit_start_range")
        self.lineEdit_start_range.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.lineEdit_start_range.sizePolicy().hasHeightForWidth())
        self.lineEdit_start_range.setSizePolicy(sizePolicy6)
        self.lineEdit_start_range.setMinimumSize(QSize(0, 30))
        self.lineEdit_start_range.setMaximumSize(QSize(120, 30))
        self.lineEdit_start_range.setFont(font2)
        self.lineEdit_start_range.setStyleSheet(u"")
        self.lineEdit_start_range.setText(u"22308")
        self.lineEdit_start_range.setMaxLength(10)
        self.lineEdit_start_range.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_start_range.setDragEnabled(False)

        self.layout_start_range.addWidget(self.lineEdit_start_range)

        self.label_text_units_start_range = QLabel(self.widget_start_range)
        self.label_text_units_start_range.setObjectName(u"label_text_units_start_range")
        sizePolicy5.setHeightForWidth(self.label_text_units_start_range.sizePolicy().hasHeightForWidth())
        self.label_text_units_start_range.setSizePolicy(sizePolicy5)
        self.label_text_units_start_range.setMinimumSize(QSize(0, 30))
        self.label_text_units_start_range.setFont(font2)
        self.label_text_units_start_range.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_start_range.addWidget(self.label_text_units_start_range)


        self.layout_frequency_range.addWidget(self.widget_start_range)

        self.widget_end_range = QWidget(self.groupBox_frequency_range)
        self.widget_end_range.setObjectName(u"widget_end_range")
        sizePolicy2.setHeightForWidth(self.widget_end_range.sizePolicy().hasHeightForWidth())
        self.widget_end_range.setSizePolicy(sizePolicy2)
        self.widget_end_range.setMinimumSize(QSize(0, 30))
        self.widget_end_range.setStyleSheet(u"")
        self.layout_end_range = QHBoxLayout(self.widget_end_range)
        self.layout_end_range.setSpacing(0)
        self.layout_end_range.setObjectName(u"layout_end_range")
        self.layout_end_range.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout_end_range.setContentsMargins(0, 0, 0, 0)
        self.label_text_end_range = QLabel(self.widget_end_range)
        self.label_text_end_range.setObjectName(u"label_text_end_range")
        sizePolicy5.setHeightForWidth(self.label_text_end_range.sizePolicy().hasHeightForWidth())
        self.label_text_end_range.setSizePolicy(sizePolicy5)
        self.label_text_end_range.setMinimumSize(QSize(0, 30))
        self.label_text_end_range.setFont(font2)
        self.label_text_end_range.setStyleSheet(u"")

        self.layout_end_range.addWidget(self.label_text_end_range)

        self.lineEdit_end_range = QLineEdit(self.widget_end_range)
        self.lineEdit_end_range.setObjectName(u"lineEdit_end_range")
        self.lineEdit_end_range.setEnabled(False)
        sizePolicy6.setHeightForWidth(self.lineEdit_end_range.sizePolicy().hasHeightForWidth())
        self.lineEdit_end_range.setSizePolicy(sizePolicy6)
        self.lineEdit_end_range.setMinimumSize(QSize(120, 30))
        self.lineEdit_end_range.setMaximumSize(QSize(120, 30))
        self.lineEdit_end_range.setFont(font2)
        self.lineEdit_end_range.setStyleSheet(u"")
        self.lineEdit_end_range.setText(u"22342")
        self.lineEdit_end_range.setMaxLength(10)
        self.lineEdit_end_range.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_end_range.setDragEnabled(False)

        self.layout_end_range.addWidget(self.lineEdit_end_range)

        self.label_text_units_end_range = QLabel(self.widget_end_range)
        self.label_text_units_end_range.setObjectName(u"label_text_units_end_range")
        sizePolicy5.setHeightForWidth(self.label_text_units_end_range.sizePolicy().hasHeightForWidth())
        self.label_text_units_end_range.setSizePolicy(sizePolicy5)
        self.label_text_units_end_range.setMinimumSize(QSize(0, 30))
        self.label_text_units_end_range.setFont(font2)
        self.label_text_units_end_range.setStyleSheet(u"")
        self.label_text_units_end_range.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_end_range.addWidget(self.label_text_units_end_range)


        self.layout_frequency_range.addWidget(self.widget_end_range)


        self.layout_data_body.addWidget(self.groupBox_frequency_range)


        self.layout_menu_data.addWidget(self.widget_data_body)


        self.Layout_scroll_menu.addWidget(self.widget_data)

        self.verticalSpacer_menu = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.Layout_scroll_menu.addItem(self.verticalSpacer_menu)

        self.scrollArea_menu_body.setWidget(self.scrollAreaWidgetContents)

        self.layout_menu_body.addWidget(self.scrollArea_menu_body)


        self.layout_menu.addWidget(self.widget_menu_body)

        self.widget_menu_bottom = QWidget(self.widget_menu)
        self.widget_menu_bottom.setObjectName(u"widget_menu_bottom")
        self.widget_menu_bottom.setMinimumSize(QSize(0, 80))
        self.widget_menu_bottom.setStyleSheet(u"QWidget#widget_menu_bottom{\n"
"	border: none;												/* \u0431\u0435\u0437 \u0433\u0440\u0430\u043d\u0438\u0446 */\n"
"	border-top:2px solid rgb(255, 255, 255);	/* \u0421 \u043f\u0440\u0430\u0432\u043e\u0439 \u043a\u0440\u0430\u0441\u043d\u043e\u0439 \u0440\u0430\u043d\u0438\u0446\u0435\u0439 */\n"
"}")
        self.layout_menu_bottom = QVBoxLayout(self.widget_menu_bottom)
        self.layout_menu_bottom.setSpacing(2)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 5, 0, 0)
        self.pushButton_close_open_table = QPushButton(self.widget_menu_bottom)
        self.pushButton_close_open_table.setObjectName(u"pushButton_close_open_table")
        sizePolicy1.setHeightForWidth(self.pushButton_close_open_table.sizePolicy().hasHeightForWidth())
        self.pushButton_close_open_table.setSizePolicy(sizePolicy1)
        self.pushButton_close_open_table.setMinimumSize(QSize(0, 35))
        self.pushButton_close_open_table.setMaximumSize(QSize(16777215, 35))
        self.pushButton_close_open_table.setFont(font1)
        self.pushButton_close_open_table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_close_open_table.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_close_open_table.setAutoFillBackground(False)
        self.pushButton_close_open_table.setStyleSheet(u"")
        self.pushButton_close_open_table.setIconSize(QSize(0, 0))
        self.pushButton_close_open_table.setCheckable(True)
        self.pushButton_close_open_table.setChecked(True)
        self.pushButton_close_open_table.setAutoRepeat(False)
        self.pushButton_close_open_table.setAutoExclusive(False)
        self.pushButton_close_open_table.setFlat(False)

        self.layout_menu_bottom.addWidget(self.pushButton_close_open_table)

        self.pushButton_menu_calculate = QPushButton(self.widget_menu_bottom)
        self.pushButton_menu_calculate.setObjectName(u"pushButton_menu_calculate")
        sizePolicy1.setHeightForWidth(self.pushButton_menu_calculate.sizePolicy().hasHeightForWidth())
        self.pushButton_menu_calculate.setSizePolicy(sizePolicy1)
        self.pushButton_menu_calculate.setMinimumSize(QSize(0, 35))
        self.pushButton_menu_calculate.setMaximumSize(QSize(16777215, 35))
        self.pushButton_menu_calculate.setFont(font1)
        self.pushButton_menu_calculate.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_menu_calculate.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_menu_calculate.setAutoFillBackground(False)
        self.pushButton_menu_calculate.setStyleSheet(u"")
        self.pushButton_menu_calculate.setIconSize(QSize(0, 0))
        self.pushButton_menu_calculate.setCheckable(True)
        self.pushButton_menu_calculate.setChecked(True)
        self.pushButton_menu_calculate.setAutoRepeat(False)
        self.pushButton_menu_calculate.setAutoExclusive(False)
        self.pushButton_menu_calculate.setFlat(False)

        self.layout_menu_bottom.addWidget(self.pushButton_menu_calculate)


        self.layout_menu.addWidget(self.widget_menu_bottom)


        self.layout_style_sheet.addWidget(self.widget_menu)

        self.widget_main = QWidget(self.widget_style_sheet)
        self.widget_main.setObjectName(u"widget_main")
        self.widget_main.setStyleSheet(u"")
        self.layout_main = QVBoxLayout(self.widget_main)
        self.layout_main.setSpacing(0)
        self.layout_main.setObjectName(u"layout_main")
        self.layout_main.setContentsMargins(0, 0, 0, 0)
        self.widget_main_body = QWidget(self.widget_main)
        self.widget_main_body.setObjectName(u"widget_main_body")
        self.widget_main_body.setStyleSheet(u"")
        self.layout__main_body = QHBoxLayout(self.widget_main_body)
        self.layout__main_body.setSpacing(0)
        self.layout__main_body.setObjectName(u"layout__main_body")
        self.layout__main_body.setContentsMargins(0, 0, 0, 0)
        self.widget_plotting = QWidget(self.widget_main_body)
        self.widget_plotting.setObjectName(u"widget_plotting")
        self.widget_plotting.setStyleSheet(u"QWidget{\n"
"background-color: rgb(240, 240, 240);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.layout_plotting = QVBoxLayout(self.widget_plotting)
        self.layout_plotting.setSpacing(0)
        self.layout_plotting.setObjectName(u"layout_plotting")
        self.layout_plotting.setContentsMargins(0, 0, 0, 0)
        self.widget_plot_1 = QWidget(self.widget_plotting)
        self.widget_plot_1.setObjectName(u"widget_plot_1")
        self.layout_plot_1 = QVBoxLayout(self.widget_plot_1)
        self.layout_plot_1.setSpacing(0)
        self.layout_plot_1.setObjectName(u"layout_plot_1")
        self.layout_plot_1.setContentsMargins(0, 0, 0, 0)

        self.layout_plotting.addWidget(self.widget_plot_1)


        self.layout__main_body.addWidget(self.widget_plotting)

        self.widget_right = QWidget(self.widget_main_body)
        self.widget_right.setObjectName(u"widget_right")
        self.widget_right.setMinimumSize(QSize(265, 0))
        self.widget_right.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget_right)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_load_result = QPushButton(self.widget_right)
        self.pushButton_load_result.setObjectName(u"pushButton_load_result")
        sizePolicy1.setHeightForWidth(self.pushButton_load_result.sizePolicy().hasHeightForWidth())
        self.pushButton_load_result.setSizePolicy(sizePolicy1)
        self.pushButton_load_result.setMinimumSize(QSize(0, 35))
        self.pushButton_load_result.setMaximumSize(QSize(16777215, 35))
        self.pushButton_load_result.setFont(font1)
        self.pushButton_load_result.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_load_result.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_load_result.setAutoFillBackground(False)
        self.pushButton_load_result.setStyleSheet(u"")
        self.pushButton_load_result.setIconSize(QSize(0, 0))
        self.pushButton_load_result.setCheckable(True)
        self.pushButton_load_result.setChecked(True)
        self.pushButton_load_result.setAutoRepeat(False)
        self.pushButton_load_result.setAutoExclusive(False)
        self.pushButton_load_result.setFlat(False)

        self.verticalLayout.addWidget(self.pushButton_load_result)

        self.widget_table = QWidget(self.widget_right)
        self.widget_table.setObjectName(u"widget_table")
        self.widget_table.setStyleSheet(u"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 - \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d*/\n"
"QCheckBox::indicator:unchecked {\n"
"	/* \u0412\u044b\u0431\u043e\u0440 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438*/\n"
"	image: url(:/table_checkbox/resource/table_checkbox/var2_color/no_red_24dp.svg);\n"
"}\n"
"\n"
"/* \u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435 -  \u0432\u044b\u0431\u0440\u0430\u043d*/\n"
"QCheckBox::indicator:checked {\n"
"	/* \u0412\u044b\u0431\u043e\u0440 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0438*/\n"
"	image: url(:/table_checkbox/resource/table_checkbox/var2_color/yes_green_24dp.svg);\n"
"}\n"
"")
        self.layout_table = QVBoxLayout(self.widget_table)
        self.layout_table.setSpacing(0)
        self.layout_table.setObjectName(u"layout_table")
        self.layout_table.setContentsMargins(2, 0, 0, 0)
        self.widget_table_view_mode = QWidget(self.widget_table)
        self.widget_table_view_mode.setObjectName(u"widget_table_view_mode")
        self.horizontalLayout = QHBoxLayout(self.widget_table_view_mode)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(2, 2, 0, 2)
        self.label_text_select_table_display = QLabel(self.widget_table_view_mode)
        self.label_text_select_table_display.setObjectName(u"label_text_select_table_display")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_text_select_table_display.sizePolicy().hasHeightForWidth())
        self.label_text_select_table_display.setSizePolicy(sizePolicy7)

        self.horizontalLayout.addWidget(self.label_text_select_table_display)

        self.comboBox_select_table_view = QComboBox(self.widget_table_view_mode)
        icon1 = QIcon()
        icon1.addFile(u":/multi_check_box/resource/multi_check_box_svg/all_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBox_select_table_view.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/multi_check_box/resource/multi_check_box_svg/undefined_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBox_select_table_view.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/multi_check_box/resource/multi_check_box_svg/no_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBox_select_table_view.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/multi_check_box/resource/multi_check_box_svg/yes_green_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBox_select_table_view.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/multi_check_box/resource/multi_check_box_svg/yes_blue_24dp.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.comboBox_select_table_view.addItem(icon5, "")
        self.comboBox_select_table_view.setObjectName(u"comboBox_select_table_view")
        self.comboBox_select_table_view.setMaximumSize(QSize(45, 16777215))
        self.comboBox_select_table_view.setStyleSheet(u"QWidget{\n"
"selection-background-color: rgb(191, 191, 191);\n"
"\n"
"}")
        self.comboBox_select_table_view.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        self.comboBox_select_table_view.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.comboBox_select_table_view)


        self.layout_table.addWidget(self.widget_table_view_mode)

        self.tableWidget_frequency_absorption = QTableWidget(self.widget_table)
        self.tableWidget_frequency_absorption.setObjectName(u"tableWidget_frequency_absorption")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.tableWidget_frequency_absorption.sizePolicy().hasHeightForWidth())
        self.tableWidget_frequency_absorption.setSizePolicy(sizePolicy8)
        self.tableWidget_frequency_absorption.setStyleSheet(u"")
        self.tableWidget_frequency_absorption.setFrameShape(QFrame.Shape.NoFrame)
        self.tableWidget_frequency_absorption.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tableWidget_frequency_absorption.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tableWidget_frequency_absorption.setEditTriggers(QAbstractItemView.EditTrigger.AnyKeyPressed|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tableWidget_frequency_absorption.setTabKeyNavigation(False)
        self.tableWidget_frequency_absorption.setProperty(u"showDropIndicator", False)
        self.tableWidget_frequency_absorption.setDragDropOverwriteMode(False)
        self.tableWidget_frequency_absorption.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidget_frequency_absorption.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidget_frequency_absorption.setIconSize(QSize(0, 0))
        self.tableWidget_frequency_absorption.setShowGrid(True)
        self.tableWidget_frequency_absorption.setSortingEnabled(False)
        self.tableWidget_frequency_absorption.setRowCount(0)
        self.tableWidget_frequency_absorption.setColumnCount(0)
        self.tableWidget_frequency_absorption.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_frequency_absorption.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget_frequency_absorption.horizontalHeader().setStretchLastSection(False)

        self.layout_table.addWidget(self.tableWidget_frequency_absorption)

        self.widget_bottom = QWidget(self.widget_table)
        self.widget_bottom.setObjectName(u"widget_bottom")
        sizePolicy5.setHeightForWidth(self.widget_bottom.sizePolicy().hasHeightForWidth())
        self.widget_bottom.setSizePolicy(sizePolicy5)
        self.widget_bottom.setMinimumSize(QSize(0, 0))
        self.widget_bottom.setStyleSheet(u"")
        self.layout_bottom = QVBoxLayout(self.widget_bottom)
        self.layout_bottom.setSpacing(0)
        self.layout_bottom.setObjectName(u"layout_bottom")
        self.layout_bottom.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout_bottom.setContentsMargins(0, 0, 0, 0)
        self.label_statistics_on_selected_frequencies = QLabel(self.widget_bottom)
        self.label_statistics_on_selected_frequencies.setObjectName(u"label_statistics_on_selected_frequencies")
        sizePolicy4.setHeightForWidth(self.label_statistics_on_selected_frequencies.sizePolicy().hasHeightForWidth())
        self.label_statistics_on_selected_frequencies.setSizePolicy(sizePolicy4)
        self.label_statistics_on_selected_frequencies.setMinimumSize(QSize(0, 30))
        self.label_statistics_on_selected_frequencies.setStyleSheet(u"")

        self.layout_bottom.addWidget(self.label_statistics_on_selected_frequencies)

        self.groupBox_window_view = QGroupBox(self.widget_bottom)
        self.groupBox_window_view.setObjectName(u"groupBox_window_view")
        self.groupBox_window_view.setMinimumSize(QSize(0, 90))
        self.groupBox_window_view.setMaximumSize(QSize(16777215, 16777215))
        self.groupBox_window_view.setSizeIncrement(QSize(0, 0))
        self.groupBox_window_view.setBaseSize(QSize(0, 0))
        self.groupBox_window_view.setFont(font2)
        self.groupBox_window_view.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.groupBox_window_view.setMouseTracking(False)
        self.groupBox_window_view.setTabletTracking(False)
        self.groupBox_window_view.setStyleSheet(u"")
        self.groupBox_window_view.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox_window_view.setFlat(True)
        self.groupBox_window_view.setCheckable(False)
        self.layout_frequency_range_3 = QVBoxLayout(self.groupBox_window_view)
        self.layout_frequency_range_3.setSpacing(0)
        self.layout_frequency_range_3.setObjectName(u"layout_frequency_range_3")
        self.layout_frequency_range_3.setContentsMargins(5, 0, 5, 0)
        self.label_text_window_width = QLabel(self.groupBox_window_view)
        self.label_text_window_width.setObjectName(u"label_text_window_width")
        self.label_text_window_width.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_frequency_range_3.addWidget(self.label_text_window_width)

        self.widget_input_window_view = QWidget(self.groupBox_window_view)
        self.widget_input_window_view.setObjectName(u"widget_input_window_view")
        sizePolicy2.setHeightForWidth(self.widget_input_window_view.sizePolicy().hasHeightForWidth())
        self.widget_input_window_view.setSizePolicy(sizePolicy2)
        self.widget_input_window_view.setMinimumSize(QSize(0, 30))
        self.widget_input_window_view.setStyleSheet(u"")
        self.layout_start_range_8 = QHBoxLayout(self.widget_input_window_view)
        self.layout_start_range_8.setSpacing(0)
        self.layout_start_range_8.setObjectName(u"layout_start_range_8")
        self.layout_start_range_8.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout_start_range_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_window_width = QLineEdit(self.widget_input_window_view)
        self.lineEdit_window_width.setObjectName(u"lineEdit_window_width")
        self.lineEdit_window_width.setEnabled(True)
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.lineEdit_window_width.sizePolicy().hasHeightForWidth())
        self.lineEdit_window_width.setSizePolicy(sizePolicy9)
        self.lineEdit_window_width.setMinimumSize(QSize(0, 30))
        self.lineEdit_window_width.setMaximumSize(QSize(120, 30))
        self.lineEdit_window_width.setStyleSheet(u"")
        self.lineEdit_window_width.setText(u"10")
        self.lineEdit_window_width.setMaxLength(10)
        self.lineEdit_window_width.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_window_width.setDragEnabled(False)

        self.layout_start_range_8.addWidget(self.lineEdit_window_width)

        self.label_text_units_window_width = QLabel(self.widget_input_window_view)
        self.label_text_units_window_width.setObjectName(u"label_text_units_window_width")
        sizePolicy.setHeightForWidth(self.label_text_units_window_width.sizePolicy().hasHeightForWidth())
        self.label_text_units_window_width.setSizePolicy(sizePolicy)
        self.label_text_units_window_width.setMinimumSize(QSize(0, 30))
        self.label_text_units_window_width.setStyleSheet(u"")
        self.label_text_units_window_width.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout_start_range_8.addWidget(self.label_text_units_window_width)


        self.layout_frequency_range_3.addWidget(self.widget_input_window_view)


        self.layout_bottom.addWidget(self.groupBox_window_view)

        self.pushButton_save_table_to_file = QPushButton(self.widget_bottom)
        self.pushButton_save_table_to_file.setObjectName(u"pushButton_save_table_to_file")
        sizePolicy1.setHeightForWidth(self.pushButton_save_table_to_file.sizePolicy().hasHeightForWidth())
        self.pushButton_save_table_to_file.setSizePolicy(sizePolicy1)
        self.pushButton_save_table_to_file.setMinimumSize(QSize(0, 35))
        self.pushButton_save_table_to_file.setMaximumSize(QSize(16777215, 35))
        self.pushButton_save_table_to_file.setFont(font1)
        self.pushButton_save_table_to_file.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_save_table_to_file.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_save_table_to_file.setAutoFillBackground(False)
        self.pushButton_save_table_to_file.setStyleSheet(u"")
        self.pushButton_save_table_to_file.setIconSize(QSize(0, 0))
        self.pushButton_save_table_to_file.setCheckable(True)
        self.pushButton_save_table_to_file.setChecked(True)
        self.pushButton_save_table_to_file.setAutoRepeat(False)
        self.pushButton_save_table_to_file.setAutoExclusive(False)
        self.pushButton_save_table_to_file.setFlat(False)

        self.layout_bottom.addWidget(self.pushButton_save_table_to_file)


        self.layout_table.addWidget(self.widget_bottom)


        self.verticalLayout.addWidget(self.widget_table)


        self.layout__main_body.addWidget(self.widget_right)

        self.layout__main_body.setStretch(0, 1)

        self.layout_main.addWidget(self.widget_main_body)


        self.layout_style_sheet.addWidget(self.widget_main)


        self.layout_dialog_main.addWidget(self.widget_style_sheet)


        self.retranslateUi(Dialog)
        self.pushButton_data_header.clicked["bool"].connect(self.widget_data_body.setVisible)
        self.radioButton_selected_range.toggled.connect(self.lineEdit_start_range.setEnabled)
        self.radioButton_selected_range.toggled.connect(self.lineEdit_end_range.setEnabled)
        self.pushButton_close_open_table.clicked["bool"].connect(self.widget_right.setVisible)
        self.pushButton_neural_network_heade.toggled.connect(self.widget_neural_network_body.setVisible)
        self.checkBox_download_with_gas.toggled.connect(self.pushButton_reading_file_no_gas.setVisible)

        self.pushButton_neural_network_heade.setDefault(False)
        self.pushButton_data_header.setDefault(False)
        self.pushButton_close_open_table.setDefault(False)
        self.pushButton_menu_calculate.setDefault(False)
        self.pushButton_load_result.setDefault(False)
        self.pushButton_save_table_to_file.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 c \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435\u043c \u043d\u0435\u0439\u0440\u043e\u043d\u043d\u043e\u0439 \u0441\u0435\u0442\u0438", None))
        self.label_imag_app.setText("")
        self.label_text_app_name.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u0442\u0435\u043a\u0442\u043e\u0440", None))
#if QT_CONFIG(accessibility)
        self.pushButton_neural_network_heade.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_neural_network_heade.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0439\u0440\u043e\u043d\u043d\u0430\u044f \u0441\u0435\u0442\u044c", None))
        self.label_text_neural_network.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442 \u0444\u0430\u0439\u043b\u0430", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_reading_file_neural_network.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.pushButton_reading_file_neural_network.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.pushButton_reading_file_neural_network.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_reading_file_neural_network.setText("")
#if QT_CONFIG(whatsthis)
        self.checkBox_download_neural_network.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.checkBox_download_neural_network.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.checkBox_download_neural_network.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.checkBox_download_neural_network.setText("")
        self.label_parameters_neural_network.setText("")
#if QT_CONFIG(accessibility)
        self.pushButton_data_header.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_data_header.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u043d\u043d\u044b\u0435", None))
        self.groupBox_no_gas.setTitle(QCoreApplication.translate("Dialog", u"\u0411\u0435\u0437 \u0438\u0441\u0441\u043b\u0435\u0434\u0443\u0435\u043c\u043e\u0433\u043e \u0432\u0435\u0449\u0435\u0441\u0442\u0432\u0430", None))
        self.label_text_file_name_no_gas.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442 \u0444\u0430\u0439\u043b\u0430", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_reading_file_no_gas.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.pushButton_reading_file_no_gas.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.pushButton_reading_file_no_gas.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_reading_file_no_gas.setText("")
#if QT_CONFIG(whatsthis)
        self.checkBox_download_no_gas.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.checkBox_download_no_gas.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.checkBox_download_no_gas.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.checkBox_download_no_gas.setText("")
        self.groupBox_with_gas.setTitle(QCoreApplication.translate("Dialog", u"\u0421 \u0438\u0441\u0441\u043b\u0435\u0434\u0443\u0435\u043c\u044b\u043c \u0432\u0435\u0449\u0435\u0441\u0442\u0432\u043e\u043c", None))
        self.label_text_file_name_with_gas.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442 \u0444\u0430\u0439\u043b\u0430", None))
        self.pushButton_reading_file_with_gas.setText("")
        self.checkBox_download_with_gas.setText("")
        self.pushButton_reset_spectrum_data.setText(QCoreApplication.translate("Dialog", u"\u0421\u0431\u0440\u043e\u0441 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.groupBox_frequency_range.setTitle(QCoreApplication.translate("Dialog", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d \u0447\u0430\u0441\u0442\u043e\u0442", None))
        self.radioButton_all_range.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0441\u044c", None))
        self.radioButton_selected_range.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u043a\u043e\u0442\u043e\u0440\u044b\u0435", None))
        self.label_text_start_range.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442: ", None))
        self.label_text_units_start_range.setText(QCoreApplication.translate("Dialog", u" [\u041c\u0413\u0446]", None))
        self.label_text_end_range.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e: ", None))
        self.label_text_units_end_range.setText(QCoreApplication.translate("Dialog", u" [\u041c\u0413\u0446]", None))
#if QT_CONFIG(accessibility)
        self.pushButton_close_open_table.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_close_open_table.setText(QCoreApplication.translate("Dialog", u"\u0422\u0430\u0431\u043b\u0438\u0446\u0430", None))
#if QT_CONFIG(accessibility)
        self.pushButton_menu_calculate.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_menu_calculate.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0447\u0438\u0441\u043b\u0438\u0442\u044c", None))
#if QT_CONFIG(accessibility)
        self.pushButton_load_result.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_load_result.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.label_text_select_table_display.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u043c\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0445: ", None))
        self.comboBox_select_table_view.setItemText(0, "")
        self.comboBox_select_table_view.setItemText(1, "")
        self.comboBox_select_table_view.setItemText(2, "")
        self.comboBox_select_table_view.setItemText(3, "")
        self.comboBox_select_table_view.setItemText(4, "")

        self.comboBox_select_table_view.setCurrentText("")
        self.label_statistics_on_selected_frequencies.setText("")
        self.groupBox_window_view.setTitle(QCoreApplication.translate("Dialog", u"\u041e\u043a\u043d\u043e \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0430", None))
        self.label_text_window_width.setText(QCoreApplication.translate("Dialog", u"\u0428\u0438\u0440\u0438\u043d\u0430 \u043e\u043a\u043d\u0430 \u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0430 \n"
" \u043d\u0430\u0439\u0434\u0435\u043d\u043d\u044b\u0445 \u0447\u0430\u0441\u0442\u043e\u0442", None))
        self.label_text_units_window_width.setText(QCoreApplication.translate("Dialog", u" [\u041c\u0413\u0446]", None))
#if QT_CONFIG(accessibility)
        self.pushButton_save_table_to_file.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.pushButton_save_table_to_file.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0432 \u0444\u0430\u0439\u043b", None))
    # retranslateUi

