import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets

form_class = uic.loadUiType("work1.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        self.ab = int(int(self.te1.text())+int(self.te2.text()))
        self.label_2.setText(str(self.ab))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    a = MyWindow()