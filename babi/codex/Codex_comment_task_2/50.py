## Daniel took the milk there.
## John journeyed to the garden.
## Daniel went back to the hallway.
## Daniel journeyed to the bathroom.
## Where is the milk? 

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
        self.milk = object("milk")

    def story(self):
        ## Daniel took the milk there.
        self.Daniel.location = "there"
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Daniel went back to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel journeyed to the bathroom.
        self.Daniel.location = "bathroom"
        self.milk.location = "bathroom"
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()