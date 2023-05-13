## John got the football there.
## John left the football.
## Daniel went back to the bathroom.
## Mary went back to the bathroom.
## Sandra travelled to the office.
## Daniel got the apple there.
## John got the football there.
## John left the football.
## Daniel journeyed to the kitchen.
## John moved to the bathroom.
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
        self.John = character("John")
        self.Daniel = character("Daniel")
        self.Mary = character("Mary")
        self.Sandra = character("Sandra")
        self.football = object("football")
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
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John left the football.
        self.drop(character = self.John, item = self.football)
        ## Daniel went back to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Mary went back to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Sandra travelled to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel got the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John left the football.
        self.drop(character = self.John, item = self.football)
        ## Daniel journeyed to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## John moved to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()