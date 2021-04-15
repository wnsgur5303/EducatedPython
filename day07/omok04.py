import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.uic.Compiler.qtproxies import QtGui
from PyQt5 import QtGui, QtCore
from PyQt5.Qt import QIcon, QSize
from bokeh.models.widgets.buttons import Button
from idlelib import tooltip
from dask.array.linalg import lu
from docutils.languages import ru
from astropy._erfa.core import ld

form_class = uic.loadUiType("omok04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.icon0 = QIcon('0.png')
        self.icon1 = QIcon('1.png')
        self.icon2 = QIcon('2.png')
        self.flag_wb = True
        self.flag_playing = True
        self.arr2dpb = []
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
            line = []
            for j in range(10):
                button = QPushButton("", self) 
                button.setGeometry(i*40, j*40, 40, 40)
                #x,y,wigth,weight
                button.setIconSize(QSize(40, 40)) 
                button.setIcon(self.icon0)

                button.setToolTip(str(i)+","+str(j))
                button.clicked.connect(self.pb_click)
                line.append(button)
            self.arr2dpb.append(line)  
        self.myrender()
        self.pbreset.clicked.connect(self.reset)
    def myrender(self):
        for i in range (10):
            for j in range(10):
                if self.arr2d[i][j] == 0 :
                    self.arr2dpb[i][j].setIcon(self.icon0)
                      
                elif self.arr2d[i][j] == 1 :
                    self.arr2dpb[i][j].setIcon(self.icon1)
                      
                elif self.arr2d[i][j] == 2 :
                    self.arr2dpb[i][j].setIcon(self.icon2)
    def pb_click(self):
        if self.flag_playing == False:
            return
        k = self.sender().toolTip()
        k = k.split(",")
        i = int(k[0])
        j = int(k[1])
        if self.arr2d[i][j] > 0:
            return 
        stone_info = 0
        if self.flag_wb :
            self.arr2d[i][j] = 1
            stone_info = 1
        else:
            self.arr2d[i][j] = 2
            stone_info = 2
            
        self.myrender()
        self.flag_wb = not self.flag_wb  
            
        up = self.getUP(i,j,stone_info)
        dw = self.getDW(i,j,stone_info)
        le = self.getLE(i,j,stone_info)
        ri = self.getRI(i,j,stone_info)
        
        lu = self.getLU(i,j,stone_info)
        ru = self.getRU(i,j,stone_info)
        ld = self.getLD(i,j,stone_info)
        rd = self.getRD(i,j,stone_info)
        
        print(up,dw,le,ri,lu,ru,ld,rd)
        if up+dw >= 4 or le+ri >= 4 or lu+rd >= 4 or ru+ld >= 4:
            if stone_info == 1:
                QMessageBox.about(self, "결과", "백돌이 승리했습니다.")
#                 self.re()
                self.flag_playing = not self.flag_playing
            else :
                QMessageBox.about(self, "결과", "흑돌이 승리했습니다.")      
#                 self.re()
                self.flag_playing = not self.flag_playing
                
    def getUP(self,i,j,stone_info):
        cnt = 0
        while True:
            j = j-1
            print(stone_info)
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else :
                    return cnt
            except:
                return cnt

    def getDW(self,i,j,stone_info):
        cnt = 0
        while True:
            j = j+1
            print(stone_info)
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else :
                    return cnt
            except:
                return cnt
            
    def getLE(self,i,j,stone_info):
        cnt = 0
        while True:
            i = i-1
            print(stone_info)
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else :
                    return cnt
            except:
                return cnt
            
    def getRI(self,i,j,stone_info):
        cnt = 0
        while True:
            i = i+1
            print(stone_info)
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else :
                    return cnt
            except:
                return cnt

    def getLU(self,i,j,stone_info):
        cnt = 0
        while True:
            i = i-1
            j = j-1
            print(stone_info)
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else :
                    return cnt
            except:
                return cnt
            
    def getRU(self,i,j,stone_info):
        cnt = 0
        while True:
            j = j-1
            i = i+1
            print(stone_info)
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else :
                    return cnt
            except:
                return cnt
            
    def getLD(self,i,j,stone_info):
        cnt = 0
        while True:
            j = j+1
            i = i-1
            print(stone_info)
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else :
                    return cnt
            except:
                return cnt
            
    def getRD(self,i,j,stone_info):
        cnt = 0
        while True:
            i = i+1
            j = j+1
            print(stone_info)
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else :
                    return cnt
            except:
                return cnt

    def reset(self):
        for i in range (10):
            for j in range(10):
                self.arr2d[i][j] = 0
                self.myrender()
                self.flag_wb = True
                self.flag_playing = True
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    