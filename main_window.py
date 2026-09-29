# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window_ver2.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 900)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setStyleSheet(u"background-color: #F0F0F0;\n"
"font-family: Aptos;\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_current_tick = QLabel(self.centralwidget)
        self.label_current_tick.setObjectName(u"label_current_tick")
        self.label_current_tick.setGeometry(QRect(10, 10, 250, 31))
        self.label_current_tick.setStyleSheet(u"color: #000000;\n"
"font-weight: bold;\n"
"font-size: 20px;")
        self.neurons_container = QFrame(self.centralwidget)
        self.neurons_container.setObjectName(u"neurons_container")
        self.neurons_container.setGeometry(QRect(10, 50, 1421, 551))
        self.neurons_container.setMouseTracking(False)
        self.neurons_container.setStyleSheet(u"background-color: #DCDCDC;")
        self.neurons_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.neurons_container.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_next_tick = QPushButton(self.centralwidget)
        self.btn_next_tick.setObjectName(u"btn_next_tick")
        self.btn_next_tick.setGeometry(QRect(20, 610, 121, 31))
        self.btn_next_tick.setStyleSheet(u"color: #000000;\n"
"background-color: #F5FFFA;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"border: 1px solid rgba(0, 0, 0, 0.4);\n"
"border-radius: 5px;")
        self.btn_reset = QPushButton(self.centralwidget)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setGeometry(QRect(1300, 10, 121, 31))
        self.btn_reset.setStyleSheet(u"color: #000000;\n"
"background-color: #F5FFFA;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"border: 1px solid rgba(0, 0, 0, 0.4);\n"
"border-radius: 5px;")
        self.btn_save_table_name = QPushButton(self.centralwidget)
        self.btn_save_table_name.setObjectName(u"btn_save_table_name")
        self.btn_save_table_name.setGeometry(QRect(20, 850, 121, 31))
        self.btn_save_table_name.setStyleSheet(u"color: #000000;\n"
"background-color: #F5FFFA;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"border: 1px solid rgba(0, 0, 0, 0.4);\n"
"border-radius: 5px;")
        self.btn_auto = QPushButton(self.centralwidget)
        self.btn_auto.setObjectName(u"btn_auto")
        self.btn_auto.setGeometry(QRect(210, 610, 121, 31))
        self.btn_auto.setStyleSheet(u"color: #000000;\n"
"background-color: #F5FFFA;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"border: 1px solid rgba(0, 0, 0, 0.4);\n"
"border-radius: 5px;")
        self.btn_jerk = QPushButton(self.centralwidget)
        self.btn_jerk.setObjectName(u"btn_jerk")
        self.btn_jerk.setGeometry(QRect(210, 690, 121, 31))
        self.btn_jerk.setStyleSheet(u"color: #000000;\n"
"background-color: #F5FFFA;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"border: 1px solid rgba(0, 0, 0, 0.4);\n"
"border-radius: 5px;")
        self.btn_visualization = QPushButton(self.centralwidget)
        self.btn_visualization.setObjectName(u"btn_visualization")
        self.btn_visualization.setGeometry(QRect(210, 850, 121, 31))
        self.btn_visualization.setStyleSheet(u"color: #000000;\n"
"background-color: #F5FFFA;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"border: 1px solid rgba(0, 0, 0, 0.4);\n"
"border-radius: 5px;")
        self.result_output = QTextBrowser(self.centralwidget)
        self.result_output.setObjectName(u"result_output")
        self.result_output.setGeometry(QRect(700, 610, 731, 281))
        self.result_output.setStyleSheet(u"background-color: #f8f9fa;       /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"border: 1px solid #dcdde1;       /* \u0410\u043a\u043a\u0443\u0440\u0430\u0442\u043d\u0430\u044f \u0442\u043e\u043d\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"border-radius: 6px;              /* \u0421\u043b\u0435\u0433\u043a\u0430 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"padding: 8px;                    /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0442\u0435\u043a\u0441\u0442\u0430 \u043e\u0442 \u043a\u0440\u0430\u0435\u0432 */\n"
"font-family: 'Segoe UI', sans-serif; /* \u041a\u0440\u0430\u0441\u0438\u0432\u044b\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"font-size: 13px;\n"
"color: #000000;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 810, 311, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_name_table = QLabel(self.layoutWidget)
        self.label_name_table.setObjectName(u"label_name_table")
        self.label_name_table.setStyleSheet(u"color: #000000;\n"
"font-weight: bold;\n"
"font-size: 15px;")

        self.horizontalLayout.addWidget(self.label_name_table)

        self.table_input_name = QLineEdit(self.layoutWidget)
        self.table_input_name.setObjectName(u"table_input_name")
        self.table_input_name.setStyleSheet(u"color: #000000;\n"
"background-color: #F8F9FA;\n"
"font-size: 15px;")

        self.horizontalLayout.addWidget(self.table_input_name)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 650, 311, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_number_jerk = QLabel(self.layoutWidget1)
        self.label_number_jerk.setObjectName(u"label_number_jerk")
        self.label_number_jerk.setStyleSheet(u"color: #000000;\n"
"font-weight: bold;\n"
"font-size: 15px;")

        self.horizontalLayout_2.addWidget(self.label_number_jerk)

        self.tick_input_number = QLineEdit(self.layoutWidget1)
        self.tick_input_number.setObjectName(u"tick_input_number")
        self.tick_input_number.setStyleSheet(u"color: #000000;\n"
"background-color: #F8F9FA;\n"
"font-size: 15px;")

        self.horizontalLayout_2.addWidget(self.tick_input_number)

        self.radio_rnd_break_box = QGroupBox(self.centralwidget)
        self.radio_rnd_break_box.setObjectName(u"radio_rnd_break_box")
        self.radio_rnd_break_box.setGeometry(QRect(500, 610, 191, 90))
        self.radio_rnd_break_box.setStyleSheet(u"/* 1. \u0421\u0422\u0418\u041b\u042c \u0414\u041b\u042f \u0421\u0410\u041c\u041e\u0419 \u0420\u0410\u041c\u041a\u0418 \u0418 \u0417\u0410\u0413\u041e\u041b\u041e\u0412\u041a\u0410 GROUP BOX */\n"
"QGroupBox {\n"
"    font-size: 14px;\n"
"    font-weight: 600;                    /* \u0414\u0435\u043b\u0430\u0435\u043c \u0442\u0435\u043a\u0441\u0442 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 \u043f\u043e\u043b\u0443\u0436\u0438\u0440\u043d\u044b\u043c */\n"
"    color: #000000;                      /* \u041a\u0440\u0430\u0441\u0438\u0432\u044b\u0439 \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439/\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: 1px solid #dcdde1;           /* \u0422\u043e\u043d\u043a\u0430\u044f \u0430\u043a\u043a\u0443\u0440\u0430\u0442\u043d\u0430\u044f \u043f\u0430\u0441\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;                  /* \u0421\u043e"
                        "\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043c\u044f\u0433\u043a\u043e\u0435 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    margin-top: 12px;                    /* \u041e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443, \u0447\u0442\u043e\u0431\u044b \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043d\u0435 \u043d\u0430\u043b\u0435\u0437\u0430\u043b \u043d\u0430 \u0440\u0430\u043c\u043a\u0443 */\n"
"    padding-top: 10px;                   /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u043e\u0442 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 \u0434\u043e \u043f\u0435\u0440\u0432\u043e\u0439 \u0440\u0430\u0434\u0438\u043e-\u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    background-color: #ffffff;           /* \u0411\u0435\u043b\u044b\u0439 \u0444\u043e\u043d \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0438 */\n"
""
                        "}\n"
"\n"
"/* 2. \u041d\u0410\u0421\u0422\u0420\u041e\u0419\u041a\u0410 \u0420\u0410\u0417\u041c\u0415\u0429\u0415\u041d\u0418\u042f \u0422\u0415\u041a\u0421\u0422\u0410 \u0417\u0410\u0413\u041e\u041b\u041e\u0412\u041a\u0410 */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;       /* \u0421\u043c\u0435\u0449\u0430\u0435\u043c \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0432 \u0432\u0435\u0440\u0445\u043d\u0438\u0439 \u043b\u0435\u0432\u044b\u0439 \u0443\u0433\u043e\u043b */\n"
"    left: 12px;                          /* \u041e\u0442\u0441\u0442\u0443\u043f \u0442\u0435\u043a\u0441\u0442\u0430 \u043e\u0442 \u043b\u0435\u0432\u043e\u0433\u043e \u043a\u0440\u0430\u044f */\n"
"    padding: 0 6px;                      /* \u0411\u0435\u043b\u043e\u0435 \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u043e \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430, \u0447\u0442\u043e\u0431\u044b \u0440\u0430\u043c\u043a\u0430"
                        " \u043f\u0440\u0435\u0440\u044b\u0432\u0430\u043b\u0430\u0441\u044c */\n"
"}\n"
"\n"
"/* 3. \u0421\u0422\u0418\u041b\u042c \u0420\u0410\u0414\u0418\u041e-\u041a\u041d\u041e\u041f\u041e\u041a \u0412\u041d\u0423\u0422\u0420\u0418 \u042d\u0422\u041e\u0413\u041e GROUP BOX */\n"
"QRadioButton {\n"
"    font-weight: normal;                 /* \u0421\u0431\u0440\u0430\u0441\u044b\u0432\u0430\u0435\u043c \u0436\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"    color: #000000;                      /* \u0421\u043f\u043e\u043a\u043e\u0439\u043d\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043e\u0431\u044b\u0447\u043d\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-size: 14px;\n"
"    spacing: 8px;                        /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0440"
                        "\u0443\u0433\u043b\u044b\u043c \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */\n"
"    padding-left: 6px;                   /* \u0421\u043b\u0435\u0433\u043a\u0430 \u043e\u0442\u043e\u0434\u0432\u0438\u0433\u0430\u0435\u043c \u043a\u043d\u043e\u043f\u043a\u0443 \u043e\u0442 \u043b\u0435\u0432\u043e\u0439 \u0440\u0430\u043c\u043a\u0438 */\n"
"    background-color: transparent;       /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u043e\u0434 \u043a\u043d\u043e\u043f\u043a\u0430\u043c\u0438 */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0441\u0430\u043c\u043e\u0433\u043e \u043a\u0440\u0443\u0433\u043b\u043e\u0433\u043e \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440\u0430 (\u043a\u043e\u0433\u0434\u0430 \u043a\u043d\u043e\u043f\u043a\u0430 \u041d\u0415 \u0432\u044b\u0431\u0440\u0430\u043d\u0430) */\n"
"QRadioButton::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border: "
                        "2px solid #cbd5e1;\n"
"    border-radius: 7px;                  /* \u0414\u0435\u043b\u0430\u0435\u043c \u0438\u0434\u0435\u0430\u043b\u044c\u043d\u043e \u043a\u0440\u0443\u0433\u043b\u044b\u043c (\u0440\u0430\u0434\u0438\u0443\u0441 = ~\u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u043e\u0442 15) */\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"/* \u042d\u0444\u0444\u0435\u043a\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 \u043d\u0430 \u0440\u0430\u0434\u0438\u043e-\u043a\u043d\u043e\u043f\u043a\u0443 */\n"
"QRadioButton::indicator:hover {\n"
"    border-color: #3498db;               /* \u0420\u0430\u043c\u043a\u0430 \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u0441\u0438\u043d\u0435\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"#radio_rnd_break_on::indicator:checked {\n"
"    border: 2px solid #808080;\n"
"    background"
                        "-color: #A9A9A9;\n"
"	image: url(none);\n"
"}\n"
"\n"
"#radio_rnd_break_off::indicator:checked {\n"
"    border: 2px solid #808080;\n"
"    background-color: #A9A9A9;\n"
"	image: url(none);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.radio_rnd_break_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radio_rnd_break_on = QRadioButton(self.radio_rnd_break_box)
        self.radio_rnd_break_on.setObjectName(u"radio_rnd_break_on")
        self.radio_rnd_break_on.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.radio_rnd_break_on)

        self.radio_rnd_break_off = QRadioButton(self.radio_rnd_break_box)
        self.radio_rnd_break_off.setObjectName(u"radio_rnd_break_off")
        self.radio_rnd_break_off.setChecked(True)

        self.verticalLayout.addWidget(self.radio_rnd_break_off)

        self.radio_new_db_box = QGroupBox(self.centralwidget)
        self.radio_new_db_box.setObjectName(u"radio_new_db_box")
        self.radio_new_db_box.setGeometry(QRect(20, 740, 191, 59))
        self.radio_new_db_box.setStyleSheet(u"/* 1. \u0421\u0422\u0418\u041b\u042c \u0414\u041b\u042f \u0421\u0410\u041c\u041e\u0419 \u0420\u0410\u041c\u041a\u0418 \u0418 \u0417\u0410\u0413\u041e\u041b\u041e\u0412\u041a\u0410 GROUP BOX */\n"
"QGroupBox {\n"
"    font-size: 14px;\n"
"    font-weight: 600;                    /* \u0414\u0435\u043b\u0430\u0435\u043c \u0442\u0435\u043a\u0441\u0442 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 \u043f\u043e\u043b\u0443\u0436\u0438\u0440\u043d\u044b\u043c */\n"
"    color: #000000;                      /* \u041a\u0440\u0430\u0441\u0438\u0432\u044b\u0439 \u0442\u0435\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439/\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    border: 1px solid #dcdde1;           /* \u0422\u043e\u043d\u043a\u0430\u044f \u0430\u043a\u043a\u0443\u0440\u0430\u0442\u043d\u0430\u044f \u043f\u0430\u0441\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;                  /* \u0421\u043e"
                        "\u0432\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0435 \u043c\u044f\u0433\u043a\u043e\u0435 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"    margin-top: 12px;                    /* \u041e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443, \u0447\u0442\u043e\u0431\u044b \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043d\u0435 \u043d\u0430\u043b\u0435\u0437\u0430\u043b \u043d\u0430 \u0440\u0430\u043c\u043a\u0443 */\n"
"    padding-top: 10px;                   /* \u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u043e\u0442\u0441\u0442\u0443\u043f \u043e\u0442 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 \u0434\u043e \u043f\u0435\u0440\u0432\u043e\u0439 \u0440\u0430\u0434\u0438\u043e-\u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    background-color: #ffffff;           /* \u0411\u0435\u043b\u044b\u0439 \u0444\u043e\u043d \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u0430\u0440\u0442\u043e\u0447\u043a\u0438 */\n"
""
                        "}\n"
"\n"
"/* 2. \u041d\u0410\u0421\u0422\u0420\u041e\u0419\u041a\u0410 \u0420\u0410\u0417\u041c\u0415\u0429\u0415\u041d\u0418\u042f \u0422\u0415\u041a\u0421\u0422\u0410 \u0417\u0410\u0413\u041e\u041b\u041e\u0412\u041a\u0410 */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;       /* \u0421\u043c\u0435\u0449\u0430\u0435\u043c \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0432 \u0432\u0435\u0440\u0445\u043d\u0438\u0439 \u043b\u0435\u0432\u044b\u0439 \u0443\u0433\u043e\u043b */\n"
"    left: 12px;                          /* \u041e\u0442\u0441\u0442\u0443\u043f \u0442\u0435\u043a\u0441\u0442\u0430 \u043e\u0442 \u043b\u0435\u0432\u043e\u0433\u043e \u043a\u0440\u0430\u044f */\n"
"    padding: 0 6px;                      /* \u0411\u0435\u043b\u043e\u0435 \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u043e \u0432\u043e\u043a\u0440\u0443\u0433 \u0442\u0435\u043a\u0441\u0442\u0430, \u0447\u0442\u043e\u0431\u044b \u0440\u0430\u043c\u043a\u0430"
                        " \u043f\u0440\u0435\u0440\u044b\u0432\u0430\u043b\u0430\u0441\u044c */\n"
"}\n"
"\n"
"/* 3. \u0421\u0422\u0418\u041b\u042c \u0420\u0410\u0414\u0418\u041e-\u041a\u041d\u041e\u041f\u041e\u041a \u0412\u041d\u0423\u0422\u0420\u0418 \u042d\u0422\u041e\u0413\u041e GROUP BOX */\n"
"QRadioButton {\n"
"    font-weight: normal;                 /* \u0421\u0431\u0440\u0430\u0441\u044b\u0432\u0430\u0435\u043c \u0436\u0438\u0440\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043e\u043a */\n"
"    color: #000000;                      /* \u0421\u043f\u043e\u043a\u043e\u0439\u043d\u044b\u0439 \u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0434\u043b\u044f \u043e\u0431\u044b\u0447\u043d\u043e\u0433\u043e \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    font-size: 14px;\n"
"    spacing: 8px;                        /* \u0420\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 \u043c\u0435\u0436\u0434\u0443 \u043a\u0440"
                        "\u0443\u0433\u043b\u044b\u043c \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440\u043e\u043c \u0438 \u0442\u0435\u043a\u0441\u0442\u043e\u043c */\n"
"    padding-left: 6px;                   /* \u0421\u043b\u0435\u0433\u043a\u0430 \u043e\u0442\u043e\u0434\u0432\u0438\u0433\u0430\u0435\u043c \u043a\u043d\u043e\u043f\u043a\u0443 \u043e\u0442 \u043b\u0435\u0432\u043e\u0439 \u0440\u0430\u043c\u043a\u0438 */\n"
"    background-color: transparent;       /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u043e\u0434 \u043a\u043d\u043e\u043f\u043a\u0430\u043c\u0438 */\n"
"}\n"
"\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0441\u0430\u043c\u043e\u0433\u043e \u043a\u0440\u0443\u0433\u043b\u043e\u0433\u043e \u0438\u043d\u0434\u0438\u043a\u0430\u0442\u043e\u0440\u0430 (\u043a\u043e\u0433\u0434\u0430 \u043a\u043d\u043e\u043f\u043a\u0430 \u041d\u0415 \u0432\u044b\u0431\u0440\u0430\u043d\u0430) */\n"
"QRadioButton::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    border: "
                        "2px solid #cbd5e1;\n"
"    border-radius: 7px;                  /* \u0414\u0435\u043b\u0430\u0435\u043c \u0438\u0434\u0435\u0430\u043b\u044c\u043d\u043e \u043a\u0440\u0443\u0433\u043b\u044b\u043c (\u0440\u0430\u0434\u0438\u0443\u0441 = ~\u043f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u043e\u0442 15) */\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"/* \u042d\u0444\u0444\u0435\u043a\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 \u043d\u0430 \u0440\u0430\u0434\u0438\u043e-\u043a\u043d\u043e\u043f\u043a\u0443 */\n"
"QRadioButton::indicator:hover {\n"
"    border-color: #3498db;               /* \u0420\u0430\u043c\u043a\u0430 \u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u0441\u044f \u0441\u0438\u043d\u0435\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"#radio_new_db_no::indicator:checked {\n"
"    border: 2px solid #808080;\n"
"    background-co"
                        "lor: #A9A9A9;\n"
"	image: url(none);\n"
"}\n"
"\n"
"#radio_new_db_yes::indicator:checked {\n"
"    border: 2px solid #808080;\n"
"    background-color: #A9A9A9;\n"
"	image: url(none);\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.radio_new_db_box)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.radio_new_db_no = QRadioButton(self.radio_new_db_box)
        self.radio_new_db_no.setObjectName(u"radio_new_db_no")
        self.radio_new_db_no.setChecked(True)

        self.horizontalLayout_3.addWidget(self.radio_new_db_no)

        self.radio_new_db_yes = QRadioButton(self.radio_new_db_box)
        self.radio_new_db_yes.setObjectName(u"radio_new_db_yes")

        self.horizontalLayout_3.addWidget(self.radio_new_db_yes)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simulating model", None))
        self.label_current_tick.setText(QCoreApplication.translate("MainWindow", u"Current tick: 0", None))
        self.btn_next_tick.setText(QCoreApplication.translate("MainWindow", u"Next tick", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_save_table_name.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_auto.setText(QCoreApplication.translate("MainWindow", u"Auto", None))
        self.btn_jerk.setText(QCoreApplication.translate("MainWindow", u"Jerk", None))
        self.btn_visualization.setText(QCoreApplication.translate("MainWindow", u"Visualization", None))
        self.result_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI','sans-serif'; font-size:13px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_name_table.setText(QCoreApplication.translate("MainWindow", u"Name of the table:", None))
        self.label_number_jerk.setText(QCoreApplication.translate("MainWindow", u"Number for a tick for a jerk:", None))
        self.radio_rnd_break_box.setTitle(QCoreApplication.translate("MainWindow", u"Random breakdowns", None))
        self.radio_rnd_break_on.setText(QCoreApplication.translate("MainWindow", u"on", None))
        self.radio_rnd_break_off.setText(QCoreApplication.translate("MainWindow", u"off", None))
        self.radio_new_db_box.setTitle(QCoreApplication.translate("MainWindow", u"Create new table?", None))
        self.radio_new_db_no.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.radio_new_db_yes.setText(QCoreApplication.translate("MainWindow", u"Yes", None))
    # retranslateUi

