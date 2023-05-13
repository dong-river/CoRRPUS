## John travelled to the bathroom.
## John travelled to the hallway.
## Mary picked up the milk there.
## Mary went back to the bedroom.
## Sandra took the football there.
## Sandra moved to the office.
## Sandra went back to the bathroom.
## John journeyed to the bedroom.
## John went back to the bathroom.
## Sandra put down the football.
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
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        ## John travelled to the bathroom.
        self.John.location = "bathroom"
        ## John travelled to the hallway.
        self.John.location = "hallway"
        ## Mary picked up the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Mary went back to the bedroom.
        self.Mary.location = "bedroom"
        ## Sandra took the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Sandra moved to the office.
        self.Sandra.location = "office"
        ## Sandra went back to the bathroom.
        self.Sandra.location = "bathroom"
        ## John journeyed to the bedroom.
        self.John.location = "bedroom"
        ## John went back to the bathroom.
        self.John.location = "bathroom"
        ## Sandra put down the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        ## Where is the football?
        print(self.football.location)
 

world = World()
world.story()