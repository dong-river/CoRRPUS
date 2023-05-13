## Sandra got the milk there.
## John grabbed the apple there.
## John journeyed to the bathroom.
## John discarded the apple.
## John journeyed to the garden.
## Sandra travelled to the bedroom.
## Sandra went back to the garden.
## Sandra left the milk there.
## John grabbed the milk there.
## John went back to the kitchen.
## Daniel went to the garden.
## Sandra journeyed to the kitchen.
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
        self.apple = object("apple")

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
        ## Sandra got the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## John grabbed the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## John journeyed to the bathroom.
        self.John.location = "bathroom"
        ## John discarded the apple.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Sandra travelled to the bedroom.
        self.Sandra.location = "bedroom"
        ## Sandra went back to the garden.
        self.Sandra.location = "garden"
        ## Sandra left the milk there.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        ## John grabbed the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## John went back to the kitchen.
        self.John.location = "kitchen"
        ## Daniel went to the garden.
        self.Daniel = character("Daniel")
        self.Daniel.location = "garden"
        ## Sandra journeyed to the kitchen.
        self.Sandra.location = "kitchen"
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()