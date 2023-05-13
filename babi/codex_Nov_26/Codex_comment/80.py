## Daniel moved to the bedroom.
## Daniel went to the bathroom.
## John moved to the garden.
## Mary travelled to the bedroom.
## Sandra travelled to the garden.
## Daniel journeyed to the garden.
## Sandra travelled to the hallway.
## John got the football there.
## John moved to the bathroom.
## Sandra travelled to the bathroom.
## 
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
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## Daniel went to the bathroom.
        self.Daniel.location = "bathroom"
        ## John moved to the garden.
        self.John.location = "garden"
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## Sandra travelled to the garden.
        self.Sandra.location = "garden"
        ## Daniel journeyed to the garden.
        self.Daniel.location = "garden"
        ## Sandra travelled to the hallway.
        self.Sandra.location = "hallway"
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John moved to the bathroom.
        self.John.location = "bathroom"
        ## Sandra travelled to the bathroom.
        self.Sandra.location = "bathroom"
        ## 
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()