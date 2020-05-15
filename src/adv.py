from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Potato", "A dusty potato."), Item("Candle", "Surprisingly, never used.")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Rock", "Just a rock."), Item("Twig", "Did it move? No. It's just a twig.")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Coin", "A rusty coin."), Item("Dandelion", "A weed found sprouting from the floor.")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Penknife", "A small, sharp, folding knife."), Item("Parchment", "A scrap of parchment.")])
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

# Make a new player object that is currently in the 'outside' room.


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

player = Player(room['outside'], [])

command = ""

while not command == "q":
    print(player.room)
    command = input("Which way will you go?\n[n] North [e] East [s] South [w] West [q] Quit\n")
    userinput = command.split()

# directional inputs here
    if len(userinput) == 1:

        if command == "n":
            try:
                player.room = player.room.n_to
            except AttributeError:
                print(f"You can't go that direction.\n \n")

        elif command == "e":
            try:
                player.room = player.room.e_to
            except AttributeError:
                print(f"You can't go that direction.\n \n")

        elif command == "s":
            try:
                player.room = player.room.s_to
            except AttributeError:
                print(f"You can't go that direction.\n \n")

        elif command == "w":
            try:
                player.room = player.room.w_to
            except AttributeError:
                print(f"You can't go that direction.\n \n")

        elif command == "quit":
            exit()
    
    # pickup /drop inputs here
    if len(userinput) == 2:   

        if userinput[0] == "drop":
            try:
                for item in player.inventory:
                    if item == userinput[1]:
                        player.room.items.append(item)
                        print(Item.on_drop)
            except AttributeError:
                print("No such item to take.")
        
        if userinput[0] == "take":
            try:
                for item in player.room.items:
                    if item == userinput[1]:
                        player.inventory.append(item)
                        print(Item.on_take)
            except AttributeError:
                print("No such item to take.")

