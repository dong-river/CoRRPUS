## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the kitchen.
## Mary travelled to the hallway.
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

    def story(self):
        self.Mary_got_the_milk_there()
        self.John_moved_to_the_bedroom()
        self.Sandra_went_back_to_the_kitchen()
        self.Mary_travelled_to_the_hallway()
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
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()