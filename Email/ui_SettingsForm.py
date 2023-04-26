# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsForm.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import rc_auto_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(587, 601)
        Form.setMinimumSize(QSize(587, 601))
        Form.setMaximumSize(QSize(587, 601))
        Form.setStyleSheet(u"background-color: rgb(21, 25, 31);\n"
"font: \"Copperplate Gothic Light\";")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 40, 567, 551))
        self.widget.setMinimumSize(QSize(567, 531))
        self.widget.setMaximumSize(QSize(1000, 1000))
        self.settingsChangeUserButton = QPushButton(self.widget)
        self.settingsChangeUserButton.setObjectName(u"settingsChangeUserButton")
        self.settingsChangeUserButton.setGeometry(QRect(20, 10, 531, 41))
        self.settingsChangeUserButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(166, 177, 211);\n"
"	background-color: rgb(38, 45, 58);\n"
"	border-left: 1px solid rgb(57, 79, 100);\n"
"	border-right: 1px solid rgb(51, 54, 60);	\n"
"	border-bottom: 3px solid rgb(28, 31, 46);\n"
"\n"
"	font-size: 16px;\n"
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
        icon.addFile(u":/Lighter/Assets/Light/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsChangeUserButton.setIcon(icon)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(20, 70, 531, 151))
        self.widget_3.setMinimumSize(QSize(521, 151))
        self.widget_3.setMaximumSize(QSize(531, 151))
        self.gridLayoutWidget = QWidget(self.widget_3)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 531, 131))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setFamilies([u"Copperplate Gothic Light"])
        font.setBold(False)
        font.setItalic(False)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_8.setMargin(2)

        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_7.setMargin(2)

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_6.setMargin(2)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.showHideWidgetChecker = QCheckBox(self.gridLayoutWidget)
        self.showHideWidgetChecker.setObjectName(u"showHideWidgetChecker")
        self.showHideWidgetChecker.setLayoutDirection(Qt.RightToLeft)
        self.showHideWidgetChecker.setStyleSheet(u"QCheckBox{\n"
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

        self.gridLayout.addWidget(self.showHideWidgetChecker, 2, 1, 1, 1)

        self.windowsStartChecker = QCheckBox(self.gridLayoutWidget)
        self.windowsStartChecker.setObjectName(u"windowsStartChecker")
        self.windowsStartChecker.setLayoutDirection(Qt.RightToLeft)
        self.windowsStartChecker.setStyleSheet(u"QCheckBox{\n"
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
"\n"
"QCheckBox::indicator::checked\n"
"{\n"
"	image: url(:/Lighter/Assets/Light/check.svg);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.windowsStartChecker, 1, 1, 1, 1)

        self.rememberMeChecker = QCheckBox(self.gridLayoutWidget)
        self.rememberMeChecker.setObjectName(u"rememberMeChecker")
        self.rememberMeChecker.setLayoutDirection(Qt.RightToLeft)
        self.rememberMeChecker.setStyleSheet(u"QCheckBox{\n"
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
        self.rememberMeChecker.setChecked(True)

        self.gridLayout.addWidget(self.rememberMeChecker, 0, 1, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(20, 220, 531, 251))
        self.widget_5.setStyleSheet(u"QLineEdit{\n"
"border: 2px solid  rgb(39, 77, 105) ;\n"
"color: #FFF;\n"
"border-radius: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"  color: rgb(75, 130, 160);	\n"
"  background-color: rgb(27,40,65);\n"
"  padding: 10px;\n"
"  selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"QComboBox {\n"
"    border: 2px solid rgb(39, 77, 105);\n"
"    border-radius: 10px;\n"
"    padding: 1px 20px 3px 5px;\n"
"    min-width: 6em;\n"
"	color: rgb(202, 206, 216);\n"
"	font-size: 14px;\n"
"	font: \"Copperplate Gothic Light\";\n"
"}\n"
"\n"
"QComboBox::drop-down \n"
"{;\n"
"	margin-left: -10px;\n"
"	margin-top: 2px;\n"
"	background-image: url(:/Lighter/Assets/Light/chevron-down.svg);\n"
"    border: 0px;\n"
"}\n"
"\n"
"\n"
"QLabel {\n"
"	font: \"Copperplate Gothic Light\";\n"
"	color: rgb(202, 206, 216);\n"
"	font-size: 16px;\n"
"}\n"
"")
        self.gridLayoutWidget_2 = QWidget(self.widget_5)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 531, 234))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.whereComboBox_1 = QComboBox(self.gridLayoutWidget_2)
        self.whereComboBox_1.addItem("")
        self.whereComboBox_1.addItem("")
        self.whereComboBox_1.addItem("")
        self.whereComboBox_1.addItem("")
        self.whereComboBox_1.setObjectName(u"whereComboBox_1")
        self.whereComboBox_1.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.whereComboBox_1, 1, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 0, 1, 1)

        self.whereComboBox_4 = QComboBox(self.gridLayoutWidget_2)
        self.whereComboBox_4.addItem("")
        self.whereComboBox_4.addItem("")
        self.whereComboBox_4.addItem("")
        self.whereComboBox_4.addItem("")
        self.whereComboBox_4.setObjectName(u"whereComboBox_4")
        self.whereComboBox_4.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.whereComboBox_4, 4, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_5.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.lineEdit_5, 5, 0, 1, 1)

        self.whereComboBox_6 = QComboBox(self.gridLayoutWidget_2)
        self.whereComboBox_6.addItem("")
        self.whereComboBox_6.addItem("")
        self.whereComboBox_6.addItem("")
        self.whereComboBox_6.addItem("")
        self.whereComboBox_6.setObjectName(u"whereComboBox_6")
        self.whereComboBox_6.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.whereComboBox_6, 6, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_4.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.lineEdit_4, 4, 0, 1, 1)

        self.lineEdit_1 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_1.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.lineEdit_1, 1, 0, 1, 1)

        self.whereComboBox_5 = QComboBox(self.gridLayoutWidget_2)
        self.whereComboBox_5.addItem("")
        self.whereComboBox_5.addItem("")
        self.whereComboBox_5.addItem("")
        self.whereComboBox_5.addItem("")
        self.whereComboBox_5.setObjectName(u"whereComboBox_5")
        self.whereComboBox_5.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.whereComboBox_5, 5, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_3.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.lineEdit_3, 3, 0, 1, 1)

        self.whereComboBox_3 = QComboBox(self.gridLayoutWidget_2)
        self.whereComboBox_3.addItem("")
        self.whereComboBox_3.addItem("")
        self.whereComboBox_3.addItem("")
        self.whereComboBox_3.addItem("")
        self.whereComboBox_3.setObjectName(u"whereComboBox_3")
        self.whereComboBox_3.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.whereComboBox_3, 3, 1, 1, 1)

        self.whereComboBox_2 = QComboBox(self.gridLayoutWidget_2)
        self.whereComboBox_2.addItem("")
        self.whereComboBox_2.addItem("")
        self.whereComboBox_2.addItem("")
        self.whereComboBox_2.addItem("")
        self.whereComboBox_2.setObjectName(u"whereComboBox_2")
        self.whereComboBox_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.whereComboBox_2, 2, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(16777215, 31))
        self.lineEdit_6.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.lineEdit_6, 6, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_1 = QLabel(self.gridLayoutWidget_2)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setLayoutDirection(Qt.LeftToRight)
        self.label_1.setStyleSheet(u"")
        self.label_1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_1, 0, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)

        self.colorComboBox_1 = QComboBox(self.gridLayoutWidget_2)
        icon1 = QIcon()
        icon1.addFile(u":/Custom/Assets/Custom/combo_red.png", QSize(), QIcon.Normal, QIcon.Off)
        self.colorComboBox_1.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/Custom/Assets/Custom/combo_Green.png", QSize(), QIcon.Normal, QIcon.Off)
        self.colorComboBox_1.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/Custom/Assets/Custom/combo_blue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.colorComboBox_1.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/Custom/Assets/Custom/combo_yellow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.colorComboBox_1.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/Custom/Assets/Custom/combo_azure.png", QSize(), QIcon.Normal, QIcon.Off)
        self.colorComboBox_1.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/Custom/Assets/Custom/combo_purple.png", QSize(), QIcon.Normal, QIcon.Off)
        self.colorComboBox_1.addItem(icon6, "")
        self.colorComboBox_1.setObjectName(u"colorComboBox_1")
        self.colorComboBox_1.setMinimumSize(QSize(143, 0))
        self.colorComboBox_1.setMaximumSize(QSize(121, 29))
        self.colorComboBox_1.setToolTipDuration(-5)
        self.colorComboBox_1.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.colorComboBox_1, 1, 2, 1, 1)

        self.colorComboBox_2 = QComboBox(self.gridLayoutWidget_2)
        self.colorComboBox_2.addItem(icon1, "")
        self.colorComboBox_2.addItem(icon2, "")
        self.colorComboBox_2.addItem(icon3, "")
        self.colorComboBox_2.addItem(icon4, "")
        self.colorComboBox_2.addItem(icon5, "")
        self.colorComboBox_2.addItem(icon6, "")
        self.colorComboBox_2.setObjectName(u"colorComboBox_2")
        self.colorComboBox_2.setMinimumSize(QSize(143, 0))
        self.colorComboBox_2.setMaximumSize(QSize(121, 29))
        self.colorComboBox_2.setToolTipDuration(-5)
        self.colorComboBox_2.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.colorComboBox_2, 2, 2, 1, 1)

        self.colorComboBox_3 = QComboBox(self.gridLayoutWidget_2)
        self.colorComboBox_3.addItem(icon1, "")
        self.colorComboBox_3.addItem(icon2, "")
        self.colorComboBox_3.addItem(icon3, "")
        self.colorComboBox_3.addItem(icon4, "")
        self.colorComboBox_3.addItem(icon5, "")
        self.colorComboBox_3.addItem(icon6, "")
        self.colorComboBox_3.setObjectName(u"colorComboBox_3")
        self.colorComboBox_3.setMinimumSize(QSize(143, 0))
        self.colorComboBox_3.setMaximumSize(QSize(121, 29))
        self.colorComboBox_3.setToolTipDuration(-5)
        self.colorComboBox_3.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.colorComboBox_3, 3, 2, 1, 1)

        self.colorComboBox_4 = QComboBox(self.gridLayoutWidget_2)
        self.colorComboBox_4.addItem(icon1, "")
        self.colorComboBox_4.addItem(icon2, "")
        self.colorComboBox_4.addItem(icon3, "")
        self.colorComboBox_4.addItem(icon4, "")
        self.colorComboBox_4.addItem(icon5, "")
        self.colorComboBox_4.addItem(icon6, "")
        self.colorComboBox_4.setObjectName(u"colorComboBox_4")
        self.colorComboBox_4.setMinimumSize(QSize(143, 0))
        self.colorComboBox_4.setMaximumSize(QSize(121, 29))
        self.colorComboBox_4.setToolTipDuration(-5)
        self.colorComboBox_4.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.colorComboBox_4, 4, 2, 1, 1)

        self.colorComboBox_5 = QComboBox(self.gridLayoutWidget_2)
        self.colorComboBox_5.addItem(icon1, "")
        self.colorComboBox_5.addItem(icon2, "")
        self.colorComboBox_5.addItem(icon3, "")
        self.colorComboBox_5.addItem(icon4, "")
        self.colorComboBox_5.addItem(icon5, "")
        self.colorComboBox_5.addItem(icon6, "")
        self.colorComboBox_5.setObjectName(u"colorComboBox_5")
        self.colorComboBox_5.setMinimumSize(QSize(143, 0))
        self.colorComboBox_5.setMaximumSize(QSize(121, 29))
        self.colorComboBox_5.setToolTipDuration(-5)
        self.colorComboBox_5.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.colorComboBox_5, 5, 2, 1, 1)

        self.colorComboBox_6 = QComboBox(self.gridLayoutWidget_2)
        self.colorComboBox_6.addItem(icon1, "")
        self.colorComboBox_6.addItem(icon2, "")
        self.colorComboBox_6.addItem(icon3, "")
        self.colorComboBox_6.addItem(icon4, "")
        self.colorComboBox_6.addItem(icon5, "")
        self.colorComboBox_6.addItem(icon6, "")
        self.colorComboBox_6.setObjectName(u"colorComboBox_6")
        self.colorComboBox_6.setMinimumSize(QSize(143, 0))
        self.colorComboBox_6.setMaximumSize(QSize(121, 29))
        self.colorComboBox_6.setToolTipDuration(-5)
        self.colorComboBox_6.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.colorComboBox_6, 6, 2, 1, 1)

        self.settingsMailWorkButton = QPushButton(self.widget)
        self.settingsMailWorkButton.setObjectName(u"settingsMailWorkButton")
        self.settingsMailWorkButton.setGeometry(QRect(30, 480, 241, 51))
        self.settingsMailWorkButton.setStyleSheet(u"QPushButton {\n"
"	color: rgb(166, 177, 211);\n"
"	background-color: rgb(38, 45, 58);\n"
"	border-left: 1px solid rgb(57, 79, 100);\n"
"	border-right: 1px solid rgb(51, 54, 60);	\n"
"	border-bottom: 3px solid rgb(28, 31, 46);\n"
"\n"
"	font-size: 16px;\n"
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
        icon7 = QIcon()
        icon7.addFile(u":/Lighter/Assets/Light/folder.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsMailWorkButton.setIcon(icon7)
        self.settingsSaveAndExitButton = QPushButton(self.widget)
        self.settingsSaveAndExitButton.setObjectName(u"settingsSaveAndExitButton")
        self.settingsSaveAndExitButton.setGeometry(QRect(380, 480, 161, 51))
        self.settingsSaveAndExitButton.setStyleSheet(u"QPushButton {\n"
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
        icon8 = QIcon()
        icon8.addFile(u":/Lighter/Assets/Light/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsSaveAndExitButton.setIcon(icon8)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-10, 0, 611, 31))
        self.widget_2.setStyleSheet(u"background-color: rgb(35, 41, 51);")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(480, -10, 121, 41))
        self.widget_4.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid transparent;\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgb(20, 25, 34);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.settingsCollapseButton = QPushButton(self.widget_4)
        self.settingsCollapseButton.setObjectName(u"settingsCollapseButton")
        icon9 = QIcon()
        icon9.addFile(u":/Lighter/Assets/Light/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsCollapseButton.setIcon(icon9)
        self.settingsCollapseButton.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.settingsCollapseButton)

        self.settingsCloseButton = QPushButton(self.widget_4)
        self.settingsCloseButton.setObjectName(u"settingsCloseButton")
        icon10 = QIcon()
        icon10.addFile(u":/Lighter/Assets/Light/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsCloseButton.setIcon(icon10)
        self.settingsCloseButton.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.settingsCloseButton)

        self.settingsCloseButton.raise_()
        self.settingsCollapseButton.raise_()
        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 131, 18))
        self.label_4.setStyleSheet(u"color: rgb(145, 160, 187);\n"
"font: \"Copperplate Gothic Light\";\n"
"font-size: 14px;")

        self.retranslateUi(Form)

        self.whereComboBox_1.setCurrentIndex(-1)
        self.whereComboBox_4.setCurrentIndex(-1)
        self.whereComboBox_6.setCurrentIndex(-1)
        self.whereComboBox_5.setCurrentIndex(-1)
        self.whereComboBox_3.setCurrentIndex(-1)
        self.whereComboBox_2.setCurrentIndex(-1)
        self.colorComboBox_1.setCurrentIndex(0)
        self.colorComboBox_2.setCurrentIndex(1)
        self.colorComboBox_3.setCurrentIndex(2)
        self.colorComboBox_4.setCurrentIndex(3)
        self.colorComboBox_5.setCurrentIndex(4)
        self.colorComboBox_6.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.settingsChangeUserButton.setText(QCoreApplication.translate("Form", u"  \u0421\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c/\u0441\u043f\u0440\u044f\u0442\u0430\u0442\u044c \u0412\u0438\u0434\u0436\u0435\u0442", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u0443\u0441\u043a\u0430\u0442\u044c \u0441 Windows", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u043c\u0435\u043d\u044f", None))
        self.showHideWidgetChecker.setText("")
        self.windowsStartChecker.setText("")
        self.rememberMeChecker.setText("")
        self.whereComboBox_1.setItemText(0, QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.whereComboBox_1.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_1.setItemText(2, QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_1.setItemText(3, QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u043b\u043e\u0436\u0435\u043d\u0438\u0439", None))

        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.whereComboBox_4.setItemText(0, QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.whereComboBox_4.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_4.setItemText(2, QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_4.setItemText(3, QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u043b\u043e\u0436\u0435\u043d\u0438\u0439", None))

        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.whereComboBox_6.setItemText(0, QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.whereComboBox_6.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_6.setItemText(2, QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_6.setItemText(3, QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u043b\u043e\u0436\u0435\u043d\u0438\u0439", None))

        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.whereComboBox_5.setItemText(0, QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.whereComboBox_5.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_5.setItemText(2, QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_5.setItemText(3, QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u043b\u043e\u0436\u0435\u043d\u0438\u0439", None))

        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.whereComboBox_3.setItemText(0, QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.whereComboBox_3.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_3.setItemText(2, QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_3.setItemText(3, QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u043b\u043e\u0436\u0435\u043d\u0438\u0439", None))

        self.whereComboBox_2.setItemText(0, QCoreApplication.translate("Form", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u0435\u043b\u044c", None))
        self.whereComboBox_2.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_2.setItemText(2, QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0441\u0442 \u043f\u0438\u0441\u044c\u043c\u0430", None))
        self.whereComboBox_2.setItemText(3, QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0432\u043b\u043e\u0436\u0435\u043d\u0438\u0439", None))

        self.lineEdit_6.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041a\u043b\u044e\u0447\u0435\u0432\u043e\u0435 \u0441\u043b\u043e\u0432\u043e/email", None))
        self.label_1.setText(QCoreApplication.translate("Form", u"\u0413\u0434\u0435 \u0438\u0441\u043a\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0426\u0432\u0435\u0442 \u0443\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f", None))
        self.colorComboBox_1.setItemText(0, QCoreApplication.translate("Form", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.colorComboBox_1.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.colorComboBox_1.setItemText(2, QCoreApplication.translate("Form", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.colorComboBox_1.setItemText(3, QCoreApplication.translate("Form", u"\u0416\u0435\u043b\u0442\u044b\u0439", None))
        self.colorComboBox_1.setItemText(4, QCoreApplication.translate("Form", u"\u041b\u0430\u0437\u0443\u0440\u043d\u044b\u0439", None))
        self.colorComboBox_1.setItemText(5, QCoreApplication.translate("Form", u"\u0424\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439", None))

        self.colorComboBox_2.setItemText(0, QCoreApplication.translate("Form", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.colorComboBox_2.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.colorComboBox_2.setItemText(2, QCoreApplication.translate("Form", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.colorComboBox_2.setItemText(3, QCoreApplication.translate("Form", u"\u0416\u0435\u043b\u0442\u044b\u0439", None))
        self.colorComboBox_2.setItemText(4, QCoreApplication.translate("Form", u"\u041b\u0430\u0437\u0443\u0440\u043d\u044b\u0439", None))
        self.colorComboBox_2.setItemText(5, QCoreApplication.translate("Form", u"\u0424\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439", None))

        self.colorComboBox_3.setItemText(0, QCoreApplication.translate("Form", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.colorComboBox_3.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.colorComboBox_3.setItemText(2, QCoreApplication.translate("Form", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.colorComboBox_3.setItemText(3, QCoreApplication.translate("Form", u"\u0416\u0435\u043b\u0442\u044b\u0439", None))
        self.colorComboBox_3.setItemText(4, QCoreApplication.translate("Form", u"\u041b\u0430\u0437\u0443\u0440\u043d\u044b\u0439", None))
        self.colorComboBox_3.setItemText(5, QCoreApplication.translate("Form", u"\u0424\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439", None))

        self.colorComboBox_4.setItemText(0, QCoreApplication.translate("Form", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.colorComboBox_4.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.colorComboBox_4.setItemText(2, QCoreApplication.translate("Form", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.colorComboBox_4.setItemText(3, QCoreApplication.translate("Form", u"\u0416\u0435\u043b\u0442\u044b\u0439", None))
        self.colorComboBox_4.setItemText(4, QCoreApplication.translate("Form", u"\u041b\u0430\u0437\u0443\u0440\u043d\u044b\u0439", None))
        self.colorComboBox_4.setItemText(5, QCoreApplication.translate("Form", u"\u0424\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439", None))

        self.colorComboBox_5.setItemText(0, QCoreApplication.translate("Form", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.colorComboBox_5.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.colorComboBox_5.setItemText(2, QCoreApplication.translate("Form", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.colorComboBox_5.setItemText(3, QCoreApplication.translate("Form", u"\u0416\u0435\u043b\u0442\u044b\u0439", None))
        self.colorComboBox_5.setItemText(4, QCoreApplication.translate("Form", u"\u041b\u0430\u0437\u0443\u0440\u043d\u044b\u0439", None))
        self.colorComboBox_5.setItemText(5, QCoreApplication.translate("Form", u"\u0424\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439", None))

        self.colorComboBox_6.setItemText(0, QCoreApplication.translate("Form", u"\u041a\u0440\u0430\u0441\u043d\u044b\u0439", None))
        self.colorComboBox_6.setItemText(1, QCoreApplication.translate("Form", u"\u0417\u0435\u043b\u0435\u043d\u044b\u0439", None))
        self.colorComboBox_6.setItemText(2, QCoreApplication.translate("Form", u"\u0421\u0438\u043d\u0438\u0439", None))
        self.colorComboBox_6.setItemText(3, QCoreApplication.translate("Form", u"\u0416\u0435\u043b\u0442\u044b\u0439", None))
        self.colorComboBox_6.setItemText(4, QCoreApplication.translate("Form", u"\u041b\u0430\u0437\u0443\u0440\u043d\u044b\u0439", None))
        self.colorComboBox_6.setItemText(5, QCoreApplication.translate("Form", u"\u0424\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439", None))

        self.settingsMailWorkButton.setText(QCoreApplication.translate("Form", u"  \u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u043f\u0438\u0441\u044c\u043c\u0430\u043c\u0438", None))
        self.settingsSaveAndExitButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438 \u0432\u044b\u0439\u0442\u0438", None))
        self.settingsCollapseButton.setText("")
        self.settingsCloseButton.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

