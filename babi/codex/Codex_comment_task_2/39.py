## John went back to the office.
## Mary went back to the hallway.
## Daniel journeyed to the bedroom.
## Mary went back to the bathroom.
## Sandra went back to the hallway.
## Sandra got the milk there.
## Mary moved to the office.
## Mary went to the hallway.
## Daniel went to the bathroom.
## Sandra went to the office.
## John journeyed to the garden.
## Sandra journeyed to the hallway.
## Daniel moved to the office.
## Mary went back to the office.
## John moved to the kitchen.
## Sandra journeyed to the bedroom.
## Sandra went back to the office.
## Daniel moved to the kitchen.
## John took the football there.
## John left the football.
## Sandra went back to the bedroom.
## Sandra went back to the hallway.
## John grabbed the football there.
## Daniel went to the bathroom.
## John left the football.
## Sandra went back to the bedroom.
## Mary went to the kitchen.
## John grabbed the football there.
## Sandra put down the milk there.
## John moved to the garden.
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
        ## John went back to the office.
        self.John.location = "office"
        ## Mary went back to the hallway.
        self.Mary.location = "hallway"
        ## Daniel journeyed to the bedroom.
        self.Daniel.location = "bedroom"
        ## Mary went back to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra got the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## Mary went to the hallway.
        self.Mary.location = "hallway"
        ## Daniel went to the bathroom.
        self.Daniel.location = "bathroom"
        ## Sandra went to the office.
        self.Sandra.location = "office"
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Sandra journeyed to the hallway.
        self.Sandra.location = "hallway"
        ## Daniel moved to the office.
        self.Daniel.location = "office"
        ## Mary went back to the office.
        self.Mary.location = "office"
        ## John moved to the kitchen.
        self.John.location = "kitchen"
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Daniel moved to the kitchen.
        self.Daniel.location = "kitchen"
        ## John took the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John left the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Sandra went back to the bedroom.
        self.Sandra.location = "bedroom"
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## John grabbed the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Daniel went to the bathroom.
        self.Daniel.location = "bathroom"
        ## John left the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Sandra went back to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary went to the kitchen.
        self.Mary.location = "kitchen"
        ## John grabbed the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Sandra put down the milk there.
        self.milk.location = "kitchen"
        self.milk.carrier = None
        ## John moved to the garden.
        self.John.location = "garden"
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()