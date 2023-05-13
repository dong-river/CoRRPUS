## Sandra journeyed to the garden.
## Sandra travelled to the bathroom.
## Daniel went back to the garden.
## Sandra got the apple there.
## Mary travelled to the bedroom.
## John went to the hallway.
## Sandra travelled to the office.
## Mary grabbed the milk there.
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
        self.Daniel = character("Daniel")
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        self.Sandra_journeyed_to_the_garden()
        self.Sandra_travelled_to_the_bathroom()
        self.Daniel_went_back_to_the_garden()
        self.Sandra_got_the_apple_there()
        self.Mary_travelled_to_the_bedroom()
        self.John_went_to_the_hallway()
        self.Sandra_travelled_to_the_office()
        self.Mary_grabbed_the_milk_there()
        self.Where_is_the_apple()

    def Sandra_journeyed_to_the_garden(self):
        self.Sandra.location = "garden"
        for item in self.Sandra.inventory:
            item.location = "garden"
        
    def Sandra_travelled_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def Daniel_went_back_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Sandra_got_the_apple_there(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def Mary_travelled_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def John_went_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def Sandra_travelled_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Mary_grabbed_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def Where_is_the_apple(self):
        print(self.apple.location)
 

world = World()
world.story()