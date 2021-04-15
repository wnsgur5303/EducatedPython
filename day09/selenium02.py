from selenium import webdriver
import time
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
import sys

form_class = uic.loadUiType("cro.ui")[0]

browser = webdriver.Chrome()
browser.get("http://192.168.42.81:8081/HelloWeb2/mylogin")
browser.get("http://192.168.42.81:8081/HelloWeb2/mycrawl")  

menus = browser.find_element_by_tag_name('table')
ttt = menus.text
print(ttt)

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        self.et.setText(ttt)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    

