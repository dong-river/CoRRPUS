## John got the football there.
## John left the football.
## Daniel went back to the bathroom.
## Mary went back to the bathroom.
## Sandra travelled to the office.
## Daniel got the apple there.
## John got the football there.
## John left the football.
## Daniel journeyed to the kitchen.
## John moved to the bathroom.
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
        self.apple = object("apple")

    def story(self):
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John left the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Daniel went back to the bathroom.
        self.Daniel.location = "bathroom"
        ## Mary went back to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## Daniel got the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John left the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Daniel journeyed to the kitchen.
        self.Daniel.location = "kitchen"
        ## John moved to the bathroom.
        self.John.location = "bathroom"
        ## Where is the apple?
        print(self.apple.location)

world = World()
world.story()