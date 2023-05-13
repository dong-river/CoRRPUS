## Mary went to the garden.
## John picked up the milk there.
## Mary journeyed to the bedroom.
## Sandra went back to the hallway.
## John discarded the milk.
## John journeyed to the bedroom.
## John got the football there.
## John moved to the bathroom.
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
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        ## Mary went to the garden.
        self.Mary.location = "garden"
        ## John picked up the milk there.
        self.John.inventory.append(self.milk)
        self.milk.location = "John's inventory"
        self.milk.carrier = self.John
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## John discarded the milk.
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "bedroom"
        ## John journeyed to the bedroom.
        self.John.location = "bedroom"
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John moved to the bathroom.
        self.John.location = "bathroom"
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()