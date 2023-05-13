## Daniel moved to the kitchen.
## John grabbed the football there.
## John left the football there.
## Mary journeyed to the hallway.
## John grabbed the milk there.
## John travelled to the kitchen.
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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.Mary = character("Mary")
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        self.Daniel_moved_to_the_kitchen()
        self.John_grabbed_the_football_there()
        self.John_left_the_football_there()
        self.Mary_journeyed_to_the_hallway()
        self.John_grabbed_the_milk_there()
        self.John_travelled_to_the_kitchen()
        self.Where_is_the_milk()

    def Daniel_moved_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def John_grabbed_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_left_the_football_there(self):
        self.John.inventory.remove(self.football)
        self.football.location = self.John.location
        
    def Mary_journeyed_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def John_grabbed_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def John_travelled_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()