## John went back to the office.
## Mary went back to the hallway.
## Daniel journeyed to the bedroom.
## Mary went back to the bathroom.
## Sandra went back to the hallway.
## Sandra got the milk there.
## Mary moved to the office.
## Mary went to the hallway.
## Daniel went to the bathroom.
## Sandra went to the office.
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

    def story(self):
        self.John_went_back_to_the_office()
        self.Mary_went_back_to_the_hallway()
        self.Daniel_journeyed_to_the_bedroom()
        self.Mary_went_back_to_the_bathroom()
        self.Sandra_went_back_to_the_hallway()
        self.Sandra_got_the_milk_there()
        self.Mary_moved_to_the_office()
        self.Mary_went_to_the_hallway()
        self.Daniel_went_to_the_bathroom()
        self.Sandra_went_to_the_office()
        self.Where_is_the_milk()

    def John_went_back_to_the_office(self):
        self.John.location = "office"
        
    def Mary_went_back_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def Daniel_journeyed_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def Mary_went_back_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        
    def Sandra_went_back_to_the_hallway(self):
        self.Sandra.location = "hallway"
        
    def Sandra_got_the_milk_there(self):
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Mary_moved_to_the_office(self):
        self.Mary.location = "office"
        
    def Mary_went_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def Daniel_went_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def Sandra_went_to_the_office(self):
        self.Sandra.location = "office"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()