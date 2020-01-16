# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name, current_room, inventory=[]):
		self.name = name
		self.current_room = current_room
		self.inventory = inventory
		for item in self.inventory:
			if item is isinstance('item', LightSource):
				# self.current_room.is_light=True
				print("True")
			else:
				print("False")
	def take(self, item):
		if item in self.current_room.items:
			item.on_take()
			self.current_room.items.remove(item)
			self.inventory.append(item)
		else:
			print('\nNo such item is here!\n')
	def drop(self, item):
		if item in self.inventory:
			item.on_drop()
			self.inventory.remove(item)
			self.current_room.items.append(item)
		else:
			print('\nYou are carrying no such item!\n')
	def inven(self):
		print('\nYou are carrying:\n')
		for item in self.inventory:
			print(item.name)