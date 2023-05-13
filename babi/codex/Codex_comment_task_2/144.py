## Daniel journeyed to the hallway.
## Daniel picked up the football there.
## Daniel journeyed to the bedroom.
## Daniel dropped the football.
## Sandra travelled to the bedroom.
## Daniel journeyed to the kitchen.
## Sandra grabbed the football there.
## John travelled to the office.
## Sandra discarded the football.
## Mary went back to the hallway.
## Daniel went to the hallway.
## Daniel travelled to the bedroom.
## Mary travelled to the office.
## John journeyed to the kitchen.
## Sandra went back to the office.
## Daniel took the football there.
## Daniel went to the garden.
## Mary travelled to the bedroom.
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

    def story(self):
        ## Daniel journeyed to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel picked up the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Daniel journeyed to the bedroom.
        self.Daniel.location = "bedroom"
        ## Daniel dropped the football.
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        ## Sandra travelled to the bedroom.
        self.Sandra.location = "bedroom"
        ## Daniel journeyed to the kitchen.
        self.Daniel.location = "kitchen"
        ## Sandra grabbed the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## John travelled to the office.
        self.John.location = "office"
        ## Sandra discarded the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        ## Mary went back to the hallway.
        self.Mary.location = "hallway"
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel travelled to the bedroom.
        self.Daniel.location = "bedroom"
        ## Mary travelled to the office.
        self.Mary.location = "office"
        ## John journeyed to the kitchen.
        self.John.location = "kitchen"
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Daniel took the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()