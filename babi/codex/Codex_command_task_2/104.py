## Mary moved to the bathroom.
## Sandra went to the kitchen.
## John travelled to the bedroom.
## Mary journeyed to the kitchen.
## Mary moved to the office.
## Sandra travelled to the bathroom.
## John travelled to the bathroom.
## John journeyed to the office.
## John took the milk there.
## Daniel travelled to the garden.
## Mary went to the kitchen.
## Daniel journeyed to the bathroom.
## John discarded the milk.
## Sandra went back to the kitchen.
## Daniel journeyed to the office.
## Sandra went back to the office.
## Daniel picked up the milk there.
## Sandra went back to the bedroom.
## John went to the garden.
## Daniel travelled to the kitchen.
## John journeyed to the bedroom.
## Sandra journeyed to the garden.
## Sandra moved to the kitchen.
## Daniel discarded the milk.
## John picked up the football there.
## Daniel took the milk there.
## John left the football.
## Mary went to the bedroom.
## Where is the football? 

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

    def story(self):
        self.Mary_moved_to_the_bathroom()
        self.Sandra_went_to_the_kitchen()
        self.John_travelled_to_the_bedroom()
        self.Mary_journeyed_to_the_kitchen()
        self.Mary_moved_to_the_office()
        self.Sandra_travelled_to_the_bathroom()
        self.John_travelled_to_the_bathroom()
        self.John_journeyed_to_the_office()
        self.John_took_the_milk_there()
        self.Daniel_travelled_to_the_garden()
        self.Mary_went_to_the_kitchen()
        self.Daniel_journeyed_to_the_bathroom()
        self.John_discarded_the_milk()
        self.Sandra_went_back_to_the_kitchen()
        self.Daniel_journeyed_to_the_office()
        self.Sandra_went_back_to_the_office()
        self.Daniel_picked_up_the_milk_there()
        self.Sandra_went_back_to_the_bedroom()
        self.John_went_to_the_garden()
        self.Daniel_travelled_to_the_kitchen()
        self.John_journeyed_to_the_bedroom()
        self.Sandra_journeyed_to_the_garden()
        self.Sandra_moved_to_the_kitchen()
        self.Daniel_discarded_the_milk()
        self.John_picked_up_the_football_there()
        self.Daniel_took_the_milk_there()
        self.John_left_the_football()
        self.Mary_went_to_the_bedroom()
        self.Where_is_the_football()

    def Mary_moved_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Sandra_went_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def John_travelled_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def Mary_journeyed_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Mary_moved_to_the_office(self):
        self.Mary.location = "office"
        for item in self.Mary.inventory:
            item.location = "office"
        
    def Sandra_travelled_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def John_travelled_to_the_bathroom(self):
        self.John.location = "bathroom"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def John_journeyed_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def John_took_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Daniel_travelled_to_the_garden(self):
        self.Daniel.location = "garden"
        for item in self.Daniel.inventory:
            item.location = "garden"
        
    def Mary_went_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def Daniel_journeyed_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def John_discarded_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Sandra_went_back_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Daniel_journeyed_to_the_office(self):
        self.Daniel.location = "office"
        for item in self.Daniel.inventory:
            item.location = "office"
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        for item in self.Sandra.inventory:
            item.location = "office"
        
    def Daniel_picked_up_the_milk_there(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def Sandra_went_back_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def John_went_to_the_garden(self):
        self.John.location = "garden"
        for item in self.John.inventory:
            item.location = "garden"
        
    def Daniel_travelled_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        for item in self.Daniel.inventory:
            item.location = "kitchen"
        
    def John_journeyed_to_the_bedroom(self):
        self.John.location = "bedroom"
        for item in self.John.inventory:
            item.location = "bedroom"
        
    def Sandra_journeyed_to_the_garden(self):
        self.Sandra.location = "garden"
        for item in self.Sandra.inventory:
            item.location = "garden"
        
    def Sandra_moved_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Daniel_discarded_the_milk(self):
        self.Daniel.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def John_picked_up_the_football_there(self):
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        
    def Daniel_took_the_milk_there(self):
        self.Daniel.inventory.append(self.milk)
        self.milk.carrier = self.Daniel
        
    def John_left_the_football(self):
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        
    def Mary_went_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Where_is_the_football(self):
        print(self.football.location)

world = World()
world.story()