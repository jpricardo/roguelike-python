#Class "skeletons" for the main scrip and game loop

import random as rd
import names as ns


class Player():
	
	roles = {}
	
	def __init__(self):
		self.name = ns.get_first_name()
		self.hp = 100
		self.att = rd.randint(0, 100)
		print(f'Name: {self.name}, HP: {self.hp}, Attack: {self.att}')
		
		
		
class Role():
	amount = 4
	
	def __init__(self):
		print('Hello')
		
		
		
