## Daniel took the milk there.
## John journeyed to the garden.
## Daniel went back to the hallway.
## Daniel journeyed to the bathroom.
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
        self.Daniel_took_the_milk_there()
        self.John_journeyed_to_the_garden()
        self.Daniel_went_back_to_the_hallway()
        self.Daniel_journeyed_to_the_bathroom()
        self.Where_is_the_milk()

    def Daniel_took_the_milk_there(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        self.Daniel.location = "kitchen"
        
    def John_journeyed_to_the_garden(self):
        self.John.location = "garden"
        
    def Daniel_went_back_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def Daniel_journeyed_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def Where_is_the_milk(self):
        print(self.milk.location)
        

world = World()
world.story()