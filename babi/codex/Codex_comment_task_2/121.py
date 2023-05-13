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
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        ## Sandra grabbed the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Sandra put down the football.
        self.football.location = self.Sandra.location
        self.football.carrier = None
        ## John grabbed the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Sandra went to the hallway.
        self.Sandra.location = "hallway"
        ## John journeyed to the hallway.
        self.John.location = "hallway"
        ## Mary grabbed the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Sandra moved to the bathroom.
        self.Sandra.location = "bathroom"
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## John picked up the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()