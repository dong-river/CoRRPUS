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

    def story(self):
        ## Daniel got the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Daniel dropped the apple.
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Mary moved to the bedroom.
        self.Mary.location = "bedroom"
        ## Daniel journeyed to the hallway.
        self.Daniel.location = "hallway"
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        ## Sandra moved to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary went back to the bathroom.
        self.Mary.location = "bathroom"
        ## Daniel moved to the kitchen.
        self.Daniel.location = "kitchen"
        ## Mary went to the kitchen.
        self.Mary.location = "kitchen"
        ## Daniel moved to the office.
        self.Daniel.location = "office"
        ## Mary picked up the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## Mary put down the football.
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None
        ## John travelled to the office.
        self.John.location = "office"
        ## Daniel went to the bathroom.
        self.Daniel.location = "bathroom"
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()