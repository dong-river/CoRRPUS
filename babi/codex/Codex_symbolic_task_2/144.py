## Daniel journeyed to the hallway.
## Daniel picked up the football there.
## Daniel journeyed to the bedroom.
## Daniel dropped the football.
## Sandra travelled to the bedroom.
## Daniel journeyed to the kitchen.
## Sandra grabbed the football there.
## John travelled to the office.
## Sandra discarded the football.
## Mary went back to the hallway.
## Daniel went to the hallway.
## Daniel travelled to the bedroom.
## Mary travelled to the office.
## John journeyed to the kitchen.
## Sandra went back to the office.
## Daniel took the football there.
## Daniel went to the garden.
## Mary travelled to the bedroom.
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
        self.Sandra = character("Sandra")
        self.John = character("John")
        self.Mary = character("Mary")
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
        ## Daniel journeyed to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel picked up the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Daniel journeyed to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel dropped the football.
        self.drop(character = self.Daniel, item = self.football)
        ## Sandra travelled to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Daniel journeyed to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Sandra grabbed the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## Sandra discarded the football.
        self.drop(character = self.Sandra, item = self.football)
        ## Mary went back to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Daniel went to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel travelled to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Mary travelled to the office.
        self.go(character = self.Mary, location = "office")
        ## John journeyed to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel took the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Mary travelled to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()