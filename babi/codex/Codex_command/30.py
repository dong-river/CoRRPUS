## Mary went back to the garden.
## John went back to the hallway.
## Daniel went back to the bedroom.
## Daniel got the milk.
## Daniel put down the milk.
## Daniel got the milk.
## Daniel dropped the milk.
## Mary picked up the apple.
## Daniel went to the hallway.
## John went back to the office.
## John moved to the bedroom.
## Daniel travelled to the office.
## Mary discarded the apple.
## John took the milk.
## Mary went to the office.
## Sandra went to the bathroom.
## Sandra went back to the office.
## Sandra moved to the garden.
## Sandra grabbed the apple there.
## John travelled to the hallway.
## Daniel went back to the garden.
## Sandra moved to the bathroom.
## John grabbed the football.
## Daniel went to the hallway.
## Sandra went to the hallway.
## Sandra moved to the office.
## Sandra moved to the kitchen.
## Sandra left the apple there.
## Where was the apple before the hallway? 

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
        self.apple = object("apple")
        self.milk = object("milk")
        self.football = object("football")

    def story(self):
        self.Mary_went_back_to_the_garden()
        self.John_went_back_to_the_hallway()
        self.Daniel_went_back_to_the_bedroom()
        self.Daniel_got_the_milk()
        self.Daniel_put_down_the_milk()
        self.Daniel_got_the_milk()
        self.Daniel_dropped_the_milk()
        self.Mary_picked_up_the_apple()
        self.Daniel_went_to_the_hallway()
        self.John_went_back_to_the_office()
        self.John_moved_to_the_bedroom()
        self.Daniel_travelled_to_the_office()
        self.Mary_discarded_the_apple()
        self.John_took_the_milk()
        self.Mary_went_to_the_office()
        self.Sandra_went_to_the_bathroom()
        self.Sandra_went_back_to_the_office()
        self.Sandra_moved_to_the_garden()
        self.Sandra_grabbed_the_apple_there()
        self.John_travelled_to_the_hallway()
        self.Daniel_went_back_to_the_garden()
        self.Sandra_moved_to_the_bathroom()
        self.John_grabbed_the_football()
        self.Daniel_went_to_the_hallway()
        self.Sandra_went_to_the_hallway()
        self.Sandra_moved_to_the_office()
        self.Sandra_moved_to_the_kitchen()
        self.Sandra_left_the_apple_there()
        self.Where_was_the_apple_before_the_hallway()

    def Mary_went_back_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def John_went_back_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def Daniel_went_back_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Daniel_got_the_milk(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def Daniel_put_down_the_milk(self):
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Daniel_got_the_milk(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def Daniel_dropped_the_milk(self):
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Mary_picked_up_the_apple(self):
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        
    def Daniel_went_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def John_went_back_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def John_moved_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def Daniel_travelled_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def Mary_discarded_the_apple(self):
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def John_took_the_milk(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Mary_went_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Sandra_went_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Sandra_moved_to_the_garden(self):
        self.Sandra.location = "garden"
        for item in self.Sandra.inventory:
            item.location = "garden"
        
    def Sandra_grabbed_the_apple_there(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def John_travelled_to_the_hallway(self):
        self.John.location = "hallway"
        for item in self.John.inventory:
            item.location = "hallway"
        
    def Daniel_went_back_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Sandra_moved_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def John_grabbed_the_football(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Daniel_went_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def Sandra_went_to_the_hallway(self):
        self.Sandra.location = "hallway"
        for item in self.Sandra.inventory:
            item.location = "hallway"
        
    def Sandra_moved_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Sandra_moved_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Sandra_left_the_apple_there(self):
        self.Sandra.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Where_was_the_apple_before_the_hallway(self):
        print(self.apple.location)

world = World()
world.story()