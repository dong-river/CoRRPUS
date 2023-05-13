## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the bathroom.
## John got the football there.
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
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        self.Mary_got_the_milk_there()
        self.John_moved_to_the_bedroom()
        self.Sandra_went_back_to_the_bathroom()
        self.John_got_the_football_there()
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
        
    def How_many_objects_is_Mary_carrying(self):
        print(len(self.Mary.inventory))

world = World()
world.story()