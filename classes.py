#Class "skeletons" for the main scrip and game loop

import random as rd


class Player():
	
	roles = {}
	
	def __init__(self):
		self.hp = 100
		self.att = rd.randint(0, 100)
		print(f'HP: {self.hp}, Attack: {self.att}')
		
		
		
class Role():
	amount = 4
	
	def __init__(self):
		print('Hello')
		
		
		
