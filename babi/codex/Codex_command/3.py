## Mary got the milk.
## John moved to the bedroom.
## Daniel journeyed to the office.
## John grabbed the apple there.
## John got the football.
## John journeyed to the garden.
## Mary left the milk.
## John left the football.
## Daniel moved to the garden.
## Daniel grabbed the football.
## Mary moved to the hallway.
## Mary went to the kitchen.
## John put down the apple there.
## John picked up the apple.
## Sandra moved to the hallway.
## Daniel left the football there.
## Daniel took the football.
## John travelled to the kitchen.
## Daniel dropped the football.
## John dropped the apple.
## John grabbed the apple.
## John went to the office.
## Sandra went back to the bedroom.
## Sandra took the milk.
## John journeyed to the bathroom.
## John travelled to the office.
## Sandra left the milk.
## Mary went to the bedroom.
## Mary moved to the office.
## John travelled to the hallway.
## Sandra moved to the garden.
## Mary moved to the kitchen.
## Daniel took the football.
## Mary journeyed to the bedroom.
## Mary grabbed the milk there.
## Mary discarded the milk.
## John went to the garden.
## John discarded the apple there.
## Sandra travelled to the bedroom.
## Daniel moved to the bathroom.
## Sandra got the milk.
## Daniel travelled to the garden.
## Sandra went back to the bathroom.
## Daniel took the apple there.
## Mary went back to the hallway.
## Daniel went to the hallway.
## Sandra went to the kitchen.
## Mary journeyed to the bedroom.
## Sandra journeyed to the hallway.
## Daniel put down the apple.
## Daniel put down the football there.
## Sandra journeyed to the garden.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.milk = object("milk")
        self.apple = object("apple")
        self.football = object("football")
        self.football.location = "garden"

    def story(self):
        self.Mary_got_the_milk()
        self.John_moved_to_the_bedroom()
        self.Daniel_journeyed_to_the_office()
        self.John_grabbed_the_apple_there()
        self.John_got_the_football()
        self.John_journeyed_to_the_garden()
        self.Mary_left_the_milk()
        self.John_left_the_football()
        self.Daniel_moved_to_the_garden()
        self.Daniel_grabbed_the_football()
        self.Mary_moved_to_the_hallway()
        self.Mary_went_to_the_kitchen()
        self.John_put_down_the_apple_there()
        self.John_picked_up_the_apple()
        self.Sandra_moved_to_the_hallway()
        self.Daniel_left_the_football_there()
        self.Daniel_took_the_football()
        self.John_travelled_to_the_kitchen()
        self.Daniel_dropped_the_football()
        self.John_dropped_the_apple()
        self.John_grabbed_the_apple()
        self.John_went_to_the_office()
        self.Sandra_went_back_to_the_bedroom()
        self.Sandra_took_the_milk()
        self.John_journeyed_to_the_bathroom()
        self.John_travelled_to_the_office()
        self.Sandra_left_the_milk()
        self.Mary_went_to_the_bedroom()
        self.Mary_moved_to_the_office()
        self.John_travelled_to_the_hallway()
        self.Sandra_moved_to_the_garden()
        self.Mary_moved_to_the_kitchen()
        self.Daniel_took_the_football()
        self.Mary_journeyed_to_the_bedroom()
        self.Mary_grabbed_the_milk_there()
        self.Mary_discarded_the_milk()
        self.John_went_to_the_garden()
        self.John_discarded_the_apple_there()
        self.Sandra_travelled_to_the_bedroom()
        self.Daniel_moved_to_the_bathroom()
        self.Sandra_got_the_milk()
        self.Daniel_travelled_to_the_garden()
        self.Sandra_went_back_to_the_bathroom()
        self.Daniel_took_the_apple_there()
        self.Mary_went_back_to_the_hallway()
        self.Daniel_went_to_the_hallway()
        self.Sandra_went_to_the_kitchen()
        self.Mary_journeyed_to_the_bedroom()
        self.Sandra_journeyed_to_the_hallway()
        self.Daniel_put_down_the_apple()
        self.Daniel_put_down_the_football_there()
        self.Sandra_journeyed_to_the_garden()
        self.Where_was_the_football_before_the_garden()

    def Mary_got_the_milk(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def John_moved_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def Daniel_journeyed_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def John_grabbed_the_apple_there(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def John_got_the_football(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_journeyed_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Mary_left_the_milk(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def John_left_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Daniel_moved_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Daniel_grabbed_the_football(self):
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        
    def Mary_moved_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def Mary_went_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def John_put_down_the_apple_there(self):
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def John_picked_up_the_apple(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def Sandra_moved_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def Daniel_left_the_football_there(self):
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        
    def Daniel_took_the_football(self):
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        
    def John_travelled_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Daniel_dropped_the_football(self):
        self.Daniel.inventory.remove(self.football)
        self.football.carrier = None
        
    def John_dropped_the_apple(self):
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def John_grabbed_the_apple(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def John_went_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def Sandra_went_back_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Sandra_took_the_milk(self):
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        
    def John_journeyed_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def John_travelled_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def Sandra_left_the_milk(self):
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Mary_went_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Mary_moved_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def John_travelled_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def Sandra_moved_to_the_garden(self):
        self.Sandra.location = "garden"
        for item in self.Sandra.inventory:
            item.location = "garden"
        
    def Mary_moved_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Daniel_took_the_football(self):
        self.Daniel.inventory.append(self.football)
        self.football.carrier = self.Daniel
        
    def Mary_journeyed_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"

world = World()
world.story()