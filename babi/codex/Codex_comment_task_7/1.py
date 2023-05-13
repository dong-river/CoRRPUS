## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the bathroom.
## John got the football there.
## How many objects is Mary carrying? 

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
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        ## Mary moved to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary got the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        self.football.location = "garden"
        ## Where is the football?
        print(self.football.location)
        ## Mary got the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## Sandra went back to the bathroom.
        self.Sandra.location = "bathroom"
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## How many objects is Mary carrying? 
        print(len(self.Mary.inventory))

world = World()
world.story()