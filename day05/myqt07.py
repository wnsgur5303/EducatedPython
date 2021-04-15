import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
import random

form_class = uic.loadUiType("myqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.btn_clicked)
        self.pb2.clicked.connect(self.btn_clicked)
        self.pb3.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        mine = self.sender().text()
        self.le1.setText(mine)
        b = random.randint(1,3)
        
        
        if b == 1:
            com = "가위"
        elif b == 2:
            com = "바위"
        else :
            com = "보"
            
        self.le2.setText(com)
            
        if mine == "가위" and com == "보" or mine == "바위" and com == "가위" or mine == "보" and com == "바위":
            result = "이겼습니다."
        elif mine == com: 
            result = "비겼습니다."
        else :
            result = "졌습니다."
        
        self.le3.setText(result)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
