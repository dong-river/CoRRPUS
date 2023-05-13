## Mary went back to the bathroom.
## Daniel went back to the bathroom.
## Mary got the milk there.
## Mary journeyed to the kitchen.
## Mary got the apple there.
## Mary moved to the hallway.
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
        self.Mary = character("Mary")
        self.Daniel = character("Daniel")
        self.milk = object("milk")
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
        ## Mary went back to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Daniel went back to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Mary got the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Mary journeyed to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary got the apple there.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Mary moved to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()