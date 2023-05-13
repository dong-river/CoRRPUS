## Mary picked up the apple there.
## Mary dropped the apple.
## Daniel went back to the garden.
## Mary journeyed to the office.
## John got the football there.
## Mary went back to the kitchen.
## Daniel picked up the milk there.
## John travelled to the bedroom.
## John moved to the hallway.
## John discarded the football.
## Daniel dropped the milk.
## John got the football there.
## Mary journeyed to the garden.
## Daniel travelled to the bathroom.
## Sandra journeyed to the bathroom.
## Mary went to the bathroom.
## Mary took the apple there.
## Mary dropped the apple.
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
        self.apple = object("apple")
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        self.Mary_picked_up_the_apple_there()
        self.Mary_dropped_the_apple()
        self.Daniel_went_back_to_the_garden()
        self.Mary_journeyed_to_the_office()
        self.John_got_the_football_there()
        self.Mary_went_back_to_the_kitchen()
        self.Daniel_picked_up_the_milk_there()
        self.John_travelled_to_the_bedroom()
        self.John_moved_to_the_hallway()
        self.John_discarded_the_football()
        self.Daniel_dropped_the_milk()
        self.John_got_the_football_there()
        self.Mary_journeyed_to_the_garden()
        self.Daniel_travelled_to_the_bathroom()
        self.Sandra_journeyed_to_the_bathroom()
        self.Mary_went_to_the_bathroom()
        self.Mary_took_the_apple_there()
        self.Mary_dropped_the_apple()
        self.Where_is_the_apple()

    def Mary_picked_up_the_apple_there(self):
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        
    def Mary_dropped_the_apple(self):
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Daniel_went_back_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Mary_journeyed_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def John_got_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Mary_went_back_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Daniel_picked_up_the_milk_there(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def John_travelled_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def John_moved_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def John_discarded_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Daniel_dropped_the_milk(self):
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def John_got_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Mary_journeyed_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def Daniel_travelled_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def Sandra_journeyed_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def Mary_went_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Mary_took_the_apple_there(self):
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        
    def Mary_dropped_the_apple(self):
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Where_is_the_apple(self):
        print(self.apple.location)

world = World()
world.story()