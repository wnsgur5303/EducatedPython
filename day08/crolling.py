import requests
from bs4 import BeautifulSoup
from future.backports.urllib.request import urlopen
html = urlopen("http://192.168.42.81:8081/HelloWeb2/croll.jsp")
soup = BeautifulSoup(html, "html.parser")

title_tag1 = soup.find_all("td")[0]
title_tag2 = soup.find_all("td")[1]

print(title_tag1.text,title_tag2.text)

print(soup.body.text)
# title_tag.text
# print(title_tag.text)
