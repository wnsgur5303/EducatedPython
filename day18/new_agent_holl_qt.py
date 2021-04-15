import pylab
import random
import numpy as np
from keras.layers import Dense
from keras.optimizers import Adam

from keras.models import Sequential
from collections import deque

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

EPISODES = 500
ACTION_SPACE = [0, 1]
COUNT = 50
FLAG_MODEL = False
TRAIN_START = 1000
MEMORY_DEQUE = 2000


form_class = uic.loadUiType("untitled.ui")[0]
class GameEnv(QMainWindow, form_class):
	def __init__(self):
		self.score = 0
		self.arr_com = []
		self.seq = 0
		self.seq_end = COUNT

	def initialize(self):
		self.score = 0
		self.arr_com = []
		self.seq = 0
		for i in range(self.seq_end):
			self.arr_com.append(random.randrange(0, len(ACTION_SPACE)))

	def get_state(self):
		a = np.array([self.arr_com[self.seq]])
		return a

	def is_end(self):
		if self.seq >= self.seq_end:
			return True
		else:
			return False

	def step(self, mine):
		now_score = self.score
		self.do_work(mine)
		next_score = self.score

		reward = next_score - now_score
		flag_end = self.is_end()
		next_state = np.array([-1])
		next_state = np.reshape(next_state, [1, 1])

		if flag_end == False:
			next_state = self.get_state()

		return next_state, reward, flag_end

	def do_work(self, mine):
		if self.arr_com[self.seq] == mine:
			self.score += 1
		self.seq += 1

class Agent:
	def __init__(self):
		self.load_model = FLAG_MODEL

		# 0: 홀 1: 짝 
		self.action_space = ACTION_SPACE
		self.action_size = len(self.action_space)
		self.state_size = 1
		self.discount_factor = 0.99
		self.learning_rate = 0.001

		self.epsilon = 1.0
		self.epsilon_decay = 0.9999
		self.epsilon_min = 0.01
		self.batch_size = 64
		self.train_start = TRAIN_START

		self.model = self.build_model()
		self.model_target = self.build_model()
		self.update_model_target()
		self.memory = deque(maxlen = MEMORY_DEQUE)

		if self.load_model:
			self.model          .load_weights('save_model/mdl_origin.h5')
			self.model_target   .load_weights('save_model/mdl_target.h5')

	def build_model(self):
		model = Sequential()
		model.add(Dense(10, input_dim = self.state_size, activation = 'relu', kernel_initializer = 'he_uniform'))
		model.add(Dense(10, activation = 'relu', kernel_initializer = 'he_uniform'))
		model.add(Dense(self.action_size, activation = 'linear', kernel_initializer = 'he_uniform'))
		model.compile(loss = 'mse', optimizer = Adam(lr = self.learning_rate))
		return model

	def append_in_memory(self, state, mine, reward, next_state, flag_end):
		self.memory.append((state, mine, reward, next_state, flag_end))

	def update_model_target(self):
		self.model_target.set_weights(self.model.get_weights())

	def get_predict(self, state):
		if np.random.rand() <= self.epsilon:
			return random.randrange(self.action_size)
		else:
			state = np.float32(state)
			q_values = self.model.predict(state)
			return np.argmax(q_values[0])

	def train_model(self):
		if self.epsilon > self.epsilon_min:
			self.epsilon *= self.epsilon_decay

		mini_batch = random.sample(self.memory, self.batch_size)

		arr_state = np.zeros((self.batch_size, self.state_size))
		arr_state_next = np.zeros((self.batch_size, self.state_size))
		arr_mine, arr_reward, arr_flag_end = [], [], []

		for i in range(self.batch_size):
			arr_state[i] = mini_batch[i][0]
			arr_mine.append(mini_batch[i][1])
			arr_reward.append(mini_batch[i][2])
			arr_state_next[i] = mini_batch[i][3]
			arr_flag_end.append(mini_batch[i][4])

		arr_predict      = self.model.predict(arr_state)
		arr_predict_target  = self.model_target.predict(arr_state_next)

		for i in range(self.batch_size):
			arr_predict[i][arr_mine[i]] = arr_reward[i] + self.discount_factor * np.amax(arr_predict_target[i])
# 			if i == 0:
# 				print(i,"------------arr_reward[i]:",arr_reward[i],"self.discount_factor:",self.discount_factor,"np.amax(arr_predict_target[i]):",arr_predict_target[i][0],arr_predict_target[i][1])
			
		self.model.fit(arr_state, arr_predict, batch_size = self.batch_size, epochs = 1, verbose = 0)

if __name__ == "__main__":
	app = QApplication(sys.argv) 
	gameenv = GameEnv()
	gameenv.show()
	app.exec_()
	agent = Agent()
	
	global_step = 0
	arr_score, arr_episode = [], []

	for epi in range(EPISODES):
		flag_end = False
		score = 0
		gameenv.initialize()
		
		while not flag_end:
			global_step += 1
			now_state = gameenv.get_state()
			now_state = np.reshape(now_state, [1, 1])
			mine = agent.get_predict(now_state)
			
			next_state, reward, flag_end = gameenv.step(mine)

			next_state = np.reshape(next_state, [1, 1])
			agent.append_in_memory(now_state, mine, reward, next_state, flag_end)

			if len(agent.memory) >= agent.train_start:
				agent.train_model()

# 			now_state = next_state
			score += reward

		if flag_end:
			agent.update_model_target()
			arr_score.append(score)
			arr_episode.append(epi)
			pylab.plot(arr_episode, arr_score, 'b')
			pylab.savefig("agent.png")
			print("episode: ", epi," global_step", global_step, " score: ", score, " epsilon: ", agent.epsilon)

		if epi % 100 == 0:
			print("save_weights")
			agent.model.save_weights("save_model/mdl_origin.h5")
			agent.model_target.save_weights("save_model/mdl_target.h5")
			print(agent.memory)

	app.exec_()