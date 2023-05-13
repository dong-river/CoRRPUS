## Sandra got the milk there.
## John grabbed the apple there.
## John journeyed to the bathroom.
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
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        ## Sandra got the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## John grabbed the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## John journeyed to the bathroom.
        self.John.location = "bathroom"
        ## John discarded the apple.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Where is the apple?
        print(self.apple.location)

world = World()
world.story()