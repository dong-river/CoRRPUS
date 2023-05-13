## Sandra went back to the hallway.
## Mary travelled to the hallway.
## Mary picked up the football there.
## John travelled to the bathroom.
## Daniel moved to the bedroom.
## Sandra moved to the bedroom.
## Sandra travelled to the hallway.
## Sandra travelled to the office.
## Mary moved to the office.
## Mary put down the football.
## Sandra grabbed the milk there.
## Sandra left the milk.
## Mary took the football there.
## Sandra took the milk there.
## Mary dropped the football.
## Mary travelled to the bedroom.
## John went to the hallway.
## Sandra took the football there.
## Mary went back to the hallway.
## Sandra travelled to the kitchen.
## John journeyed to the garden.
## Sandra journeyed to the bathroom.
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
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        ## Mary picked up the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## John travelled to the bathroom.
        self.John.location = "bathroom"
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## Sandra moved to the bedroom.
        self.Sandra.location = "bedroom"
        ## Sandra travelled to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## Mary put down the football.
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "office"
        ## Sandra grabbed the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra left the milk.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "office"
        ## Mary took the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## Sandra took the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Mary dropped the football.
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "office"
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## John went to the hallway.
        self.John.location = "hallway"
        ## Sandra took the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Mary went back to the hallway.
        self.Mary.location = "hallway"
        ## Sandra travelled to the kitchen.
        self.Sandra.location = "kitchen"
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Sandra journeyed to the bathroom.
        self.Sandra.location = "bathroom"
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()