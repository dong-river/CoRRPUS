## John went to the hallway.
## John went back to the bathroom.
## John grabbed the milk there.
## Sandra went back to the office.
## Sandra journeyed to the kitchen.
## Sandra got the apple there.
## Sandra dropped the apple there.
## John dropped the milk.
## Mary went back to the garden.
## Sandra journeyed to the hallway.
## Sandra got the football there.
## Mary moved to the kitchen.
## 
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
        self.milk = object("milk")
        self.apple = object("apple")
        self.football = object("football")
        self.milk.location = "hallway"
        self.apple.location = "kitchen"
        self.football.location = "hallway"

    def story(self):
        self.John_went_to_the_hallway()
        self.John_went_back_to_the_bathroom()
        self.John_grabbed_the_milk_there()
        self.Sandra_went_back_to_the_office()
        self.Sandra_journeyed_to_the_kitchen()
        self.Sandra_got_the_apple_there()
        self.Sandra_dropped_the_apple_there()
        self.John_dropped_the_milk()
        self.Mary_went_back_to_the_garden()
        self.Sandra_journeyed_to_the_hallway()
        self.Sandra_got_the_football_there()
        self.Mary_moved_to_the_kitchen()
        self.Where_is_the_milk()
        
    def John_went_to_the_hallway(self):
        self.John.location = "hallway"
        
    def John_went_back_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def John_grabbed_the_milk_there(self):
        self.milk.location = "bathroom"
        self.milk.carrier = self.John
        self.John.inventory.append(self.milk)
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        
    def Sandra_journeyed_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        
    def Sandra_got_the_apple_there(self):
        self.apple.location = "kitchen"
        self.apple.carrier = self.Sandra
        self.Sandra.inventory.append(self.apple)
        
    def Sandra_dropped_the_apple_there(self):
        self.apple.location = "kitchen"
        self.apple.carrier = None
        self.Sandra.inventory.remove(self.apple)
        
    def John_dropped_the_milk(self):
        self.milk.location = "bathroom"
        self.milk.carrier = None
        self.John.inventory.remove(self.milk)
        
    def Mary_went_back_to_the_garden(self):
        self.Mary.location = "garden"
        
    def Sandra_journeyed_to_the_hallway(self):
        self.Sandra.location = "hallway"
        
    def Sandra_got_the_football_there(self):
        self.football.location = "hallway"
        self.football.carrier = self.Sandra
        self.Sandra.inventory.append(self.football)
        
    def Mary_moved_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()