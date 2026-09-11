# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

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
        self.neurons_container.setGeometry(QRect(10, 50, 1421, 571))
        self.neurons_container.setMouseTracking(False)
        self.neurons_container.setStyleSheet(u"background-color: #DCDCDC;")
        self.neurons_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.neurons_container.setFrameShadow(QFrame.Shadow.Raised)
        self.btn_next_tick = QPushButton(self.centralwidget)
        self.btn_next_tick.setObjectName(u"btn_next_tick")
        self.btn_next_tick.setGeometry(QRect(20, 630, 121, 31))
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
        self.btn_auto.setGeometry(QRect(210, 630, 121, 31))
        self.btn_auto.setStyleSheet(u"color: #000000;\n"
"background-color: #F5FFFA;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"border: 1px solid rgba(0, 0, 0, 0.4);\n"
"border-radius: 5px;")
        self.btn_jerk = QPushButton(self.centralwidget)
        self.btn_jerk.setObjectName(u"btn_jerk")
        self.btn_jerk.setGeometry(QRect(210, 710, 121, 31))
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
        self.result_output.setGeometry(QRect(700, 630, 731, 261))
        self.result_output.setStyleSheet(u"background-color: #f8f9fa;       /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u043f\u0440\u0438\u044f\u0442\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"border: 1px solid #dcdde1;       /* \u0410\u043a\u043a\u0443\u0440\u0430\u0442\u043d\u0430\u044f \u0442\u043e\u043d\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"border-radius: 6px;              /* \u0421\u043b\u0435\u0433\u043a\u0430 \u0441\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"padding: 8px;                    /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0442\u0435\u043a\u0441\u0442\u0430 \u043e\u0442 \u043a\u0440\u0430\u0435\u0432 */\n"
"font-family: 'Segoe UI', sans-serif; /* \u041a\u0440\u0430\u0441\u0438\u0432\u044b\u0439 \u0441\u0438\u0441\u0442\u0435\u043c\u043d\u044b\u0439 \u0448\u0440\u0438\u0444\u0442 */\n"
"font-size: 13px; \n"
"color: #000000;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 810, 311, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_name_table = QLabel(self.widget)
        self.label_name_table.setObjectName(u"label_name_table")
        self.label_name_table.setStyleSheet(u"color: #000000;\n"
"font-weight: bold;\n"
"font-size: 15px;")

        self.horizontalLayout.addWidget(self.label_name_table)

        self.table_input_name = QLineEdit(self.widget)
        self.table_input_name.setObjectName(u"table_input_name")
        self.table_input_name.setStyleSheet(u"color: #000000;\n"
"background-color: #F8F9FA;\n"
"font-size: 15px;")

        self.horizontalLayout.addWidget(self.table_input_name)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 670, 311, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_number_jerk = QLabel(self.widget1)
        self.label_number_jerk.setObjectName(u"label_number_jerk")
        self.label_number_jerk.setStyleSheet(u"color: #000000;\n"
"font-weight: bold;\n"
"font-size: 15px;")

        self.horizontalLayout_2.addWidget(self.label_number_jerk)

        self.tick_input_number = QLineEdit(self.widget1)
        self.tick_input_number.setObjectName(u"tick_input_number")
        self.tick_input_number.setStyleSheet(u"color: #000000;\n"
"background-color: #F8F9FA;\n"
"font-size: 15px;")

        self.horizontalLayout_2.addWidget(self.tick_input_number)

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
    # retranslateUi

