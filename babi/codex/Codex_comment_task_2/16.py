## Daniel journeyed to the office.
## John took the football there.
## John discarded the football.
## John travelled to the garden.
## Daniel travelled to the garden.
## Sandra went to the garden.
## Daniel travelled to the kitchen.
## Daniel moved to the office.
## Mary grabbed the milk there.
## Daniel journeyed to the bedroom.
## John travelled to the office.
## Daniel travelled to the bathroom.
## John travelled to the kitchen.
## Mary travelled to the garden.
## Mary dropped the milk.
## John went back to the garden.
## Sandra got the milk there.
## Sandra put down the milk.
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

    def story(self):
        ## Daniel journeyed to the office.
        self.Daniel.location = "office"
        ## John took the football there.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John discarded the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## John travelled to the garden.
        self.John.location = "garden"
        ## Daniel travelled to the garden.
        self.Daniel.location = "garden"
        ## Sandra went to the garden.
        self.Sandra.location = "garden"
        ## Daniel travelled to the kitchen.
        self.Daniel.location = "kitchen"
        ## Daniel moved to the office.
        self.Daniel.location = "office"
        ## Mary grabbed the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Daniel journeyed to the bedroom.
        self.Daniel.location = "bedroom"
        ## John travelled to the office.
        self.John.location = "office"
        ## Daniel travelled to the bathroom.
        self.Daniel.location = "bathroom"
        ## John travelled to the kitchen.
        self.John.location = "kitchen"
        ## Mary travelled to the garden.
        self.Mary.location = "garden"
        ## Mary dropped the milk.
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        ## John went back to the garden.
        self.John.location = "garden"
        ## Sandra got the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra put down the milk.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()