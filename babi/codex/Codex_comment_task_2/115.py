## John grabbed the football there.
## John journeyed to the office.
## Where is the football? 

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

    def story(self):
        ## Mary moved to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary got the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        self.football.location = "garden"
        ## Where is the football?
        print(self.football.location)
        ## John grabbed the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John journeyed to the office.
        self.John.location = "office"
        self.football.location = "office"
        ## Where is the football? 
        print(self.football.location)

world = World()
world.story()