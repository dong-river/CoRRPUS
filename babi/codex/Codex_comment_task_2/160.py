## John moved to the bedroom.
## Sandra journeyed to the office.
## Sandra moved to the kitchen.
## Daniel travelled to the bedroom.
## John went back to the office.
## Mary travelled to the garden.
## Sandra moved to the hallway.
## Sandra went to the garden.
## John went back to the kitchen.
## Daniel went to the office.
## Sandra moved to the hallway.
## Daniel picked up the apple there.
## Mary went to the bedroom.
## Daniel went back to the garden.
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

    def story(self):
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## Sandra journeyed to the office.
        self.Sandra.location = "office"
        ## Sandra moved to the kitchen.
        self.Sandra.location = "kitchen"
        ## Daniel travelled to the bedroom.
        self.Daniel.location = "bedroom"
        ## John went back to the office.
        self.John.location = "office"
        ## Mary travelled to the garden.
        self.Mary.location = "garden"
        ## Sandra moved to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra went to the garden.
        self.Sandra.location = "garden"
        ## John went back to the kitchen.
        self.John.location = "kitchen"
        ## Daniel went to the office.
        self.Daniel.location = "office"
        ## Sandra moved to the hallway.
        self.Sandra.location = "hallway"
        ## Daniel picked up the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Mary went to the bedroom.
        self.Mary.location = "bedroom"
        ## Daniel went back to the garden.
        self.Daniel.location = "garden"
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()