## Mary travelled to the bedroom.
## Daniel grabbed the apple there.
## Daniel went to the garden.
## John travelled to the office.
## Daniel left the apple.
## John travelled to the hallway.
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
        self.football = object("football")
        self.apple = object("apple")

    def story(self):
        ## Mary moved to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary got the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        self.football.location = "garden"
        ## Where is the football?
        print(self.football.location)
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## Daniel grabbed the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Daniel went to the garden.
        self.Mary.location = "garden"
        ## John travelled to the office.
        self.John.location = "office"
        ## Daniel left the apple.
        self.apple.carrier = None
        ## John travelled to the hallway.
        self.John.location = "hallway"
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()