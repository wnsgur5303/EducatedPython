import requests
import json

url = "https://dapi.kakao.com/v2/search/cafe"
queryString = {"query":"맛집"}
header = {'authorization':'KakaoAK d6c2a7f2a1bb2197f5730fa38462df37'} 
r = requests.get(url, headers=header, params=queryString)

jsonobj = json.loads(r.text)
docus = jsonobj.get("documents")

for i in docus:
    print("cafename:",i.get("cafename"),end=" ")#end 하고 뒤에 있으면하는 단어 쓰면 한탄 아래로 내리는거 대신나옴
    print("contents:",i.get("contents"),end=" ")
    print("datetime:",i.get("datetime"),end=" ")
    print("thumbnail:",i.get("thumbnail"),end=" ")
    print("title:",i.get("title"),end=" ")
    print("url:",i.get("url"))
    