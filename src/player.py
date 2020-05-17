# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, room, inventory=[]):
        self.room = room
        self.inventory = inventory

    def log_inv(self):
        print("Your inventory contains:")
        for item in self.inventory:
            print(f"{item.name}")
        print("")