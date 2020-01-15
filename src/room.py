# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	def __init__(self, name, description, items=[]):
		self.name = name
		self.description = description
		self.items = items
		self.n_to = self
		self.e_to = self
		self.s_to = self
		self.w_to = self
	def move(self, direction):
		new_room = self.__getattribute__(direction)
		if new_room == self:
			print("\nYou can't go that way!\n")
		return new_room
	