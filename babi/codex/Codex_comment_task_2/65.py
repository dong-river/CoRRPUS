## Daniel journeyed to the hallway.
## Daniel journeyed to the garden.
## Mary went back to the kitchen.
## Daniel went back to the office.
## Mary journeyed to the bathroom.
## John moved to the hallway.
## Daniel grabbed the football there.
## Daniel went to the kitchen.
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

    def story(self):
        ## Daniel journeyed to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel journeyed to the garden.
        self.Daniel.location = "garden"
        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        ## Daniel went back to the office.
        self.Daniel.location = "office"
        ## Mary journeyed to the bathroom.
        self.Mary.location = "bathroom"
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## Daniel grabbed the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Daniel went to the kitchen.
        self.Daniel.location = "kitchen"
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()