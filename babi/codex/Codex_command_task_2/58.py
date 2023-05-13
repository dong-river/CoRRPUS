## John went to the bathroom.
## Daniel travelled to the kitchen.
## John journeyed to the kitchen.
## Daniel journeyed to the hallway.
## Sandra travelled to the kitchen.
## Mary moved to the office.
## Daniel went back to the office.
## Sandra went back to the bathroom.
## John grabbed the milk there.
## John grabbed the apple there.
## Sandra journeyed to the office.
## Mary went to the hallway.
## John went to the bathroom.
## John discarded the apple.
## John put down the milk.
## John picked up the apple there.
## Daniel went back to the bathroom.
## John took the milk there.
## Daniel travelled to the garden.
## Sandra journeyed to the bathroom.
## John travelled to the kitchen.
## Mary went back to the office.
## Mary moved to the hallway.
## John left the milk.
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
        self.John = character("John")
        self.Daniel = character("Daniel")
        self.Sandra = character("Sandra")
        self.Mary = character("Mary")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        self.John_went_to_the_bathroom()
        self.Daniel_travelled_to_the_kitchen()
        self.John_journeyed_to_the_kitchen()
        self.Daniel_journeyed_to_the_hallway()
        self.Sandra_travelled_to_the_kitchen()
        self.Mary_moved_to_the_office()
        self.Daniel_went_back_to_the_office()
        self.Sandra_went_back_to_the_bathroom()
        self.John_grabbed_the_milk_there()
        self.John_grabbed_the_apple_there()
        self.Sandra_journeyed_to_the_office()
        self.Mary_went_to_the_hallway()
        self.John_went_to_the_bathroom()
        self.John_discarded_the_apple()
        self.John_put_down_the_milk()
        self.John_picked_up_the_apple_there()
        self.Daniel_went_back_to_the_bathroom()
        self.John_took_the_milk_there()
        self.Daniel_travelled_to_the_garden()
        self.Sandra_journeyed_to_the_bathroom()
        self.John_travelled_to_the_kitchen()
        self.Mary_went_back_to_the_office()
        self.Mary_moved_to_the_hallway()
        self.John_left_the_milk()
        self.Where_is_the_milk()

    def John_went_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def Daniel_travelled_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        for item in self.Daniel.inventory:
            item.location = "kitchen"
        
    def John_journeyed_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Daniel_journeyed_to_the_hallway(self):
        self.Daniel.location = "hallway"
        for item in self.Daniel.inventory:
            item.location = "hallway"
        
    def Sandra_travelled_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Mary_moved_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Daniel_went_back_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def Sandra_went_back_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def John_grabbed_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def John_grabbed_the_apple_there(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def Sandra_journeyed_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Mary_went_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def John_went_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def John_discarded_the_apple(self):
        self.John.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def John_put_down_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def John_picked_up_the_apple_there(self):
        self.John.inventory.append(self.apple)
        self.apple.carrier = self.John
        
    def Daniel_went_back_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def John_took_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Daniel_travelled_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Sandra_journeyed_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def John_travelled_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "kitchen"
        
    def Mary_went_back_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Mary_moved_to_the_hallway(self):
        self.Mary.location = "hallway"
        for item in self.Mary.inventory:
            item.location = "hallway"
        
    def John_left_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Where_is_the_milk(self):
        print(self.milk.location)

world = World()
world.story()