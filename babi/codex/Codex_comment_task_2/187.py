## Sandra journeyed to the bathroom.
## Mary took the apple there.
## Sandra went back to the kitchen.
## Mary went back to the office.
## Sandra took the milk there.
## Mary discarded the apple.
## Mary got the apple there.
## Daniel moved to the bedroom.
## John went to the bedroom.
## Sandra dropped the milk there.
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
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        ## Sandra journeyed to the bathroom.
        self.Sandra.location = "bathroom"
        ## Mary took the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Sandra went back to the kitchen.
        self.Sandra.location = "kitchen"
        ## Mary went back to the office.
        self.Mary.location = "office"
        ## Sandra took the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Mary discarded the apple.
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Mary got the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## John went to the bedroom.
        self.John.location = "bedroom"
        ## Sandra dropped the milk there.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()