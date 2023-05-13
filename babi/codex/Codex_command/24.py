## John took the football.
## Daniel went back to the garden.
## Mary moved to the bathroom.
## Mary went to the bedroom.
## Mary went to the hallway.
## John dropped the football.
## Daniel journeyed to the hallway.
## Sandra grabbed the football.
## John moved to the office.
## Sandra put down the football.
## Sandra took the football.
## Daniel went to the bedroom.
## Mary moved to the office.
## Mary journeyed to the bedroom.
## Mary grabbed the apple there.
## Sandra went back to the kitchen.
## Sandra picked up the milk there.
## Mary discarded the apple.
## John went back to the bathroom.
## Mary got the apple.
## Mary left the apple.
## Mary took the apple.
## Mary put down the apple.
## Sandra put down the milk.
## Daniel went to the kitchen.
## Sandra journeyed to the office.
## Sandra journeyed to the bedroom.
## John moved to the garden.
## Sandra journeyed to the garden.
## Mary got the apple.
## Mary discarded the apple.
## Mary travelled to the hallway.
## Daniel went to the garden.
## Sandra went back to the hallway.
## Sandra travelled to the garden.
## Sandra went back to the office.
## Daniel went to the bathroom.
## Sandra dropped the football.
## Mary went back to the kitchen.
## Mary went back to the hallway.
## Sandra went back to the hallway.
## Mary journeyed to the bathroom.
## John travelled to the bathroom.
## Sandra journeyed to the office.
## John went to the bedroom.
## Sandra went back to the bedroom.
## John took the apple.
## John went to the office.
## Sandra travelled to the kitchen.
## John put down the apple.
## Daniel travelled to the bedroom.
## John journeyed to the bedroom.
## John went to the garden.
## Daniel went to the hallway.
## Daniel went to the office.
## Sandra grabbed the milk there.
## Mary went to the garden.
## Sandra went back to the office.
## John travelled to the office.
## Sandra journeyed to the kitchen.
## Daniel went to the garden.
## John grabbed the football.
## Sandra went to the bedroom.
## John grabbed the apple.
## Daniel went back to the bathroom.
## Daniel went back to the office.
## Mary moved to the hallway.
## Mary travelled to the kitchen.
## John discarded the football.
## John dropped the apple.
## Mary went to the hallway.
## John grabbed the apple.
## John got the football.
## Sandra put down the milk.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        self.John_took_the_football()
        self.Daniel_went_back_to_the_garden()
        self.Mary_moved_to_the_bathroom()
        self.Mary_went_to_the_bedroom()
        self.Mary_went_to_the_hallway()
        self.John_dropped_the_football()
        self.Daniel_journeyed_to_the_hallway()
        self.Sandra_grabbed_the_football()
        self.John_moved_to_the_office()
        self.Sandra_put_down_the_football()
        self.Sandra_took_the_football()
        self.Daniel_went_to_the_bedroom()
        self.Mary_moved_to_the_office()
        self.Mary_journeyed_to_the_bedroom()
        self.Mary_grabbed_the_apple_there()
        self.Sandra_went_back_to_the_kitchen()
        self.Sandra_picked_up_the_milk_there()
        self.Mary_discarded_the_apple()
        self.John_went_back_to_the_bathroom()
        self.Mary_got_the_apple()
        self.Mary_left_the_apple()
        self.Mary_took_the_apple()
        self.Mary_put_down_the_apple()
        self.Sandra_put_down_the_milk()
        self.Daniel_went_to_the_kitchen()
        self.Sandra_journeyed_to_the_office()
        self.Sandra_journeyed_to_the_bedroom()
        self.John_moved_to_the_garden()
        self.Sandra_journeyed_to_the_garden()
        self.Mary_got_the_apple()
        self.Mary_discarded_the_apple()
        self.Mary_travelled_to_the_hallway()
        self.Daniel_went_to_the_garden()
        self.Sandra_went_back_to_the_hallway()
        self.Sandra_travelled_to_the_garden()
        self.Sandra_went_back_to_the_office()
        self.Daniel_went_to_the_bathroom()
        self.Sandra_dropped_the_football()
        self.Mary_went_back_to_the_kitchen()
        self.Mary_went_back_to_the_hallway()
        self.Sandra_went_back_to_the_hallway()
        self.Mary_journeyed_to_the_bathroom()
        self.John_travelled_to_the_bathroom()
        self.Sandra_journeyed_to_the_office()
        self.John_went_to_the_bedroom()
        self.Sandra_went_back_to_the_bedroom()
        self.John_took_the_apple()
        self.John_went_to_the_office()
        self.Sandra_travelled_to_the_kitchen()
        self.John_put_down_the_apple()
        self.Daniel_travelled_to_the_bedroom()
        self.John_journeyed_to_the_bedroom()
        self.John_went_to_the_garden()
        self.Daniel_went_to_the_hallway()
        self.Daniel_went_to_the_office()
        self.Sandra_grabbed_the_milk_there()
        self.Mary_went_to_the_garden()
        self.Sandra_went_back_to_the_office()
        self.John_travelled_to_the_office()
        self.Sandra_journeyed_to_the_kitchen()
        self.Daniel_went_to_the_garden()
        self.John_grabbed_the_football()
        self.Sandra_went_to_the_bedroom()
        self.John_grabbed_the_apple()
        self.Daniel_went_back_to_the_bathroom()
        self.Daniel_went_back_to_the_office()
        self.Mary_moved_to_the_hallway()
        self.Mary_travelled_to_the_kitchen()
        self.John_discarded_the_football()
        self.John_dropped_the_apple()
        self.Mary_went_to_the_hallway()
        self.John_grabbed_the_apple()
        self.John_got_the_football()
        self.Sandra_put_down_the_milk()
        self.Where_was_the_milk_before_the_bedroom()
        
    def John_took_the_football(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Daniel_went_back_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Mary_moved_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Mary_went_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Mary_went_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def John_dropped_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Daniel_journeyed_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def Sandra_grabbed_the_football(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def John_moved_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def Sandra_put_down_the_football(self):
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        
    def Sandra_took_the_football(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def Daniel_went_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Mary_moved_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Mary_journeyed_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Mary_grabbed_the_apple_there(self):
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        
    def Sandra_went_back_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Sandra_picked_up_the_milk_there(self):
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def Mary_discarded_the_apple(self):
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def John_went_back_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def Mary_got_the_apple(self):
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        
    def Mary_left_the_apple(self):
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Mary_took_the_apple(self):
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        
    def Mary_put_down_the_apple(self):
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Sandra_put_down_the_milk(self):
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Daniel_went_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        for item in self.Daniel.inventory:
            item.location = "kitchen"
        
    def Sandra_journeyed_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location
world = World()
world.story()