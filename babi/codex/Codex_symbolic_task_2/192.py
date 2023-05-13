## Mary travelled to the bedroom.
## Daniel grabbed the apple there.
## Daniel went to the garden.
## John travelled to the office.
## Daniel left the apple.
## John travelled to the hallway.
## Sandra went to the office.
## Daniel journeyed to the hallway.
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
        ## Mary travelled to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Daniel grabbed the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## Daniel left the apple.
        self.drop(character = self.Daniel, item = self.apple)
        ## John travelled to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Sandra went to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel journeyed to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()