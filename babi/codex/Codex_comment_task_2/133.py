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
## Daniel went to the garden.
## Daniel went to the bathroom.
## Mary moved to the bedroom.
## Mary took the apple there.
## Sandra went back to the hallway.
## Sandra discarded the football.
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
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

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
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        ## Daniel went to the bathroom.
        self.Daniel.location = "bathroom"
        ## Mary moved to the bedroom.
        self.Mary.location = "bedroom"
        ## Mary took the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra discarded the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()