import numpy as np
from keras.layers import Dense
from keras.optimizers import Adam
from keras.models import Sequential
from collections import deque
from random import *

def build_model():
	model = Sequential()
	model.add(Dense(10, input_dim = 1, activation = 'relu', kernel_initializer = 'he_uniform'))
	model.add(Dense(10, activation = 'relu', kernel_initializer = 'he_uniform'))
	model.add(Dense(2, activation = 'linear', kernel_initializer = 'he_uniform'))
	model.compile(loss = 'mse', optimizer = Adam(lr = 0.001))
	return model



if __name__ == "__main__":
	model = build_model()
	model.load_weights('save_model/mdl_origin.h5')
	
	model.summary()


	jumsu = 0
	for i in range(50):
		mine = randint(0,1)

		numpy_mine = np.array([mine])
		#numpy로 해야 속도가 나옴
		numpy_mine = np.reshape(numpy_mine, [1, 1])
	
		# 인공지능의 출력을 받는다 
		numpy_mine = np.float32(numpy_mine)
		#신경망을 통해서 주는값
		q_values = model.predict(numpy_mine)
		print(q_values)
		com = np.argmax(q_values[0])

		# 데이터 출력
		if mine == 0:
			print('mine: 홀',end=" ")
		elif mine == 1:
			print('mine: 짝',end=" ")
			
		if com == 0:
			print('com: 홀',end=" ")
		elif com == 1:
			print('com: 짝',end=" ")
			
		if mine == com :
			jumsu+=1
	
	print("jumsu:",jumsu)
