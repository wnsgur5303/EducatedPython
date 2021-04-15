#홀짝선택  ㅁle ㅁpb
#컴퓨터의 선택 le2 
#결과 le3 같으면 이기고 다르면 진다.
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from asn1crypto.core import Integer
import random
from PyQt5.Qt import QPalette, Qt

form_class = uic.loadUiType("myqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btn_clicked)
        
    
    def btn_clicked(self):
        a = self.le1.text()
        b = random.randint(1,2)
        if b == 1:
            self.le2.setText("홀")
        else :
            self.le2.setText("짝")
        if a == self.le2.text():
            self.le3.setText("당신이 이겼습니다.")
            self.le3.setStyleSheet("QLineEdit"
                        "{"
                        "background : green;"
                        "}")
        else:
            self.le3.setText("당신이 졌습니다.")
            self.le3.setStyleSheet("QLineEdit"
                        "{"
                        "background : red;"
                        "}")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    a = MyWindow()