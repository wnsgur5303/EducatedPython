import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.uic.Compiler.qtproxies import QtGui
from PyQt5 import QtGui, QtCore
from PyQt5.Qt import QIcon, QSize

form_class = uic.loadUiType("omok01.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        for i in range (10):
            for j in range(10):
                self.button = QPushButton("", self) 
                self.button.setGeometry(i*40, j*40, 40, 40)
                #x,y,wigth,weight
                self.button.setIcon(QIcon('0.png'))
                self.button.setIconSize(QSize(40, 40)) 
                self.button.clicked.connect(self.pb_click)  
        
    def pb_click(self):
        self.button.setIcon(QtGui.QIcon('1.png'))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    