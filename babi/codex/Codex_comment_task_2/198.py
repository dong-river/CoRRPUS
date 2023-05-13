## Sandra got the milk there.
## John grabbed the apple there.
## John journeyed to the bathroom.
## John discarded the apple.
## John journeyed to the garden.
## Sandra travelled to the bedroom.
## Sandra went back to the garden.
## Sandra left the milk there.
## John grabbed the milk there.
## John went back to the kitchen.
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
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        ## Sandra got the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        self.Sandra.location = "bedroom"
        ## John grabbed the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        self.John.location = "bedroom"
        ## John journeyed to the bathroom.
        self.John.location = "bathroom"
        ## John discarded the apple.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "bathroom"
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Sandra travelled to the bedroom.
        self.Sandra.location = "bedroom"
        ## Sandra went back to the garden.
        self.Sandra.location = "garden"
        ## Sandra left the milk there.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "garden"
        ## John grabbed the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## John went back to the kitchen.
        self.John.location = "kitchen"
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()