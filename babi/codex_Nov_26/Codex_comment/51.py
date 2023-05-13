## Daniel took the milk there.
## John journeyed to the garden.
## Daniel went back to the hallway.
## Daniel journeyed to the bathroom.
## Daniel dropped the milk.
## Daniel took the milk there.
## John grabbed the apple there.
## Sandra journeyed to the kitchen.
## John went to the hallway.
## Sandra went back to the garden.
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
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        ## Daniel took the milk there.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Daniel went back to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel journeyed to the bathroom.
        self.Daniel.location = "bathroom"
        ## Daniel dropped the milk.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Daniel took the milk there.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## John grabbed the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Sandra journeyed to the kitchen.
        self.Sandra.location = "kitchen"
        ## John went to the hallway.
        self.John.location = "hallway"
        ## Sandra went back to the garden.
        self.Sandra.location = "garden"
        ## Where is the apple?
        print(self.apple.location)

world = World()
world.story()