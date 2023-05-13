## Daniel moved to the hallway.
## Mary went back to the kitchen.
## John got the milk there.
## John put down the milk.
## John got the milk there.
## Mary went back to the garden.
## John went back to the bedroom.
## Mary picked up the football there.
## John went to the office.
## John left the milk.
## Mary went to the bedroom.
## John went to the bedroom.
## John went to the bathroom.
## Mary moved to the bathroom.
## Mary went to the kitchen.
## Mary travelled to the office.
## Sandra moved to the kitchen.
## Daniel picked up the apple there.
## Sandra travelled to the garden.
## Mary travelled to the bedroom.
## Daniel went to the kitchen.
## Mary put down the football.
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
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        ## Daniel moved to the hallway.
        self.Daniel.location = "hallway"
        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        ## John got the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## John put down the milk.
        self.milk.location = "kitchen"
        self.milk.carrier = None
        ## John got the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        ## John went back to the bedroom.
        self.John.location = "bedroom"
        ## Mary picked up the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## John went to the office.
        self.John.location = "office"
        ## John left the milk.
        self.milk.location = "office"
        self.milk.carrier = None
        ## Mary went to the bedroom.
        self.Mary.location = "bedroom"
        ## John went to the bedroom.
        self.John.location = "bedroom"
        ## John went to the bathroom.
        self.John.location = "bathroom"
        ## Mary moved to the bathroom.
        self.Mary.location = "bathroom"
        ## Mary went to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary travelled to the office.
        self.Mary.location = "office"
        ## Sandra moved to the kitchen.
        self.Sandra.location = "kitchen"
        ## Daniel picked up the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## Sandra travelled to the garden.
        self.Sandra.location = "garden"
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## Daniel went to the kitchen.
        self.Daniel.location = "kitchen"
        ## Mary put down the football.
        self.football.location = "bedroom"
        self.football.carrier = None
        ## 
        ## Where is the apple? 
        print(self.apple.location)

world = World()
world.story()