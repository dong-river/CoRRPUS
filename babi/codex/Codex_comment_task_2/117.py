## John grabbed the football there.
## John journeyed to the office.
## John went back to the garden.
## John went to the hallway.
## John dropped the football.
## John grabbed the football there.
## Sandra travelled to the bathroom.
## Sandra picked up the milk there.
## Sandra went to the office.
## John moved to the bathroom.
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
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        ## Mary moved to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary got the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        self.football.location = "garden"
        ## Where is the football?
        print(self.football.location)
        ## John grabbed the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John journeyed to the office.
        self.John.location = "office"
        self.football.location = "office"
        ## John went back to the garden.
        self.John.location = "garden"
        self.football.location = "garden"
        ## John went to the hallway.
        self.John.location = "hallway"
        self.football.location = "hallway"
        ## John dropped the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## John grabbed the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Sandra travelled to the bathroom.
        self.Sandra.location = "bathroom"
        ## Sandra picked up the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra went to the office.
        self.Sandra.location = "office"
        self.milk.location = "office"
        ## John moved to the bathroom.
        self.John.location = "bathroom"
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()