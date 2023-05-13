## John went to the hallway.
## Mary went back to the office.
## Mary got the milk.
## John journeyed to the garden.
## Daniel went to the kitchen.
## Mary put down the milk.
## John travelled to the bathroom.
## Daniel went back to the hallway.
## John took the apple.
## Daniel journeyed to the office.
## Daniel grabbed the milk.
## John discarded the apple.
## Daniel went to the garden.
## Daniel dropped the milk.
## Mary travelled to the garden.
## Daniel travelled to the office.
## Mary travelled to the bedroom.
## Mary moved to the garden.
## John picked up the football.
## John picked up the apple.
## John left the football.
## John moved to the office.
## Sandra travelled to the bathroom.
## Sandra got the football.
## Sandra travelled to the office.
## Daniel went back to the bedroom.
## Mary went back to the office.
## Daniel travelled to the hallway.
## Mary went back to the hallway.
## Sandra moved to the bedroom.
## Daniel moved to the bedroom.
## Sandra moved to the bathroom.
## John dropped the apple.
## John picked up the apple.
## Mary went back to the bedroom.
## Sandra went to the bedroom.
## Sandra dropped the football there.
## John dropped the apple.
## Where was the football before the bedroom? 

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
        self.Daniel = character("Daniel")
        self.Sandra = character("Sandra")
        self.milk = object("milk")
        self.apple = object("apple")
        self.football = object("football")

    def story(self):
        ## John went to the hallway.
        self.John.location = "hallway"
        ## Mary went back to the office.
        self.Mary.location = "office"
        ## Mary got the milk.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Daniel went to the kitchen.
        self.Daniel.location = "kitchen"
        ## Mary put down the milk.
        self.milk.location = "office"
        self.milk.carrier = None
        ## John travelled to the bathroom.
        self.John.location = "bathroom"
        ## Daniel went back to the hallway.
        self.Daniel.location = "hallway"
        ## John took the apple.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Daniel journeyed to the office.
        self.Daniel.location = "office"
        ## Daniel grabbed the milk.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## John discarded the apple.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        ## Daniel dropped the milk.
        self.milk.location = "garden"
        self.milk.carrier = None
        ## Mary travelled to the garden.
        self.Mary.location = "garden"
        ## Daniel travelled to the office.
        self.Daniel.location = "office"
        ## Mary travelled to the bedroom.
        self.Mary.location = "bedroom"
        ## Mary moved to the garden.
        self.Mary.location = "garden"
        ## John picked up the football.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John picked up the apple.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## John left the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## John moved to the office.
        self.John.location = "office"
        ## Sandra travelled to the bathroom.
        self.Sandra.location = "bathroom"
        ## Sandra got the football.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## Daniel went back to the bedroom.
        self.Daniel.location = "bedroom"
        ## Mary went back to the hallway.
        self.Mary.location = "hallway"
        ## Sandra moved to the bedroom.
        self.Sandra.location = "bedroom"
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## Sandra moved to the bathroom.
        self.Sandra.location = "bathroom"
        ## John dropped the apple.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        ## John picked up the apple.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Mary went back to the bedroom.
        self.Mary.location = "bedroom"
        ## Sandra went to the bedroom.
        self.Sandra.location = "bedroom"
        ## Sandra dropped the football there.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "bedroom"
        ## John dropped the apple.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Where was the football before the bedroom? 
        print(self.football.location)

world = World()
world.story()