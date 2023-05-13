## Daniel moved to the bedroom.
## Daniel went to the bathroom.
## John moved to the garden.
## Mary travelled to the bedroom.
## Sandra travelled to the garden.
## Daniel journeyed to the garden.
## Sandra travelled to the hallway.
## John got the football there.
## John moved to the bathroom.
## Sandra travelled to the bathroom.
## Daniel moved to the bedroom.
## Daniel travelled to the kitchen.
## Mary moved to the hallway.
## Sandra travelled to the office.
## Daniel moved to the hallway.
## Daniel went back to the kitchen.
## John went back to the hallway.
## Daniel went back to the hallway.
## Daniel went to the bedroom.
## John moved to the kitchen.
## Mary moved to the office.
## John went back to the garden.
## Sandra took the apple there.
## Daniel went to the office.
## Mary went back to the kitchen.
## Mary went to the bedroom.
## John journeyed to the bathroom.
## Sandra went back to the hallway.
## Sandra moved to the bedroom.
## Daniel moved to the garden.
## John went back to the bedroom.
## Mary went back to the office.
## John moved to the kitchen.
## John grabbed the milk there.
## Daniel journeyed to the bedroom.
## John discarded the football.
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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.Mary = character("Mary")
        self.Sandra = character("Sandra")
        self.football = object("football")
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        self.Daniel_moved_to_the_bedroom()
        self.Daniel_went_to_the_bathroom()
        self.John_moved_to_the_garden()
        self.Mary_travelled_to_the_bedroom()
        self.Sandra_travelled_to_the_garden()
        self.Daniel_journeyed_to_the_garden()
        self.Sandra_travelled_to_the_hallway()
        self.John_got_the_football_there()
        self.John_moved_to_the_bathroom()
        self.Sandra_travelled_to_the_bathroom()
        self.Daniel_moved_to_the_bedroom()
        self.Daniel_travelled_to_the_kitchen()
        self.Mary_moved_to_the_hallway()
        self.Sandra_travelled_to_the_office()
        self.Daniel_moved_to_the_hallway()
        self.Daniel_went_back_to_the_kitchen()
        self.John_went_back_to_the_hallway()
        self.Daniel_went_back_to_the_hallway()
        self.Daniel_went_to_the_bedroom()
        self.John_moved_to_the_kitchen()
        self.Mary_moved_to_the_office()
        self.John_went_back_to_the_garden()
        self.Sandra_took_the_apple_there()
        self.Daniel_went_to_the_office()
        self.Mary_went_back_to_the_kitchen()
        self.Mary_went_to_the_bedroom()
        self.John_journeyed_to_the_bathroom()
        self.Sandra_went_back_to_the_hallway()
        self.Sandra_moved_to_the_bedroom()
        self.Daniel_moved_to_the_garden()
        self.John_went_back_to_the_bedroom()
        self.Mary_went_back_to_the_office()
        self.John_moved_to_the_kitchen()
        self.John_grabbed_the_milk_there()
        self.Daniel_journeyed_to_the_bedroom()
        self.John_discarded_the_football()
        
    def Daniel_moved_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def Daniel_went_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def John_moved_to_the_garden(self):
        self.John.location = "garden"
        
    def Mary_travelled_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def Sandra_travelled_to_the_garden(self):
        self.Sandra.location = "garden"
        
    def Daniel_journeyed_to_the_garden(self):
        self.Daniel.location = "garden"
        
    def Sandra_travelled_to_the_hallway(self):
        self.Sandra.location = "hallway"
        
    def John_got_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_moved_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def Sandra_travelled_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        
    def Daniel_moved_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def Daniel_travelled_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def Mary_moved_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def Sandra_travelled_to_the_office(self):
        self.Sandra.location = "office"
        
    def Daniel_moved_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def Daniel_went_back_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def John_went_back_to_the_hallway(self):
        self.John.location = "hallway"
        
    def Daniel_went_back_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def Daniel_went_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def John_moved_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Mary_moved_to_the_office(self):
        self.Mary.location = "office"
        
    def John_went_back_to_the_garden(self):
        self.John.location = "garden"
        
    def Sandra_took_the_apple_there(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def Daniel_went_to_the_office(self):
        self.Daniel.location = "office"
        
    def Mary_went_back_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        
    def Mary_went_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def John_journeyed_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def Sandra_went_back_to_the_hallway(self):
        self.Sandra.location = "hallway"
        
    def Sandra_moved_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        
    def Daniel_moved_to_the_garden(self):
        self.Daniel.location = "garden"
        
    def John_went_back_to_the_bedroom(self):
        self.John.location = "bedroom"
        
    def Mary_went_back_to_the_office(self):
        self.Mary.location = "office"
        
    def John_moved_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def John_grabbed_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Daniel_journeyed_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def John_discarded_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "bedroom"
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()