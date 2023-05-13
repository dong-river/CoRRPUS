## Sandra grabbed the football there.
## Sandra put down the football.
## John grabbed the apple there.
## Sandra went to the hallway.
## John journeyed to the hallway.
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
        self.football = object("football")
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        self.Sandra_grabbed_the_football_there()
        self.Sandra_put_down_the_football()
        self.John_grabbed_the_apple_there()
        self.Sandra_went_to_the_hallway()
        self.John_journeyed_to_the_hallway()
        self.Mary_grabbed_the_milk_there()
        self.Where_is_the_apple()

    def Sandra_grabbed_the_football_there(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def Sandra_put_down_the_football(self):
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        
    def John_grabbed_the_apple_there(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def Sandra_went_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def John_journeyed_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def Mary_grabbed_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def Where_is_the_apple(self):
        print(self.apple.location)

world = World()
world.story()