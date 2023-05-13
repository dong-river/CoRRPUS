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
## Sandra grabbed the football.
## John took the apple.
## Mary travelled to the hallway.
## Mary journeyed to the office.
## Sandra discarded the football.
## John put down the apple there.
## Mary went to the bathroom.
## Daniel picked up the football.
## Daniel travelled to the bathroom.
## Mary moved to the kitchen.
## John took the apple.
## John moved to the kitchen.
## Daniel went back to the office.
## John left the apple there.
## Mary picked up the apple there.
## Mary dropped the apple.
## Daniel went back to the bedroom.
## John moved to the hallway.
## Mary went back to the garden.
## Mary travelled to the bedroom.
## Mary travelled to the kitchen.
## John journeyed to the bedroom.
## Daniel journeyed to the kitchen.
## Daniel got the apple there.
## Sandra moved to the office.
## Sandra journeyed to the bedroom.
## Daniel went to the garden.
## John went back to the bathroom.
## Mary moved to the hallway.
## Mary journeyed to the kitchen.
## Sandra moved to the office.
## Daniel journeyed to the office.
## Mary travelled to the bedroom.
## Daniel put down the football there.
## Sandra journeyed to the bathroom.
## Daniel left the apple there.
## John moved to the bedroom.
## Sandra journeyed to the office.
## Sandra got the football.
## Mary went back to the hallway.
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
        self.apple = object("apple")
        self.football = object("football")
        self.milk = object("milk")

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
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "office"
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
        self.apple.location = "bathroom"
        ## Daniel went to the garden.
        self.Daniel.location = "garden"
        ## Daniel dropped the milk.
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "garden"
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
        self.football.location = "garden"
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
        ## Mary went back to the office.
        self.Mary.location = "office"
        ## Daniel travelled to the hallway.
        self.Daniel.location = "hallway"
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
        self.apple.location = "office"
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
        self.apple.location = "office"
        ## Sandra grabbed the football.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## John took the apple.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        ## Mary journeyed to the office.
        self.Mary.location = "office"
        ## Sandra discarded the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "bedroom"
        ## John put down the apple there.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "office"
        ## Mary went to the bathroom.
        self.Mary.location = "bathroom"
        ## Daniel picked up the football.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Daniel travelled to the bathroom.
        self.Daniel.location = "bathroom"
        ## Mary moved to the kitchen.
        self.Mary.location = "kitchen"
        ## John took the apple.
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        ## John moved to the kitchen.
        self.John.location = "kitchen"
        ## Daniel went back to the office.
        self.Daniel.location = "office"
        ## John left the apple there.
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "kitchen"
        ## Mary picked up the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Mary dropped the apple.
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "kitchen"
        ## Daniel went back to the bedroom.
        self.Daniel.location = "bedroom"
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## Sandra journeyed to the office.
        self.Sandra.location = "office"
        ## Sandra got the football.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Mary went back to the hallway.
        self.Mary.location = "hallway"
        ## Where was the apple before the office? 
        print(self.apple.location)

world = World()
world.story()