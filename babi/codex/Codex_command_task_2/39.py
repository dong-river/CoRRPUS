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
## Mary went to the kitchen.
## John grabbed the football there.
## Sandra put down the milk there.
## John moved to the garden.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.milk = object("milk")
        self.football = object("football")

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
        self.Mary_went_to_the_kitchen()
        self.John_grabbed_the_football_there()
        self.Sandra_put_down_the_milk_there()
        self.John_moved_to_the_garden()
        self.Where_is_the_milk()

    def John_went_back_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def Mary_went_back_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def Daniel_journeyed_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Mary_went_back_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Sandra_went_back_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def Sandra_got_the_milk_there(self):
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Mary_moved_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Mary_went_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def Daniel_went_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def Sandra_went_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def John_journeyed_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Sandra_journeyed_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def Daniel_moved_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def Mary_went_back_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def John_moved_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Daniel_moved_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        for item in self.Daniel.inventory:
            item.location = "kitchen"
        
    def John_took_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_left_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Sandra_went_back_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Sandra_went_back_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def John_grabbed_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Daniel_went_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def John_left_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Sandra_went_back_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Mary_went_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def John_grabbed_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Sandra_put_down_the_milk_there(self):
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier =
world = World()
world.story()