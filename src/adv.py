from room import Room
from player import Player
from textwrap import fill
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
def location(player, prev_room = ''):
	if player.current_room.name!= prev_room:
		print(f"\n{player.name} is in room: {player.current_room.name}\n{fill(player.current_room.description, 50)}\n")
# Make a new player object that is currently in the 'outside' room.
player = Player('Leon', room['outside'])

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


location(player)
while True:

	cmd = input('(N/E/S/W) -->')

	if moves.get(cmd):
		prev_room = player.current_room.name
		player.current_room = player.current_room.move(moves[cmd])
		location(player, prev_room)
	elif cmd == 'q':
		break
	else:
		print('\n Invalid command \n')