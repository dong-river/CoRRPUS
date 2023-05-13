## Sandra took the milk there.
## Sandra journeyed to the garden.
## Sandra dropped the milk there.
## Sandra journeyed to the bathroom.
## John travelled to the garden.
## John went to the kitchen.
## John got the apple there.
## Daniel moved to the bathroom.
## John dropped the apple.
## Daniel moved to the hallway.
## John picked up the apple there.
## Mary went back to the office.
## Mary journeyed to the kitchen.
## John discarded the apple.
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
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        ## Sandra took the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra journeyed to the garden.
        self.Sandra.location = "garden"
        ## Sandra dropped the milk there.
        self.milk.location = "garden"
        self.milk.carrier = None
        ## Sandra journeyed to the bathroom.
        self.Sandra.location = "bathroom"
        ## John travelled to the garden.
        self.John.location = "garden"
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## John got the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Daniel moved to the bathroom.
        ## John dropped the apple.
        self.apple.location = "bathroom"
        self.apple.carrier = None
        ## Daniel moved to the hallway.
        ## John picked up the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Mary went back to the office.
        self.Mary.location = "office"
        ## Mary journeyed to the kitchen.
        self.Mary.location = "kitchen"
        ## John discarded the apple.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Where is the apple? 
        print(self.apple.location)

world = World()
world.story()