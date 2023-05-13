## John went to the hallway.
## John went back to the bathroom.
## John grabbed the milk there.
## Sandra went back to the office.
## Sandra journeyed to the kitchen.
## Sandra got the apple there.
## Sandra dropped the apple there.
## John dropped the milk.
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
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")
        self.office = "office"
        self.hallway = "hallway"
        self.bathroom = "bathroom"
        self.kitchen = "kitchen"

    def story(self):
        self.John_went_to_the_hallway()
        self.John_went_back_to_the_bathroom()
        self.John_grabbed_the_milk_there()
        self.Sandra_went_back_to_the_office()
        self.Sandra_journeyed_to_the_kitchen()
        self.Sandra_got_the_apple_there()
        self.Sandra_dropped_the_apple_there()
        self.John_dropped_the_milk()
        self.Where_is_the_milk()

    def John_went_to_the_hallway(self):
        self.John.location = self.hallway
        
    def John_went_back_to_the_bathroom(self):
        self.John.location = self.bathroom
        
    def John_grabbed_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = self.office
        
    def Sandra_journeyed_to_the_kitchen(self):
        self.Sandra.location = self.kitchen
        
    def Sandra_got_the_apple_there(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def Sandra_dropped_the_apple_there(self):
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.kitchen
        
    def John_dropped_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = self.John.location
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()