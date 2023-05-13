## Mary journeyed to the bathroom.
## Sandra went to the garden.
## Daniel went back to the garden.
## Daniel went to the office.
## Sandra grabbed the milk there.
## Sandra put down the milk there.
## Daniel went to the hallway.
## Sandra got the milk there.
## Daniel went to the garden.
## Daniel journeyed to the kitchen.
## Daniel journeyed to the bedroom.
## Mary journeyed to the garden.
## Daniel took the football there.
## Mary moved to the office.
## Sandra travelled to the bedroom.
## Daniel dropped the football.
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
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        self.Mary_journeyed_to_the_bathroom()
        self.Sandra_went_to_the_garden()
        self.Daniel_went_back_to_the_garden()
        self.Daniel_went_to_the_office()
        self.Sandra_grabbed_the_milk_there()
        self.Sandra_put_down_the_milk_there()
        self.Daniel_went_to_the_hallway()
        self.Sandra_got_the_milk_there()
        self.Daniel_went_to_the_garden()
        self.Daniel_journeyed_to_the_kitchen()
        self.Daniel_journeyed_to_the_bedroom()
        self.Mary_journeyed_to_the_garden()
        self.Daniel_took_the_football_there()
        self.Mary_moved_to_the_office()
        self.Sandra_travelled_to_the_bedroom()
        self.Daniel_dropped_the_football()
        
        self.Where_is_the_football()

    def Mary_journeyed_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        
    def Sandra_went_to_the_garden(self):
        self.Sandra.location = "garden"
        
    def Daniel_went_back_to_the_garden(self):
        self.Daniel.location = "garden"
        
    def Daniel_went_to_the_office(self):
        self.Daniel.location = "office"
        
    def Sandra_grabbed_the_milk_there(self):
        self.milk.location = "garden"
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Sandra_put_down_the_milk_there(self):
        self.milk.location = "garden"
        self.milk.carrier = None
        
    def Daniel_went_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def Sandra_got_the_milk_there(self):
        self.milk.location = "hallway"
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Daniel_went_to_the_garden(self):
        self.Daniel.location = "garden"
        
    def Daniel_journeyed_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def Daniel_journeyed_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def Mary_journeyed_to_the_garden(self):
        self.Mary.location = "garden"
        
    def Daniel_took_the_football_there(self):
        self.football.location = "garden"
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        
    def Mary_moved_to_the_office(self):
        self.Mary.location = "office"
        
    def Sandra_travelled_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        
    def Daniel_dropped_the_football(self):
        self.football.location = self.Daniel.location
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()