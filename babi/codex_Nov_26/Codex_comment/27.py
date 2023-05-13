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
## 
## Where is the apple? 

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
        self.garden = object("garden")
        self.kitchen = object("kitchen")
        self.bathroom = object("bathroom")
        self.office = object("office")
        self.hallway = object("hallway")

    def story(self):
        ## Daniel moved to the kitchen.
        self.Daniel.location = self.kitchen
        ## John grabbed the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John left the football there.
        self.football.location = self.kitchen
        ## Mary journeyed to the hallway.
        self.Mary.location = self.hallway
        ## John grabbed the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## John travelled to the kitchen.
        self.John.location = self.kitchen
        ## Mary journeyed to the kitchen.
        self.Mary.location = self.kitchen
        ## Sandra went to the office.
        self.Sandra.location = self.office
        ## Daniel went to the bathroom.
        self.Daniel.location = self.bathroom
        ## Daniel picked up the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Sandra travelled to the garden.
        self.Sandra.location = self.garden
        ## Daniel dropped the apple there.
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.garden
        ##
        ## Where is the apple?
        print(self.apple.location)

world = World()
world.story()