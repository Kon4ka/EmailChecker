from PyQt5 import QtWidgets, QtCore
from Auth import Ui_Form
from PyQt5.QtCore import Qt
import os.path

from Workflow.Auth_crypto import AuthConfig


class AuthForm(QtWidgets.QDialog):

    def __init__(self, parent_all_conf, login_call, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.AuthLoginButton.clicked.connect(self.get_line_text)
        self.ui.rememverMeChecker.stateChanged.connect(self.remembered_changed)

        self.login, self.password = None, None
        self.conf = AuthConfig("Workflow/auth_config.json")
        self.parent_all_conf = parent_all_conf
        self.login_call = login_call

        if self.parent_all_conf.config["remember"] is True and self.remembered_authorisation() is not -1 or self.login and self.password:
            self.login, self.password = self.conf.read_config()
            self.login_signal_success()
        else: self.login_signal_failed()

    def get_line_text(self):
        self.login = self.ui.emailLine.text()
        self.password = self.ui.passwordLine.text()
        self.login_signal_success()

    def remembered_changed(self, state):
        # state может принимать значения: Qt.Unchecked, Qt.PartiallyChecked, Qt.Checked
        if state == Qt.Checked:
            self.parent_all_conf.config["remember"] = True
        else:
            self.parent_all_conf.config["remember"] = False

    def login_signal_success(self):
        self.login_call(self.login, self.password)


    def login_signal_failed(self):
        self.login_call("", "")

    def first_authorisation(self, login, password):
        self.conf.create_config(login, password)

    def remembered_authorisation(self):
        if os.path.isfile("Workflow/auth_config.json"):
            login, password = self.conf.read_config()
            return login, password
        else:
            return -1



