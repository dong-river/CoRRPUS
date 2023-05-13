## Mary journeyed to the bathroom.
## Sandra went to the garden.
## Daniel went back to the garden.
## Daniel went to the office.
## Sandra grabbed the milk there.
## Sandra put down the milk there.
## Daniel went to the hallway.
## Sandra got the milk there.
## Daniel went to the garden.
## Daniel journeyed to the kitchen.
## Daniel journeyed to the bedroom.
## Mary journeyed to the garden.
## Daniel took the football there.
## Mary moved to the office.
## Sandra travelled to the bedroom.
## Daniel dropped the football.
## Sandra left the milk there.
## Daniel grabbed the football there.
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
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        ## Mary journeyed to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra went to the garden.
        self.Sandra.location = "garden"
        ## Daniel went back to the garden.
        self.Daniel.location = "garden"
        ## Daniel went to the office.
        self.Daniel.location = "office"
        ## Sandra grabbed the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra put down the milk there.
        self.milk.location = "office"
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## Sandra got the milk there.
        self.milk.location = "hallway"
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        ## Daniel journeyed to the kitchen.
        self.Daniel.location = "kitchen"
        ## Daniel journeyed to the bedroom.
        self.Daniel.location = "bedroom"
        ## Mary journeyed to the garden.
        self.Mary.location = "garden"
        ## Daniel took the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## Sandra travelled to the bedroom.
        self.Sandra.location = "bedroom"
        ## Daniel dropped the football.
        self.football.location = "office"
        ## Sandra left the milk there.
        self.milk.location = "office"
        ## Daniel grabbed the football there.
        self.football.location = "office"
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()