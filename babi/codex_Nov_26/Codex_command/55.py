## John went to the bathroom.
## Daniel travelled to the kitchen.
## John journeyed to the kitchen.
## Daniel journeyed to the hallway.
## Sandra travelled to the kitchen.
## Mary moved to the office.
## Daniel went back to the office.
## Sandra went back to the bathroom.
## John grabbed the milk there.
## John grabbed the apple there.
## Sandra journeyed to the office.
## Mary went to the hallway.
## John went to the bathroom.
## John discarded the apple.
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
        self.John = character("John")
        self.Daniel = character("Daniel")
        self.Sandra = character("Sandra")
        self.Mary = character("Mary")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        self.John_went_to_the_bathroom()
        self.Daniel_travelled_to_the_kitchen()
        self.John_journeyed_to_the_kitchen()
        self.Daniel_journeyed_to_the_hallway()
        self.Sandra_travelled_to_the_kitchen()
        self.Mary_moved_to_the_office()
        self.Daniel_went_back_to_the_office()
        self.Sandra_went_back_to_the_bathroom()
        self.John_grabbed_the_milk_there()
        self.John_grabbed_the_apple_there()
        self.Sandra_journeyed_to_the_office()
        self.Mary_went_to_the_hallway()
        self.John_went_to_the_bathroom()
        self.John_discarded_the_apple()
        self.Where_is_the_apple()

    def John_went_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def Daniel_travelled_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def John_journeyed_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Daniel_journeyed_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def Sandra_travelled_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        
    def Mary_moved_to_the_office(self):
        self.Mary.location = "office"
        
    def Daniel_went_back_to_the_office(self):
        self.Daniel.location = "office"
        
    def Sandra_went_back_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        
    def John_grabbed_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def John_grabbed_the_apple_there(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def Sandra_journeyed_to_the_office(self):
        self.Sandra.location = "office"
        
    def Mary_went_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def John_went_to_the_bathroom(self):
        self.John.location = "bathroom"
        
    def John_discarded_the_apple(self):
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Where_is_the_apple(self):
        print(self.apple.location)

world = World()
world.story()