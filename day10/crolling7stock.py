import pymysql
import requests
from bs4 import BeautifulSoup
from future.backports.urllib.request import urlopen
import datetime

juso_db = pymysql.connect(
    user='root', 
    passwd='java', 
    host='localhost', 
    db='python', 
    charset='utf8'
)
cursor = juso_db.cursor()

html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")
soup = BeautifulSoup(html, "html.parser")

tds = soup.select(".st2")

now = datetime.datetime.now()
in_time = now.strftime("%Y%m%d,%H%M")

count = 0
for td in tds:
    s_code = td.find(["a"]).get('title')
    s_name = td.text
    s_price = td.parent.select("td")[1].text.replace(",","")
    sql = "INSERT INTO `stock` (s_code,s_name,s_price,in_time) VALUES ('"+s_code+"', '"+s_name+"', '"+s_price+"', '"+in_time+"');"
    cursor.execute(sql)


juso_db.commit()    

