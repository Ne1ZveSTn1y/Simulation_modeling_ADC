# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_graph_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1080, 675)
        Dialog.setStyleSheet(u"background-color: #F0F0F0;\n"
"font-family: Aptos;\n"
"")
        self.chart_container = QFrame(Dialog)
        self.chart_container.setObjectName(u"chart_container")
        self.chart_container.setGeometry(QRect(10, 10, 1061, 651))
        self.chart_container.setStyleSheet(u"#chart_container {\n"
"    background-color: #f8f9fa;         /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u043f\u0440\u0435\u043c\u0438\u0430\u043b\u044c\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1px solid #dcdde1;         /* \u0427\u0443\u0442\u044c \u0431\u043e\u043b\u0435\u0435 \u043e\u0442\u0447\u0435\u0442\u043b\u0438\u0432\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.chart_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.chart_container.setFrameShadow(QFrame.Shadow.Raised)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

