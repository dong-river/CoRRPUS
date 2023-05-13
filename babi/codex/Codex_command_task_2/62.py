## Daniel moved to the office.
## Daniel travelled to the bedroom.
## John took the milk there.
## John travelled to the garden.
## Sandra moved to the office.
## Daniel went back to the office.
## John went to the kitchen.
## Mary travelled to the garden.
## John picked up the football there.
## John dropped the football.
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
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        self.Daniel_moved_to_the_office()
        self.Daniel_travelled_to_the_bedroom()
        self.John_took_the_milk_there()
        self.John_travelled_to_the_garden()
        self.Sandra_moved_to_the_office()
        self.Daniel_went_back_to_the_office()
        self.John_went_to_the_kitchen()
        self.Mary_travelled_to_the_garden()
        self.John_picked_up_the_football_there()
        self.John_dropped_the_football()
        self.Where_is_the_football()

    def Daniel_moved_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def Daniel_travelled_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def John_took_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def John_travelled_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Sandra_moved_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Daniel_went_back_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Mary_travelled_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def John_picked_up_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_dropped_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()