class Item:
	def __init__(self, name, description):
		self.name = name
		self.description = description
	def on_take(self):
		print(f"You have picked up {self.name}")
	def on_drop(self):
		print(f"You drop {self.name}")

class LightSource(Item):
	def __init__(self, name, description):
		self.name = name
		self.description = description
	def on_drop(self):
		print(f"Ok, if you think dropping your {self.name} in a dark cave is a good idea, who am I to argue?")

