import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from guest import Ui_MainWindow
from PyQt5 import uic

class ListForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.nameText.textChanged.connect(self.nameTextChanged)
        self.nameText.returnPressed.connect(self.nameTextEntered)


    def nameTextChanged(self):
        self.statusbar.showMessage(self.nameText.text())

    def nameTextEntered(self):
        inputText=self.nameText.text()
        inputList=inputText.split()
        inputList.append('x') #폰넘버 안쳤을경우 x 넣어 출력하도록 append
        self.listPlain.appendPlainText("name:{0}, phone:{1}".format(inputList[0], inputList[1]))
        self.nameText.clear()

if __name__=="__main__":
    app = QApplication(sys.argv)
    window=ListForm()
    window.show()
    app.exec_()
