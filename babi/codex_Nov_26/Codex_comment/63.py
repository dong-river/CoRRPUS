## Daniel moved to the office.
## Daniel travelled to the bedroom.
## John took the milk there.
## John travelled to the garden.
## Sandra moved to the office.
## Daniel went back to the office.
## John went to the kitchen.
## Mary travelled to the garden.
## John picked up the football there.
## John dropped the football.
## John put down the milk.
## Daniel moved to the kitchen.
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
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        ## Daniel moved to the office.
        self.Daniel.location = "office"
        ## Daniel travelled to the bedroom.
        self.Daniel.location = "bedroom"
        ## John took the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        self.milk.location = "bedroom"
        ## John travelled to the garden.
        self.John.location = "garden"
        self.milk.location = "garden"
        ## Sandra moved to the office.
        self.Sandra.location = "office"
        ## Daniel went back to the office.
        self.Daniel.location = "office"
        ## John went to the kitchen.
        self.John.location = "kitchen"
        self.milk.location = "kitchen"
        ## Mary travelled to the garden.
        self.Mary.location = "garden"
        ## John picked up the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John dropped the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "garden"
        ## John put down the milk.
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "kitchen"
        ## Daniel moved to the kitchen.
        self.Daniel.location = "kitchen"
        ## 
        ## Where is the football? 
        print(self.football.location)

world = World()
world.story()