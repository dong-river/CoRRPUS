## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the kitchen.
## Mary travelled to the hallway.
## John got the football there.
## John went to the hallway.
## John put down the football.
## Mary went to the garden.
## John went to the kitchen.
## Sandra travelled to the hallway.
## Daniel went to the hallway.
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
        self.Mary_got_the_milk_there()
        self.John_moved_to_the_bedroom()
        self.Sandra_went_back_to_the_kitchen()
        self.Mary_travelled_to_the_hallway()
        self.John_got_the_football_there()
        self.John_went_to_the_hallway()
        self.John_put_down_the_football()
        self.Mary_went_to_the_garden()
        self.John_went_to_the_kitchen()
        self.Sandra_travelled_to_the_hallway()
        self.Daniel_went_to_the_hallway()
        self.Mary_discarded_the_milk()
        self.Where_is_the_milk()

    def Mary_got_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def John_moved_to_the_bedroom(self):
        self.John.location = "bedroom"
        
    def Sandra_went_back_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        
    def Mary_travelled_to_the_hallway(self):
        self.Mary.location = "hallway"
        self.milk.location = "hallway"
        
    def John_got_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_went_to_the_hallway(self):
        self.John.location = "hallway"
        self.football.location = "hallway"
        
    def John_put_down_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Mary_went_to_the_garden(self):
        self.Mary.location = "garden"
        self.milk.location = "garden"
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        self.football.location = "kitchen"
        
    def Sandra_travelled_to_the_hallway(self):
        self.Sandra.location = "hallway"
        
    def Daniel_went_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def Mary_discarded_the_milk(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()