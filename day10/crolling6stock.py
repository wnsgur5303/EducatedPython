import requests
from bs4 import BeautifulSoup
from future.backports.urllib.request import urlopen

html = urlopen("https://vip.mk.co.kr/newSt/rate/item_all.php")
soup = BeautifulSoup(html, "html.parser")

tds = soup.select(".st2")

for td in tds:
    s_code = td.find(["a"]).get('title')
    s_name = td.text
    s_price = td.parent.select("td")[1].text.replace(",","")
    print("s_code: ", s_code, end=" ")
    print("s_name: ", s_name, end=" ")
    print("s_price: ", s_price)
#     print(td.parent.text)


# YYYYMMDD.HHMM
# now