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
## Mary journeyed to the garden.
## Daniel travelled to the bathroom.
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
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.apple = object("apple")
        self.milk = object("milk")

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
        ## Mary picked up the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Mary dropped the apple.
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Daniel went back to the garden.
        self.Daniel.location = "garden"
        ## Mary journeyed to the office.
        self.Mary.location = "office"
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        ## Daniel picked up the milk there.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## John travelled to the bedroom.
        self.John.location = "bedroom"
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## John discarded the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Daniel dropped the milk.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Mary journeyed to the garden.
        self.Mary.location = "garden"
        ## Daniel travelled to the bathroom.
        self.Daniel.location = "bathroom"
        ## 
        ## Where is the milk? 
        print(self.milk.location)

world = World()
world.story()