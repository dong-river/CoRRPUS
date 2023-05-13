## Daniel moved to the kitchen.
## John grabbed the football there.
## John left the football there.
## Mary journeyed to the hallway.
## John grabbed the milk there.
## John travelled to the kitchen.
## Mary journeyed to the kitchen.
## Sandra went to the office.
## Daniel went to the bathroom.
## Daniel picked up the apple there.
## Sandra travelled to the garden.
## Daniel dropped the apple there.
## Sandra went back to the office.
## Daniel journeyed to the kitchen.
## John put down the milk.
## Daniel moved to the bedroom.
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
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        ## Daniel moved to the kitchen.
        self.Daniel.location = "kitchen"
        ## John grabbed the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John left the football there.
        self.football.location = self.John.location
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Mary journeyed to the hallway.
        self.Mary.location = "hallway"
        ## John grabbed the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## John travelled to the kitchen.
        self.John.location = "kitchen"
        self.milk.location = "kitchen"
        ## Mary journeyed to the kitchen.
        self.Mary.location = "kitchen"
        ## Sandra went to the office.
        self.Sandra.location = "office"
        ## Daniel went to the bathroom.
        self.Daniel.location = "bathroom"
        ## Daniel picked up the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Sandra travelled to the garden.
        self.Sandra.location = "garden"
        ## Daniel dropped the apple there.
        self.apple.location = self.Sandra.location
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Daniel journeyed to the kitchen.
        self.Daniel.location = "kitchen"
        ## John put down the milk.
        self.milk.location = self.John.location
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## 
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()