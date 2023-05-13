## Mary travelled to the bathroom.
## John took the milk there.
## Sandra moved to the hallway.
## Sandra grabbed the football there.
## Daniel went back to the bedroom.
## Daniel travelled to the kitchen.
## Sandra put down the football.
## John moved to the bedroom.
## Mary journeyed to the hallway.
## John dropped the milk.
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

    def story(self):
        ## Mary travelled to the bathroom.
        self.Mary.location = "bathroom"
        ## John took the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Sandra moved to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra grabbed the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Daniel went back to the bedroom.
        self.Daniel.location = "bedroom"
        ## Daniel travelled to the kitchen.
        self.Daniel.location = "kitchen"
        ## Sandra put down the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "hallway"
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## Mary journeyed to the hallway.
        self.Mary.location = "hallway"
        ## John dropped the milk.
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "bedroom"
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()