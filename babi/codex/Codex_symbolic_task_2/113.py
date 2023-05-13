## Mary went back to the kitchen.
## Mary travelled to the hallway.
## John journeyed to the bedroom.
## John moved to the garden.
## Daniel went to the hallway.
## John moved to the hallway.
## Daniel journeyed to the bathroom.
## Mary travelled to the garden.
## Daniel went to the hallway.
## John travelled to the office.
## John travelled to the bedroom.
## Mary journeyed to the bedroom.
## John picked up the football there.
## John dropped the football.
## Sandra travelled to the office.
## Mary travelled to the hallway.
## Sandra grabbed the apple there.
## John grabbed the football there.
## Mary went back to the bathroom.
## John discarded the football.
## John picked up the football there.
## Daniel went to the office.
## Sandra discarded the apple.
## Sandra grabbed the apple there.
## John put down the football.
## Daniel moved to the garden.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
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
        ## Mary went back to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary travelled to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John journeyed to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## John moved to the garden.
        self.go(character = self.John, location = "garden")
        ## Daniel went to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## John moved to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Daniel journeyed to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Mary travelled to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Daniel went to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## John travelled to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Mary journeyed to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## John picked up the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John dropped the football.
        self.drop(character = self.John, item = self.football)
        ## Sandra travelled to the office.
        self.go(character = self.Sandra, location = "office")
        ## Mary travelled to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Sandra grabbed the apple there.
        self.pick_up(character = self.Sandra, item = self.apple)
        ## John grabbed the football there.
        self.pick_up(character = self.John, item = self.football)
        ## Mary went back to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## John discarded the football.
        self.drop(character = self.John, item = self.football)
        ## John picked up the football there.
        self.pick_up(character = self.John, item = self.football)
        ## Daniel went to the office.
        self.go(character = self.Daniel, location = "office")
        ## Sandra discarded the apple.
        self.drop(character = self.Sandra, item = self.apple)
        ## Sandra grabbed the apple there.
        self.pick_up(character = self.Sandra, item = self.apple)
        ## John put down the football.
        self.drop(character = self.John, item = self.football)
        ## Daniel moved to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()