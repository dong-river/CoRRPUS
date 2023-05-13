## John got the football there.
## John left the football.
## Daniel went back to the bathroom.
## Mary went back to the bathroom.
## Sandra travelled to the office.
## Daniel got the apple there.
## John got the football there.
## John left the football.
## Daniel journeyed to the kitchen.
## John moved to the bathroom.
## John went to the office.
## Mary took the milk there.
## John journeyed to the garden.
## Sandra went to the garden.
## Daniel grabbed the football there.
## Mary discarded the milk.
## Sandra moved to the office.
## Mary got the milk there.
## Mary moved to the garden.
## Mary left the milk.
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
        self.apple = object("apple")

    def story(self):
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John left the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Daniel went back to the bathroom.
        self.Daniel.location = "bathroom"
        ## Mary went back to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## Daniel got the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## John got the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John left the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Daniel journeyed to the kitchen.
        self.Daniel.location = "kitchen"
        ## John moved to the bathroom.
        self.John.location = "bathroom"
        ## John went to the office.
        self.John.location = "office"
        ## Mary took the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Sandra went to the garden.
        self.Sandra.location = "garden"
        ## Daniel grabbed the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Mary discarded the milk.
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Sandra moved to the office.
        self.Sandra.location = "office"
        ## Mary got the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Mary moved to the garden.
        self.Mary.location = "garden"
        ## Mary left the milk.
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()