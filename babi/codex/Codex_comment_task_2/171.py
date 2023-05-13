## John went back to the bedroom.
## John journeyed to the kitchen.
## John took the milk there.
## Sandra took the football there.
## Daniel travelled to the hallway.
## Daniel picked up the apple there.
## Mary travelled to the bedroom.
## Daniel journeyed to the bedroom.
## John went back to the hallway.
## Daniel went back to the bathroom.
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
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        ## John went back to the bedroom.
        self.John.location = "bedroom"
        ## John journeyed to the kitchen.
        self.John.location = "kitchen"
        ## John took the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Sandra took the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Daniel travelled to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel picked up the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## Daniel journeyed to the bedroom.
        self.Daniel.location = "bedroom"
        ## John went back to the hallway.
        self.John.location = "hallway"
        ## Daniel went back to the bathroom.
        self.Daniel.location = "bathroom"
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()