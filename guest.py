# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guest.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 512)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(463, 512))
        MainWindow.setMaximumSize(QtCore.QSize(463, 512))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 21))
        self.label.setObjectName("label")
        self.nameText = QtWidgets.QLineEdit(self.centralwidget)
        self.nameText.setGeometry(QtCore.QRect(120, 30, 321, 20))
        self.nameText.setInputMask("")
        self.nameText.setText("")
        self.nameText.setObjectName("nameText")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 80, 56, 12))
        self.label_2.setObjectName("label_2")
        self.listPlain = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.listPlain.setReadOnly(True)
        self.listPlain.setGeometry(QtCore.QRect(20, 100, 421, 361))
        self.listPlain.setObjectName("listPlain")
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "방명록"))
        self.label.setText(_translate("MainWindow", "이름, 전화번호"))
        self.label_2.setText(_translate("MainWindow", "참석자"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
