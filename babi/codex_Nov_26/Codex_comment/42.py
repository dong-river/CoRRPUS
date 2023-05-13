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
## 
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
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.milk = object("milk")

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
        ## 
        ## Where is the milk? 
        print(self.milk.location)

world = World()
world.story()