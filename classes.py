#Class "skeletons" for the main scrip and game loop

import random as rd



class Player():
	
	roles = {}
	
	def __init__(self):
		self.name = 'jotinha'
		self.hp = 100
		self.att = rd.randint(0, 100)
		self.inventory = Inventory(size=10, items=['Sword', 'Shield'])
		print(f'Name: {self.name}, HP: {self.hp}, Attack: {self.att}, {self.inventory.items}')
		
	def pick_item(self, item):
		self.inventory.add_item(item)
		
	def drop_item(self, item=False):
		if item:
			self.inventory.items.remove(item)
		else:
			self.inventory.items.pop()
		









		
class Inventory():
	
	def __init__(self, size, items=False):
	
		self.items = []
		if items:
			self.items = items
		
		self.max_size = size
		
	def item_list(self):
		return self.items
		
	def add_item(self, item):
		self.item_list().append(item)
		
class Role():
	amount = 4
	
	def __init__(self):
		print('Hello')
		
		
		
