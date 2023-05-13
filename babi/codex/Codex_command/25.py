## John went to the hallway.
## Mary went back to the office.
## Mary got the milk.
## John journeyed to the garden.
## Daniel went to the kitchen.
## Mary put down the milk.
## John travelled to the bathroom.
## Daniel went back to the hallway.
## John took the apple.
## Daniel journeyed to the office.
## Daniel grabbed the milk.
## John discarded the apple.
## Daniel went to the garden.
## Daniel dropped the milk.
## Mary travelled to the garden.
## Daniel travelled to the office.
## Mary travelled to the bedroom.
## Mary moved to the garden.
## John picked up the football.
## John picked up the apple.
## John left the football.
## John moved to the office.
## Sandra travelled to the bathroom.
## Sandra got the football.
## Sandra travelled to the office.
## Daniel went back to the bedroom.
## Mary went back to the office.
## Daniel travelled to the hallway.
## Mary went back to the hallway.
## Sandra moved to the bedroom.
## Daniel moved to the bedroom.
## Sandra moved to the bathroom.
## John dropped the apple.
## John picked up the apple.
## Mary went back to the bedroom.
## Sandra went to the bedroom.
## Sandra dropped the football there.
## John dropped the apple.
## Where was the football before the bedroom? 

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
        self.apple = object("apple")
        self.football = object("football")

    def story(self):
        self.John_went_to_the_hallway()
        self.Mary_went_back_to_the_office()
        self.Mary_got_the_milk()
        self.John_journeyed_to_the_garden()
        self.Daniel_went_to_the_kitchen()
        self.Mary_put_down_the_milk()
        self.John_travelled_to_the_bathroom()
        self.Daniel_went_back_to_the_hallway()
        self.John_took_the_apple()
        self.Daniel_journeyed_to_the_office()
        self.Daniel_grabbed_the_milk()
        self.John_discarded_the_apple()
        self.Daniel_went_to_the_garden()
        self.Daniel_dropped_the_milk()
        self.Mary_travelled_to_the_garden()
        self.Daniel_travelled_to_the_office()
        self.Mary_travelled_to_the_bedroom()
        self.Mary_moved_to_the_garden()
        self.John_picked_up_the_football()
        self.John_picked_up_the_apple()
        self.John_left_the_football()
        self.John_moved_to_the_office()
        self.Sandra_travelled_to_the_bathroom()
        self.Sandra_got_the_football()
        self.Sandra_travelled_to_the_office()
        self.Daniel_went_back_to_the_bedroom()
        self.Mary_went_back_to_the_office()
        self.Daniel_travelled_to_the_hallway()
        self.Mary_went_back_to_the_hallway()
        self.Sandra_moved_to_the_bedroom()
        self.Daniel_moved_to_the_bedroom()
        self.Sandra_moved_to_the_bathroom()
        self.John_dropped_the_apple()
        self.John_picked_up_the_apple()
        self.Mary_went_back_to_the_bedroom()
        self.Sandra_went_to_the_bedroom()
        self.Sandra_dropped_the_football_there()
        self.John_dropped_the_apple()
        self.Where_was_the_football_before_the_bedroom()
        
    def John_went_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def Mary_went_back_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Mary_got_the_milk(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def John_journeyed_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Daniel_went_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        for item in self.Daniel.inventory:
            item.location = "kitchen"
        
    def Mary_put_down_the_milk(self):
        self.milk.location = "office"
        self.milk.carrier = None
        
    def John_travelled_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def Daniel_went_back_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def John_took_the_apple(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def Daniel_journeyed_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def Daniel_grabbed_the_milk(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def John_discarded_the_apple(self):
        self.apple.location = "bathroom"
        self.apple.carrier = None
        
    def Daniel_went_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Daniel_dropped_the_milk(self):
        self.milk.location = "garden"
        self.milk.carrier = None
        
    def Mary_travelled_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def Daniel_travelled_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def Mary_travelled_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Mary_moved_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def John_picked_up_the_football(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_picked_up_the_apple(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def John_left_the_football(self):
        self.football.location = "office"
        self.football.carrier = None
        
    def John_moved_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def Sandra_travelled_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def Sandra_got_the_football(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def Sandra_travelled_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Daniel_went_back_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Mary_went_back_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Daniel_travelled_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def Mary_went_back_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def Sandra_moved_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Daniel_moved_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Sandra_moved_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def John_dropped_the_apple(self):
        self.apple.location = "office"
        self.apple.carrier = None
        
    def John_picked_up_the_apple(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def Mary_went_back_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Sandra_went_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Sandra_dropped_the_football_there(self):
        self.football.location = "bedroom"
        self.football.carrier = None
        
    def John_dropped_the_apple(self):
        self.apple.location = "office"
        self.apple.carrier = None
        
    def Where_was_the_football_before_the_
world = World()
world.story()