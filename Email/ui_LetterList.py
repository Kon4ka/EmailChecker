# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LetterList.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QWidget)
import rc_auto_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(752, 371)
        Form.setStyleSheet(u"background-color: rgb(21, 25, 31);\n"
"font: \"Copperplate Gothic Light\";")
        self.mailListTriggerListTable = QTableView(Form)
        self.mailListTriggerListTable.setObjectName(u"mailListTriggerListTable")
        self.mailListTriggerListTable.setGeometry(QRect(20, 40, 711, 321))
        self.mailListTriggerListTable.setStyleSheet(u"QTableView {\n"
"         Color: white; /* text color in the table */\n"
"         Gridline-color: black; /*The inner frame color*/\n"
"         Background-color: rgb(33, 39, 48); /* background color in the table*/\n"
"    alternate-background-color: rgb(42, 50, 62);\n"
"         Selection-color: white; /* The text color of the selected area*/\n"
"         Selection-background-color: rgb(84, 89, 97); /*The background color of the selected area*/\n"
"    border: 2px groove rgb(12, 14, 17);\n"
"    border-radius: 30px;\n"
"    padding: 2px 4px;\n"
"}\n"
"\n"
"QHeaderView {\n"
"    color: white;\n"
"    font: bold 10pt;\n"
"         Background-color: rgb(50, 70, 90);/*Set the background color of the header blank area*/\n"
"    border: 0px solid rgb(144, 144, 144);\n"
"    border: 0px solid rgb(191,191,191);\n"
"    border-left-color: rgba(255, 255, 255, 0);\n"
"    border-top-color: rgba(255, 255, 255, 0);\n"
"    border-radius:10px;\n"
"    min-height:29px;\n"
"}\n"
"\n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar"
                        ":vertical {\n"
"	border: none;\n"
"    background: rgb(27, 32, 40);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(77, 87, 99);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(107, 117, 139);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(117, 135, 150);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(37, 42, 50);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"/*QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}*/\n"
"QScrollBar::sub-line:vertical:pressed {	\n"
"	background-color: rgb(47, 52, 60);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::a"
                        "dd-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(37, 42, 50);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"/*QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}*/\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color:  rgb(47, 52, 60);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 0, 761, 31))
        self.widget_2.setStyleSheet(u"background-color: rgb(35, 41, 51);")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(650, -10, 101, 51))
        self.widget_4.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid transparent;\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgb(20, 25, 34);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mailListTriggerCollapseButton = QPushButton(self.widget_4)
        self.mailListTriggerCollapseButton.setObjectName(u"mailListTriggerCollapseButton")
        icon = QIcon()
        icon.addFile(u":/Light/Assets/Light/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.mailListTriggerCollapseButton.setIcon(icon)
        self.mailListTriggerCollapseButton.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.mailListTriggerCollapseButton)

        self.mailListTriggerCloseButton = QPushButton(self.widget_4)
        self.mailListTriggerCloseButton.setObjectName(u"mailListTriggerCloseButton")
        icon1 = QIcon()
        icon1.addFile(u":/Light/Assets/Light/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.mailListTriggerCloseButton.setIcon(icon1)
        self.mailListTriggerCloseButton.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.mailListTriggerCloseButton)

        self.mailListTriggerCloseButton.raise_()
        self.mailListTriggerCollapseButton.raise_()
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 131, 18))
        self.label.setStyleSheet(u"color: rgb(145, 160, 187);\n"
"font: \"Copperplate Gothic Light\";\n"
"font-size: 14px;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mailListTriggerCollapseButton.setText("")
        self.mailListTriggerCloseButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0430\u0436\u043d\u044b\u0435 \u043f\u0438\u0441\u044c\u043c\u0430", None))
    # retranslateUi

