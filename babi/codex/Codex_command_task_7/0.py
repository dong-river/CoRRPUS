## Mary got the milk there.
## John moved to the bedroom.
## How many objects is Mary carrying? 

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
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        self.Mary_moved_to_the_bathroom()
        self.Sandra_journeyed_to_the_bedroom()
        self.Mary_got_the_football_there()
        self.John_went_to_the_kitchen()
        self.Mary_went_back_to_the_garden()
        self.Where_is_the_football()
        self.Mary_got_the_milk_there()
        self.John_moved_to_the_bedroom()
        self.How_many_objects_is_Mary_carrying()

    def Mary_moved_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Mary_got_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def Mary_went_back_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def Where_is_the_football(self):
        print(self.football.location)
        
    def Mary_got_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def John_moved_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def How_many_objects_is_Mary_carrying(self):
        print(len(self.Mary.inventory))

world = World()
world.story()