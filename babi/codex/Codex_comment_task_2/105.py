## Sandra took the football there.
## Mary travelled to the kitchen.
## John went to the office.
## Daniel travelled to the bedroom.
## Daniel journeyed to the bathroom.
## Mary went back to the bedroom.
## Sandra travelled to the kitchen.
## Mary went to the bathroom.
## Sandra went back to the bathroom.
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

    def story(self):
        ## Sandra took the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        self.Sandra.location = "bedroom"
        ## Mary travelled to the kitchen.
        self.Mary.location = "kitchen"
        ## John went to the office.
        self.John.location = "office"
        ## Daniel travelled to the bedroom.
        self.Daniel.location = "bedroom"
        ## Daniel journeyed to the bathroom.
        self.Daniel.location = "bathroom"
        ## Mary went back to the bedroom.
        self.Mary.location = "bedroom"
        ## Sandra travelled to the kitchen.
        self.Sandra.location = "kitchen"
        ## Mary went to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra went back to the bathroom.
        self.Sandra.location = "bathroom"
        ## Sandra discarded the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        ## Where is the football?
        print(self.football.location)
 

world = World()
world.story()