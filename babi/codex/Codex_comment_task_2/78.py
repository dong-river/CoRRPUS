## Sandra journeyed to the garden.
## Sandra travelled to the bathroom.
## Daniel went back to the garden.
## Sandra got the apple there.
## Mary travelled to the bedroom.
## John went to the hallway.
## Sandra travelled to the office.
## Mary grabbed the milk there.
## John went to the kitchen.
## Mary moved to the hallway.
## Sandra discarded the apple.
## Mary left the milk.
## Mary took the milk there.
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
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        ## Sandra journeyed to the garden.
        self.Sandra.location = "garden"
        ## Sandra travelled to the bathroom.
        self.Sandra.location = "bathroom"
        ## Daniel went back to the garden.
        self.Daniel.location = "garden"
        ## Sandra got the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## John went to the hallway.
        self.John.location = "hallway"
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## Mary grabbed the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Mary moved to the hallway.
        self.Mary.location = "hallway"
        ## Sandra discarded the apple.
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Mary left the milk.
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Mary took the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Mary left the milk.
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()