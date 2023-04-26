# This Python file uses the following encoding: utf-8
import sys
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_Auth import Ui_Form  #SmallWidgetLamp, SettingsForm, LetterList, LetterSearch, Auth

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


def move2RightBottomCorner(win):    #Move to right bottom
    screen_geometry = QApplication.screens()[0].size()
    screen_size = (screen_geometry.width(), screen_geometry.height())
    win_size = (win.frameSize().width(), win.frameSize().height())
    x = screen_size[0] - (win_size[0]+40)
    y = screen_size[1] - (win_size[1]+40)
    win.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = EmailApp()
    widget.move(widget.width() * -3, 0) # чтобы не мелькало
    widget.show()
    move2RightBottomCorner(widget)
    sys.exit(app.exec())




