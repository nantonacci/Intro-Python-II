# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items


    def __str__(self):
        output = ""

        output += f"You enter the {self.name}.\n{self.description}\n\n After a quick glance around the room, you notice the following items:\n"

        for item in self.items:
            output += item.name + "\n"

        return output