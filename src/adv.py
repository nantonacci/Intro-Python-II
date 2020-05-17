from room import Room
from player import Player
from item import Item

# Declare all the items

items = {
    'potato': Item("potato", "A dusty potato."),
    'candle': Item("candle", "Surprisingly, never used."),
    'rock': Item("rock", "Just a rock."),
    'twig': Item("twig", "Did it move? No. It's just a twig."),
    'coin': Item("coin", "A rusty coin."),
    'dandelion': Item("dandelion", "A weed found sprouting from the floor."),
    'penknife': Item("penknife", "A small, sharp, folding knife."),
    'parchment': Item("parchment", "A scrap of parchment.")
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['potato'], items['candle']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['rock'], items['twig']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items['coin'], items['dandelion']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['penknife'], items['parchment']])
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

player = Player(room['outside'])

command = ""

while not command == "q":
    print(player.room)
    command = input("Which way will you go?\n[n] North [e] East [s] South [w] West\n[take 'item name'] [drop 'item name'] [i] inventory [q] Quit\n")
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

        elif command == "i":
            Player.log_inv(player)

        elif command == "quit":
            exit()
    
    # pickup /drop inputs here
    if len(userinput) == 2:   
        if userinput [1] not in items.keys():
            print("No such item")
            continue
        item = items[userinput[1]]

        if userinput[0] == "drop":
            if item in player.inventory:
                player.room.items.append(item)
                player.inventory.remove(item)
                Item.on_drop(item)
                Player.log_inv(player)
        
        elif userinput[0] == "take":
            if item in player.room.items:
                player.inventory.append(item)
                player.room.items.remove(item)
                Item.on_take(item)
                Player.log_inv(player)
