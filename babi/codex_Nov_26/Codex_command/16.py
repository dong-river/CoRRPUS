## Daniel journeyed to the office.
## John took the football there.
## John discarded the football.
## John travelled to the garden.
## Daniel travelled to the garden.
## Sandra went to the garden.
## Daniel travelled to the kitchen.
## Daniel moved to the office.
## Mary grabbed the milk there.
## Daniel journeyed to the bedroom.
## John travelled to the office.
## Daniel travelled to the bathroom.
## John travelled to the kitchen.
## Mary travelled to the garden.
## Mary dropped the milk.
## John went back to the garden.
## Sandra got the milk there.
## Sandra put down the milk.
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
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        self.Daniel_journeyed_to_the_office()
        self.John_took_the_football_there()
        self.John_discarded_the_football()
        self.John_travelled_to_the_garden()
        self.Daniel_travelled_to_the_garden()
        self.Sandra_went_to_the_garden()
        self.Daniel_travelled_to_the_kitchen()
        self.Daniel_moved_to_the_office()
        self.Mary_grabbed_the_milk_there()
        self.Daniel_journeyed_to_the_bedroom()
        self.John_travelled_to_the_office()
        self.Daniel_travelled_to_the_bathroom()
        self.John_travelled_to_the_kitchen()
        self.Mary_travelled_to_the_garden()
        self.Mary_dropped_the_milk()
        self.John_went_back_to_the_garden()
        self.Sandra_got_the_milk_there()
        self.Sandra_put_down_the_milk()
        self.Where_is_the_milk()

    def Daniel_journeyed_to_the_office(self):
        self.Daniel.location = "office"
        
    def John_took_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_discarded_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def John_travelled_to_the_garden(self):
        self.John.location = "garden"
        
    def Daniel_travelled_to_the_garden(self):
        self.Daniel.location = "garden"
        
    def Sandra_went_to_the_garden(self):
        self.Sandra.location = "garden"
        
    def Daniel_travelled_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def Daniel_moved_to_the_office(self):
        self.Daniel.location = "office"
        
    def Mary_grabbed_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def Daniel_journeyed_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def John_travelled_to_the_office(self):
        self.John.location = "office"
        
    def Daniel_travelled_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def John_travelled_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Mary_travelled_to_the_garden(self):
        self.Mary.location = "garden"
        
    def Mary_dropped_the_milk(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def John_went_back_to_the_garden(self):
        self.John.location = "garden"
        
    def Sandra_got_the_milk_there(self):
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Sandra_put_down_the_milk(self):
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()