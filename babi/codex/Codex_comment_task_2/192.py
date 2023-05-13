## Mary travelled to the bedroom.
## Daniel grabbed the apple there.
## Daniel went to the garden.
## John travelled to the office.
## Daniel left the apple.
## John travelled to the hallway.
## Sandra went to the office.
## Daniel journeyed to the hallway.
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
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## Daniel grabbed the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        self.apple.location = "garden"
        ## John travelled to the office.
        self.John.location = "office"
        ## Daniel left the apple.
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        ## John travelled to the hallway.
        self.John.location = "hallway"
        ## Sandra went to the office.
        self.Sandra.location = "office"
        ## Daniel journeyed to the hallway.
        self.Daniel.location = "hallway"
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()