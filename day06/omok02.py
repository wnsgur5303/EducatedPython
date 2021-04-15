import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.uic.Compiler.qtproxies import QtGui
from PyQt5 import QtGui, QtCore
from PyQt5.Qt import QIcon, QSize
from bokeh.models.widgets.buttons import Button

form_class = uic.loadUiType("omok02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.icon0 = QIcon('0.png')
        self.icon1 = QIcon('1.png')
        self.icon2 = QIcon('2.png')
        self.arrpb = []
        self.arr2d = [
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0],
                        [0,0,0,0,0, 0,0,0,0,0]
                     ]
        
        for i in range (10):
            for j in range(10):
                button = QPushButton("", self) 
                button.setGeometry(i*40, j*40, 40, 40)
                #x,y,wigth,weight
                button.setIconSize(QSize(40, 40)) 
                button.setIcon(self.icon0)
                button.clicked.connect(self.pb_click)
                self.arrpb.append(button)
                
        self.myrender()
    
    def myrender(self):
        for i in range (10):
            for j in range(10):
                idx = i*10+j
                if self.arr2d[i][j] == 0 :
                    self.arrpb[idx].setIcon(self.icon0)
                    
                elif self.arr2d[i][j] == 1 :
                    self.arrpb[idx].setIcon(self.icon1)
                    
                elif self.arr2d[i][j] == 2 :
                    self.arrpb[idx].setIcon(self.icon2)
    def pb_click(self):
        print("a")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    