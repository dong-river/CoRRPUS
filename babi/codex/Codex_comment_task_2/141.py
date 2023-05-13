## Daniel journeyed to the hallway.
## Daniel picked up the football there.
## Daniel journeyed to the bedroom.
## Daniel dropped the football.
## Sandra travelled to the bedroom.
## Daniel journeyed to the kitchen.
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
        self.football = object("football")

    def story(self):
        ## Daniel journeyed to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel picked up the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Daniel journeyed to the bedroom.
        self.Daniel.location = "bedroom"
        ## Daniel dropped the football.
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "bedroom"
        ## Sandra travelled to the bedroom.
        ## Daniel journeyed to the kitchen.
        self.Daniel.location = "kitchen"
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()