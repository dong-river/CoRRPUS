## John went back to the kitchen.
## Daniel picked up the milk.
## Sandra went back to the bedroom.
## Mary moved to the garden.
## Sandra got the apple.
## Mary journeyed to the office.
## Mary journeyed to the garden.
## Sandra went to the hallway.
## Daniel moved to the bedroom.
## Sandra grabbed the football.
## Daniel discarded the milk.
## John journeyed to the garden.
## John went to the hallway.
## Mary journeyed to the office.
## John journeyed to the bedroom.
## Sandra moved to the garden.
## John travelled to the garden.
## Daniel grabbed the milk.
## Mary journeyed to the bathroom.
## Daniel dropped the milk.
## Daniel went to the office.
## Daniel travelled to the garden.
## John went back to the bedroom.
## Sandra discarded the football.
## Mary went back to the hallway.
## John journeyed to the garden.
## Daniel went back to the hallway.
## John went to the bedroom.
## Sandra travelled to the bathroom.
## John moved to the hallway.
## Daniel travelled to the kitchen.
## Daniel journeyed to the bedroom.
## John journeyed to the office.
## Mary travelled to the garden.
## Daniel went to the hallway.
## Daniel went to the garden.
## Daniel travelled to the hallway.
## Mary journeyed to the bathroom.
## John travelled to the kitchen.
## Sandra dropped the apple.
## Sandra grabbed the apple there.
## Mary went to the office.
## Sandra left the apple there.
## Daniel went to the bedroom.
## Sandra went back to the bedroom.
## Mary travelled to the hallway.
## Mary went to the office.
## Sandra took the milk.
## Mary went to the bathroom.
## John moved to the bathroom.
## Daniel moved to the kitchen.
## Mary grabbed the apple.
## Daniel moved to the office.
## Sandra went to the kitchen.
## Sandra went back to the office.
## Mary dropped the apple.
## Sandra dropped the milk.
## John went to the kitchen.
## Daniel grabbed the milk.
## Mary picked up the apple.
## Sandra went back to the hallway.
## Daniel journeyed to the hallway.
## John moved to the bedroom.
## John went to the bathroom.
## Daniel discarded the milk there.
## Mary moved to the kitchen.
## Mary journeyed to the office.
## Daniel got the milk.
## John moved to the garden.
## Sandra travelled to the kitchen.
## Mary put down the apple.
## John took the football.
## Sandra travelled to the garden.
## Sandra travelled to the bedroom.
## Where was the apple before the office? 

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
        self.John = character("John")
        self.Daniel = character("Daniel")
        self.Sandra = character("Sandra")
        self.Mary = character("Mary")
        self.apple = object("apple")
        self.football = object("football")
        self.milk = object("milk")

    def story(self):
        self.John_went_back_to_the_kitchen()
        self.Daniel_picked_up_the_milk()
        self.Sandra_went_back_to_the_bedroom()
        self.Mary_moved_to_the_garden()
        self.Sandra_got_the_apple()
        self.Mary_journeyed_to_the_office()
        self.Mary_journeyed_to_the_garden()
        self.Sandra_went_to_the_hallway()
        self.Daniel_moved_to_the_bedroom()
        self.Sandra_grabbed_the_football()
        self.Daniel_discarded_the_milk()
        self.John_journeyed_to_the_garden()
        self.John_went_to_the_hallway()
        self.Mary_journeyed_to_the_office()
        self.John_journeyed_to_the_bedroom()
        self.Sandra_moved_to_the_garden()
        self.John_travelled_to_the_garden()
        self.Daniel_grabbed_the_milk()
        self.Mary_journeyed_to_the_bathroom()
        self.Daniel_dropped_the_milk()
        self.Daniel_went_to_the_office()
        self.Daniel_travelled_to_the_garden()
        self.John_went_back_to_the_bedroom()
        self.Sandra_discarded_the_football()
        self.Mary_went_back_to_the_hallway()
        self.John_journeyed_to_the_garden()
        self.Daniel_went_back_to_the_hallway()
        self.John_went_to_the_bedroom()
        self.Sandra_travelled_to_the_bathroom()
        self.John_moved_to_the_hallway()
        self.Daniel_travelled_to_the_kitchen()
        self.Daniel_journeyed_to_the_bedroom()
        self.John_journeyed_to_the_office()
        self.Mary_travelled_to_the_garden()
        self.Daniel_went_to_the_hallway()
        self.Daniel_went_to_the_garden()
        self.Daniel_travelled_to_the_hallway()
        self.Mary_journeyed_to_the_bathroom()
        self.John_travelled_to_the_kitchen()
        self.Sandra_dropped_the_apple()
        self.Sandra_grabbed_the_apple_there()
        self.Mary_went_to_the_office()
        self.Sandra_left_the_apple_there()
        self.Daniel_went_to_the_bedroom()
        self.Sandra_went_back_to_the_bedroom()
        self.Mary_travelled_to_the_hallway()
        self.Mary_went_to_the_office()
        self.Sandra_took_the_milk()
        self.Mary_went_to_the_bathroom()
        self.John_moved_to_the_bathroom()
        self.Daniel_moved_to_the_kitchen()
        self.Mary_grabbed_the_apple()
        self.Daniel_moved_to_the_office()
        self.Sandra_went_to_the_kitchen()
        self.Sandra_went_back_to_the_office()
        self.Mary_dropped_the_apple()
        self.Sandra_dropped_the_milk()
        self.John_went_to_the_kitchen()
        self.Daniel_grabbed_the_milk()
        self.Mary_picked_up_the_apple()
        self.Sandra_went_back_to_the_hallway()
        self.Daniel_journeyed_to_the_hallway()
        self.John_moved_to_the_bedroom()
        self.John_went_to_the_bathroom()
        self.Daniel_discarded_the_milk_there()
        self.Mary_moved_to_the_kitchen()
        self.Mary_journeyed_to_the_office()
        self.Daniel_got_the_milk()
        self.John_moved_to_the_garden()
        self.Sandra_travelled_to_the_kitchen()
        self.Mary_put_down_the_apple()
        self.John_took_the_football()
        self.Sandra_travelled_to_the_garden()
        self.Sandra_travelled_to_the_bedroom()
        self.Where_was_the_apple_before_the_office()

    def John_went_back_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Daniel_picked_up_the_milk(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def Sandra_went_back_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Mary_moved_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def Sandra_got_the_apple(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def Mary_journeyed_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Mary_journeyed_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def Sandra_went_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def Daniel_moved_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Sandra_grabbed_the_football(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def Daniel_discarded_the_milk(self):
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def John_journeyed_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def John_went_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def Mary_journeyed_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def John_journeyed_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def Sandra_moved_to_the_garden(self):
        self.Sandra.location = "garden"
        for item in self.Sandra.inventory:
            item.location = "garden"
        
    def John_travelled_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Daniel_grabbed_the_milk(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def Mary_journeyed_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Daniel_dropped_the_milk(self):
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Daniel_went_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def Daniel_travelled_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def John_went_back_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def Sandra_discarded_the_football(self):
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        
    def Mary_went_back_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def John_journeyed_
world = World()
world.story()