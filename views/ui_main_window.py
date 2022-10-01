# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QSize(400, 600))
        MainWindow.setMaximumSize(QSize(400, 600))
        MainWindow.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(MainWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.centralWidget = QFrame(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setFrameShape(QFrame.StyledPanel)
        self.centralWidget.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.background_Frame = QFrame(self.centralWidget)
        self.background_Frame.setObjectName(u"background_Frame")
        self.background_Frame.setAutoFillBackground(False)
        self.background_Frame.setStyleSheet(u"background-color: #F4F4F4;")
        self.background_Frame.setFrameShape(QFrame.StyledPanel)
        self.background_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_Frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.top_content_frame = QFrame(self.background_Frame)
        self.top_content_frame.setObjectName(u"top_content_frame")
        self.top_content_frame.setStyleSheet(u"")
        self.top_content_frame.setFrameShape(QFrame.StyledPanel)
        self.top_content_frame.setFrameShadow(QFrame.Raised)
        self.top_bar_frame = QFrame(self.top_content_frame)
        self.top_bar_frame.setObjectName(u"top_bar_frame")
        self.top_bar_frame.setGeometry(QRect(0, 0, 581, 161))
        self.top_bar_frame.setStyleSheet(u"background-color:  rgb(232, 164, 42);")
        self.top_bar_frame.setFrameShape(QFrame.StyledPanel)
        self.top_bar_frame.setFrameShadow(QFrame.Raised)
        self.top_text = QLabel(self.top_bar_frame)
        self.top_text.setObjectName(u"top_text")
        self.top_text.setGeometry(QRect(40, 20, 291, 41))
        font = QFont()
        font.setFamilies([u"Ubuntu Mono"])
        font.setPointSize(16)
        font.setBold(True)
        self.top_text.setFont(font)
        self.top_text.setStyleSheet(u"color: rgb(65, 65, 65);")
        self.top_text_2 = QLabel(self.top_bar_frame)
        self.top_text_2.setObjectName(u"top_text_2")
        self.top_text_2.setGeometry(QRect(40, 90, 291, 41))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu Mono"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.top_text_2.setFont(font1)
        self.top_text_2.setLayoutDirection(Qt.LeftToRight)
        self.top_text_2.setStyleSheet(u"color: rgb(65, 65, 65);")
        self.top_text_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.content_frame = QFrame(self.top_content_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setGeometry(QRect(0, 160, 381, 421))
        self.content_frame.setAutoFillBackground(False)
        self.content_frame.setStyleSheet(u"")
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.content_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.num1_button = QPushButton(self.content_frame)
        self.num1_button.setObjectName(u"num1_button")
        self.num1_button.setMinimumSize(QSize(100, 100))
        self.num1_button.setMaximumSize(QSize(100, 100))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu Mono"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.num1_button.setFont(font2)
        self.num1_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #F4F4F4;\n"
"	color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton::hover{background-color: #E9E9E9}")

        self.gridLayout.addWidget(self.num1_button, 0, 1, 1, 1)

        self.suma_button = QPushButton(self.content_frame)
        self.suma_button.setObjectName(u"suma_button")
        self.suma_button.setMinimumSize(QSize(100, 100))
        self.suma_button.setMaximumSize(QSize(100, 100))
        self.suma_button.setFont(font2)
        self.suma_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #F4F4F4;\n"
"	color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton::hover{background-color: #E9E9E9}")

        self.gridLayout.addWidget(self.suma_button, 0, 3, 1, 1)

        self.num2_button = QPushButton(self.content_frame)
        self.num2_button.setObjectName(u"num2_button")
        self.num2_button.setMinimumSize(QSize(100, 100))
        self.num2_button.setMaximumSize(QSize(100, 100))
        self.num2_button.setFont(font2)
        self.num2_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #F4F4F4;\n"
"	color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton::hover{background-color: #E9E9E9}")

        self.gridLayout.addWidget(self.num2_button, 0, 2, 1, 1)

        self.num3_button = QPushButton(self.content_frame)
        self.num3_button.setObjectName(u"num3_button")
        self.num3_button.setMinimumSize(QSize(100, 100))
        self.num3_button.setMaximumSize(QSize(100, 100))
        self.num3_button.setFont(font2)
        self.num3_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #F4F4F4;\n"
"	color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton::hover{background-color: #E9E9E9}")

        self.gridLayout.addWidget(self.num3_button, 1, 1, 1, 1)

        self.num4_button = QPushButton(self.content_frame)
        self.num4_button.setObjectName(u"num4_button")
        self.num4_button.setMinimumSize(QSize(100, 100))
        self.num4_button.setMaximumSize(QSize(100, 100))
        self.num4_button.setFont(font2)
        self.num4_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #F4F4F4;\n"
"	color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton::hover{background-color: #E9E9E9}")

        self.gridLayout.addWidget(self.num4_button, 1, 2, 1, 1)

        self.resta_button = QPushButton(self.content_frame)
        self.resta_button.setObjectName(u"resta_button")
        self.resta_button.setMinimumSize(QSize(100, 100))
        self.resta_button.setMaximumSize(QSize(100, 100))
        self.resta_button.setFont(font2)
        self.resta_button.setStyleSheet(u"QPushButton{\n"
"	background-color: #F4F4F4;\n"
"	color: rgb(65, 65, 65);\n"
"}\n"
"QPushButton::hover{background-color: #E9E9E9}")

        self.gridLayout.addWidget(self.resta_button, 1, 3, 1, 1)


        self.verticalLayout_3.addWidget(self.top_content_frame)


        self.verticalLayout_2.addWidget(self.background_Frame)


        self.verticalLayout.addWidget(self.centralWidget)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Form", None))
        self.top_text.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.top_text_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.num1_button.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.suma_button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.num2_button.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.num3_button.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.num4_button.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.resta_button.setText(QCoreApplication.translate("MainWindow", u"-", None))
    # retranslateUi

