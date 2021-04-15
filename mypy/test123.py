import cx_Oracle
conn=cx_Oracle.connect("team3_202008f/java@112.220.114.130:1521/xe")
cursor=conn.cursor() #커서 생성
sql="select * from test"
cursor.execute(sql)

for row in cursor:
    for i in range(len(row)):
        if i==3:
            description=row[3].read() #CLOB필드 읽는 방법
        print(row[i], end=" ")
    print()

cursor.close()
conn.close()