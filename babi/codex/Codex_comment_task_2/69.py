## Daniel journeyed to the hallway.
## Daniel journeyed to the garden.
## Mary went back to the kitchen.
## Daniel went back to the office.
## Mary journeyed to the bathroom.
## John moved to the hallway.
## Daniel grabbed the football there.
## Daniel went to the kitchen.
## Daniel discarded the football.
## John went to the bathroom.
## Daniel took the football there.
## John travelled to the kitchen.
## Mary travelled to the office.
## John travelled to the hallway.
## John went back to the office.
## Daniel journeyed to the bedroom.
## Daniel got the milk there.
## Daniel discarded the milk.
## Sandra went to the bathroom.
## Mary went back to the bedroom.
## Daniel took the apple there.
## Daniel dropped the football.
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
        ## Daniel journeyed to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel journeyed to the garden.
        self.Daniel.location = "garden"
        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        ## Daniel went back to the office.
        self.Daniel.location = "office"
        ## Mary journeyed to the bathroom.
        self.Mary.location = "bathroom"
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## Daniel grabbed the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Daniel went to the kitchen.
        self.Daniel.location = "kitchen"
        ## Daniel discarded the football.
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        ## John went to the bathroom.
        self.John.location = "bathroom"
        ## Daniel took the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## John travelled to the kitchen.
        self.John.location = "kitchen"
        ## Mary travelled to the office.
        self.Mary.location = "office"
        ## John travelled to the hallway.
        self.John.location = "hallway"
        ## John went back to the office.
        self.John.location = "office"
        ## Daniel journeyed to the bedroom.
        self.Daniel.location = "bedroom"
        ## Daniel got the milk there.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## Daniel discarded the milk.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Sandra went to the bathroom.
        self.Sandra.location = "bathroom"
        ## Mary went back to the bedroom.
        self.Mary.location = "bedroom"
        ## Daniel took the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Daniel dropped the football.
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()