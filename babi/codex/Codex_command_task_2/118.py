## John grabbed the football there.
## John journeyed to the office.
## John went back to the garden.
## John went to the hallway.
## John dropped the football.
## John grabbed the football there.
## Sandra travelled to the bathroom.
## Sandra picked up the milk there.
## Sandra went to the office.
## John moved to the bathroom.
## John grabbed the apple there.
## Sandra travelled to the bedroom.
## Where is the milk? 

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
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        self.John_grabbed_the_football_there()
        self.John_journeyed_to_the_office()
        self.John_went_back_to_the_garden()
        self.John_went_to_the_hallway()
        self.John_dropped_the_football()
        self.John_grabbed_the_football_there()
        self.Sandra_travelled_to_the_bathroom()
        self.Sandra_picked_up_the_milk_there()
        self.Sandra_went_to_the_office()
        self.John_moved_to_the_bathroom()
        self.John_grabbed_the_apple_there()
        self.Sandra_travelled_to_the_bedroom()
        self.Where_is_the_milk() 
        
    def John_grabbed_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_journeyed_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def John_went_back_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def John_went_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def John_dropped_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def John_grabbed_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Sandra_travelled_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def Sandra_picked_up_the_milk_there(self):
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Sandra_went_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def John_moved_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def John_grabbed_the_apple_there(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def Sandra_travelled_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()