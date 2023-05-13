## John travelled to the bathroom.
## John travelled to the hallway.
## Mary picked up the milk there.
## Mary went back to the bedroom.
## Sandra took the football there.
## Sandra moved to the office.
## Sandra went back to the bathroom.
## John journeyed to the bedroom.
## John went back to the bathroom.
## Sandra put down the football.
## Mary discarded the milk.
## Sandra moved to the kitchen.
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
        self.football = object("football")

    def story(self):
        self.John_travelled_to_the_bathroom()
        self.John_travelled_to_the_hallway()
        self.Mary_picked_up_the_milk_there()
        self.Mary_went_back_to_the_bedroom()
        self.Sandra_took_the_football_there()
        self.Sandra_moved_to_the_office()
        self.Sandra_went_back_to_the_bathroom()
        self.John_journeyed_to_the_bedroom()
        self.John_went_back_to_the_bathroom()
        self.Sandra_put_down_the_football()
        self.Mary_discarded_the_milk()
        self.Sandra_moved_to_the_kitchen()
        self.Where_is_the_milk()

    def John_travelled_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def John_travelled_to_the_hallway(self):
        self.John.location = "hallway"
        
    def Mary_picked_up_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        self.milk.location = "bedroom"
        
    def Mary_went_back_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def Sandra_took_the_football_there(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        self.football.location = "office"
        
    def Sandra_moved_to_the_office(self):
        self.Sandra.location = "office"
        
    def Sandra_went_back_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        
    def John_journeyed_to_the_bedroom(self):
        self.John.location = "bedroom"
        
    def John_went_back_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def Sandra_put_down_the_football(self):
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "bathroom"
        
    def Mary_discarded_the_milk(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "bedroom"
        
    def Sandra_moved_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()