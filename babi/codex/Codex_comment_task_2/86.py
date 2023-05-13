## John went to the hallway.
## John went back to the bathroom.
## John grabbed the milk there.
## Sandra went back to the office.
## Sandra journeyed to the kitchen.
## Sandra got the apple there.
## Sandra dropped the apple there.
## John dropped the milk.
## Mary went back to the garden.
## Sandra journeyed to the hallway.
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
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        ## John went to the hallway.
        self.John.location = "hallway"
        ## John went back to the bathroom.
        self.John.location = "bathroom"
        ## John grabbed the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Sandra journeyed to the kitchen.
        self.Sandra.location = "kitchen"
        ## Sandra got the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## Sandra dropped the apple there.
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "kitchen"
        ## John dropped the milk.
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "bathroom"
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        ## Sandra journeyed to the hallway.
        self.Sandra.location = "hallway"
        ## Where is the apple?
        print(self.apple.location)

world = World()
world.story()