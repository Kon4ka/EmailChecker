# -*- coding: utf-8 -*-
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget

import auto_res_rc
from Auth import Ui_Form
from Workflow.Auth_crypto import AuthConfig
from Workflow.Auth_work import AuthForm
from Workflow.Config import Config
from Workflow.Lamp_work import LampForm
from Workflow.MailCheckerClass import MailChecker


class EmailApp(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    # вызывается при нажатии кнопки мыши
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = event.pos()

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)


def move2RightBottomCorner(win):  # Move to right bottom
    screen_geometry = QApplication.screens()[0].size()
    screen_size = (screen_geometry.width(), screen_geometry.height())
    win_size = (win.frameSize().width(), win.frameSize().height())
    x = screen_size[0] - (win_size[0] + 40)
    y = screen_size[1] - (win_size[1] + 40)
    win.move(x, y)


class MyScript(QWidget):
    def __init__(self):
        self.run()
        self.app = QApplication(sys.argv)
        self.conf = Config("Workflow/conf.json")
        self.widget_auth = None
        self.widget_lamp = None
        self.login, self.password = "", ""
        self.mail_checker = MailChecker(imap_server="imap.rambler.ru")

    def run(self):
        self.app = QApplication(sys.argv)
        self.conf = Config("Workflow/conf.json")
        self.widget_lamp = LampForm()
        self.widget_auth = AuthForm(self.conf, self.success_file_login_received)
        self.mail_checker = MailChecker(imap_server="imap.rambler.ru")
        self.start_auth_widget()
        # widget.move(widget.width() * -3, 0)  # чтобы не мелькало
        # 
        # # first_authorisation("toster.net@ro.ru","Asdzxcqwe01")
        # 
        # widget.show()
        # move2RightBottomCorner(widget)
        sys.exit(self.app.exec())

    def start_auth_widget(self):
        if self.login == "" or self.password == "":
            self.widget_auth.show()
        else:
            if self.mail_checker.log_in(self.login, self.password) != -1:
                self.start_lamp_widget()
            else:
                self.widget_auth.show()


    def start_lamp_widget(self):
        self.widget_lamp.move(self.widget_lamp.width() * -3, 0)  # чтобы не мелькало
        self.widget_lamp.show()
        move2RightBottomCorner(self.widget_lamp)

    def success_file_login_received(self, l, p):
        self.login, self.password = l, p
        # if self.mail_checker.log_in(self.login, self.password) is not -1:
        #     pass
        ### TODO try to login if false go back





if __name__ == "__main__":
    all = MyScript()
    # all.run()
