## Daniel moved to the hallway.
## Mary went back to the kitchen.
## John got the milk there.
## John put down the milk.
## John got the milk there.
## Mary went back to the garden.
## John went back to the bedroom.
## Mary picked up the football there.
## John went to the office.
## John left the milk.
## Mary went to the bedroom.
## John went to the bedroom.
## John went to the bathroom.
## Mary moved to the bathroom.
## Mary went to the kitchen.
## Mary travelled to the office.
## Sandra moved to the kitchen.
## Daniel picked up the apple there.
## Sandra travelled to the garden.
## Mary travelled to the bedroom.
## Daniel went to the kitchen.
## Mary put down the football.
## Where is the apple? 

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
        self.apple = object("apple")

    def story(self):
        self.Daniel_moved_to_the_hallway()
        self.Mary_went_back_to_the_kitchen()
        self.John_got_the_milk_there()
        self.John_put_down_the_milk()
        self.John_got_the_milk_there()
        self.Mary_went_back_to_the_garden()
        self.John_went_back_to_the_bedroom()
        self.Mary_picked_up_the_football_there()
        self.John_went_to_the_office()
        self.John_left_the_milk()
        self.Mary_went_to_the_bedroom()
        self.John_went_to_the_bedroom()
        self.John_went_to_the_bathroom()
        self.Mary_moved_to_the_bathroom()
        self.Mary_went_to_the_kitchen()
        self.Mary_travelled_to_the_office()
        self.Sandra_moved_to_the_kitchen()
        self.Daniel_picked_up_the_apple_there()
        self.Sandra_travelled_to_the_garden()
        self.Mary_travelled_to_the_bedroom()
        self.Daniel_went_to_the_kitchen()
        self.Mary_put_down_the_football()
        self.Where_is_the_apple()

    def Daniel_moved_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def Mary_went_back_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def John_got_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def John_put_down_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def John_got_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Mary_went_back_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def John_went_back_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def Mary_picked_up_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def John_went_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def John_left_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Mary_went_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def John_went_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def John_went_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def Mary_moved_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Mary_went_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Mary_travelled_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Sandra_moved_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Daniel_picked_up_the_apple_there(self):
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        
    def Sandra_travelled_to_the_garden(self):
        self.Sandra.location = "garden"
        for item in self.Sandra.inventory:
            item.location = "garden"
        
    def Mary_travelled_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Daniel_went_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        for item in self.Daniel.inventory:
            item.location = "kitchen"
        
    def Mary_put_down_the_football(self):
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None
        
    def Where_is_the_apple(self):
        print(self.apple.location)

world = World()
world.story()