## Daniel journeyed to the office.
## John took the football there.
## John discarded the football.
## John travelled to the garden.
## Daniel travelled to the garden.
## Sandra went to the garden.
## Daniel travelled to the kitchen.
## Daniel moved to the office.
## Mary grabbed the milk there.
## Daniel journeyed to the bedroom.
## John travelled to the office.
## Daniel travelled to the bathroom.
## John travelled to the kitchen.
## Mary travelled to the garden.
## Mary dropped the milk.
## John went back to the garden.
## Sandra got the milk there.
## Sandra put down the milk.
## Mary went back to the bathroom.
## Mary travelled to the bedroom.
## John got the milk there.
## Daniel went back to the office.
## Daniel moved to the kitchen.
## Daniel grabbed the apple there.
## John left the milk.
## Daniel discarded the apple.
## John picked up the milk there.
## Daniel went to the hallway.
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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Mary = character("Mary")
        self.football = object("football")
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        self.Daniel_journeyed_to_the_office()
        self.John_took_the_football_there()
        self.John_discarded_the_football()
        self.John_travelled_to_the_garden()
        self.Daniel_travelled_to_the_garden()
        self.Sandra_went_to_the_garden()
        self.Daniel_travelled_to_the_kitchen()
        self.Daniel_moved_to_the_office()
        self.Mary_grabbed_the_milk_there()
        self.Daniel_journeyed_to_the_bedroom()
        self.John_travelled_to_the_office()
        self.Daniel_travelled_to_the_bathroom()
        self.John_travelled_to_the_kitchen()
        self.Mary_travelled_to_the_garden()
        self.Mary_dropped_the_milk()
        self.John_went_back_to_the_garden()
        self.Sandra_got_the_milk_there()
        self.Sandra_put_down_the_milk()
        self.Mary_went_back_to_the_bathroom()
        self.Mary_travelled_to_the_bedroom()
        self.John_got_the_milk_there()
        self.Daniel_went_back_to_the_office()
        self.Daniel_moved_to_the_kitchen()
        self.Daniel_grabbed_the_apple_there()
        self.John_left_the_milk()
        self.Daniel_discarded_the_apple()
        self.John_picked_up_the_milk_there()
        self.Daniel_went_to_the_hallway()
        self.Where_is_the_apple()

    def Daniel_journeyed_to_the_office(self):
        self.Daniel.location = "office"
        
    def John_took_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_discarded_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def John_travelled_to_the_garden(self):
        self.John.location = "garden"
        
    def Daniel_travelled_to_the_garden(self):
        self.Daniel.location = "garden"
        
    def Sandra_went_to_the_garden(self):
        self.Sandra.location = "garden"
        
    def Daniel_travelled_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def Daniel_moved_to_the_office(self):
        self.Daniel.location = "office"
        
    def Mary_grabbed_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def Daniel_journeyed_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def John_travelled_to_the_office(self):
        self.John.location = "office"
        
    def Daniel_travelled_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def John_travelled_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Mary_travelled_to_the_garden(self):
        self.Mary.location = "garden"
        
    def Mary_dropped_the_milk(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def John_went_back_to_the_garden(self):
        self.John.location = "garden"
        
    def Sandra_got_the_milk_there(self):
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Sandra_put_down_the_milk(self):
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Mary_went_back_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        
    def Mary_travelled_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def John_got_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Daniel_went_back_to_the_office(self):
        self.Daniel.location = "office"
        
    def Daniel_moved_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def Daniel_grabbed_the_apple_there(self):
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        
    def John_left_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Daniel_discarded_the_apple(self):
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def John_picked_up_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Daniel_went_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def Where_is_the_apple(self):
        print(self.apple.location)

world = World()
world.story()