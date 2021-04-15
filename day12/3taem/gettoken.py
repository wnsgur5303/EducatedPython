import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "37794964eee6e9c1331f0e44ebbcb7f9",
    "redirect_uri" : "https://localhost.com",
    "code"         : "CATYRoPlVc_aW5Vmbj0q7WW1NCnBjo6ZcBJoMXR59ZZ8Or1alYl8vTiYnlPoRh3UfVGlNgo9dRkAAAF22iLKig"
    
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)