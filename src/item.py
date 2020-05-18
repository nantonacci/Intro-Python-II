class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"You picked up {self.name} - {self.description}\n")

    def on_drop(self):
        print(f"You dropped {self.name} - {self.description}")