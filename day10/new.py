import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pymysql

fig = plt.figure()
ax = fig.gca(projection='3d')

juso_db = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)

cursor = juso_db.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM `stock` order by s_name,in_time;"
cursor.execute(sql)
result = cursor.fetchall()

for i in range(len(result)):
    print(result[i]['s_name'])
    if result[i]['s_name'] == result[i-1]['s_name']:
        print(result[i]['s_price']-result[i-1]['s_price'])
        