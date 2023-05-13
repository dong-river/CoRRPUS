## Mary moved to the kitchen.
## Mary travelled to the office.
## Daniel grabbed the football there.
## Mary moved to the hallway.
## Sandra moved to the bedroom.
## Mary went back to the bedroom.
## John grabbed the milk there.
## John put down the milk.
## Daniel journeyed to the bathroom.
## Sandra journeyed to the bathroom.
## John got the milk there.
## Mary took the apple there.
## Mary left the apple.
## John journeyed to the bedroom.
## Mary travelled to the office.
## Daniel put down the football.
## John went back to the kitchen.
## Sandra got the football there.
## John travelled to the hallway.
## Sandra discarded the football there.
## John left the milk.
## John grabbed the milk there.
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
        self.Mary_moved_to_the_kitchen()
        self.Mary_travelled_to_the_office()
        self.Daniel_grabbed_the_football_there()
        self.Mary_moved_to_the_hallway()
        self.Sandra_moved_to_the_bedroom()
        self.Mary_went_back_to_the_bedroom()
        self.John_grabbed_the_milk_there()
        self.John_put_down_the_milk()
        self.Daniel_journeyed_to_the_bathroom()
        self.Sandra_journeyed_to_the_bathroom()
        self.John_got_the_milk_there()
        self.Mary_took_the_apple_there()
        self.Mary_left_the_apple()
        self.John_journeyed_to_the_bedroom()
        self.Mary_travelled_to_the_office()
        self.Daniel_put_down_the_football()
        self.John_went_back_to_the_kitchen()
        self.Sandra_got_the_football_there()
        self.John_travelled_to_the_hallway()
        self.Sandra_discarded_the_football_there()
        self.John_left_the_milk()
        self.John_grabbed_the_milk_there()
        
        self.Where_is_the_football()

    def Mary_moved_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        
    def Mary_travelled_to_the_office(self):
        self.Mary.location = "office"
        
    def Daniel_grabbed_the_football_there(self):
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        
    def Mary_moved_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def Sandra_moved_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        
    def Mary_went_back_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def John_grabbed_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def John_put_down_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = self.John.location
        
    def Daniel_journeyed_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def Sandra_journeyed_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        
    def John_got_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        self.milk.location = ""
        
    def Mary_took_the_apple_there(self):
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        
    def Mary_left_the_apple(self):
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        self.apple.location = self.Mary.location
        
    def John_journeyed_to_the_bedroom(self):
        self.John.location = "bedroom"
        
    def Mary_travelled_to_the_office(self):
        self.Mary.location = "office"
        
    def Daniel_put_down_the_football(self):
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.Daniel.location
        
    def John_went_back_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Sandra_got_the_football_there(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        self.football.location = ""
        
    def John_travelled_to_the_hallway(self):
        self.John.location = "hallway"
        
    def Sandra_discarded_the_football_there(self):
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = self.Sandra.location
        
    def John_left_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = self.John.location
        
    def John_grabbed_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        self.milk.location = ""
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()