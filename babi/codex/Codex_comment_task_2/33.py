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
## Sandra got the apple there.
## John went to the kitchen.
## Mary went to the bathroom.
## Mary journeyed to the garden.
## Sandra went back to the kitchen.
## Sandra put down the apple there.
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
        self.apple.location = "garden"
        ## Mary left the football.
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "garden"
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## John went back to the bedroom.
        self.John.location = "bedroom"
        ## Sandra got the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Mary went to the bathroom.
        self.Mary.location = "bathroom"
        ## Mary journeyed to the garden.
        self.Mary.location = "garden"
        ## Sandra went back to the kitchen.
        self.Sandra.location = "kitchen"
        ## Sandra put down the apple there.
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "kitchen"
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()