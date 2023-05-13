## Daniel moved to the kitchen.
## John grabbed the football there.
## John left the football there.
## Mary journeyed to the hallway.
## John grabbed the milk there.
## John travelled to the kitchen.
## Mary journeyed to the kitchen.
## Sandra went to the office.
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

    def story(self):
        ## Daniel moved to the kitchen.
        self.Daniel.location = "kitchen"
        ## John grabbed the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John left the football there.
        self.football.location = "kitchen"
        ## Mary journeyed to the hallway.
        self.Mary.location = "hallway"
        ## John grabbed the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## John travelled to the kitchen.
        self.John.location = "kitchen"
        ## Mary journeyed to the kitchen.
        self.Mary.location = "kitchen"
        ## Sandra went to the office.
        self.Sandra.location = "office"
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()