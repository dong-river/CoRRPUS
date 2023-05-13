## Sandra grabbed the football there.
## Sandra put down the football.
## John grabbed the apple there.
## Sandra went to the hallway.
## John journeyed to the hallway.
## Mary grabbed the milk there.
## John journeyed to the garden.
## Sandra moved to the bathroom.
## Mary journeyed to the bedroom.
## John picked up the football there.
## John dropped the football.
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
        self.apple = object("apple")

    def story(self):
        ## Sandra grabbed the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Sandra put down the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        ## John grabbed the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Sandra went to the hallway.
        self.Sandra.location = "hallway"
        ## John journeyed to the hallway.
        self.John.location = "hallway"
        ## Mary grabbed the milk there.
        self.Mary.location = "milk"
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Sandra moved to the bathroom.
        self.Sandra.location = "bathroom"
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## John picked up the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John dropped the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## John discarded the apple.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()