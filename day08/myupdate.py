import pymysql

juso_db = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)

cursor = juso_db.cursor()

sql = "update `sample` set col1 = '124' ,col2 = '124',col3 = '124' where col1 = 1;"

cursor.execute(sql)
juso_db.commit()

sql = "SELECT * FROM `sample`;"
cursor.execute(sql)
result = cursor.fetchall()

print(result)