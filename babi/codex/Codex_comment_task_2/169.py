## John went back to the garden.
## Daniel went to the bathroom.
## Daniel went to the hallway.
## Daniel grabbed the football there.
## Daniel travelled to the bathroom.
## Daniel went to the garden.
## John went back to the kitchen.
## Daniel discarded the football.
## Sandra picked up the football there.
## Mary went back to the office.
## John picked up the apple there.
## John journeyed to the hallway.
## Mary travelled to the bedroom.
## Daniel went back to the bathroom.
## Sandra went back to the office.
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
        self.apple = object("apple")

    def story(self):
        ## John went back to the garden.
        self.John.location = "garden"
        ## Daniel went to the bathroom.
        self.Daniel.location = "bathroom"
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel grabbed the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Daniel travelled to the bathroom.
        self.Daniel.location = "bathroom"
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        self.football.location = "garden"
        ## John went back to the kitchen.
        self.John.location = "kitchen"
        ## Daniel discarded the football.
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "garden"
        ## Sandra picked up the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Mary went back to the office.
        self.Mary.location = "office"
        ## John picked up the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## John journeyed to the hallway.
        self.John.location = "hallway"
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## Daniel went back to the bathroom.
        self.Daniel.location = "bathroom"
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Sandra discarded the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "office"
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()