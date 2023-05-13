## Daniel moved to the bedroom.
## Daniel went to the bathroom.
## John moved to the garden.
## Mary travelled to the bedroom.
## Sandra travelled to the garden.
## Daniel journeyed to the garden.
## Sandra travelled to the hallway.
## John got the football there.
## John moved to the bathroom.
## Sandra travelled to the bathroom.
## Daniel moved to the bedroom.
## Daniel travelled to the kitchen.
## Mary moved to the hallway.
## Sandra travelled to the office.
## Daniel moved to the hallway.
## Daniel went back to the kitchen.
## John went back to the hallway.
## Daniel went back to the hallway.
## Daniel went to the bedroom.
## John moved to the kitchen.
## Mary moved to the office.
## John went back to the garden.
## Sandra took the apple there.
## Daniel went to the office.
## Mary went back to the kitchen.
## Mary went to the bedroom.
## John journeyed to the bathroom.
## Sandra went back to the hallway.
## Sandra moved to the bedroom.
## Daniel moved to the garden.
## John went back to the bedroom.
## Mary went back to the office.
## John moved to the kitchen.
## John grabbed the milk there.
## Daniel journeyed to the bedroom.
## John discarded the football.
## John left the milk.
## John took the milk there.
## John picked up the football there.
## John put down the football.
## 
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
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## Daniel went to the bathroom.
        self.Daniel.location = "bathroom"
        ## John moved to the garden.
        self.John.location = "garden"
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## Sandra travelled to the garden.
        self.Sandra.location = "garden"
        ## Daniel journeyed to the garden.
        self.Daniel.location = "garden"
        ## Sandra travelled to the hallway.
        self.Sandra.location = "hallway"
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John moved to the bathroom.
        self.John.location = "bathroom"
        ## Sandra travelled to the bathroom.
        self.Sandra.location = "bathroom"
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## Daniel travelled to the kitchen.
        self.Daniel.location = "kitchen"
        ## Mary moved to the hallway.
        self.Mary.location = "hallway"
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## Daniel moved to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel went back to the kitchen.
        self.Daniel.location = "kitchen"
        ## John went back to the hallway.
        self.John.location = "hallway"
        ## Daniel went back to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel went to the bedroom.
        self.Daniel.location = "bedroom"
        ## John moved to the kitchen.
        self.John.location = "kitchen"
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## John went back to the garden.
        self.John.location = "garden"
        ## Sandra took the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## Daniel went to the office.
        self.Daniel.location = "office"
        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary went to the bedroom.
        self.Mary.location = "bedroom"
        ## John journeyed to the bathroom.
        self.John.location = "bathroom"
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra moved to the bedroom.
        self.Sandra.location = "bedroom"
        ## Daniel moved to the garden.
        self.Daniel.location = "garden"
        ## John went back to the bedroom.
        self.John.location = "bedroom"
        ## Mary went back to the office.
        self.Mary.location = "office"
        ## John moved to the kitchen.
        self.John.location = "kitchen"
        ## John grabbed the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Daniel journeyed to the bedroom.
        self.Daniel.location = "bedroom"
        ## John discarded the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.John.location
        ## John left the milk.
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = self.John.location
        ## John took the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## John picked up the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John put down the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.John.location
        ## 
        ## Where is the football? 
        print(self.football.location)

world = World()
world.story()