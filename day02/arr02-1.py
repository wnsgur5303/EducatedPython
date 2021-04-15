import random

from asn1crypto.core import Integer

mine = input("가위,바위,보를 선택.\n")
print(mine)
rnd=random.randint(1,3)
print(rnd)
if rnd ==1:
    com = "가위"
elif rnd == 2:
    com = "바위"
else :
    com = "보"  
result = ""
if mine == "가위" and com == "보" or mine == "바위" and com == "가위" or mine == "보" and com == "바위":
    result = "이겼습니다."
elif mine == com: 
    result = "비겼습니다."
else :
    result = "졌습니다."
print("mine:",mine)
print("com:",com)
print("result:",result)