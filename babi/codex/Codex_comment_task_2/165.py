## John went back to the garden.
## Daniel went to the bathroom.
## Daniel went to the hallway.
## Daniel grabbed the football there.
## Daniel travelled to the bathroom.
## Daniel went to the garden.
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
        ## John went back to the garden.
        self.John.location = "garden"
        ## Daniel went to the bathroom.
        self.Daniel.location = "bathroom"
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel grabbed the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Daniel travelled to the bathroom.
        self.Daniel.location = "bathroom"
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        self.football.location = "garden"
        ## Where is the football? 
        print(self.football.location)
world = World()
world.story()