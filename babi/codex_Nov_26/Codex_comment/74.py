## Sandra moved to the garden.
## Daniel took the apple there.
## Daniel dropped the apple.
## Sandra travelled to the office.
## John moved to the kitchen.
## Sandra moved to the garden.
## Daniel went back to the bathroom.
## Mary travelled to the hallway.
## Sandra went to the bathroom.
## John went back to the bedroom.
## Mary moved to the garden.
## John picked up the apple there.
## John went back to the kitchen.
## John went back to the garden.
## Mary went to the office.
## Daniel went to the bedroom.
## John went to the bathroom.
## John dropped the apple.
## Mary journeyed to the bedroom.
## Sandra grabbed the apple there.
## Daniel moved to the kitchen.
## Sandra left the apple.
## John grabbed the apple there.
## Sandra journeyed to the kitchen.
## Sandra journeyed to the bathroom.
## Daniel travelled to the office.
## John put down the apple.
## Mary journeyed to the kitchen.
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
        self.apple = object("apple")

    def story(self):
        ## Sandra moved to the garden.
        self.Sandra.location = "garden"
        ## Daniel took the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Daniel dropped the apple.
        self.apple.carrier = None
        self.apple.location = self.Daniel.location
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## John moved to the kitchen.
        self.John.location = "kitchen"
        ## Sandra moved to the garden.
        self.Sandra.location = "garden"
        ## Daniel went back to the bathroom.
        self.Daniel.location = "bathroom"
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        ## Sandra went to the bathroom.
        self.Sandra.location = "bathroom"
        ## John went back to the bedroom.
        self.John.location = "bedroom"
        ## Mary moved to the garden.
        self.Mary.location = "garden"
        ## John picked up the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## John went back to the kitchen.
        self.John.location = "kitchen"
        ## John went back to the garden.
        self.John.location = "garden"
        ## Mary went to the office.
        self.Mary.location = "office"
        ## Daniel went to the bedroom.
        self.Daniel.location = "bedroom"
        ## John went to the bathroom.
        self.John.location = "bathroom"
        ## John dropped the apple.
        self.apple.carrier = None
        self.apple.location = self.John.location
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## Sandra grabbed the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## Daniel moved to the kitchen.
        self.Daniel.location = "kitchen"
        ## Sandra left the apple.
        self.apple.carrier = None
        self.apple.location = self.Sandra.location
        ## John grabbed the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Sandra journeyed to the kitchen.
        self.Sandra.location = "kitchen"
        ## Sandra journeyed to the bathroom.
        self.Sandra.location = "bathroom"
        ## Daniel travelled to the office.
        self.Daniel.location = "office"
        ## John put down the apple.
        self.apple.carrier = None
        self.apple.location = self.John.location
        ## Mary journeyed to the kitchen.
        self.Mary.location = "kitchen"
        ## 
        ## Where is the apple? 
        print(self.apple.location)

world = World()
world.story()