import pymysql
import time

juso_db = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)


cursor = juso_db.cursor()
# pymysql.cursors.DictCursor
count = 0
sql = "INSERT INTO sample (col1,col2,col3) VALUES (%s, %s, %s)"
start = time.time()
for i in range(300000):
    cursor.execute(sql,(count,2,4))
    count+=1

juso_db.commit()
end = time.time()
print(end - start)
