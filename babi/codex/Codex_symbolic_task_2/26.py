## Daniel moved to the kitchen.
## John grabbed the football there.
## John left the football there.
## Mary journeyed to the hallway.
## John grabbed the milk there.
## John travelled to the kitchen.
## Mary journeyed to the kitchen.
## Sandra went to the office.
## Where is the milk? 

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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.Mary = character("Mary")
        self.Sandra = character("Sandra")
        self.football = object("football")
        self.milk = object("milk")

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
        ## Daniel moved to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## John grabbed the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John left the football there.
        self.drop(character = self.John, item = self.football)
        ## Mary journeyed to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John grabbed the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## John travelled to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary journeyed to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Sandra went to the office.
        self.go(character = self.Sandra, location = "office")
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()