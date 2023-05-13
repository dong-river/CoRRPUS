## John went back to the office.
## Mary went back to the hallway.
## Daniel journeyed to the bedroom.
## Mary went back to the bathroom.
## Sandra went back to the hallway.
## Sandra got the milk there.
## Mary moved to the office.
## Mary went to the hallway.
## Daniel went to the bathroom.
## Sandra went to the office.
## John journeyed to the garden.
## Sandra journeyed to the hallway.
## Daniel moved to the office.
## Mary went back to the office.
## John moved to the kitchen.
## Sandra journeyed to the bedroom.
## Sandra went back to the office.
## Daniel moved to the kitchen.
## John took the football there.
## John left the football.
## Sandra went back to the bedroom.
## Sandra went back to the hallway.
## John grabbed the football there.
## Daniel went to the bathroom.
## John left the football.
## Sandra went back to the bedroom.
## 
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
        self.milk = object("milk")

    def story(self):
        self.John_went_back_to_the_office()
        self.Mary_went_back_to_the_hallway()
        self.Daniel_journeyed_to_the_bedroom()
        self.Mary_went_back_to_the_bathroom()
        self.Sandra_went_back_to_the_hallway()
        self.Sandra_got_the_milk_there()
        self.Mary_moved_to_the_office()
        self.Mary_went_to_the_hallway()
        self.Daniel_went_to_the_bathroom()
        self.Sandra_went_to_the_office()
        self.John_journeyed_to_the_garden()
        self.Sandra_journeyed_to_the_hallway()
        self.Daniel_moved_to_the_office()
        self.Mary_went_back_to_the_office()
        self.John_moved_to_the_kitchen()
        self.Sandra_journeyed_to_the_bedroom()
        self.Sandra_went_back_to_the_office()
        self.Daniel_moved_to_the_kitchen()
        self.John_took_the_football_there()
        self.John_left_the_football()
        self.Sandra_went_back_to_the_bedroom()
        self.Sandra_went_back_to_the_hallway()
        self.John_grabbed_the_football_there()
        self.Daniel_went_to_the_bathroom()
        self.John_left_the_football()
        self.Sandra_went_back_to_the_bedroom()

    def John_went_back_to_the_office(self):
        self.John.location = "office"
        
    def Mary_went_back_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def Daniel_journeyed_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        
    def Mary_went_back_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        
    def Sandra_went_back_to_the_hallway(self):
        self.Sandra.location = "hallway"
        
    def Sandra_got_the_milk_there(self):
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Mary_moved_to_the_office(self):
        self.Mary.location = "office"
        
    def Mary_went_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def Daniel_went_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def Sandra_went_to_the_office(self):
        self.Sandra.location = "office"
        
    def John_journeyed_to_the_garden(self):
        self.John.location = "garden"
        
    def Sandra_journeyed_to_the_hallway(self):
        self.Sandra.location = "hallway"
        
    def Daniel_moved_to_the_office(self):
        self.Daniel.location = "office"
        
    def Mary_went_back_to_the_office(self):
        self.Mary.location = "office"
        
    def John_moved_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        
    def Daniel_moved_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def John_took_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_left_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Sandra_went_back_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        
    def Sandra_went_back_to_the_hallway(self):
        self.Sandra.location = "hallway"
        
    def John_grabbed_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Daniel_went_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        
    def John_left_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Sandra_went_back_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()