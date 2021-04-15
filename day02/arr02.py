import random
from asn1crypto.core import Integer
mine = input("홀/짝을 선택하시오.\n")

print(mine)

rnd=random.random()
print(rnd)

if rnd > 0.5 :
    com = "홀"
else:
    com = "짝"
    
result = ""
if mine == com :
    result = "이겼습니다."
else :
    result = "졌습니다."
    
print("com:",com)
print("rnd:",rnd)
print("result:",result)