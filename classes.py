#Class "skeletons" for the main scrip and game loop

import random as rd



class Player():
	
	roles = {}
	
	def __init__(self):
		self.name = 'jotinha'
		self.hp = 100
		self.att = rd.randint(0, 100)
		self.inventory = Inventory(size=10, items=['Sword'])
		print(f'Name: {self.name}, HP: {self.hp}, Attack: {self.att}, {self.inventory.items}')
		
		
class Inventory():
	
	def __init__(self, size, items=False):
	
		self.items = []
		if items:
			self.items = items
		
		self.max_size = size
		
class Role():
	amount = 4
	
	def __init__(self):
		print('Hello')
		
		
		
