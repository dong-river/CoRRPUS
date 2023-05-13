## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the kitchen.
## Mary travelled to the hallway.
## John got the football there.
## John went to the hallway.
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
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        ## Mary got the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        self.milk.location = "bathroom"
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## Sandra went back to the kitchen.
        self.Sandra.location = "kitchen"
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        self.milk.location = "hallway"
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        self.football.location = "hallway"
        ## John went to the hallway.
        self.John.location = "hallway"
        ## Where is the football?
        print(self.football.location)


world = World()
world.story()