## Daniel took the milk there.
## John journeyed to the garden.
## Daniel went back to the hallway.
## Daniel journeyed to the bathroom.
## Daniel dropped the milk.
## Daniel took the milk there.
## John grabbed the apple there.
## Sandra journeyed to the kitchen.
## John went to the hallway.
## Sandra went back to the garden.
## Daniel journeyed to the kitchen.
## Sandra journeyed to the bedroom.
## Daniel went back to the hallway.
## Sandra went back to the kitchen.
## Sandra went back to the bathroom.
## John went to the kitchen.
## Sandra got the football there.
## Sandra went to the kitchen.
## Daniel left the milk.
## Sandra put down the football.
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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.milk = object("milk")
        self.apple = object("apple")
        self.football = object("football")

    def story(self):
        self.Daniel_took_the_milk_there()
        self.John_journeyed_to_the_garden()
        self.Daniel_went_back_to_the_hallway()
        self.Daniel_journeyed_to_the_bathroom()
        self.Daniel_dropped_the_milk()
        self.Daniel_took_the_milk_there()
        self.John_grabbed_the_apple_there()
        self.Sandra_journeyed_to_the_kitchen()
        self.John_went_to_the_hallway()
        self.Sandra_went_back_to_the_garden()
        self.Daniel_journeyed_to_the_kitchen()
        self.Sandra_journeyed_to_the_bedroom()
        self.Daniel_went_back_to_the_hallway()
        self.Sandra_went_back_to_the_kitchen()
        self.Sandra_went_back_to_the_bathroom()
        self.John_went_to_the_kitchen()
        self.Sandra_got_the_football_there()
        self.Sandra_went_to_the_kitchen()
        self.Daniel_left_the_milk()
        self.Sandra_put_down_the_football()
        self.Where_is_the_football()

    def Daniel_took_the_milk_there(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def John_journeyed_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Daniel_went_back_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def Daniel_journeyed_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def Daniel_dropped_the_milk(self):
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Daniel_took_the_milk_there(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def John_grabbed_the_apple_there(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def Sandra_journeyed_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def John_went_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def Sandra_went_back_to_the_garden(self):
        self.Sandra.location = "garden"
        for item in self.Sandra.inventory:
            item.location = "garden"
        
    def Daniel_journeyed_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        for item in self.Daniel.inventory:
            item.location = "kitchen"
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Daniel_went_back_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def Sandra_went_back_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Sandra_went_back_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Sandra_got_the_football_there(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def Sandra_went_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Daniel_left_the_milk(self):
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Sandra_put_down_the_football(self):
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()