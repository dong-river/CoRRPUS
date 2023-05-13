## John went to the hallway.
## John went back to the bathroom.
## John grabbed the milk there.
## Sandra went back to the office.
## Sandra journeyed to the kitchen.
## Sandra got the apple there.
## Sandra dropped the apple there.
## John dropped the milk.
## Mary went back to the garden.
## Sandra journeyed to the hallway.
## Sandra got the football there.
## Mary moved to the kitchen.
## Sandra journeyed to the bedroom.
## Mary grabbed the apple there.
## Sandra went back to the office.
## Mary discarded the apple.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        self.John_went_to_the_hallway()
        self.John_went_back_to_the_bathroom()
        self.John_grabbed_the_milk_there()
        self.Sandra_went_back_to_the_office()
        self.Sandra_journeyed_to_the_kitchen()
        self.Sandra_got_the_apple_there()
        self.Sandra_dropped_the_apple_there()
        self.John_dropped_the_milk()
        self.Mary_went_back_to_the_garden()
        self.Sandra_journeyed_to_the_hallway()
        self.Sandra_got_the_football_there()
        self.Mary_moved_to_the_kitchen()
        self.Sandra_journeyed_to_the_bedroom()
        self.Mary_grabbed_the_apple_there()
        self.Sandra_went_back_to_the_office()
        self.Mary_discarded_the_apple()
        self.Where_is_the_apple()

    def John_went_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def John_went_back_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def John_grabbed_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Sandra_journeyed_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Sandra_got_the_apple_there(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def Sandra_dropped_the_apple_there(self):
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def John_dropped_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Mary_went_back_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def Sandra_journeyed_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def Sandra_got_the_football_there(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def Mary_moved_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Mary_grabbed_the_apple_there(self):
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Mary_discarded_the_apple(self):
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Where_is_the_apple(self):
        print(self.apple.location)

world = World()
world.story()