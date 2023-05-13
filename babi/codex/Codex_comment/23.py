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
## Sandra went back to the hallway.
## Mary journeyed to the bathroom.
## John travelled to the bathroom.
## Sandra journeyed to the office.
## John went to the bedroom.
## Sandra went back to the bedroom.
## John took the apple.
## John went to the office.
## Sandra travelled to the kitchen.
## John put down the apple.
## Daniel travelled to the bedroom.
## John journeyed to the bedroom.
## John went to the garden.
## Daniel went to the hallway.
## Daniel went to the office.
## Sandra grabbed the milk there.
## Mary went to the garden.
## Sandra went back to the office.
## John travelled to the office.
## Sandra journeyed to the kitchen.
## Where was the milk before the kitchen? 

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
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## Mary journeyed to the bathroom.
        self.Mary.location = "bathroom"
        ## John travelled to the bathroom.
        self.John.location = "bathroom"
        ## Sandra journeyed to the office.
        self.Sandra.location = "office"
        ## John went to the bedroom.
        self.John.location = "bedroom"
        ## Sandra went back to the bedroom.
        self.Sandra.location = "bedroom"
        ## John took the apple.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## John went to the office.
        self.John.location = "office"
        ## Sandra travelled to the kitchen.
        self.Sandra.location = "kitchen"
        ## John put down the apple.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.John.location
        ## Daniel travelled to the bedroom.
        self.Daniel.location = "bedroom"
        ## John journeyed to the bedroom.
        self.John.location = "bedroom"
        ## John went to the garden.
        self.John.location = "garden"
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel went to the office.
        self.Daniel.location = "office"
        ## Sandra grabbed the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Mary went to the garden.
        self.Mary.location = "garden"
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## John travelled to the office.
        self.John.location = "office"
        ## Sandra journeyed to the kitchen.
        self.Sandra.location = "kitchen"
        ## Where was the milk before the kitchen? 
        print(self.milk.location)

world = World()
world.story()