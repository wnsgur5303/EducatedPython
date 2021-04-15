import requests
from bs4 import BeautifulSoup
from future.backports.urllib.request import urlopen
html = urlopen("http://192.168.42.81:8081/HelloWeb2/croll.jsp")
soup = BeautifulSoup(html, "html.parser")

tds = soup.select("td");

for i in tds:
    print(i.text)
