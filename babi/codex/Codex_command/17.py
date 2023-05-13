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
## Mary journeyed to the bedroom.
## Mary took the milk.
## John went to the kitchen.
## Mary travelled to the garden.
## John grabbed the apple.
## John discarded the apple.
## John travelled to the garden.
## Mary went to the bedroom.
## Mary discarded the milk.
## John went back to the office.
## Where was the milk before the bedroom? 

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
        self.apple = object("apple")

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
        self.Mary_journeyed_to_the_bedroom()
        self.Mary_took_the_milk()
        self.John_went_to_the_kitchen()
        self.Mary_travelled_to_the_garden()
        self.John_grabbed_the_apple()
        self.John_discarded_the_apple()
        self.John_travelled_to_the_garden()
        self.Mary_went_to_the_bedroom()
        self.Mary_discarded_the_milk()
        self.John_went_back_to_the_office()
        self.Where_was_the_milk_before_the_bedroom()
        
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
        
    def Mary_journeyed_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Mary_took_the_milk(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Mary_travelled_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def John_grabbed_the_apple(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def John_discarded_the_apple(self):
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def John_travelled_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Mary_went_to_the_bedroom(self):

world = World()
world.story()