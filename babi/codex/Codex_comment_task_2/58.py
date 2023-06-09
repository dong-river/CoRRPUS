## John went to the bathroom.
## Daniel travelled to the kitchen.
## John journeyed to the kitchen.
## Daniel journeyed to the hallway.
## Sandra travelled to the kitchen.
## Mary moved to the office.
## Daniel went back to the office.
## Sandra went back to the bathroom.
## John grabbed the milk there.
## John grabbed the apple there.
## Sandra journeyed to the office.
## Mary went to the hallway.
## John went to the bathroom.
## John discarded the apple.
## John put down the milk.
## John picked up the apple there.
## Daniel went back to the bathroom.
## John took the milk there.
## Daniel travelled to the garden.
## Sandra journeyed to the bathroom.
## John travelled to the kitchen.
## Mary went back to the office.
## Mary moved to the hallway.
## John left the milk.
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
        self.John = character("John")
        self.Daniel = character("Daniel")
        self.Sandra = character("Sandra")
        self.Mary = character("Mary")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        ## John went to the bathroom.
        self.John.location = "bathroom"
        ## Daniel travelled to the kitchen.
        self.Daniel.location = "kitchen"
        ## John journeyed to the kitchen.
        self.John.location = "kitchen"
        ## Daniel journeyed to the hallway.
        self.Daniel.location = "hallway"
        ## Sandra travelled to the kitchen.
        self.Sandra.location = "kitchen"
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## Daniel went back to the office.
        self.Daniel.location = "office"
        ## Sandra went back to the bathroom.
        self.Sandra.location = "bathroom"
        ## John grabbed the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## John grabbed the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Sandra journeyed to the office.
        self.Sandra.location = "office"
        ## Mary went to the hallway.
        self.Mary.location = "hallway"
        ## John went to the bathroom.
        self.John.location = "bathroom"
        ## John discarded the apple.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        ## John put down the milk.
        self.milk.carrier = None
        ## John picked up the apple there.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Daniel went back to the bathroom.
        self.Daniel.location = "bathroom"
        ## John took the milk there.
        self.milk.carrier = self.John
        ## Daniel travelled to the garden.
        self.Daniel.location = "garden"
        ## Sandra journeyed to the bathroom.
        self.Sandra.location = "bathroom"
        ## John travelled to the kitchen.
        self.John.location = "kitchen"
        ## Mary went back to the office.
        self.Mary.location = "office"
        ## Mary moved to the hallway.
        self.Mary.location = "hallway"
        ## John left the milk.
        self.milk.carrier = None
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()