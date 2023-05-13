## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the kitchen.
## Mary travelled to the hallway.
## John got the football there.
## John went to the hallway.
## John put down the football.
## Mary went to the garden.
## John went to the kitchen.
## Sandra travelled to the hallway.
## Daniel went to the hallway.
## Mary discarded the milk.
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
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        ## Mary got the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## Sandra went back to the kitchen.
        self.Sandra.location = "kitchen"
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        self.milk.location = "hallway"
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John went to the hallway.
        self.John.location = "hallway"
        self.football.location = "hallway"
        ## John put down the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Mary went to the garden.
        self.Mary.location = "garden"
        self.milk.location = "garden"
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Sandra travelled to the hallway.
        self.Sandra.location = "hallway"
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## Mary discarded the milk.
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()