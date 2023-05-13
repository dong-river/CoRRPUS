## Daniel moved to the bathroom.
## John got the football.
## Sandra grabbed the milk.
## Sandra put down the milk.
## Daniel journeyed to the bedroom.
## Sandra took the milk.
## Sandra put down the milk there.
## John put down the football.
## Mary travelled to the hallway.
## John took the football.
## Sandra went back to the office.
## Mary moved to the garden.
## Daniel moved to the garden.
## Daniel went back to the office.
## Sandra journeyed to the hallway.
## Mary went to the office.
## Sandra went back to the office.
## Sandra moved to the bathroom.
## John dropped the football.
## Sandra got the football.
## Sandra left the football there.
## Daniel moved to the bedroom.
## Daniel journeyed to the office.
## John went back to the office.
## Sandra got the football.
## Sandra discarded the football.
## Mary travelled to the bathroom.
## Mary got the football.
## Mary went back to the kitchen.
## Mary journeyed to the garden.
## Where was the football before the garden? 

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
        self.Mary = character("Mary")
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        self.Daniel_moved_to_the_bathroom()
        self.John_got_the_football()
        self.Sandra_grabbed_the_milk()
        self.Sandra_put_down_the_milk()
        self.Daniel_journeyed_to_the_bedroom()
        self.Sandra_took_the_milk()
        self.Sandra_put_down_the_milk_there()
        self.John_put_down_the_football()
        self.Mary_travelled_to_the_hallway()
        self.John_took_the_football()
        self.Sandra_went_back_to_the_office()
        self.Mary_moved_to_the_garden()
        self.Daniel_moved_to_the_garden()
        self.Daniel_went_back_to_the_office()
        self.Sandra_journeyed_to_the_hallway()
        self.Mary_went_to_the_office()
        self.Sandra_went_back_to_the_office()
        self.Sandra_moved_to_the_bathroom()
        self.John_dropped_the_football()
        self.Sandra_got_the_football()
        self.Sandra_left_the_football_there()
        self.Daniel_moved_to_the_bedroom()
        self.Daniel_journeyed_to_the_office()
        self.John_went_back_to_the_office()
        self.Sandra_got_the_football()
        self.Sandra_discarded_the_football()
        self.Mary_travelled_to_the_bathroom()
        self.Mary_got_the_football()
        self.Mary_went_back_to_the_kitchen()
        self.Mary_journeyed_to_the_garden()
        self.Where_was_the_football_before_the_garden()
        
    def Daniel_moved_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def John_got_the_football(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Sandra_grabbed_the_milk(self):
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Sandra_put_down_the_milk(self):
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Daniel_journeyed_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Sandra_took_the_milk(self):
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Sandra_put_down_the_milk_there(self):
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def John_put_down_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Mary_travelled_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def John_took_the_football(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Mary_moved_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def Daniel_moved_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Daniel_went_back_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def Sandra_journeyed_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def Mary_went_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Sandra_moved_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def John_dropped_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Sandra_got_the_football(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def Sandra_left_the_football_there(self):
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        
    def Daniel_moved_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Daniel_journeyed_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def John_went_back_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def Sandra_got_the_football(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def Sandra_discarded_the_football(self):
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        
    def Mary_travelled_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Mary_got_the_football(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def Mary_went_back_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Mary_journeyed_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def Where_was_the_football_before_the_garden(self):
        print(self.football.location)

world = World()
world.story()