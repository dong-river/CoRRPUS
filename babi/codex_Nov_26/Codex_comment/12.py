## Mary picked up the apple there.
## Mary dropped the apple.
## Daniel went back to the garden.
## Mary journeyed to the office.
## John got the football there.
## Mary went back to the kitchen.
## Daniel picked up the milk there.
## John travelled to the bedroom.
## John moved to the hallway.
## John discarded the football.
## Daniel dropped the milk.
## John got the football there.
## 
## Where is the milk? 

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
        self.Daniel = character("Daniel")
        self.apple = object("apple")
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        ## Mary picked up the apple there.
        self.Mary.location = "garden"
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Mary dropped the apple.
        self.apple.carrier = None
        self.apple.location = "garden"
        self.Mary.inventory.remove(self.apple)
        ## Daniel went back to the garden.
        self.Daniel.location = "garden"
        ## Mary journeyed to the office.
        self.Mary.location = "office"
        ## John got the football there.
        self.John.location = "kitchen"
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        ## Daniel picked up the milk there.
        self.Daniel.location = "kitchen"
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## John travelled to the bedroom.
        self.John.location = "bedroom"
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## John discarded the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "hallway"
        ## Daniel dropped the milk.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "kitchen"
        ## John got the football there.
        self.John.location = "hallway"
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Where is the milk?
        print(self.milk.location)
        ## Where is the football?
        print(self.football.location)
        ## Where is the apple?
        print(self.apple.location)

world = World()
world.story()