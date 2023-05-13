## Daniel journeyed to the office.
## Daniel went back to the bedroom.
## Mary went back to the kitchen.
## Mary got the football there.
## Daniel travelled to the hallway.
## John journeyed to the bedroom.
## Daniel got the apple there.
## Sandra travelled to the garden.
## Daniel travelled to the garden.
## Daniel dropped the apple.
## Mary left the football.
## Mary journeyed to the bedroom.
## John moved to the hallway.
## John went back to the bedroom.
## 
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
        self.football = object("football")
        self.Daniel = character("Daniel")
        self.apple = object("apple")

    def story(self):
        ## Daniel journeyed to the office.
        self.Daniel.location = "office"
        ## Daniel went back to the bedroom.
        self.Daniel.location = "bedroom"
        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary got the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## Daniel travelled to the hallway.
        self.Daniel.location = "hallway"
        ## John journeyed to the bedroom.
        self.John.location = "bedroom"
        ## Daniel got the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Sandra travelled to the garden.
        self.Sandra.location = "garden"
        ## Daniel travelled to the garden.
        self.Daniel.location = "garden"
        ## Daniel dropped the apple.
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Mary left the football.
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## John went back to the bedroom.
        self.John.location = "bedroom"
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()