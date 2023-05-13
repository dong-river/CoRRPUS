## Daniel moved to the kitchen.
## John grabbed the football there.
## John left the football there.
## Mary journeyed to the hallway.
## John grabbed the milk there.
## John travelled to the kitchen.
## Mary journeyed to the kitchen.
## Sandra went to the office.
## Daniel went to the bathroom.
## Daniel picked up the apple there.
## Sandra travelled to the garden.
## Daniel dropped the apple there.
## Sandra went back to the office.
## Daniel journeyed to the kitchen.
## John put down the milk.
## Daniel moved to the bedroom.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        self.Daniel_moved_to_the_kitchen()
        self.John_grabbed_the_football_there()
        self.John_left_the_football_there()
        self.Mary_journeyed_to_the_hallway()
        self.John_grabbed_the_milk_there()
        self.John_travelled_to_the_kitchen()
        self.Mary_journeyed_to_the_kitchen()
        self.Sandra_went_to_the_office()
        self.Daniel_went_to_the_bathroom()
        self.Daniel_picked_up_the_apple_there()
        self.Sandra_travelled_to_the_garden()
        self.Daniel_dropped_the_apple_there()
        self.Sandra_went_back_to_the_office()
        self.Daniel_journeyed_to_the_kitchen()
        self.John_put_down_the_milk()
        self.Daniel_moved_to_the_bedroom()
        
        self.Where_is_the_milk()

    def Daniel_moved_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def John_grabbed_the_football_there(self):
        self.football.location = "kitchen"
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_left_the_football_there(self):
        self.football.location = "kitchen"
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Mary_journeyed_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def John_grabbed_the_milk_there(self):
        self.milk.location = "hallway"
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def John_travelled_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Mary_journeyed_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        
    def Sandra_went_to_the_office(self):
        self.Sandra.location = "office"
        
    def Daniel_went_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def Daniel_picked_up_the_apple_there(self):
        self.apple.location = "bathroom"
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        
    def Sandra_travelled_to_the_garden(self):
        self.Sandra.location = "garden"
        
    def Daniel_dropped_the_apple_there(self):
        self.apple.location = "garden"
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        
    def Daniel_journeyed_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def John_put_down_the_milk(self):
        self.milk.location = "kitchen"
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Daniel_moved_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()