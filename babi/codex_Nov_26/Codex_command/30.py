## Daniel journeyed to the office.
## Daniel went back to the bedroom.
## Mary went back to the kitchen.
## Mary got the football there.
## Daniel travelled to the hallway.
## John journeyed to the bedroom.
## Daniel got the apple there.
## Sandra travelled to the garden.
## Daniel travelled to the garden.
## Daniel dropped the apple.
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
        self.apple = object("apple")

    def story(self):
        self.Daniel_journeyed_to_the_office()
        self.Daniel_went_back_to_the_bedroom()
        self.Mary_went_back_to_the_kitchen()
        self.Mary_got_the_football_there()
        self.Daniel_travelled_to_the_hallway()
        self.John_journeyed_to_the_bedroom()
        self.Daniel_got_the_apple_there()
        self.Sandra_travelled_to_the_garden()
        self.Daniel_travelled_to_the_garden()
        self.Daniel_dropped_the_apple()
        self.Where_is_the_apple()

    def Daniel_journeyed_to_the_office(self):
        self.Daniel.location = "office"
        
    def Daniel_went_back_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def Mary_went_back_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        
    def Mary_got_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def Daniel_travelled_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def John_journeyed_to_the_bedroom(self):
        self.John.location = "bedroom"
        
    def Daniel_got_the_apple_there(self):
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        
    def Sandra_travelled_to_the_garden(self):
        self.Sandra.location = "garden"
        
    def Daniel_travelled_to_the_garden(self):
        self.Daniel.location = "garden"
        
    def Daniel_dropped_the_apple(self):
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = "garden"
        
    def Where_is_the_apple(self):
        print(self.apple.location)

world = World()
world.story()