## John took the football.
## Daniel went back to the garden.
## Mary moved to the bathroom.
## Mary went to the bedroom.
## Mary went to the hallway.
## John dropped the football.
## Daniel journeyed to the hallway.
## Sandra grabbed the football.
## John moved to the office.
## Sandra put down the football.
## Sandra took the football.
## Daniel went to the bedroom.
## Mary moved to the office.
## Mary journeyed to the bedroom.
## Mary grabbed the apple there.
## Sandra went back to the kitchen.
## Sandra picked up the milk there.
## Mary discarded the apple.
## John went back to the bathroom.
## Mary got the apple.
## Mary left the apple.
## Mary took the apple.
## Mary put down the apple.
## Sandra put down the milk.
## Daniel went to the kitchen.
## Sandra journeyed to the office.
## Sandra journeyed to the bedroom.
## John moved to the garden.
## Sandra journeyed to the garden.
## Mary got the apple.
## Mary discarded the apple.
## Mary travelled to the hallway.
## Daniel went to the garden.
## Sandra went back to the hallway.
## Sandra travelled to the garden.
## Sandra went back to the office.
## Daniel went to the bathroom.
## Sandra dropped the football.
## Mary went back to the kitchen.
## Mary went back to the hallway.
## Where was the football before the office? 

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
        self.football = object("football")
        self.apple = object("apple")
        self.milk = object("milk")
        self.Daniel = character("Daniel")

    def story(self):
        ## John took the football.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Daniel went back to the garden.
        self.Daniel.location = "garden"
        ## Mary moved to the bathroom.
        self.Mary.location = "bathroom"
        ## Mary went to the bedroom.
        self.Mary.location = "bedroom"
        ## Mary went to the hallway.
        self.Mary.location = "hallway"
        ## John dropped the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.John.location
        ## Daniel journeyed to the hallway.
        self.Daniel.location = "hallway"
        ## Sandra grabbed the football.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## John moved to the office.
        self.John.location = "office"
        ## Sandra put down the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.Sandra.location
        ## Sandra took the football.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Daniel went to the bedroom.
        self.Daniel.location = "bedroom"
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## Mary grabbed the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Sandra went back to the kitchen.
        self.Sandra.location = "kitchen"
        ## Sandra picked up the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Mary discarded the apple.
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.Mary.location
        ## John went back to the bathroom.
        self.John.location = "bathroom"
        ## Mary got the apple.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Mary left the apple.
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.Mary.location
        ## Mary took the apple.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Mary put down the apple.
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.Mary.location
        ## Sandra put down the milk.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = self.Sandra.location
        ## Daniel went to the kitchen.
        self.Daniel.location = "kitchen"
        ## Sandra journeyed to the office.
        self.Sandra.location = "office"
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        ## John moved to the garden.
        self.John.location = "garden"
        ## Sandra journeyed to the garden.
        self.Sandra.location = "garden"
        ## Mary got the apple.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Mary discarded the apple.
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.Mary.location
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra travelled to the garden.
        self.Sandra.location = "garden"
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Daniel went to the bathroom.
        self.Daniel.location = "bathroom"
        ## Sandra dropped the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.Sandra.location
        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary went back to the hallway.
        self.Mary.location = "hallway"
        ## Where was the football before the office?
        print(self.football.location)

world = World()
world.story()