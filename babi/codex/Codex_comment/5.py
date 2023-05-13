## John went back to the kitchen.
## Daniel picked up the milk.
## Sandra went back to the bedroom.
## Mary moved to the garden.
## Sandra got the apple.
## Mary journeyed to the office.
## Mary journeyed to the garden.
## Sandra went to the hallway.
## Daniel moved to the bedroom.
## Sandra grabbed the football.
## Daniel discarded the milk.
## John journeyed to the garden.
## John went to the hallway.
## Mary journeyed to the office.
## John journeyed to the bedroom.
## Sandra moved to the garden.
## John travelled to the garden.
## Daniel grabbed the milk.
## Mary journeyed to the bathroom.
## Daniel dropped the milk.
## Daniel went to the office.
## Daniel travelled to the garden.
## John went back to the bedroom.
## Sandra discarded the football.
## Mary went back to the hallway.
## John journeyed to the garden.
## Daniel went back to the hallway.
## John went to the bedroom.
## Sandra travelled to the bathroom.
## John moved to the hallway.
## Daniel travelled to the kitchen.
## Daniel journeyed to the bedroom.
## John journeyed to the office.
## Mary travelled to the garden.
## Daniel went to the hallway.
## Daniel went to the garden.
## Daniel travelled to the hallway.
## Mary journeyed to the bathroom.
## John travelled to the kitchen.
## Sandra dropped the apple.
## Where was the apple before the bathroom? 

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
        self.football = object("football")

    def story(self):
        ## John went back to the kitchen.
        self.John.location = "kitchen"
        ## Daniel picked up the milk.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## Sandra went back to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary moved to the garden.
        self.Mary.location = "garden"
        ## Sandra got the apple.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## Mary journeyed to the office.
        self.Mary.location = "office"
        ## Mary journeyed to the garden.
        self.Mary.location = "garden"
        ## Sandra went to the hallway.
        self.Sandra.location = "hallway"
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## Sandra grabbed the football.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Daniel discarded the milk.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "bedroom"
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## John went to the hallway.
        self.John.location = "hallway"
        ## Mary journeyed to the office.
        self.Mary.location = "office"
        ## John journeyed to the bedroom.
        self.John.location = "bedroom"
        ## Sandra moved to the garden.
        self.Sandra.location = "garden"
        ## John travelled to the garden.
        self.John.location = "garden"
        ## Daniel grabbed the milk.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## Mary journeyed to the bathroom.
        self.Mary.location = "bathroom"
        ## Daniel dropped the milk.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "hallway"
        ## Daniel went to the office.
        self.Daniel.location = "office"
        ## Daniel travelled to the garden.
        self.Daniel.location = "garden"
        ## John went back to the bedroom.
        self.John.location = "bedroom"
        ## Sandra discarded the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "garden"
        ## Mary went back to the hallway.
        self.Mary.location = "hallway"
        ## John journeyed to the garden.
        self.John.location = "garden"
        ## Daniel went back to the hallway.
        self.Daniel.location = "hallway"
        ## John went to the bedroom.
        self.John.location = "bedroom"
        ## Sandra travelled to the bathroom.
        self.Sandra.location = "bathroom"
        ## John moved to the hallway.
        self.John.location = "hallway"
        ## Daniel travelled to the kitchen.
        self.Daniel.location = "kitchen"
        ## Daniel journeyed to the bedroom.
        self.Daniel.location = "bedroom"
        ## John journeyed to the office.
        self.John.location = "office"
        ## Mary travelled to the garden.
        self.Mary.location = "garden"
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        ## Daniel travelled to the hallway.
        self.Daniel.location = "hallway"
        ## Mary journeyed to the bathroom.
        self.Mary.location = "bathroom"
        ## John travelled to the kitchen.
        self.John.location = "kitchen"
        ## Sandra dropped the apple.
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "bathroom"
        ## Where was the apple before the bathroom? 
        print(self.apple.location)

world = World()
world.story()