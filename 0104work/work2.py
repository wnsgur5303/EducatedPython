import requests
import folium
import pandas as pd
import json

#카카오 지도에서 검색하고자하는 위치 키워드
address = '함정 GS25'

url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
rest_api_key = '14659ef91e285f52e32a528a96b91271'
header = {'Authorization': 'KakaoAK ' + rest_api_key}
places = requests.get(url, headers = header).json()['documents']

#우리가 필요한 위도/경도/GS25 지점이름 데이타를 가져오고 Dataframe 형태로 변환
lat=[]
lon=[]
name=[]
for i in places:
    lat.append(i['y'])
    lon.append(i['x'])
    name.append(i['place_name'])
add=pd.DataFrame()
add['lat']=lat
add['lon']=lon
add['name']=name

#위도/경도 데이타 타입이 문자열이라 float으로 변환
add['lat']=add['lat'].apply(lambda x: float(x))
add['lon']=add['lon'].apply(lambda x: float(x))

#folium 패키지로 카카오API에서 받아온 GS25 위도 경도 위치를 표시한다
#지도를 어디 중심으로 표시할지를 설정해줘야되는데 여기서는 카카오에서 받아온 1번째 GS25 지점을 기준으로 설정
map = folium.Map(location=[add['lat'][0],add['lon'][0]], zoom_start=15)
for index, row in add.iterrows():
    folium.Marker(location=[row['lat'],row['lon']], popup=row['name'], icon=folium.Icon(color='red')).add_to(map)

#folium 지도 파일 저장
map.save('gs25.html')