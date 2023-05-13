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
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.Daniel.location
        
    def John_went_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def Where_is_the_football(self):
        print(self.football.location)
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John journeyed to the office.
## John journeyed to the bedroom.
## John journeyed to the kitchen.
## John journeyed to the bathroom.
## John journeyed to the hallway.
## John journeyed to the garden.
## John
world = World()
world.story()