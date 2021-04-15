import pymysql

juso_db = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)

cursor = juso_db.cursor(pymysql.cursors.DictCursor)

sql = "SELECT * FROM `sample`;"
cursor.execute(sql)
result = cursor.fetchall()

print(result)