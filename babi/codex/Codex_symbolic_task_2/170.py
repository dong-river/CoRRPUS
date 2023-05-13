## John went back to the bedroom.
## John journeyed to the kitchen.
## John took the milk there.
## Sandra took the football there.
## Daniel travelled to the hallway.
## Daniel picked up the apple there.
## Mary travelled to the bedroom.
## Daniel journeyed to the bedroom.
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
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.football = object("football")
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
        ## John went back to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## John journeyed to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## John took the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## Sandra took the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Daniel travelled to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel picked up the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## Mary travelled to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Daniel journeyed to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()