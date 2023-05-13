## Mary went back to the kitchen.
## Mary travelled to the hallway.
## John journeyed to the bedroom.
## John moved to the garden.
## Daniel went to the hallway.
## John moved to the hallway.
## Daniel journeyed to the bathroom.
## Mary travelled to the garden.
## Daniel went to the hallway.
## John travelled to the office.
## John travelled to the bedroom.
## Mary journeyed to the bedroom.
## John picked up the football there.
## John dropped the football.
## Sandra travelled to the office.
## Mary travelled to the hallway.
## Sandra grabbed the apple there.
## John grabbed the football there.
## Mary went back to the bathroom.
## John discarded the football.
## John picked up the football there.
## Daniel went to the office.
## Sandra discarded the apple.
## Sandra grabbed the apple there.
## John put down the football.
## Daniel moved to the garden.
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
        self.apple = object("apple")

    def story(self):
        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        ## John journeyed to the bedroom.
        self.John.location = "bedroom"
        ## John moved to the garden.
        self.John.location = "garden"
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## Daniel journeyed to the bathroom.
        self.Daniel.location = "bathroom"
        ## Mary travelled to the garden.
        self.Mary.location = "garden"
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## John travelled to the office.
        self.John.location = "office"
        ## John travelled to the bedroom.
        self.John.location = "bedroom"
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## John picked up the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John dropped the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.John.location
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        ## Sandra grabbed the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## John grabbed the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Mary went back to the bathroom.
        self.Mary.location = "bathroom"
        ## John discarded the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.John.location
        ## John picked up the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Daniel went to the office.
        self.Daniel.location = "office"
        ## Sandra discarded the apple.
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.Sandra.location
        ## Sandra grabbed the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## John put down the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.John.location
        ## Daniel moved to the garden.
        self.Daniel.location = "garden"
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()