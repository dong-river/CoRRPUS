## Daniel moved to the office.
## Daniel travelled to the bedroom.
## John took the milk there.
## John travelled to the garden.
## Sandra moved to the office.
## Daniel went back to the office.
## John went to the kitchen.
## Mary travelled to the garden.
## John picked up the football there.
## John dropped the football.
## Where is the football? 

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
        self.Sandra = character("Sandra")
        self.Mary = character("Mary")
        self.milk = object("milk")
        self.football = object("football")

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
        ## Daniel moved to the office.
        self.go(character = self.Daniel, location = "office")
        ## Daniel travelled to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John took the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## John travelled to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra moved to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel went back to the office.
        self.go(character = self.Daniel, location = "office")
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary travelled to the garden.
        self.go(character = self.Mary, location = "garden")
        ## John picked up the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John dropped the football.
        self.drop(character = self.John, item = self.football)
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()