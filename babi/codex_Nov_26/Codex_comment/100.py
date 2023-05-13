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
## 
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
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Sandra went back to the kitchen.
        self.Sandra.location = "kitchen"
        ## 
        ## Where is the milk? 
        print(self.milk.location)

world = World()
world.story()