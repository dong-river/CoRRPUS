## Mary went to the garden.
## John picked up the milk there.
## Mary journeyed to the bedroom.
## Sandra went back to the hallway.
## John discarded the milk.
## John journeyed to the bedroom.
## John got the football there.
## John moved to the bathroom.
## Sandra went to the office.
## Daniel went back to the hallway.
## John put down the football.
## Mary journeyed to the kitchen.
## Mary picked up the milk there.
## Mary moved to the hallway.
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
        self.milk = object("milk")

    def story(self):
        ## Mary went to the garden.
        self.Mary.location = "garden"
        ## John picked up the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## John discarded the milk.
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        ## John journeyed to the bedroom.
        self.John.location = "bedroom"
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John moved to the bathroom.
        self.John.location = "bathroom"
        ## Sandra went to the office.
        self.Sandra.location = "office"
        ## Daniel went back to the hallway.
        self.Daniel.location = "hallway"
        ## John put down the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Mary journeyed to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary picked up the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Mary moved to the hallway.
        self.Mary.location = "hallway"
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()