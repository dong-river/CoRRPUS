## Sandra journeyed to the garden.
## Sandra travelled to the bathroom.
## Daniel went back to the garden.
## Sandra got the apple there.
## Mary travelled to the bedroom.
## John went to the hallway.
## Sandra travelled to the office.
## Mary grabbed the milk there.
## John went to the kitchen.
## Mary moved to the hallway.
## Sandra discarded the apple.
## Mary left the milk.
## Mary took the milk there.
## Mary left the milk.
## John got the football there.
## John moved to the hallway.
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
        self.Daniel = character("Daniel")
        self.apple = object("apple")
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        self.Sandra_journeyed_to_the_garden()
        self.Sandra_travelled_to_the_bathroom()
        self.Daniel_went_back_to_the_garden()
        self.Sandra_got_the_apple_there()
        self.Mary_travelled_to_the_bedroom()
        self.John_went_to_the_hallway()
        self.Sandra_travelled_to_the_office()
        self.Mary_grabbed_the_milk_there()
        self.John_went_to_the_kitchen()
        self.Mary_moved_to_the_hallway()
        self.Sandra_discarded_the_apple()
        self.Mary_left_the_milk()
        self.Mary_took_the_milk_there()
        self.Mary_left_the_milk()
        self.John_got_the_football_there()
        self.John_moved_to_the_hallway()
        
        self.Where_is_the_milk()

    def Sandra_journeyed_to_the_garden(self):
        self.Sandra.location = "garden"
        
    def Sandra_travelled_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        
    def Daniel_went_back_to_the_garden(self):
        self.Daniel.location = "garden"
        
    def Sandra_got_the_apple_there(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def Mary_travelled_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def John_went_to_the_hallway(self):
        self.John.location = "hallway"
        
    def Sandra_travelled_to_the_office(self):
        self.Sandra.location = "office"
        
    def Mary_grabbed_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Mary_moved_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def Sandra_discarded_the_apple(self):
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.Sandra.location
        
    def Mary_left_the_milk(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = self.Mary.location
        
    def Mary_took_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def John_got_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_moved_to_the_hallway(self):
        self.John.location = "hallway"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()