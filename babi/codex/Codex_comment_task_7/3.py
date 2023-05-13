## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the bathroom.
## John got the football there.
## Mary journeyed to the bathroom.
## Mary gave the milk to Sandra.
## John went back to the bathroom.
## John left the football.
## How many objects is John carrying? 

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
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## Sandra went back to the bathroom.
        self.Sandra.location = "bathroom"
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Mary journeyed to the bathroom.
        self.Mary.location = "bathroom"
        ## Mary gave the milk to Sandra.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        self.Mary.inventory.remove(self.milk)
        ## John went back to the bathroom.
        self.John.location = "bathroom"
        ## John left the football.
        self.football.carrier = None
        self.John.inventory.remove(self.football)
        ## How many objects is John carrying?
        print(len(self.John.inventory))

world = World()
world.story()