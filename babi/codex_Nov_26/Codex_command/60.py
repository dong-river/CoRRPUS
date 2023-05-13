## Daniel moved to the office.
## Daniel travelled to the bedroom.
## John took the milk there.
## John travelled to the garden.
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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.milk = object("milk")

    def story(self):
        self.Daniel_moved_to_the_office()
        self.Daniel_travelled_to_the_bedroom()
        self.John_took_the_milk_there()
        self.John_travelled_to_the_garden()
        self.Where_is_the_milk()

    def Daniel_moved_to_the_office(self):
        self.Daniel.location = "office"
        
    def Daniel_travelled_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def John_took_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def John_travelled_to_the_garden(self):
        self.John.location = "garden"
        self.milk.location = "garden"
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()