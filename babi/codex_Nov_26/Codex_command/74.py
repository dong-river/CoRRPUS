## Sandra moved to the garden.
## Daniel took the apple there.
## Daniel dropped the apple.
## Sandra travelled to the office.
## John moved to the kitchen.
## Sandra moved to the garden.
## Daniel went back to the bathroom.
## Mary travelled to the hallway.
## Sandra went to the bathroom.
## John went back to the bedroom.
## Mary moved to the garden.
## John picked up the apple there.
## John went back to the kitchen.
## John went back to the garden.
## Mary went to the office.
## Daniel went to the bedroom.
## John went to the bathroom.
## John dropped the apple.
## Mary journeyed to the bedroom.
## Sandra grabbed the apple there.
## Daniel moved to the kitchen.
## Sandra left the apple.
## John grabbed the apple there.
## Sandra journeyed to the kitchen.
## Sandra journeyed to the bathroom.
## Daniel travelled to the office.
## John put down the apple.
## Mary journeyed to the kitchen.
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
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.Mary = character("Mary")
        self.apple = object("apple")

    def story(self):
        self.Sandra_moved_to_the_garden()
        self.Daniel_took_the_apple_there()
        self.Daniel_dropped_the_apple()
        self.Sandra_travelled_to_the_office()
        self.John_moved_to_the_kitchen()
        self.Sandra_moved_to_the_garden()
        self.Daniel_went_back_to_the_bathroom()
        self.Mary_travelled_to_the_hallway()
        self.Sandra_went_to_the_bathroom()
        self.John_went_back_to_the_bedroom()
        self.Mary_moved_to_the_garden()
        self.John_picked_up_the_apple_there()
        self.John_went_back_to_the_kitchen()
        self.John_went_back_to_the_garden()
        self.Mary_went_to_the_office()
        self.Daniel_went_to_the_bedroom()
        self.John_went_to_the_bathroom()
        self.John_dropped_the_apple()
        self.Mary_journeyed_to_the_bedroom()
        self.Sandra_grabbed_the_apple_there()
        self.Daniel_moved_to_the_kitchen()
        self.Sandra_left_the_apple()
        self.John_grabbed_the_apple_there()
        self.Sandra_journeyed_to_the_kitchen()
        self.Sandra_journeyed_to_the_bathroom()
        self.Daniel_travelled_to_the_office()
        self.John_put_down_the_apple()
        self.Mary_journeyed_to_the_kitchen()

        self.Where_is_the_apple()

    def Sandra_moved_to_the_garden(self):
        self.Sandra.location = "garden"
        
    def Daniel_took_the_apple_there(self):
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        
    def Daniel_dropped_the_apple(self):
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Sandra_travelled_to_the_office(self):
        self.Sandra.location = "office"
        
    def John_moved_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Sandra_moved_to_the_garden(self):
        self.Sandra.location = "garden"
        
    def Daniel_went_back_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def Mary_travelled_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def Sandra_went_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        
    def John_went_back_to_the_bedroom(self):
        self.John.location = "bedroom"
        
    def Mary_moved_to_the_garden(self):
        self.Mary.location = "garden"
        self.apple.location = "garden"
        
    def John_picked_up_the_apple_there(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def John_went_back_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def John_went_back_to_the_garden(self):
        self.John.location = "garden"
        self.apple.location = "garden"
        
    def Mary_went_to_the_office(self):
        self.Mary.location = "office"
        
    def Daniel_went_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def John_went_to_the_bathroom(self):
        self.John.location = "bathroom"
        self.apple.location = "bathroom"
        
    def John_dropped_the_apple(self):
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Mary_journeyed_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def Sandra_grabbed_the_apple_there(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def Daniel_moved_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def Sandra_left_the_apple(self):
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def John_grabbed_the_apple_there(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def Sandra_journeyed_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        
    def Sandra_journeyed_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        
    def Daniel_travelled_to_the_office(self):
        self.Daniel.location = "office"
        
    def John_put_down_the_apple(self):
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Mary_journeyed_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        
    def Where_is_the_apple(self):
        print(self.apple.location)

world = World()
world.story()