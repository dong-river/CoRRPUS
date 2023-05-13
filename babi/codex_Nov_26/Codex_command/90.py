## Daniel moved to the bathroom.
## Sandra went back to the kitchen.
## John moved to the bathroom.
## Mary picked up the milk there.
## John travelled to the garden.
## Mary dropped the milk there.
## Sandra journeyed to the bedroom.
## John journeyed to the bathroom.
## Daniel went back to the office.
## John moved to the hallway.
## Mary got the milk there.
## Daniel took the apple there.
## John picked up the football there.
## Mary went to the kitchen.
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
        self.Sandra = character("Sandra")
        self.John = character("John")
        self.Mary = character("Mary")
        self.milk = object("milk")
        self.football = object("football")
        self.apple = object("apple")

    def story(self):
        self.Daniel_moved_to_the_bathroom()
        self.Sandra_went_back_to_the_kitchen()
        self.John_moved_to_the_bathroom()
        self.Mary_picked_up_the_milk_there()
        self.John_travelled_to_the_garden()
        self.Mary_dropped_the_milk_there()
        self.Sandra_journeyed_to_the_bedroom()
        self.John_journeyed_to_the_bathroom()
        self.Daniel_went_back_to_the_office()
        self.John_moved_to_the_hallway()
        self.Mary_got_the_milk_there()
        self.Daniel_took_the_apple_there()
        self.John_picked_up_the_football_there()
        self.Mary_went_to_the_kitchen()
        self.Where_is_the_milk()

    def Daniel_moved_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def Sandra_went_back_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        
    def John_moved_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def Mary_picked_up_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def John_travelled_to_the_garden(self):
        self.John.location = "garden"
        
    def Mary_dropped_the_milk_there(self):
        self.milk.location = "garden"
        self.milk.carrier = None
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        
    def John_journeyed_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def Daniel_went_back_to_the_office(self):
        self.Daniel.location = "office"
        
    def John_moved_to_the_hallway(self):
        self.John.location = "hallway"
        
    def Mary_got_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def Daniel_took_the_apple_there(self):
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        
    def John_picked_up_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Mary_went_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()