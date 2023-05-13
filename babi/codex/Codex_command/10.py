## Sandra moved to the bathroom.
## John picked up the football.
## John dropped the football.
## Daniel went to the kitchen.
## Daniel got the apple.
## John went to the kitchen.
## Mary went back to the hallway.
## Daniel travelled to the office.
## John travelled to the garden.
## John journeyed to the kitchen.
## Mary moved to the kitchen.
## Daniel moved to the garden.
## Mary journeyed to the bathroom.
## Daniel grabbed the milk.
## Mary went to the hallway.
## Mary got the football there.
## Mary dropped the football.
## Sandra moved to the bedroom.
## Mary went back to the office.
## John travelled to the office.
## Mary went back to the bathroom.
## John moved to the hallway.
## Sandra went to the office.
## Mary journeyed to the kitchen.
## Sandra travelled to the garden.
## John went back to the garden.
## Sandra went back to the office.
## Mary went to the hallway.
## Daniel went to the bedroom.
## Mary picked up the football there.
## John travelled to the kitchen.
## Mary moved to the bedroom.
## Sandra went to the bathroom.
## Daniel put down the milk.
## Daniel discarded the apple.
## Mary took the milk.
## Where was the apple before the bedroom? 

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
        self.Sandra = character("Sandra")
        self.John = character("John")
        self.Daniel = character("Daniel")
        self.Mary = character("Mary")
        self.football = object("football")
        self.apple = object("apple")
        self.milk = object("milk")

    def story(self):
        self.Sandra_moved_to_the_bathroom()
        self.John_picked_up_the_football()
        self.John_dropped_the_football()
        self.Daniel_went_to_the_kitchen()
        self.Daniel_got_the_apple()
        self.John_went_to_the_kitchen()
        self.Mary_went_back_to_the_hallway()
        self.Daniel_travelled_to_the_office()
        self.John_travelled_to_the_garden()
        self.John_journeyed_to_the_kitchen()
        self.Mary_moved_to_the_kitchen()
        self.Daniel_moved_to_the_garden()
        self.Mary_journeyed_to_the_bathroom()
        self.Daniel_grabbed_the_milk()
        self.Mary_went_to_the_hallway()
        self.Mary_got_the_football_there()
        self.Mary_dropped_the_football()
        self.Sandra_moved_to_the_bedroom()
        self.Mary_went_back_to_the_office()
        self.John_travelled_to_the_office()
        self.Mary_went_back_to_the_bathroom()
        self.John_moved_to_the_hallway()
        self.Sandra_went_to_the_office()
        self.Mary_journeyed_to_the_kitchen()
        self.Sandra_travelled_to_the_garden()
        self.John_went_back_to_the_garden()
        self.Sandra_went_back_to_the_office()
        self.Mary_went_to_the_hallway()
        self.Daniel_went_to_the_bedroom()
        self.Mary_picked_up_the_football_there()
        self.John_travelled_to_the_kitchen()
        self.Mary_moved_to_the_bedroom()
        self.Sandra_went_to_the_bathroom()
        self.Daniel_put_down_the_milk()
        self.Daniel_discarded_the_apple()
        self.Mary_took_the_milk()
        self.Where_was_the_apple_before_the_bedroom()

    def Sandra_moved_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def John_picked_up_the_football(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def John_dropped_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Daniel_went_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        for item in self.Daniel.inventory:
            item.location = "kitchen"
        
    def Daniel_got_the_apple(self):
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Mary_went_back_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def Daniel_travelled_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def John_travelled_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def John_journeyed_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Mary_moved_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Daniel_moved_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Mary_journeyed_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Daniel_grabbed_the_milk(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def Mary_went_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def Mary_got_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def Mary_dropped_the_football(self):
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None
        
    def Sandra_moved_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Mary_went_back_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def John_travelled_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def Mary_went_back_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def John_moved_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def Sandra_went_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Mary_journeyed_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Sandra_travelled_to_the_garden(self):
        self.Sandra.location = "garden"
        for item in self.Sandra.inventory:
            item.location = "garden"
        
    def John_went_back_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Mary_went_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def Daniel_went_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Mary_picked_up_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def John_travelled_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Mary_moved_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Sandra_went_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def Daniel_put_down_the_milk(self):
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Daniel_discarded_the_apple(self):
        self.Daniel.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Mary_took_the_milk(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def Where_was_the_apple_before_the_bedroom(self):
        print(self.apple.location)

world = World()
world.story()