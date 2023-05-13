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
        self.Where_is_the_apple()

    def Daniel_moved_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        for item in self.Daniel.inventory:
            item.location = "kitchen"
        
    def John_grabbed_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_left_the_football_there(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Mary_journeyed_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def John_grabbed_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def John_travelled_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Mary_journeyed_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Sandra_went_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Daniel_went_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def Daniel_picked_up_the_apple_there(self):
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        
    def Sandra_travelled_to_the_garden(self):
        self.Sandra.location = "garden"
        for item in self.Sandra.inventory:
            item.location = "garden"
        
    def Daniel_dropped_the_apple_there(self):
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Where_is_the_apple(self):
        print(self.apple.location)
 

world = World()
world.story()