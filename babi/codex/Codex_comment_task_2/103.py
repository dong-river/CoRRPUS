## Mary moved to the bathroom.
## Sandra went to the kitchen.
## John travelled to the bedroom.
## Mary journeyed to the kitchen.
## Mary moved to the office.
## Sandra travelled to the bathroom.
## John travelled to the bathroom.
## John journeyed to the office.
## John took the milk there.
## Daniel travelled to the garden.
## Mary went to the kitchen.
## Daniel journeyed to the bathroom.
## John discarded the milk.
## Sandra went back to the kitchen.
## Daniel journeyed to the office.
## Sandra went back to the office.
## Daniel picked up the milk there.
## Sandra went back to the bedroom.
## John went to the garden.
## Daniel travelled to the kitchen.
## John journeyed to the bedroom.
## Sandra journeyed to the garden.
## Sandra moved to the kitchen.
## Daniel discarded the milk.
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
        self.milk = object("milk")

    def story(self):
        ## Mary moved to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra went to the kitchen.
        self.Sandra.location = "kitchen"
        ## John travelled to the bedroom.
        self.John.location = "bedroom"
        ## Mary journeyed to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## Sandra travelled to the bathroom.
        self.Sandra.location = "bathroom"
        ## John travelled to the bathroom.
        self.John.location = "bathroom"
        ## John journeyed to the office.
        self.John.location = "office"
        ## John took the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Daniel travelled to the garden.
        self.Daniel.location = "garden"
        ## Mary went to the kitchen.
        self.Mary.location = "kitchen"
        ## Daniel journeyed to the bathroom.
        self.Daniel.location = "bathroom"
        ## John discarded the milk.
        self.milk.location = "office"
        self.milk.carrier = None
        ## Sandra went back to the kitchen.
        self.Sandra.location = "kitchen"
        ## Daniel journeyed to the office.
        self.Daniel.location = "office"
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Daniel picked up the milk there.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## Sandra went back to the bedroom.
        self.Sandra.location = "bedroom"
        ## John went to the garden.
        self.John.location = "garden"
        ## Daniel travelled to the kitchen.
        self.Daniel.location = "kitchen"
        ## John journeyed to the bedroom.
        self.John.location = "bedroom"
        ## Sandra journeyed to the garden.
        self.Sandra.location = "garden"
        ## Sandra moved to the kitchen.
        self.Sandra.location = "kitchen"
        ## Daniel discarded the milk.
        self.milk.location = "kitchen"
        self.milk.carrier = None
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()