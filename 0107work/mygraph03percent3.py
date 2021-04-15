import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymysql

class MyManager:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='java', db='python', charset='utf8')
        self.curs = self.conn.cursor()
    
    def __del__(self):    
        self.conn.close()
        
    def getAllScode(self):
        sql = "SELECT s_code FROM stock GROUP BY s_code  "
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        codes = []    
        for row in rows :
            codes.append(row[0])
        return codes
        

    def getPrices(self,s_name):
        sql = "select s_price,in_time from stock WHERE s_name = '"+s_name+"' order by in_time desc  "
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        prices = []    
        for row in rows :
            prices.append(row[0])
        return prices
    
    def getPricesPer(self,s_name):
        sql = "select s_price,in_time from stock WHERE s_name = '"+s_name+"' order by in_time  "
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        prices = []    
        p_init = 0;
        for idx, row in enumerate(rows) :
            if idx == 0:
                p_init = row[0]
            prices.append((row[0]/p_init)*100)
        return prices
    
    def getPricesPerNumpy(self,s_name):
        sql = "select s_price,in_time from stock WHERE s_name = '"+s_name+"' order by in_time  "
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        prices = []    
        p_init = 0;
        for idx, row in enumerate(rows) :
            if idx == 0:
                p_init = row[0]
            prices.append((row[0]/p_init)*100)
        return np.array(prices)    
    
    def getPricesPerNumpyFromCode(self,s_code):
        sql = "select s_price,in_time from stock WHERE s_code = '"+s_code+"' order by in_time  "
        self.curs.execute(sql)
        rows = self.curs.fetchall()

        prices = []    
        p_init = 100;
        for idx, row in enumerate(rows) :
            
            if idx == 0:
                if row[0] > 0 :
                    p_init = row[0]
            
            per = (row[0]/p_init)*100        
             
            if per == 0:
                per = 96       
              
            prices.append(per)
        return np.array(prices)  
    

mm = MyManager()
fig = plt.figure()
ax = fig.gca(projection='3d')
codes = mm.getAllScode()
print(len(codes))

zs = []
for code in codes:
    print("code",code)
    zs.append(mm.getPricesPerNumpyFromCode(code))


x = np.zeros(len(zs[0]))
y = np.array(range(len(zs[0])))


for i,z in enumerate(zs):
    ax.plot(x+i , y, z)
    
# ax.plot(x+0 , y, zs[0])
# ax.plot(x+1 , y, zs[1])
# ax.plot(x+2 , y, zs[2])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()