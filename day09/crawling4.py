import requests
import json

url = "https://dapi.kakao.com/v2/search/cafe"
queryString = {"query":"류현진"}
header = {'authorization':'KakaoAK d6c2a7f2a1bb2197f5730fa38462df37'} 
r = requests.get(url, headers=header, params=queryString)

print(json.loads(r.text))