from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon, QPixmap
import os

ruta_dir = os.path.dirname(os.path.abspath(__file__))
#Path of parent directory
parentDirectory = os.path.dirname(ruta_dir)
#print('ruta_abs= ', parentDirectory)

class MsgBox(QMessageBox):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(title)
        self.setInformativeText(text)

    def set_custom_icon(self, icon):
        self.setIconPixmap(QPixmap(icon))
        q_icon = QIcon(icon)
        self.setWindowIcon(q_icon)

    def set_yes_no_buttons(self):
        self.setStandardButtons(QMessageBox.Yes| QMessageBox.No)


def errorBoxes(title, text):
    icon = os.path.join(parentDirectory, "assets", "iconos", "error32px.png")
    msgBox = MsgBox(title, text)
    msgBox.set_custom_icon(icon)
    msgBox.exec()

def okBoxes (title,text):
    icon = os.path.join(parentDirectory, "assets", "iconos", "checked64.png")
    msgBox = MsgBox(title, text)
    msgBox.set_custom_icon(icon)
    msgBox.exec()

def confirmationBox(title, text):
    icon = os.path.join(parentDirectory, "assets", "iconos", "warning64.png")
    msgBox = MsgBox(title,text)
    msgBox.set_custom_icon(icon)
    msgBox.set_yes_no_buttons()
    by = msgBox.button(QMessageBox.Yes)
    by.setText("Si")
    bn = msgBox.button(QMessageBox.No)
    bn.setText("No")
    resp = msgBox.exec()
    return resp

def questionBox(title, text):
    icon = os.path.join(parentDirectory, "assets", "iconos", "question-mark.png")
    msgBox = MsgBox(title, text)
    msgBox.set_custom_icon(icon)
    msgBox.set_yes_no_buttons()
    by = msgBox.button(QMessageBox.Yes)
    by.setText("Si")
    bn = msgBox.button(QMessageBox.No)
    bn.setText("No")
    resp = msgBox.exec_()
    return resp
def warningInfo(title, text):
    icon = os.path.join(parentDirectory, "assets", "iconos", "warning64.png" )
    msgBox = MsgBox(title, text)
    msgBox.set_custom_icon(icon)
    msgBox.exec()

if __name__ =="__main__":
    print(parentDirectory)
    path2 = os.path.join(parentDirectory, "resources", "iconos", "warning64.png" )
    print(path2)