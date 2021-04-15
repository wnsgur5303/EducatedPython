import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from asn1crypto.core import Integer

form_class = uic.loadUiType("work2.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        a = int(self.te1.text())
        b = int(self.te2.text())
        sum = 0
        for i in range(a,b+1):
            sum = i+sum
            print(sum)

        self.lbl.setText(str(sum)) 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    a = MyWindow()