import requests
from flask import Flask
 
def getLatLng(address):
    result = ""
 
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    rest_api_key = '15846e51cb8ace77e040eaac2bb7fbbf'
    
    header = {'Authorization': 'KakaoAK ' + rest_api_key}
    r = requests.get(url, headers=header)
 
    if r.status_code == 200:
        result_address = r.json()["documents"][0]["address"]
        
        result = result_address["y"], result_address["x"]
    else:
        result = "ERROR[" + str(r.status_code) + "]"
    
    return result
 
 
def getKakaoMapHtml(address_latlng):
    javascript_key = "88d281c441303fd7c44399fa87dde382"
    rest_api_key = '15846e51cb8ace77e040eaac2bb7fbbf'
    result = ""
    result = result + "<div id='map' style='width:1200px;height:1000px;display:inline-block;'></div>" + "\n"
    result = result + "<script type='text/javascript' src='//dapi.kakao.com/v2/maps/sdk.js?appkey=" + rest_api_key + "'></script>" + "\n"
    result = result + "<script>" + "\n"
    result = result + "    var container = document.getElementById('map'); " + "\n"
    result = result + "    var options = {" + "\n"
    result = result + "           center: new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ")," + "\n"
    result = result + "           level: 3" + "\n"
    result = result + "    }; " + "\n"
    result = result + "    var map = new kakao.maps.Map(container, options); " + "\n"
    
    result = result + "    var markerPosition  = new kakao.maps.LatLng(" + address_latlng[0] + ", " + address_latlng[1] + ");  " + "\n"
    result = result + "    var marker = new kakao.maps.Marker({position: markerPosition}); " + "\n"
    result = result + "    var zoomControl = new kakao.maps.ZoomControl(); " + "\n"
    result = result + "    map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT); " + "\n"
    result = result + "    var mapTypeControl = new kakao.maps.MapTypeControl(); " + "\n"
    result = result + "    map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT); " + "\n"
    
    result = result + "    marker.setMap(map); " + "\n"
 
    result = result + "</script>" + "\n"
    
    return result
 
# main()
if __name__ == "__main__":
    address = "대전광역시 중구 대흥동 500-5"
    
    # 카카오 REST API로 좌표 구하기
    address_latlng = getLatLng(address)
 
    # 좌표로 지도 첨부 HTML 생성
    if str(address_latlng).find("ERROR") < 0:
        map_html = getKakaoMapHtml(address_latlng)
        with open('C:\workspace_python\HelloWeb2\WebContent\day12/01.html', 'w') as html_file:
           html_file.write(map_html)
           
        print(map_html)
    else:
        print("[ERROR]getLatLng")
 


