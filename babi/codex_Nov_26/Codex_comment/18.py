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
## Mary went back to the bathroom.
## Mary travelled to the bedroom.
## John got the milk there.
## Daniel went back to the office.
## Daniel moved to the kitchen.
## Daniel grabbed the apple there.
## John left the milk.
## Daniel discarded the apple.
## 
## Where is the apple? 

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
        ## Daniel journeyed to the office.
        self.Daniel.location = "office"
        ## John took the football there.
        self.John.location = "office"
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John discarded the football.
        self.John.inventory.remove(self.football)
        self.football.location = "office"
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
        self.milk.location = "office"
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
        self.milk.location = "garden"
        ## John went back to the garden.
        self.John.location = "garden"
        ## Sandra got the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra put down the milk.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "garden"
        ## Mary went back to the bathroom.
        self.Mary.location = "bathroom"
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## John got the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Daniel went back to the office.
        self.Daniel.location = "office"
        ## Daniel moved to the kitchen.
        self.Daniel.location = "kitchen"
        ## Daniel grabbed the apple there.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        self.apple.location = "kitchen"
        ## John left the milk.
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "bedroom"
        ## Daniel discarded the apple.
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "kitchen"
        ## 
        ## Where is the apple? 
        print(self.apple.location)

world = World()
world.story()