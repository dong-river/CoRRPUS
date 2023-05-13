## Mary went back to the kitchen.
## Mary travelled to the hallway.
## John journeyed to the bedroom.
## John moved to the garden.
## Daniel went to the hallway.
## John moved to the hallway.
## Daniel journeyed to the bathroom.
## Mary travelled to the garden.
## Daniel went to the hallway.
## John travelled to the office.
## John travelled to the bedroom.
## Mary journeyed to the bedroom.
## John picked up the football there.
## John dropped the football.
## Sandra travelled to the office.
## Mary travelled to the hallway.
## Sandra grabbed the apple there.
## John grabbed the football there.
## Mary went back to the bathroom.
## John discarded the football.
## John picked up the football there.
## Daniel went to the office.
## Sandra discarded the apple.
## Sandra grabbed the apple there.
## John put down the football.
## Daniel moved to the garden.
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
        self.apple = object("apple")

    def story(self):
        self.Mary_went_back_to_the_kitchen()
        self.Mary_travelled_to_the_hallway()
        self.John_journeyed_to_the_bedroom()
        self.John_moved_to_the_garden()
        self.Daniel_went_to_the_hallway()
        self.John_moved_to_the_hallway()
        self.Daniel_journeyed_to_the_bathroom()
        self.Mary_travelled_to_the_garden()
        self.Daniel_went_to_the_hallway()
        self.John_travelled_to_the_office()
        self.John_travelled_to_the_bedroom()
        self.Mary_journeyed_to_the_bedroom()
        self.John_picked_up_the_football_there()
        self.John_dropped_the_football()
        self.Sandra_travelled_to_the_office()
        self.Mary_travelled_to_the_hallway()
        self.Sandra_grabbed_the_apple_there()
        self.John_grabbed_the_football_there()
        self.Mary_went_back_to_the_bathroom()
        self.John_discarded_the_football()
        self.John_picked_up_the_football_there()
        self.Daniel_went_to_the_office()
        self.Sandra_discarded_the_apple()
        self.Sandra_grabbed_the_apple_there()
        self.John_put_down_the_football()
        self.Daniel_moved_to_the_garden()
        self.Where_is_the_football() 
        
    def Mary_went_back_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Mary_travelled_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def John_journeyed_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def John_moved_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Daniel_went_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def John_moved_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def Daniel_journeyed_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def Mary_travelled_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def Daniel_went_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def John_travelled_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def John_travelled_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def Mary_journeyed_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def John_picked_up_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_dropped_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Sandra_travelled_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Mary_travelled_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def Sandra_grabbed_the_apple_there(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def John_grabbed_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Mary_went_back_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def John_discarded_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def John_picked_up_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Daniel_went_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def Sandra_discarded_the_apple(self):
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Sandra_grabbed_the_apple_there(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def John_put_down_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Daniel_moved_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()