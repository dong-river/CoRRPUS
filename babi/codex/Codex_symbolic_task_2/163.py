## John moved to the bedroom.
## Sandra journeyed to the office.
## Sandra moved to the kitchen.
## Daniel travelled to the bedroom.
## John went back to the office.
## Mary travelled to the garden.
## Sandra moved to the hallway.
## Sandra went to the garden.
## John went back to the kitchen.
## Daniel went to the office.
## Sandra moved to the hallway.
## Daniel picked up the apple there.
## Mary went to the bedroom.
## Daniel went back to the garden.
## Daniel left the apple.
## Daniel grabbed the apple there.
## Sandra took the football there.
## Daniel discarded the apple.
## Mary journeyed to the kitchen.
## Sandra journeyed to the kitchen.
## Daniel travelled to the bedroom.
## Sandra went to the bedroom.
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
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.Mary = character("Mary")
        self.apple = object("apple")
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
        ## John moved to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra journeyed to the office.
        self.go(character = self.Sandra, location = "office")
        ## Sandra moved to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Daniel travelled to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John went back to the office.
        self.go(character = self.John, location = "office")
        ## Mary travelled to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Sandra moved to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Sandra went to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## John went back to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Daniel went to the office.
        self.go(character = self.Daniel, location = "office")
        ## Sandra moved to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Daniel picked up the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## Mary went to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Daniel went back to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel left the apple.
        self.drop(character = self.Daniel, item = self.apple)
        ## Daniel grabbed the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## Sandra took the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Daniel discarded the apple.
        self.drop(character = self.Daniel, item = self.apple)
        ## Mary journeyed to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Sandra journeyed to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Daniel travelled to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Sandra went to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()