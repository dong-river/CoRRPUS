## Mary moved to the kitchen.
## Mary travelled to the office.
## Daniel grabbed the football there.
## Mary moved to the hallway.
## Sandra moved to the bedroom.
## Mary went back to the bedroom.
## John grabbed the milk there.
## John put down the milk.
## Daniel journeyed to the bathroom.
## Sandra journeyed to the bathroom.
## John got the milk there.
## Mary took the apple there.
## Mary left the apple.
## John journeyed to the bedroom.
## Mary travelled to the office.
## Daniel put down the football.
## John went back to the kitchen.
## Sandra got the football there.
## John travelled to the hallway.
## Sandra discarded the football there.
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
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        ## Mary moved to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary travelled to the office.
        self.Mary.location = "office"
        ## Daniel grabbed the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Mary moved to the hallway.
        self.Mary.location = "hallway"
        ## Sandra moved to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary went back to the bedroom.
        self.Mary.location = "bedroom"
        ## John grabbed the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## John put down the milk.
        self.milk.location = "bedroom"
        self.milk.carrier = None
        ## Daniel journeyed to the bathroom.
        self.Daniel.location = "bathroom"
        ## Sandra journeyed to the bathroom.
        self.Sandra.location = "bathroom"
        ## John got the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Mary took the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Mary left the apple.
        self.apple.location = "office"
        self.apple.carrier = None
        ## John journeyed to the bedroom.
        self.John.location = "bedroom"
        ## Mary travelled to the office.
        self.Mary.location = "office"
        ## Daniel put down the football.
        self.football.location = "office"
        self.football.carrier = None
        ## John went back to the kitchen.
        self.John.location = "kitchen"
        ## Sandra got the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## John travelled to the hallway.
        self.John.location = "hallway"
        ## Sandra discarded the football there.
        self.football.location = "hallway"
        self.football.carrier = None
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()