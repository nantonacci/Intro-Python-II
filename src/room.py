# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description


    def __str__(self):
        output = ""

        output += f"You enter the {self.name}.\n{self.description}\n"

        # for item in self.items:
        #     output += item + "\n"

        return output

# class List:
#     def __init__(self, name, description, items, n_to, s_to, e_to, w_to):
#         super().__init__(name, description, items, n_to, s_to, e_to, w_to)