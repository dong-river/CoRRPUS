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
        self.Where_is_the_football()

    def Daniel_moved_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Daniel_went_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def John_moved_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Mary_travelled_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Sandra_travelled_to_the_garden(self):
        self.Sandra.location = "garden"
        for item in self.Sandra.inventory:
            item.location = "garden"
        
    def Daniel_journeyed_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Sandra_travelled_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def John_got_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_moved_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def Sandra_travelled_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def Daniel_moved_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Daniel_travelled_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        for item in self.Daniel.inventory:
            item.location = "kitchen"
        
    def Where_is_the_football(self):
        print(self.football.location)
world = World()
world.story()