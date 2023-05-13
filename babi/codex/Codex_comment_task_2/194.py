## Mary travelled to the bedroom.
## Daniel grabbed the apple there.
## Daniel went to the garden.
## John travelled to the office.
## Daniel left the apple.
## John travelled to the hallway.
## Sandra went to the office.
## Daniel journeyed to the hallway.
## Daniel went to the kitchen.
## John journeyed to the kitchen.
## Mary moved to the office.
## Mary went back to the garden.
## Mary moved to the office.
## John went back to the bathroom.
## John travelled to the office.
## Daniel went back to the garden.
## John travelled to the kitchen.
## Mary went to the bedroom.
## Daniel moved to the bathroom.
## Daniel picked up the football there.
## Sandra travelled to the hallway.
## Daniel picked up the milk there.
## Daniel dropped the milk.
## Daniel took the milk there.
## Daniel moved to the bedroom.
## Sandra went to the garden.
## Sandra travelled to the kitchen.
## Sandra travelled to the office.
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
        self.apple = object("apple")
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## Daniel grabbed the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        self.apple.location = "garden"
        ## John travelled to the office.
        self.John.location = "office"
        ## Daniel left the apple.
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        ## John travelled to the hallway.
        self.John.location = "hallway"
        ## Sandra went to the office.
        self.Sandra.location = "office"
        ## Daniel journeyed to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel went to the kitchen.
        self.Daniel.location = "kitchen"
        ## John journeyed to the kitchen.
        self.John.location = "kitchen"
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## John went back to the bathroom.
        self.John.location = "bathroom"
        ## John travelled to the office.
        self.John.location = "office"
        ## Daniel went back to the garden.
        self.Daniel.location = "garden"
        ## John travelled to the kitchen.
        self.John.location = "kitchen"
        ## Mary went to the bedroom.
        self.Mary.location = "bedroom"
        ## Daniel moved to the bathroom.
        self.Daniel.location = "bathroom"
        ## Daniel picked up the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Sandra travelled to the hallway.
        self.Sandra.location = "hallway"
        ## Daniel picked up the milk there.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## Daniel dropped the milk.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Daniel took the milk there.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## Sandra went to the garden.
        self.Sandra.location = "garden"
        ## Sandra travelled to the kitchen.
        self.Sandra.location = "kitchen"
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()