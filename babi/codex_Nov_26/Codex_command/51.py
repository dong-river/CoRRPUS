## Daniel took the milk there.
## John journeyed to the garden.
## Daniel went back to the hallway.
## Daniel journeyed to the bathroom.
## Daniel dropped the milk.
## Daniel took the milk there.
## John grabbed the apple there.
## Sandra journeyed to the kitchen.
## John went to the hallway.
## Sandra went back to the garden.
## 
## Where is the apple? 

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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        self.Daniel_took_the_milk_there()
        self.John_journeyed_to_the_garden()
        self.Daniel_went_back_to_the_hallway()
        self.Daniel_journeyed_to_the_bathroom()
        self.Daniel_dropped_the_milk()
        self.Daniel_took_the_milk_there()
        self.John_grabbed_the_apple_there()
        self.Sandra_journeyed_to_the_kitchen()
        self.John_went_to_the_hallway()
        self.Sandra_went_back_to_the_garden()
        self.Where_is_the_apple()
        
    def Daniel_took_the_milk_there(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def John_journeyed_to_the_garden(self):
        self.John.location = "garden"
        
    def Daniel_went_back_to_the_hallway(self):
        self.Daniel.location = "hallway"
        self.milk.location = "hallway"
        
    def Daniel_journeyed_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def Daniel_dropped_the_milk(self):
        self.Daniel.inventory.remove(self.milk)
        self.milk.location = "bathroom"
        
    def Daniel_took_the_milk_there(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def John_grabbed_the_apple_there(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def Sandra_journeyed_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        
    def John_went_to_the_hallway(self):
        self.John.location = "hallway"
        self.apple.location = "hallway"
        
    def Sandra_went_back_to_the_garden(self):
        self.Sandra.location = "garden"
        
    def Where_is_the_apple(self):
        print(self.apple.location)

world = World()
world.story()