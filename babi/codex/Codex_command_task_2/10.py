## Mary picked up the apple there.
## Mary dropped the apple.
## Daniel went back to the garden.
## Mary journeyed to the office.
## John got the football there.
## Mary went back to the kitchen.
## Daniel picked up the milk there.
## John travelled to the bedroom.
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
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        self.Mary_picked_up_the_apple_there()
        self.Mary_dropped_the_apple()
        self.Daniel_went_back_to_the_garden()
        self.Mary_journeyed_to_the_office()
        self.John_got_the_football_there()
        self.Mary_went_back_to_the_kitchen()
        self.Daniel_picked_up_the_milk_there()
        self.John_travelled_to_the_bedroom()
        self.Where_is_the_football()

    def Mary_picked_up_the_apple_there(self):
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        
    def Mary_dropped_the_apple(self):
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Daniel_went_back_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Mary_journeyed_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def John_got_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Mary_went_back_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Daniel_picked_up_the_milk_there(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def John_travelled_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()