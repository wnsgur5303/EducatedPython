import simplejson,requests
import sys
url = "https://dapi.kakao.com/v2/search/cafe"
apikey = "d6c2a7f2a1bb2197f5730fa38462df37"
subj = "아이유"
r = requests.get( url, params = {'query':subj}, headers={'Authorization' : 'KakaoAK ' + apikey } )
js = simplejson.JSONEncoder().encode(r.json())
for i in r.json()["documents"] :
    print (i["title"])
    a = i["title"]
    a = a.replace('<b>', '').replace('</b>', '')
    print (a)
    print (i["url"])
    print (i["datetime"])
    print (i["contents"])