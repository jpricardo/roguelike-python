#Main code and game loop

from classes import Player, Role, Inventory

player = Player()


while True:
	i = Player()
	Role.amount -= 1
	if Role.amount == 0:
		x = Role()
		break
		
player.drop_item('Sword')
print(player.inventory.item_list())
player.pick_item('Spear')
print(player.inventory.item_list())
