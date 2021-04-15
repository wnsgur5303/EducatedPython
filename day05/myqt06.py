#홀짝선택  ㅁle ㅁpb
#컴퓨터의 선택 le2 
#결과 le3 같으면 이기고 다르면 진다.
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from asn1crypto.core import Integer
import random
from PyQt5.Qt import QPalette, Qt
from networkx.generators.tests.test_small import null

form_class = uic.loadUiType("myqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.pbnum_click)
        self.pb2.clicked.connect(self.pbnum_click)
        self.pb3.clicked.connect(self.pbnum_click)
        self.pb4.clicked.connect(self.pbnum_click)
        self.pb5.clicked.connect(self.pbnum_click)
        self.pb6.clicked.connect(self.pbnum_click)
        self.pb7.clicked.connect(self.pbnum_click)
        self.pb8.clicked.connect(self.pbnum_click)
        self.pb9.clicked.connect(self.pbnum_click)
        self.pb0.clicked.connect(self.pbnum_click)
        self.pbcall.clicked.connect(self.btn_clickedcall)
        
        
    
    def pbnum_click(self):
        txt_old = self.le1.text()
        txt_new = self.sender().text()
        self.le1.setText(txt_old+txt_new)
        
    def btn_clickedcall(self):
        a = self.le1.text()
        QMessageBox.about(self, "calling", a)

        
#        self.msg = QMessageBox()
#        self.msg.setIcon(QMessageBox.Information)
#        self.msg.setWindowTitle('call')
#        self.msg.setText(a + "전화중")
#        self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#        self.msg.setStandardButtons(QMessageBox.Ok)
 #       retval = self.msg.exec_()
    
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    a = MyWindow()