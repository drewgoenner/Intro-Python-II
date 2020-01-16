from room import Room
from player import Player
from textwrap import fill
from item import Item
from item import LightSource
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", True),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", False),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", False),

    'dungeon': Room("Filthy Dungeon", """The stench of death overwhelms you as you enter the room.  Ancient bones and more freshly rotten corpses litter the floor, walls, and cells of this dungeon.  It looks like no one fed the prisoners and they died agonizing deaths. A grimy passage leads to the west.""", False)
}

item = {
	'lamp': LightSource("lamp", "a lamp that glows brightly"),

	'goblet': Item("goblet", "an empty silver goblet"),

	'hat': Item("hat", "a brightly plumed hat"),

	'nothing': Item("nothing", "a frightening, overwhelming lack of anything"),

	'dagger': Item("dagger", "an old, rusty dagger"),

	'feces': Item("feces", "rat droppings, they look fresh"),

	'rags': Item("rags", "some rags cover old, unfound treasure. these are just rags"),

	'femur': Item("femur", "an ancient human femur, still mostly whole, though sharpened on one end.")
	
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['dungeon']
room['dungeon'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#

# Add items to rooms
room['outside'].items =[item['lamp']]
room['foyer'].items = [item['goblet'], item['hat']]
room['overlook'].items = [item['nothing']]
room['narrow'].items = [item['dagger'], item['feces']]
room['treasure'].items = [item['rags']]
room['dungeon'].items = [item['femur']]
# Main
#
def location(player, prev_room = ''):
	if player.current_room.name!= prev_room:
		print(f"\n{player.name} is in room: {player.current_room.name}\n{fill(player.current_room.description, 50)}\n")
	if player.current_room.is_light==True:
		print("\nIn this room you see: \n ")
		for item in player.current_room.items:
			print(item.name)
		print('\nYou are carrying:\n')
		for item in player.inventory:
			print(item.name)
	else:
		print("\nIn this room you see:\nNothing, it's dark!\n")
# Make a new player object that is currently in the 'outside' room.
player = Player(input("What is your name? "), room['outside'], [])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def intro():
	print('\nWelcome to the game!\n')

intro()
moves = {'n':'n_to', 'e':'e_to', 's':'s_to', 'w':'w_to'}
inv = ['i', 'inventory']
grab = ['take', 'get']

location(player)
while True:

	cmd = input('What would you like to do? -->')
	words = cmd.split(' ')

	if moves.get(cmd):
		prev_room = player.current_room.name
		player.current_room = player.current_room.move(moves[cmd])
		location(player, prev_room)
	elif words[0] in grab:
		player.take(item.get(words[1]))
	elif words[0] == 'drop':
		player.drop(item.get(words[1]))
	elif cmd in inv:
		player.inven()
	elif cmd == 'q':
		print('\nThanks for playing, come again!\n')
		break
	else:
		print('\n "What were you trying to do?" \n')