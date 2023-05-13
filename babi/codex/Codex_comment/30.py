## Mary went back to the garden.
## John went back to the hallway.
## Daniel went back to the bedroom.
## Daniel got the milk.
## Daniel put down the milk.
## Daniel got the milk.
## Daniel dropped the milk.
## Mary picked up the apple.
## Daniel went to the hallway.
## John went back to the office.
## John moved to the bedroom.
## Daniel travelled to the office.
## Mary discarded the apple.
## John took the milk.
## Mary went to the office.
## Sandra went to the bathroom.
## Sandra went back to the office.
## Sandra moved to the garden.
## Sandra grabbed the apple there.
## John travelled to the hallway.
## Daniel went back to the garden.
## Sandra moved to the bathroom.
## John grabbed the football.
## Daniel went to the hallway.
## Sandra went to the hallway.
## Sandra moved to the office.
## Sandra moved to the kitchen.
## Sandra left the apple there.
## Where was the apple before the hallway? 

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
        self.apple = object("apple")
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        self.apple.location = "garden"
        ## John went back to the hallway.
        self.John.location = "hallway"
        ## Daniel went back to the bedroom.
        self.Daniel.location = "bedroom"
        ## Daniel got the milk.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## Daniel put down the milk.
        self.milk.carrier = None
        ## Daniel got the milk.
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        ## Daniel dropped the milk.
        self.milk.carrier = None
        ## Mary picked up the apple.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## John went back to the office.
        self.John.location = "office"
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## Daniel travelled to the office.
        self.Daniel.location = "office"
        ## Mary discarded the apple.
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        ## John took the milk.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## Mary went to the office.
        self.Mary.location = "office"
        ## Sandra went to the bathroom.
        self.Sandra.location = "bathroom"
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Sandra moved to the garden.
        self.Sandra.location = "garden"
        ## Sandra grabbed the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        ## John travelled to the hallway.
        self.John.location = "hallway"
        ## Daniel went back to the garden.
        self.Daniel.location = "garden"
        ## Sandra moved to the bathroom.
        self.Sandra.location = "bathroom"
        ## John grabbed the football.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Daniel went to the hallway.
        self.Daniel.location = "hallway"
        ## Sandra went to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra moved to the office.
        self.Sandra.location = "office"
        ## Sandra moved to the kitchen.
        self.Sandra.location = "kitchen"
        ## Sandra left the apple there.
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        ## Where was the apple before the hallway?
        print(self.apple.location)

world = World()
world.story()