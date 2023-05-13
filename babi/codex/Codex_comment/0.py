## Mary got the milk.
## John moved to the bedroom.
## Daniel journeyed to the office.
## John grabbed the apple there.
## John got the football.
## John journeyed to the garden.
## Mary left the milk.
## John left the football.
## Daniel moved to the garden.
## Daniel grabbed the football.
## Mary moved to the hallway.
## Mary went to the kitchen.
## John put down the apple there.
## John picked up the apple.
## Sandra moved to the hallway.
## Daniel left the football there.
## Daniel took the football.
## John travelled to the kitchen.
## Daniel dropped the football.
## John dropped the apple.
## John grabbed the apple.
## John went to the office.
## Sandra went back to the bedroom.
## Sandra took the milk.
## John journeyed to the bathroom.
## John travelled to the office.
## Sandra left the milk.
## Mary went to the bedroom.
## Mary moved to the office.
## John travelled to the hallway.
## Sandra moved to the garden.
## Mary moved to the kitchen.
## Daniel took the football.
## Mary journeyed to the bedroom.
## Mary grabbed the milk there.
## Mary discarded the milk.
## John went to the garden.
## John discarded the apple there.
## Where was the apple before the bathroom? 

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
        ## Mary got the milk.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## Daniel journeyed to the office.
        self.Daniel.location = "office"
        ## John grabbed the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## John got the football.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John journeyed to the garden.
        self.John.location = "garden"
        self.apple.location = "garden"
        self.football.location = "garden"
        ## Mary left the milk.
        self.milk.carrier = None
        self.milk.location = "garden"
        ## John left the football.
        self.football.carrier = None
        self.football.location = "garden"
        ## Daniel moved to the garden.
        self.Daniel.location = "garden"
        ## Daniel grabbed the football.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Mary moved to the hallway.
        self.Mary.location = "hallway"
        ## Mary went to the kitchen.
        self.Mary.location = "kitchen"
        self.milk.location = "kitchen"
        ## John put down the apple there.
        self.apple.carrier = None
        self.apple.location = "kitchen"
        ## John picked up the apple.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## John went to the office.
        self.John.location = "office"
        self.apple.location = "office"
        ## Sandra moved to the hallway.
        self.Sandra.location = "hallway"
        ## Daniel left the football there.
        self.football.carrier = None
        self.football.location = "office"
        ## Daniel took the football.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## John travelled to the kitchen.
        self.John.location = "kitchen"
        self.apple.location = "kitchen"
        ## Daniel dropped the football.
        self.football.carrier = None
        self.football.location = "kitchen"
        ## John dropped the apple.
        self.apple.carrier = None
        self.apple.location = "kitchen"
        ## John grabbed the apple.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## John went to the office.
        self.John.location = "office"
        self.apple.location = "office"
        ## Sandra went back to the bedroom.
        self.Sandra.location = "bedroom"
        ## Sandra took the milk.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## John journeyed to the bathroom.
        self.John.location = "bathroom"
        self.apple.location = "bathroom"
        ## John travelled to the office.
        self.John.location = "office"
        self.apple.location = "office"
        ## Sandra left the milk.
        self.milk.carrier = None
        self.milk.location = "office"
        ## Mary went to the bedroom.
        self.Mary.location = "bedroom"
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## John travelled to the hallway.
        self.John.location = "hallway"
        self.apple.location = "hallway"
        ## Sandra moved to the garden.
        self.Sandra.location = "garden"
        ## Mary moved to the kitchen.
        self.Mary.location = "kitchen"
        ## Daniel took the football.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## Mary grabbed the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Mary discarded the milk.
        self.milk.carrier = None
        self.milk.location = "bedroom"
        ## John went to the garden.
        self.John.location = "garden"
        self.apple.location = "garden"
        ## John discarded the apple there.
        self.apple.carrier = None
        self.apple.location = "garden"
        ## Where was the apple before the bathroom?
        print(self.apple.location)

world = World()
world.story()