## Mary went to the garden.
## John picked up the milk there.
## Mary journeyed to the bedroom.
## Sandra went back to the hallway.
## John discarded the milk.
## John journeyed to the bedroom.
## John got the football there.
## John moved to the bathroom.
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
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        self.Mary_went_to_the_garden()
        self.John_picked_up_the_milk_there()
        self.Mary_journeyed_to_the_bedroom()
        self.Sandra_went_back_to_the_hallway()
        self.John_discarded_the_milk()
        self.John_journeyed_to_the_bedroom()
        self.John_got_the_football_there()
        self.John_moved_to_the_bathroom()
        self.Where_is_the_football()

    def Mary_went_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def John_picked_up_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Mary_journeyed_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Sandra_went_back_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def John_discarded_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def John_journeyed_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def John_got_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_moved_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()