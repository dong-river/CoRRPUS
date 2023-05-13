## Mary went back to the bathroom.
## Daniel went back to the bathroom.
## Mary got the milk there.
## Mary journeyed to the kitchen.
## Mary got the apple there.
## Mary moved to the hallway.
## Mary went back to the bedroom.
## Mary moved to the kitchen.
## John journeyed to the bathroom.
## John went back to the hallway.
## John moved to the bedroom.
## Mary journeyed to the garden.
## Daniel travelled to the office.
## Daniel picked up the football there.
## Mary journeyed to the office.
## John journeyed to the bathroom.
## Daniel discarded the football.
## Mary discarded the milk.
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
        self.apple = object("apple")

    def story(self):
        ## Mary went back to the bathroom.
        self.Mary.location = "bathroom"
        ## Daniel went back to the bathroom.
        self.Daniel.location = "bathroom"
        ## Mary got the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Mary journeyed to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary got the apple there.
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        ## Mary moved to the hallway.
        self.Mary.location = "hallway"
        ## Mary went back to the bedroom.
        self.Mary.location = "bedroom"
        ## Mary moved to the kitchen.
        self.Mary.location = "kitchen"
        ## John journeyed to the bathroom.
        self.John.location = "bathroom"
        ## John went back to the hallway.
        self.John.location = "hallway"
        ## John moved to the bedroom.
        self.John.location = "bedroom"
        ## Mary journeyed to the garden.
        self.Mary.location = "garden"
        ## Daniel travelled to the office.
        self.Daniel.location = "office"
        ## Daniel picked up the football there.
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        ## Mary journeyed to the office.
        self.Mary.location = "office"
        ## John journeyed to the bathroom.
        self.John.location = "bathroom"
        ## Daniel discarded the football.
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        ## Mary discarded the milk.
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()