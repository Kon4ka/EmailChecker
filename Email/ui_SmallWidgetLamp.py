# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SmallWidgetLamp.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)
import rc_auto_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(250, 200)
        Form.setMinimumSize(QSize(250, 200))
        Form.setMaximumSize(QSize(250, 200))
        Form.setWindowOpacity(0.800000000000000)
        Form.setStyleSheet(u"background-color: rgb(44, 52, 65);")
        self.colorIndicator = QLabel(Form)
        self.colorIndicator.setObjectName(u"colorIndicator")
        self.colorIndicator.setEnabled(True)
        self.colorIndicator.setGeometry(QRect(20, 50, 101, 91))
        self.colorIndicator.setPixmap(QPixmap(u":/Custom/Assets/Custom/red.png"))
        self.smallWidgetMailListButton = QPushButton(Form)
        self.smallWidgetMailListButton.setObjectName(u"smallWidgetMailListButton")
        self.smallWidgetMailListButton.setGeometry(QRect(170, 70, 41, 41))
        self.smallWidgetMailListButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid transparent;\n"
"	border-radius: 10px\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgb(20, 25, 34);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Light/Assets/Light/mail.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.smallWidgetMailListButton.setIcon(icon)
        self.smallWidgetMailListButton.setIconSize(QSize(36, 36))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(130, 0, 121, 61))
        self.widget.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid transparent;\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgb(20, 25, 34);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.smallWidgetSettings = QPushButton(self.widget)
        self.smallWidgetSettings.setObjectName(u"smallWidgetSettings")
        icon1 = QIcon()
        icon1.addFile(u":/Light/Assets/Light/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.smallWidgetSettings.setIcon(icon1)
        self.smallWidgetSettings.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.smallWidgetSettings)

        self.smallWidgetCollapseButton = QPushButton(self.widget)
        self.smallWidgetCollapseButton.setObjectName(u"smallWidgetCollapseButton")
        icon2 = QIcon()
        icon2.addFile(u":/Light/Assets/Light/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.smallWidgetCollapseButton.setIcon(icon2)
        self.smallWidgetCollapseButton.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.smallWidgetCollapseButton)

        self.smallWidgetCloseButton = QPushButton(self.widget)
        self.smallWidgetCloseButton.setObjectName(u"smallWidgetCloseButton")
        icon3 = QIcon()
        icon3.addFile(u":/Light/Assets/Light/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.smallWidgetCloseButton.setIcon(icon3)
        self.smallWidgetCloseButton.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.smallWidgetCloseButton)

        self.username = QLabel(Form)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(20, 160, 211, 21))
        self.username.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;\n"
"font: \"Copperplate Gothic Light\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.colorIndicator.setText("")
        self.smallWidgetMailListButton.setText("")
        self.smallWidgetSettings.setText("")
        self.smallWidgetCollapseButton.setText("")
        self.smallWidgetCloseButton.setText("")
        self.username.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0447\u0442\u043e\u0432\u044b\u0439 \u044f\u0449\u0438\u043a", None))
    # retranslateUi

