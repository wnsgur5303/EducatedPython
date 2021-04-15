import pymysql

juso_db = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)

cursor = juso_db.cursor()
# pymysql.cursors.DictCursor
sql = "INSERT INTO `sample` (col1,col2,col3) VALUES ('1', '2', '4');"

cursor.execute(sql)
juso_db.commit()

sql = "SELECT * FROM `sample`;"
cnt = cursor.execute(sql)
result = cursor.fetchall()

print(cnt)
print(result)
juso_db.close()