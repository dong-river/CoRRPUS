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
## Sandra grabbed the apple there.
## Mary went to the office.
## Sandra left the apple there.
## Daniel went to the bedroom.
## Sandra went back to the bedroom.
## Mary travelled to the hallway.
## Mary went to the office.
## Sandra took the milk.
## Mary went to the bathroom.
## John moved to the bathroom.
## Daniel moved to the kitchen.
## Mary grabbed the apple.
## Daniel moved to the office.
## Sandra went to the kitchen.
## Sandra went back to the office.
## Mary dropped the apple.
## Sandra dropped the milk.
## John went to the kitchen.
## Daniel grabbed the milk.
## Mary picked up the apple.
## Sandra went back to the hallway.
## Daniel journeyed to the hallway.
## John moved to the bedroom.
## John went to the bathroom.
## Daniel discarded the milk there.
## Mary moved to the kitchen.
## Mary journeyed to the office.
## Daniel got the milk.
## John moved to the garden.
## Sandra travelled to the kitchen.
## Mary put down the apple.
## John took the football.
## Sandra travelled to the garden.
## Sandra travelled to the bedroom.
## Where was the apple before the office? 

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
        self.milk.location = "bedroom"
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
        self.apple.location = "hallway"
        ## Sandra grabbed the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## Mary went to the office.
        self.Mary.location = "office"
        ## Sandra left the apple there.
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "hallway"
        ## Daniel went to the bedroom.
        self.Daniel.location = "bedroom"
        ## Sandra went back to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        ## Mary went to the office.
        self.Mary.location = "office"
        ## Sandra took the milk.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Mary went to the bathroom.
        self.Mary.location = "bathroom"
        ## John moved to the bathroom.
        self.John.location = "bathroom"
        ## Daniel moved to the kitchen.
        self.Daniel.location = "kitchen"
        ## Mary grabbed the apple.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Daniel moved to the office.
        self.Daniel.location = "office"
        ## Sandra went to the kitchen.
        self.Sandra.location = "kitchen"
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Mary dropped the apple.
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "bathroom"
        ## Sandra dropped the milk.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "office"
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Daniel grabbed the milk.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## Mary picked up the apple.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Daniel moved to the office.
        self.Daniel.location = "office"
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## Daniel journeyed to the hallway.
        self.Daniel.location = "hallway"
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## John went to the bathroom.
        self.John.location = "bathroom"
        ## Daniel discarded the milk there.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "hallway"
        ## Mary moved to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary journeyed to the office.
        self.Mary.location = "office"
        ## Daniel got the milk.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## John moved to the garden.
        self.John.location = "garden"
        ## Sandra travelled to the kitchen.
        self.Sandra.location = "kitchen"
        ## Mary put down the apple.
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "office"
        ## John took the football.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Sandra travelled to the garden.
        self.Sandra.location = "garden"
        ## Sandra travelled to the bedroom.
        self.Sandra.location = "bedroom"
        ## Where was the apple before the office? 
        print(self.apple.location)

world = World()
world.story()