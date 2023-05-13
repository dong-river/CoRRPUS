## Daniel travelled to the garden.
## Sandra went back to the bedroom.
## John travelled to the bedroom.
## Sandra grabbed the apple there.
## Daniel travelled to the kitchen.
## Sandra left the apple.
## Sandra travelled to the office.
## Sandra went back to the bathroom.
## John travelled to the bathroom.
## Daniel went back to the hallway.
## Sandra travelled to the bedroom.
## Sandra journeyed to the hallway.
## Sandra went back to the kitchen.
## Mary travelled to the office.
## Sandra journeyed to the hallway.
## Mary went back to the hallway.
## Mary travelled to the garden.
## Mary took the football there.
## Mary went to the kitchen.
## Mary grabbed the milk there.
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
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        ## Daniel travelled to the garden.
        self.Daniel.location = "garden"
        ## Sandra went back to the bedroom.
        self.Sandra.location = "bedroom"
        ## John travelled to the bedroom.
        self.John.location = "bedroom"
        ## Sandra grabbed the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## Daniel travelled to the kitchen.
        self.Daniel.location = "kitchen"
        ## Sandra left the apple.
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "kitchen"
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## Sandra went back to the bathroom.
        self.Sandra.location = "bathroom"
        ## John travelled to the bathroom.
        self.John.location = "bathroom"
        ## Daniel went back to the hallway.
        self.Daniel.location = "hallway"
        ## Sandra travelled to the bedroom.
        self.Sandra.location = "bedroom"
        ## Sandra journeyed to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra went back to the kitchen.
        self.Sandra.location = "kitchen"
        ## Mary travelled to the office.
        self.Mary.location = "office"
        ## Sandra journeyed to the hallway.
        self.Sandra.location = "hallway"
        ## Mary went back to the hallway.
        self.Mary.location = "hallway"
        ## Mary travelled to the garden.
        self.Mary.location = "garden"
        ## Mary took the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## Mary went to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary grabbed the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()