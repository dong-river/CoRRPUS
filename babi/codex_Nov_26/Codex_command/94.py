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
## Mary dropped the milk.
## Daniel travelled to the bedroom.
## John journeyed to the office.
## Daniel went to the garden.
## Mary picked up the milk there.
## Mary left the milk.
## John travelled to the garden.
## Mary travelled to the office.
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
        self.Mary_dropped_the_milk()
        self.Daniel_travelled_to_the_bedroom()
        self.John_journeyed_to_the_office()
        self.Daniel_went_to_the_garden()
        self.Mary_picked_up_the_milk_there()
        self.Mary_left_the_milk()
        self.John_travelled_to_the_garden()
        self.Mary_travelled_to_the_office()
        
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
        self.Mary.inventory.remove(self.milk)
        self.milk.location = "garden"
        
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
        
    def Mary_dropped_the_milk(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.location = "kitchen"
        
    def Daniel_travelled_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def John_journeyed_to_the_office(self):
        self.John.location = "office"
        
    def Daniel_went_to_the_garden(self):
        self.Daniel.location = "garden"
        
    def Mary_picked_up_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def Mary_left_the_milk(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.location = "garden"
        
    def John_travelled_to_the_garden(self):
        self.John.location = "garden"
        
    def Mary_travelled_to_the_office(self):
        self.Mary.location = "office"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()