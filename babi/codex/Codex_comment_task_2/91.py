## Daniel moved to the bathroom.
## Sandra went back to the kitchen.
## John moved to the bathroom.
## Mary picked up the milk there.
## John travelled to the garden.
## Mary dropped the milk there.
## Sandra journeyed to the bedroom.
## John journeyed to the bathroom.
## Daniel went back to the office.
## John moved to the hallway.
## Mary got the milk there.
## Daniel took the apple there.
## John picked up the football there.
## Mary went to the kitchen.
## Mary dropped the milk.
## Daniel travelled to the bedroom.
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
        self.milk = object("milk")
        self.apple = object("apple")
        self.football = object("football")

    def story(self):
        ## Daniel moved to the bathroom.
        self.Daniel.location = "bathroom"
        ## Sandra went back to the kitchen.
        self.Sandra.location = "kitchen"
        ## John moved to the bathroom.
        self.John.location = "bathroom"
        ## Mary picked up the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## John travelled to the garden.
        self.John.location = "garden"
        ## Mary dropped the milk there.
        self.milk.location = "garden"
        self.milk.carrier = None
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        ## John journeyed to the bathroom.
        self.John.location = "bathroom"
        ## Daniel went back to the office.
        self.Daniel.location = "office"
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## Mary got the milk there.
        self.milk.location = "hallway"
        self.milk.carrier = self.Mary
        ## Daniel took the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## John picked up the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Mary went to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary dropped the milk.
        self.milk.location = "kitchen"
        self.milk.carrier = None
        ## Daniel travelled to the bedroom.
        self.Daniel.location = "bedroom"
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()