## Daniel journeyed to the hallway.
## Daniel journeyed to the garden.
## Mary went back to the kitchen.
## Daniel went back to the office.
## Mary journeyed to the bathroom.
## John moved to the hallway.
## Daniel grabbed the football there.
## Daniel went to the kitchen.
## Daniel discarded the football.
## John went to the bathroom.
## Daniel took the football there.
## John travelled to the kitchen.
## Mary travelled to the office.
## John travelled to the hallway.
## John went back to the office.
## Daniel journeyed to the bedroom.
## Daniel got the milk there.
## Daniel discarded the milk.
## Sandra went to the bathroom.
## Mary went back to the bedroom.
## Daniel took the apple there.
## Daniel dropped the football.
## 
## Where is the football? 

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
        self.Daniel_journeyed_to_the_hallway()
        self.Daniel_journeyed_to_the_garden()
        self.Mary_went_back_to_the_kitchen()
        self.Daniel_went_back_to_the_office()
        self.Mary_journeyed_to_the_bathroom()
        self.John_moved_to_the_hallway()
        self.Daniel_grabbed_the_football_there()
        self.Daniel_went_to_the_kitchen()
        self.Daniel_discarded_the_football()
        self.John_went_to_the_bathroom()
        self.Daniel_took_the_football_there()
        self.John_travelled_to_the_kitchen()
        self.Mary_travelled_to_the_office()
        self.John_travelled_to_the_hallway()
        self.John_went_back_to_the_office()
        self.Daniel_journeyed_to_the_bedroom()
        self.Daniel_got_the_milk_there()
        self.Daniel_discarded_the_milk()
        self.Sandra_went_to_the_bathroom()
        self.Mary_went_back_to_the_bedroom()
        self.Daniel_took_the_apple_there()
        self.Daniel_dropped_the_football()
        
        self.Where_is_the_football()

    def Daniel_journeyed_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def Daniel_journeyed_to_the_garden(self):
        self.Daniel.location = "garden"
        
    def Mary_went_back_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        
    def Daniel_went_back_to_the_office(self):
        self.Daniel.location = "office"
        
    def Mary_journeyed_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        
    def John_moved_to_the_hallway(self):
        self.John.location = "hallway"
        
    def Daniel_grabbed_the_football_there(self):
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        
    def Daniel_went_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def Daniel_discarded_the_football(self):
        self.football.location = "kitchen"
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        
    def John_went_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def Daniel_took_the_football_there(self):
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        
    def John_travelled_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Mary_travelled_to_the_office(self):
        self.Mary.location = "office"
        
    def John_travelled_to_the_hallway(self):
        self.John.location = "hallway"
        
    def John_went_back_to_the_office(self):
        self.John.location = "office"
        
    def Daniel_journeyed_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def Daniel_got_the_milk_there(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def Daniel_discarded_the_milk(self):
        self.milk.location = "bedroom"
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Sandra_went_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        
    def Mary_went_back_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def Daniel_took_the_apple_there(self):
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        
    def Daniel_dropped_the_football(self):
        self.football.location = "bedroom"
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()