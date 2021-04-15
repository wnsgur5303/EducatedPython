import numpy as np

a = [1,2,3,4,5,6,7,8]
print(a)

b=np.reshape(a,[2,4])
b= b+1
#자바에선 말이 안되는데 여기선 됨 각각의 수에 1이 더해짐 
#이게 np(넘피)의 기능 선형대수학을 하기 위한 라이브러리
print(b)

c = [
        [1,2,3,4],
        [5,6,7,8]
    ]
print(c[1][2])
print(b[1,2])