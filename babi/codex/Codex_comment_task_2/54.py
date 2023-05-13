## Daniel took the milk there.
## John journeyed to the garden.
## Daniel went back to the hallway.
## Daniel journeyed to the bathroom.
## Daniel dropped the milk.
## Daniel took the milk there.
## John grabbed the apple there.
## Sandra journeyed to the kitchen.
## John went to the hallway.
## Sandra went back to the garden.
## Daniel journeyed to the kitchen.
## Sandra journeyed to the bedroom.
## Daniel went back to the hallway.
## Sandra went back to the kitchen.
## Sandra went back to the bathroom.
## John went to the kitchen.
## Sandra got the football there.
## Sandra went to the kitchen.
## Daniel left the milk.
## Sandra put down the football.
## Sandra picked up the football there.
## Sandra put down the football.
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
        ## Daniel took the milk there.
        self.Daniel.location = "bathroom"
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Daniel went back to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel journeyed to the bathroom.
        self.Daniel.location = "bathroom"
        ## Daniel dropped the milk.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "bathroom"
        ## Daniel took the milk there.
        self.Daniel.location = "bathroom"
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## John grabbed the apple there.
        self.John.location = "garden"
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Sandra journeyed to the kitchen.
        self.Sandra.location = "kitchen"
        ## John went to the hallway.
        self.John.location = "hallway"
        ## Sandra went back to the garden.
        self.Sandra.location = "garden"
        ## Daniel journeyed to the kitchen.
        self.Daniel.location = "kitchen"
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        ## Daniel went back to the hallway.
        self.Daniel.location = "hallway"
        ## Sandra went back to the kitchen.
        self.Sandra.location = "kitchen"
        ## Sandra went back to the bathroom.
        self.Sandra.location = "bathroom"
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Sandra got the football there.
        self.Sandra.location = "kitchen"
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Sandra went to the kitchen.
        self.Sandra.location = "kitchen"
        ## Daniel left the milk.
        self.Daniel.location = "hallway"
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "bathroom"
        ## Sandra put down the football.
        self.Sandra.location = "kitchen"
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "kitchen"
        ## Sandra picked up the football there.
        self.Sandra.location = "kitchen"
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Sandra put down the football.
        self.Sandra.location = "kitchen"
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "kitchen"
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()