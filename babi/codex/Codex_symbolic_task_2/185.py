## Sandra journeyed to the bathroom.
## Mary took the apple there.
## Sandra went back to the kitchen.
## Mary went back to the office.
## Where is the apple? 

class character:
    def __init__(self, name):
        self.name = name
        self.location = ""
        self.inventory = []

class object:
    def __init__(self, name):
        self.name = name
        self.location = ""
        self.carrier = None

class World:
    def __init__(self):
        self.Sandra = character("Sandra")
        self.Mary = character("Mary")
        self.apple = object("apple")

    def go(self, character, location):
        character.location = location
        for item in character.inventory:
            item.location = location

    def pick_up(self, character, item):
        character.inventory.append(item)
        item.location = character.location
        item.carrier = character

    def drop(self, character, item):
        character.inventory.remove(item)
        item.location = character.location
        item.carrier = None

    def story(self):
        ## Sandra journeyed to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Mary took the apple there.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Sandra went back to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Mary went back to the office.
        self.go(character = self.Mary, location = "office")
        ## Where is the apple?
        print(self.apple.location)

world = World()
world.story()