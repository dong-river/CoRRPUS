## Mary went to the garden.
## John picked up the milk there.
## Mary journeyed to the bedroom.
## Sandra went back to the hallway.
## John discarded the milk.
## John journeyed to the bedroom.
## John got the football there.
## John moved to the bathroom.
## Sandra went to the office.
## Daniel went back to the hallway.
## John put down the football.
## Mary journeyed to the kitchen.
## Mary picked up the milk there.
## Mary moved to the hallway.
## John went to the garden.
## Mary discarded the milk.
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
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        self.Mary_went_to_the_garden()
        self.John_picked_up_the_milk_there()
        self.Mary_journeyed_to_the_bedroom()
        self.Sandra_went_back_to_the_hallway()
        self.John_discarded_the_milk()
        self.John_journeyed_to_the_bedroom()
        self.John_got_the_football_there()
        self.John_moved_to_the_bathroom()
        self.Sandra_went_to_the_office()
        self.Daniel_went_back_to_the_hallway()
        self.John_put_down_the_football()
        self.Mary_journeyed_to_the_kitchen()
        self.Mary_picked_up_the_milk_there()
        self.Mary_moved_to_the_hallway()
        self.John_went_to_the_garden()
        self.Mary_discarded_the_milk()
        self.Where_is_the_milk()

    def Mary_went_to_the_garden(self):
        self.Mary.location = "garden"
        
    def John_picked_up_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        self.milk.location = "John's inventory"
        
    def Mary_journeyed_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def Sandra_went_back_to_the_hallway(self):
        self.Sandra.location = "hallway"
        
    def John_discarded_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "garden"
        
    def John_journeyed_to_the_bedroom(self):
        self.John.location = "bedroom"
        
    def John_got_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        self.football.location = "John's inventory"
        
    def John_moved_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def Sandra_went_to_the_office(self):
        self.Sandra.location = "office"
        
    def Daniel_went_back_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def John_put_down_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "bathroom"
        
    def Mary_journeyed_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        
    def Mary_picked_up_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        self.milk.location = "Mary's inventory"
        
    def Mary_moved_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def John_went_to_the_garden(self):
        self.John.location = "garden"
        
    def Mary_discarded_the_milk(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "hallway"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()