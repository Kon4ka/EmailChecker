# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LetterSearch.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)
import rc_auto_res

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(765, 697)
        Form.setStyleSheet(u"font: \"Copperplate Gothic Light\";\n"
"background-color: rgb(21, 25, 31);")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 40, 745, 311))
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 0, 121, 24))
        font = QFont()
        font.setFamilies([u"Copperplate Gothic Light"])
        font.setBold(False)
        font.setItalic(False)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 18px;\n"
"font: \"Copperplate Gothic Light\";")
        self.label_9.setMargin(2)
        self.gridLayoutWidget = QWidget(self.widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 721, 241))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.gridLayoutWidget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.widget_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_10.setMargin(2)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.WordsInSubjectLine = QLineEdit(self.widget_6)
        self.WordsInSubjectLine.setObjectName(u"WordsInSubjectLine")
        self.WordsInSubjectLine.setMinimumSize(QSize(0, 21))
        self.WordsInSubjectLine.setMaximumSize(QSize(16777215, 31))
        self.WordsInSubjectLine.setStyleSheet(u"QLineEdit{\n"
"border: 0px solid  rgb(39, 77, 105) ;\n"
"	background-color: rgb(14, 16, 20);\n"
"color: #FFF;\n"
"border-radius: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.WordsInSubjectLine)


        self.gridLayout.addWidget(self.widget_6, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.gridLayoutWidget)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.widget_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_8.setMargin(2)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.fromWhoLine = QLineEdit(self.widget_5)
        self.fromWhoLine.setObjectName(u"fromWhoLine")
        self.fromWhoLine.setMinimumSize(QSize(0, 21))
        self.fromWhoLine.setMaximumSize(QSize(16777215, 31))
        self.fromWhoLine.setStyleSheet(u"QLineEdit{\n"
"border: 0px solid  rgb(39, 77, 105) ;\n"
"	background-color: rgb(14, 16, 20);\n"
"color: #FFF;\n"
"border-radius: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.fromWhoLine)


        self.gridLayout.addWidget(self.widget_5, 0, 0, 1, 1)

        self.widget_8 = QWidget(self.gridLayoutWidget)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.widget_8)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_12.setMargin(2)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.WordsInAttachLine = QLineEdit(self.widget_8)
        self.WordsInAttachLine.setObjectName(u"WordsInAttachLine")
        self.WordsInAttachLine.setMinimumSize(QSize(0, 21))
        self.WordsInAttachLine.setMaximumSize(QSize(16777215, 31))
        self.WordsInAttachLine.setStyleSheet(u"QLineEdit{\n"
"border: 0px solid  rgb(39, 77, 105) ;\n"
"	background-color: rgb(14, 16, 20);\n"
"color: #FFF;\n"
"border-radius: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.WordsInAttachLine)


        self.gridLayout.addWidget(self.widget_8, 3, 0, 1, 1)

        self.widget_7 = QWidget(self.gridLayoutWidget)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_11.setMargin(2)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.WordsInTextLine = QLineEdit(self.widget_7)
        self.WordsInTextLine.setObjectName(u"WordsInTextLine")
        self.WordsInTextLine.setMinimumSize(QSize(0, 21))
        self.WordsInTextLine.setMaximumSize(QSize(16777215, 31))
        self.WordsInTextLine.setStyleSheet(u"QLineEdit{\n"
"border: 0px solid  rgb(39, 77, 105) ;\n"
"	background-color: rgb(14, 16, 20);\n"
"color: #FFF;\n"
"border-radius: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.WordsInTextLine)


        self.gridLayout.addWidget(self.widget_7, 2, 0, 1, 1)

        self.widget_9 = QWidget(self.gridLayoutWidget)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"outline: 0px;")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_13 = QLabel(self.widget_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_13.setMargin(2)

        self.horizontalLayout_6.addWidget(self.label_13)

        self.dateEdit = QDateEdit(self.widget_9)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(331, 31))
        self.dateEdit.setStyleSheet(u"QDateEdit {\n"
"	color: rgb(202, 206, 216);\n"
"	font-size: 14px;\n"
"	border: 0px solid  rgb(39, 77, 105) ;\n"
"	background-color: rgb(14, 16, 20);\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 20px;\n"
"}\n"
"\n"
"QDateEdit::drop-down \n"
"{;\n"
"	margin-left: -12px;\n"
"	margin-top: 2px;\n"
"	background-image: url(:/Light/Assets/Light/chevron-down.svg);\n"
"    border: 0px solid red;\n"
"}\n"
"/*\n"
"QDateEdit QAbstracctItemView: enabled {\n"
"	\n"
"	background-color: rgb(35, 41, 51);\n"
"	color: rgb(179, 203, 231);\n"
"}*/\n"
"\n"
"QCalendarWidget QToolButton {\n"
"  	/*height: 60px;\n"
"  	width: 150px;*/\n"
"  	color: white;\n"
"  	font-size: 14px;\n"
"  	icon-size: 16px, 16px;\n"
"  	background-color:transparent;\n"
"  }\n"
"  QCalendarWidget QMenu {\n"
"  	/*width: 150px;*/\n"
"  	left: 20px;\n"
"  	color: white;\n"
"  	font-size: 14px;\n"
"  	background-color: rgb(100, 100, 120);\n"
"  }\n"
"  QCalendarWidget QSpinBox { \n"
"  	/*width: 50px; */\n"
"  	font-size: 14px; \n"
"  "
                        "	color: white; \n"
"  	background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333); \n"
"  	selection-background-color: rgb(136, 136, 136);\n"
"  	selection-color: rgb(255, 255, 255);\n"
"  }\n"
"  QCalendarWidget QSpinBox::up-button { subcontrol-origin: border;  subcontrol-position: top right;  width:25px; }\n"
"  QCalendarWidget QSpinBox::down-button {subcontrol-origin: border; subcontrol-position: bottom right;  width:25px;}\n"
"  QCalendarWidget QSpinBox::up-arrow { width:20px;  height:20px; }\n"
"  QCalendarWidget QSpinBox::down-arrow { width:20px;  height:20px; }\n"
"   \n"
"  /* header row */\n"
"  QCalendarWidget QWidget { alternate-background-color: rgb(58, 65, 98); }\n"
"   \n"
"  /* normal days */\n"
"  QCalendarWidget QAbstractItemView:enabled \n"
"  {\n"
"  	font-size: 16px;  \n"
"  	color: rgb(180, 180, 180);  \n"
"  	background-color: rgb(35, 41, 51);  \n"
"  	selection-background-color: rgb(55, 61, 100);  \n"
"  	selection-color: rgb(0, 255, 0); \n"
"  }\n"
"   \n"
""
                        "  /* days in other months */\n"
"  /* navigation bar */\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar\n"
"{ \n"
"  background-color: rgb(37, 42, 50); \n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:disabled \n"
"{ \n"
"color: rgb(64, 64, 64); \n"
"}\n"
"")
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.dateEdit)

        self.mailWorkSearchButton = QPushButton(self.widget_9)
        self.mailWorkSearchButton.setObjectName(u"mailWorkSearchButton")
        self.mailWorkSearchButton.setMinimumSize(QSize(200, 30))
        self.mailWorkSearchButton.setStyleSheet(u"QPushButton {\n"
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
        icon.addFile(u":/Lighter/Assets/Light/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.mailWorkSearchButton.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.mailWorkSearchButton)


        self.gridLayout.addWidget(self.widget_9, 4, 0, 1, 1)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(10, 320, 741, 361))
        self.widget_2.setStyleSheet(u"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
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
"/* BTN"
                        " BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
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
"\n"
"\n"
"")
        self.mailList = QListWidget(self.widget_2)
        self.mailList.setObjectName(u"mailList")
        self.mailList.setGeometry(QRect(10, 0, 271, 361))
        self.mailList.setStyleSheet(u"QListWidget\n"
"{\n"
"border : 0px solid black;\n"
"border-radius: 20px;\n"
"background : rgb(12, 14, 18);\n"
"padding: 6px;\n"
"outline: 0px;\n"
"font-size: 18px;\n"
"}\n"
" QListView::item:selected\n"
"{\n"
"border : 2px solid rgb(21, 25, 31);\n"
"background : rgb(41, 49, 61);\n"
"}\n"
"\n"
"QListView::item {\n"
"	color: rgb(202, 206, 216);\n"
"    background-color:rgb(21, 25, 31);\n"
"	border-radius: 10px;\n"
"	padding: 12px;\n"
"	margin: 5px\n"
"}\n"
"\n"
"/*QListWidget QScrollBar\n"
"{\n"
"background : rgb(33, 39, 48);\n"
"border: 2px solid red;\n"
"border-radius: 10px;\n"
"}\n"
"QListWidget QScrollBar::handle\n"
"{\n"
"background : rgb(91, 100, 105);\n"
"}\n"
"\n"
"QListWidget QScrollBar::handle::pressed\n"
"{\n"
"background : rgb(107, 117, 127);\n"
"}\n"
"QListView  QScrollBar::down-arrow:vertical {               \n"
"\n"
"	height: 40px; \n"
"	width: 40px  \n"
" }\n"
"*/")
        self.mailList.setAutoScroll(True)
        self.mailList.setProperty("showDropIndicator", False)
        self.widget_10 = QWidget(self.widget_2)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setGeometry(QRect(290, 10, 441, 351))
        self.gridLayoutWidget_2 = QWidget(self.widget_10)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 441, 137))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.gridLayoutWidget_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.widget_12)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_16.setMargin(2)

        self.horizontalLayout_8.addWidget(self.label_16)

        self.searchedSubjectLine = QLineEdit(self.widget_12)
        self.searchedSubjectLine.setObjectName(u"searchedSubjectLine")
        self.searchedSubjectLine.setMinimumSize(QSize(221, 21))
        self.searchedSubjectLine.setStyleSheet(u"QLineEdit{\n"
"border: 0px solid  rgb(39, 77, 105) ;\n"
"	background-color: rgb(14, 16, 20);\n"
"color: #FFF;\n"
"border-radius: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"")
        self.searchedSubjectLine.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.searchedSubjectLine)


        self.gridLayout_2.addWidget(self.widget_12, 1, 0, 1, 1)

        self.widget_11 = QWidget(self.gridLayoutWidget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_14 = QLabel(self.widget_11)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_14.setMargin(2)

        self.horizontalLayout_7.addWidget(self.label_14)

        self.searchedFromWhoLine = QLineEdit(self.widget_11)
        self.searchedFromWhoLine.setObjectName(u"searchedFromWhoLine")
        self.searchedFromWhoLine.setMinimumSize(QSize(221, 21))
        self.searchedFromWhoLine.setStyleSheet(u"QLineEdit{\n"
"border: 0px solid  rgb(39, 77, 105) ;\n"
"	background-color: rgb(14, 16, 20);\n"
"color: #FFF;\n"
"border-radius: 10px;\n"
"padding-left: 20px;\n"
"padding-right: 20px;\n"
"}\n"
"")
        self.searchedFromWhoLine.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.searchedFromWhoLine)


        self.gridLayout_2.addWidget(self.widget_11, 0, 0, 1, 1)

        self.widget_13 = QWidget(self.gridLayoutWidget_2)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_15 = QLabel(self.widget_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"color: rgb(202, 206, 216);\n"
"font-size: 14px;")
        self.label_15.setMargin(2)

        self.horizontalLayout_9.addWidget(self.label_15)

        self.searchedDateEdit = QDateEdit(self.widget_13)
        self.searchedDateEdit.setObjectName(u"searchedDateEdit")
        self.searchedDateEdit.setStyleSheet(u"QDateEdit {\n"
"	color: rgb(202, 206, 216);\n"
"	font-size: 14px;\n"
"	border: 0px solid  rgb(39, 77, 105) ;\n"
"	background-color: rgb(14, 16, 20);\n"
"	border-radius: 10px;\n"
"	padding-left: 10px;\n"
"	padding-right: 20px;\n"
"}")
        self.searchedDateEdit.setReadOnly(True)
        self.searchedDateEdit.setCalendarPopup(False)

        self.horizontalLayout_9.addWidget(self.searchedDateEdit)


        self.gridLayout_2.addWidget(self.widget_13, 2, 0, 1, 1)

        self.textMailBrowser = QTextBrowser(self.widget_10)
        self.textMailBrowser.setObjectName(u"textMailBrowser")
        self.textMailBrowser.setGeometry(QRect(0, 130, 441, 211))
        self.textMailBrowser.setStyleSheet(u"QTextBrowser {\n"
"	color: rgb(202, 206, 216);\n"
"	background-color: rgb(35, 41, 51);\n"
"	border-radius: 15px;\n"
"	padding: 10px;\n"
"}")
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 771, 31))
        self.widget_3.setStyleSheet(u"background-color: rgb(35, 41, 51);")
        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(670, -10, 91, 51))
        self.widget_4.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid transparent;\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgb(20, 25, 34);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mailWorkCollapseButton = QPushButton(self.widget_4)
        self.mailWorkCollapseButton.setObjectName(u"mailWorkCollapseButton")
        icon1 = QIcon()
        icon1.addFile(u":/Lighter/Assets/Light/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.mailWorkCollapseButton.setIcon(icon1)
        self.mailWorkCollapseButton.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.mailWorkCollapseButton)

        self.mailWorkCloseButton = QPushButton(self.widget_4)
        self.mailWorkCloseButton.setObjectName(u"mailWorkCloseButton")
        icon2 = QIcon()
        icon2.addFile(u":/Lighter/Assets/Light/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.mailWorkCloseButton.setIcon(icon2)
        self.mailWorkCloseButton.setIconSize(QSize(22, 22))

        self.horizontalLayout.addWidget(self.mailWorkCloseButton)

        self.mailWorkCloseButton.raise_()
        self.mailWorkCollapseButton.raise_()
        self.label = QLabel(self.widget_3)
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
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u0421\u043e \u0441\u043b\u043e\u0432\u0430\u043c\u0438 \u0432 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0435: ", None))
        self.WordsInSubjectLine.setPlaceholderText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041e\u0442 \u043a\u043e\u0433\u043e:", None))
        self.fromWhoLine.setPlaceholderText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0421\u043e \u0441\u043b\u043e\u0432\u043e\u043c \u0432 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0438 \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043a \u043f\u0438\u0441\u044c\u043c\u0443: ", None))
        self.WordsInAttachLine.setPlaceholderText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"\u0421\u043e \u0441\u043b\u043e\u0432\u0430\u043c\u0438 \u0432 \u0442\u0435\u043a\u0441\u0442\u0435:", None))
        self.WordsInTextLine.setPlaceholderText("")
        self.label_13.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f: ", None))
        self.mailWorkSearchButton.setText(QCoreApplication.translate("Form", u"  \u041f\u043e\u0438\u0441\u043a", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043c\u0430:", None))
        self.searchedSubjectLine.setPlaceholderText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"\u041e\u0442 \u043a\u043e\u0433\u043e:", None))
        self.searchedFromWhoLine.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f: ", None))
        self.textMailBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:8.50909pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.50909pt;\"><br /></p></body></html>", None))
        self.mailWorkCollapseButton.setText("")
        self.mailWorkCloseButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0431\u043e\u0442\u0430 \u0441 \u043f\u0438\u0441\u044c\u043c\u0430\u043c\u0438", None))
    # retranslateUi

