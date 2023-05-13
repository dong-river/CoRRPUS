## Sandra took the milk there.
## Sandra journeyed to the garden.
## Sandra dropped the milk there.
## Sandra journeyed to the bathroom.
## John travelled to the garden.
## John went to the kitchen.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.milk = object("milk")

    def story(self):
        ## Sandra took the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra journeyed to the garden.
        self.Sandra.location = "garden"
        ## Sandra dropped the milk there.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "garden"
        ## Sandra journeyed to the bathroom.
        self.Sandra.location = "bathroom"
        ## John travelled to the garden.
        self.John.location = "garden"
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()