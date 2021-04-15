import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

# make 3d axes
fig = plt.figure()
ax = fig.gca(projection='3d')

# test data
# np # 파이썬에서 선형 대수학을 만들어주는..
x = np.array([1,1,1,1,1])#1단위로 -10부터 10까지인듯
y = np.array([5,4,3,2,1])#선형 대수학을 빨리하기위한 
z = np.array([0,0,4,2,0])




# plot test data
ax.plot(x+1, y, z)
ax.plot(x+2, y, z)
ax.plot(x+3, y, z)


# make labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()