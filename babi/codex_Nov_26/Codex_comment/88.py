## John went to the hallway.
## John went back to the bathroom.
## John grabbed the milk there.
## Sandra went back to the office.
## Sandra journeyed to the kitchen.
## Sandra got the apple there.
## Sandra dropped the apple there.
## John dropped the milk.
## Mary went back to the garden.
## Sandra journeyed to the hallway.
## Sandra got the football there.
## Mary moved to the kitchen.
## Sandra journeyed to the bedroom.
## Mary grabbed the apple there.
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
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        self.Mary.location = "bathroom"
        self.Sandra.location = "bedroom"
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        self.John.location = "kitchen"
        self.Mary.location = "garden"
        self.football.location = "garden"
        print(self.football.location)
        ## John went to the hallway.
        self.John.location = "hallway"
        ## John went back to the bathroom.
        self.John.location = "bathroom"
        ## John grabbed the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Sandra journeyed to the kitchen.
        self.Sandra.location = "kitchen"
        ## Sandra got the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## Sandra dropped the apple there.
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.Sandra.location
        ## John dropped the milk.
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = self.John.location
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        ## Sandra journeyed to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra got the football there.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Mary moved to the kitchen.
        self.Mary.location = "kitchen"
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary grabbed the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ##
        ## Where is the football? 
        print(self.football.location)

world = World()
world.story()


world = World()
world.story()