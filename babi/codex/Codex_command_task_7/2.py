## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the bathroom.
## John got the football there.
## Mary journeyed to the bathroom.
## Mary gave the milk to Sandra.
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
        self.Mary_got_the_milk_there()
        self.John_moved_to_the_bedroom()
        self.Sandra_went_back_to_the_bathroom()
        self.John_got_the_football_there()
        self.Mary_journeyed_to_the_bathroom()
        self.Mary_gave_the_milk_to_Sandra()
        self.How_many_objects_is_Mary_carrying()

    def Mary_got_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def John_moved_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def Sandra_went_back_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def John_got_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Mary_journeyed_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Mary_gave_the_milk_to_Sandra(self):
        self.Mary.inventory.remove(self.milk)
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def How_many_objects_is_Mary_carrying(self):
        print(len(self.Mary.inventory))

world = World()
world.story()