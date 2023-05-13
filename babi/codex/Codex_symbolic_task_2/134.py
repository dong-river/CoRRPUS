## Daniel travelled to the hallway.
## Mary moved to the kitchen.
## John grabbed the football there.
## John discarded the football.
## Sandra journeyed to the kitchen.
## Sandra picked up the milk there.
## Daniel moved to the office.
## John took the football there.
## John went to the kitchen.
## Mary moved to the office.
## Sandra put down the milk.
## John left the football.
## John moved to the hallway.
## Sandra picked up the football there.
## Daniel went to the garden.
## Daniel went to the bathroom.
## Mary moved to the bedroom.
## Mary took the apple there.
## Sandra went back to the hallway.
## Sandra discarded the football.
## Sandra grabbed the football there.
## Daniel moved to the garden.
## Daniel travelled to the bedroom.
## Daniel moved to the garden.
## Sandra discarded the football.
## John travelled to the office.
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
        ## Daniel travelled to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Mary moved to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## John grabbed the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John discarded the football.
        self.drop(character = self.John, item = self.football)
        ## Sandra journeyed to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Sandra picked up the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Daniel moved to the office.
        self.go(character = self.Daniel, location = "office")
        ## John took the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## Sandra put down the milk.
        self.drop(character = self.Sandra, item = self.milk)
        ## John left the football.
        self.drop(character = self.John, item = self.football)
        ## John moved to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Sandra picked up the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel went to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Mary moved to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary took the apple there.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Sandra went back to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Sandra discarded the football.
        self.drop(character = self.Sandra, item = self.football)
        ## Sandra grabbed the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Daniel moved to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel travelled to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel moved to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Sandra discarded the football.
        self.drop(character = self.Sandra, item = self.football)
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()