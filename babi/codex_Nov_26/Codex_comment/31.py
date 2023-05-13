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
## 
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
        self.apple = object("apple")
        self.football = object("football")

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
        self.apple.carrier = None
        self.apple.location = "garden"
        self.Daniel.inventory.remove(self.apple)
        ## Mary left the football.
        self.football.carrier = None
        self.football.location = "garden"
        self.Mary.inventory.remove(self.football)
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## 
        ## Where is the apple? 
        print(self.apple.location)

world = World()
world.story()