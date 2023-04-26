# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Auth.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import rc_auto_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(488, 391)
        Form.setWindowOpacity(0.800000000000000)
        Form.setStyleSheet(u"background-color: rgb(21, 25, 31);\n"
"font: \"Copperplate Gothic Light\";")
        self.Window = QWidget(Form)
        self.Window.setObjectName(u"Window")
        self.Window.setGeometry(QRect(0, 20, 491, 351))
        font = QFont()
        font.setFamilies([u"Copperplate Gothic Light"])
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        self.Window.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(self.Window)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Image_2 = QWidget(self.Window)
        self.Image_2.setObjectName(u"Image_2")
        self.horizontalLayout_5 = QHBoxLayout(self.Image_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget_5 = QWidget(self.Image_2)
        self.widget_5.setObjectName(u"widget_5")

        self.horizontalLayout_6.addWidget(self.widget_5)

        self.label_4 = QLabel(self.Image_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(61, 61))
        self.label_4.setPixmap(QPixmap(u":/Lighter/Assets/Light/user.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)

        self.horizontalLayout_6.addWidget(self.label_4)

        self.widget_6 = QWidget(self.Image_2)
        self.widget_6.setObjectName(u"widget_6")

        self.horizontalLayout_6.addWidget(self.widget_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout_3.addWidget(self.Image_2)

        self.Logpass_2 = QWidget(self.Window)
        self.Logpass_2.setObjectName(u"Logpass_2")
        self.horizontalLayout_7 = QHBoxLayout(self.Logpass_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_7 = QWidget(self.Logpass_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"")
        self.emailLine = QLineEdit(self.widget_7)
        self.emailLine.setObjectName(u"emailLine")
        self.emailLine.setGeometry(QRect(120, 10, 321, 35))
        self.emailLine.setFont(font)
        self.emailLine.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(79, 117, 145) ;\n"
"color: #FFF;\n"
"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"padding-bottom: 4px;\n"
"}")
        self.label_5 = QLabel(self.widget_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 20, 46, 15))
        font1 = QFont()
        font1.setFamilies([u"Copperplate Gothic Light"])
        font1.setBold(False)
        font1.setItalic(False)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")

        self.verticalLayout_4.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.Logpass_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"")
        self.label_6 = QLabel(self.widget_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 10, 55, 21))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_6.setMargin(2)
        self.passwordLine = QLineEdit(self.widget_8)
        self.passwordLine.setObjectName(u"passwordLine")
        self.passwordLine.setGeometry(QRect(120, 10, 321, 35))
        self.passwordLine.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid rgb(79, 117, 145) ;\n"
"color: #FFF;\n"
"border-radius: 15px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"padding-bottom: 4px;\n"
"}")

        self.verticalLayout_4.addWidget(self.widget_8)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addWidget(self.Logpass_2)

        self.Remember_2 = QWidget(self.Window)
        self.Remember_2.setObjectName(u"Remember_2")
        self.Remember_2.setMaximumSize(QSize(451, 90))
        self.rememverMeChecker = QCheckBox(self.Remember_2)
        self.rememverMeChecker.setObjectName(u"rememverMeChecker")
        self.rememverMeChecker.setGeometry(QRect(30, 30, 151, 24))
        self.rememverMeChecker.setStyleSheet(u"QCheckBox{\n"
"color: rgb(202, 206, 216);\n"
"font-size: 14px;\n"
"font: \"Copperplate Gothic Light\";\n"
"}\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"border : 2px solid rgb(79, 117, 145);\n"
"width : 20px;\n"
"height : 20px;\n"
"border-radius : 10px;\n"
"}\n"
"\n"
"\n"
"QCheckBox::hover {\n"
"	color: #9ebad6\n"
"}\n"
"\n"
"\n"
"QCheckBox::hover::checked {\n"
"	border: solid #232933;\n"
"}\n"
"/*\n"
"QCheckBox:hover::unchecked {\n"
"	border: solid rgb(79, 117, 145);\n"
"}\n"
"\n"
"\n"
"QCheckBox:indicator: {\n"
"	border: 4px\n"
"}\n"
"\n"
"QCheckBox:indicator:unchecked:hover {\n"
"	color:#576e84\n"
"}\n"
"*/\n"
"\n"
"QCheckBox::indicator::checked\n"
"{\n"
"	image: url(:/Lighter/Assets/Light/check.svg);\n"
"}\n"
"")
        self.AuthLoginButton = QPushButton(self.Remember_2)
        self.AuthLoginButton.setObjectName(u"AuthLoginButton")
        self.AuthLoginButton.setGeometry(QRect(280, 30, 141, 41))
        self.AuthLoginButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(166, 177, 211);\n"
"	background-color: rgb(38, 45, 58);\n"
"	border-left: 1px solid rgb(57, 79, 100);\n"
"	border-right: 1px solid rgb(51, 54, 60);	\n"
"	border-bottom: 3px solid rgb(28, 31, 46);\n"
"\n"
"	font-size: 14px;\n"
"	font: \"Copperplate Gothic Light\";\n"
"\n"
"	border-radius: 10px\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(25, 45, 64);\n"
"	border-left: 2px solid rgb(37, 46, 53);\n"
"	border-right: 2px solid rgb(31, 34, 40);	\n"
"	border-bottom: 3px solid rgb(18, 21, 26);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"	background-color: rgb(20, 25, 34);\n"
"	border-left: 2px solid rgb(5, 26, 33);\n"
"	border-right: 2px solid rgb(5, 24, 30);	\n"
"	border-bottom: 3px solid rgb(5, 21, 26);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Lighter/Assets/Light/corner-down-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.AuthLoginButton.setIcon(icon)
        self.authErrorLaber = QLabel(self.Remember_2)
        self.authErrorLaber.setObjectName(u"authErrorLaber")
        self.authErrorLaber.setGeometry(QRect(34, 0, 401, 21))
        self.authErrorLaber.setFont(font1)
        self.authErrorLaber.setStyleSheet(u"color: rgb(250, 100, 100);\n"
"font-size: 14px;")
        self.authErrorLaber.setAlignment(Qt.AlignCenter)
        self.authErrorLaber.setMargin(2)

        self.verticalLayout_3.addWidget(self.Remember_2)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 501, 31))
        self.widget_2.setStyleSheet(u"background-color: rgb(35, 41, 51);")
        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(390, -10, 101, 51))
        self.widget_9.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid transparent;\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgb(20, 25, 34);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.authCollapseButton = QPushButton(self.widget_9)
        self.authCollapseButton.setObjectName(u"authCollapseButton")
        icon1 = QIcon()
        icon1.addFile(u":/Lighter/Assets/Light/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.authCollapseButton.setIcon(icon1)
        self.authCollapseButton.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.authCollapseButton)

        self.authCloseButton = QPushButton(self.widget_9)
        self.authCloseButton.setObjectName(u"authCloseButton")
        icon2 = QIcon()
        icon2.addFile(u":/Lighter/Assets/Light/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.authCloseButton.setIcon(icon2)
        self.authCloseButton.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.authCloseButton)

        self.authCloseButton.raise_()
        self.authCollapseButton.raise_()
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 131, 18))
        self.label_2.setStyleSheet(u"color: rgb(145, 160, 187);\n"
"font: \"Copperplate Gothic Light\";\n"
"font-size: 14px;")
        self.label_2.raise_()
        self.widget_9.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText("")
        self.emailLine.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u0430\u0434\u0440\u0435\u0441 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.passwordLine.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0432\u0430\u0448 \u043f\u0430\u0440\u043e\u043b\u044c \u043e\u0442 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u043d\u043d\u043e\u0439 \u043f\u043e\u0447\u0442\u044b", None))
        self.rememverMeChecker.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u043c\u0435\u043d\u044f", None))
        self.AuthLoginButton.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.authErrorLaber.setText("")
        self.authCollapseButton.setText("")
        self.authCloseButton.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
    # retranslateUi

