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
sql = "delete from `sample` where col3 = 4;"

cursor.execute(sql)
juso_db.commit()

sql = "SELECT * FROM `sample`;"
cursor.execute(sql)
result = cursor.fetchall()

print(result)