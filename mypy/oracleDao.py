# cx_Oracle 패키지 모듈들을 import
import cx_Oracle as oci

# Oracle 서버와 연결(Connection 맺기)
conn = oci.connect('scott/tiger@localhost:1521/xe')

# Connection 확인
print(conn.version)

# Oracle DB의 test_member 테이블 검색(select)
cursor = conn.cursor() # cursor 객체 얻어오기
cursor.execute('select * from test_member') # SQL 문장 실행
print(cursor.fetchall())
# for rs in cursor:
#     print(rs)

cursor.close() # cursor 객체 닫기

# Oracle 서버와 연결 끊기
conn.close