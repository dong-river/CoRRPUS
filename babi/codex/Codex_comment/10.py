## Sandra moved to the bathroom.
## John picked up the football.
## John dropped the football.
## Daniel went to the kitchen.
## Daniel got the apple.
## John went to the kitchen.
## Mary went back to the hallway.
## Daniel travelled to the office.
## John travelled to the garden.
## John journeyed to the kitchen.
## Mary moved to the kitchen.
## Daniel moved to the garden.
## Mary journeyed to the bathroom.
## Daniel grabbed the milk.
## Mary went to the hallway.
## Mary got the football there.
## Mary dropped the football.
## Sandra moved to the bedroom.
## Mary went back to the office.
## John travelled to the office.
## Mary went back to the bathroom.
## John moved to the hallway.
## Sandra went to the office.
## Mary journeyed to the kitchen.
## Sandra travelled to the garden.
## John went back to the garden.
## Sandra went back to the office.
## Mary went to the hallway.
## Daniel went to the bedroom.
## Mary picked up the football there.
## John travelled to the kitchen.
## Mary moved to the bedroom.
## Sandra went to the bathroom.
## Daniel put down the milk.
## Daniel discarded the apple.
## Mary took the milk.
## Where was the apple before the bedroom? 

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
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        ## Sandra moved to the bathroom.
        self.Sandra.location = "bathroom"
        ## John picked up the football.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## John dropped the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.John.location
        ## Daniel went to the kitchen.
        self.Daniel.location = "kitchen"
        ## Daniel got the apple.
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Mary went back to the hallway.
        self.Mary.location = "hallway"
        ## Daniel travelled to the office.
        self.Daniel.location = "office"
        ## John travelled to the garden.
        self.John.location = "garden"
        ## John journeyed to the kitchen.
        self.John.location = "kitchen"
        ## Mary moved to the kitchen.
        self.Mary.location = "kitchen"
        ## Daniel moved to the garden.
        self.Daniel.location = "garden"
        ## Mary journeyed to the bathroom.
        self.Mary.location = "bathroom"
        ## Daniel grabbed the milk.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## Mary went to the hallway.
        self.Mary.location = "hallway"
        ## Mary got the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## Mary dropped the football.
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.Mary.location
        ## Sandra moved to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary went back to the office.
        self.Mary.location = "office"
        ## John travelled to the office.
        self.John.location = "office"
        ## Mary went back to the bathroom.
        self.Mary.location = "bathroom"
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## Sandra went to the office.
        self.Sandra.location = "office"
        ## Mary journeyed to the kitchen.
        self.Mary.location = "kitchen"
        ## Sandra travelled to the garden.
        self.Sandra.location = "garden"
        ## John went back to the garden.
        self.John.location = "garden"
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Mary went to the hallway.
        self.Mary.location = "hallway"
        ## Daniel went to the bedroom.
        self.Daniel.location = "bedroom"
        ## Mary picked up the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## John travelled to the kitchen.
        self.John.location = "kitchen"
        ## Mary moved to the bedroom.
        self.Mary.location = "bedroom"
        ## Sandra went to the bathroom.
        self.Sandra.location = "bathroom"
        ## Daniel put down the milk.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = self.Daniel.location
        ## Daniel discarded the apple.
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.Daniel.location
        ## Mary took the milk.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Where was the apple before the bedroom? 
        print(self.apple.location)

world = World()
world.story()