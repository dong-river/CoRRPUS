## Mary went back to the bathroom.
## Daniel went back to the bathroom.
## Mary got the milk there.
## Mary journeyed to the kitchen.
## Mary got the apple there.
## Mary moved to the hallway.
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
        self.Daniel = character("Daniel")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        ## Mary went back to the bathroom.
        self.Mary.location = "bathroom"
        ## Daniel went back to the bathroom.
        self.Daniel.location = "bathroom"
        ## Mary got the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Mary journeyed to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary got the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Mary moved to the hallway.
        self.Mary.location = "hallway"
        self.apple.location = "hallway"
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()