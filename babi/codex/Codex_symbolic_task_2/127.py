## Daniel got the apple there.
## Daniel dropped the apple.
## Mary moved to the bedroom.
## Daniel journeyed to the hallway.
## Mary travelled to the hallway.
## Sandra moved to the bedroom.
## Mary went back to the bathroom.
## Daniel moved to the kitchen.
## Mary went to the kitchen.
## Daniel moved to the office.
## Mary picked up the football there.
## Mary put down the football.
## John travelled to the office.
## Daniel went to the bathroom.
## Mary got the football there.
## Mary discarded the football.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
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
        ## Daniel got the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## Daniel dropped the apple.
        self.drop(character = self.Daniel, item = self.apple)
        ## Mary moved to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Daniel journeyed to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Mary travelled to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Sandra moved to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Mary went back to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Daniel moved to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Mary went to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Daniel moved to the office.
        self.go(character = self.Daniel, location = "office")
        ## Mary picked up the football there.
        self.pick_up(character = self.Mary, item = self.football)
        ## Mary put down the football.
        self.drop(character = self.Mary, item = self.football)
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## Daniel went to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Mary got the football there.
        self.pick_up(character = self.Mary, item = self.football)
        ## Mary discarded the football.
        self.drop(character = self.Mary, item = self.football)
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()