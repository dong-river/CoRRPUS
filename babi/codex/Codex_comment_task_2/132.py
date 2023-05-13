## Daniel travelled to the hallway.
## Mary moved to the kitchen.
## John grabbed the football there.
## John discarded the football.
## Sandra journeyed to the kitchen.
## Sandra picked up the milk there.
## Daniel moved to the office.
## John took the football there.
## John went to the kitchen.
## Mary moved to the office.
## Sandra put down the milk.
## John left the football.
## John moved to the hallway.
## Sandra picked up the football there.
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
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        ## Daniel travelled to the hallway.
        self.Daniel.location = "hallway"
        ## Mary moved to the kitchen.
        self.Mary.location = "kitchen"
        ## John grabbed the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John discarded the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Sandra journeyed to the kitchen.
        self.Sandra.location = "kitchen"
        ## Sandra picked up the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Daniel moved to the office.
        self.Daniel.location = "office"
        ## John took the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## Sandra put down the milk.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        ## John left the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## Sandra picked up the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()