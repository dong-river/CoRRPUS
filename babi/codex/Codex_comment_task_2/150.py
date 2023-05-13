## Daniel travelled to the garden.
## Sandra went back to the bedroom.
## John travelled to the bedroom.
## Sandra grabbed the apple there.
## Daniel travelled to the kitchen.
## Sandra left the apple.
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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.apple = object("apple")

    def story(self):
        ## Daniel travelled to the garden.
        self.Daniel.location = "garden"
        ## Sandra went back to the bedroom.
        self.Sandra.location = "bedroom"
        ## John travelled to the bedroom.
        self.John.location = "bedroom"
        ## Sandra grabbed the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## Daniel travelled to the kitchen.
        self.Daniel.location = "kitchen"
        ## Sandra left the apple.
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()