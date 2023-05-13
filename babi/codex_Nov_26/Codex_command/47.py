## John travelled to the bathroom.
## John travelled to the hallway.
## Mary picked up the milk there.
## Mary went back to the bedroom.
## Sandra took the football there.
## Sandra moved to the office.
## Sandra went back to the bathroom.
## John journeyed to the bedroom.
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
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        self.John_travelled_to_the_bathroom()
        self.John_travelled_to_the_hallway()
        self.Mary_picked_up_the_milk_there()
        self.Mary_went_back_to_the_bedroom()
        self.Sandra_took_the_football_there()
        self.Sandra_moved_to_the_office()
        self.Sandra_went_back_to_the_bathroom()
        self.John_journeyed_to_the_bedroom()
        self.Where_is_the_football()

    def John_travelled_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def John_travelled_to_the_hallway(self):
        self.John.location = "hallway"
        
    def Mary_picked_up_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def Mary_went_back_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def Sandra_took_the_football_there(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def Sandra_moved_to_the_office(self):
        self.Sandra.location = "office"
        
    def Sandra_went_back_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        
    def John_journeyed_to_the_bedroom(self):
        self.John.location = "bedroom"
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()