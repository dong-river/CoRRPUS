## Sandra took the football there.
## Mary travelled to the kitchen.
## John went to the office.
## Daniel travelled to the bedroom.
## Daniel journeyed to the bathroom.
## Mary went back to the bedroom.
## Sandra travelled to the kitchen.
## Mary went to the bathroom.
## Sandra went back to the bathroom.
## Sandra discarded the football.
## Mary journeyed to the bedroom.
## Sandra picked up the football there.
## Mary grabbed the milk there.
## Mary discarded the milk.
## Daniel moved to the bedroom.
## Mary picked up the milk there.
## Mary got the apple there.
## Sandra went back to the kitchen.
## Mary discarded the apple there.
## Daniel took the apple there.
## Mary put down the milk there.
## Daniel travelled to the bathroom.
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
        self.Sandra_took_the_football_there()
        self.Mary_travelled_to_the_kitchen()
        self.John_went_to_the_office()
        self.Daniel_travelled_to_the_bedroom()
        self.Daniel_journeyed_to_the_bathroom()
        self.Mary_went_back_to_the_bedroom()
        self.Sandra_travelled_to_the_kitchen()
        self.Mary_went_to_the_bathroom()
        self.Sandra_went_back_to_the_bathroom()
        self.Sandra_discarded_the_football()
        self.Mary_journeyed_to_the_bedroom()
        self.Sandra_picked_up_the_football_there()
        self.Mary_grabbed_the_milk_there()
        self.Mary_discarded_the_milk()
        self.Daniel_moved_to_the_bedroom()
        self.Mary_picked_up_the_milk_there()
        self.Mary_got_the_apple_there()
        self.Sandra_went_back_to_the_kitchen()
        self.Mary_discarded_the_apple_there()
        self.Daniel_took_the_apple_there()
        self.Mary_put_down_the_milk_there()
        self.Daniel_travelled_to_the_bathroom()
        self.Where_is_the_apple()

    def Sandra_took_the_football_there(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def Mary_travelled_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        for item in self.Mary.inventory:
            item.location = "kitchen"
        
    def John_went_to_the_office(self):
        self.John.location = "office"
        for item in self.John.inventory:
            item.location = "office"
        
    def Daniel_travelled_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Daniel_journeyed_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def Mary_went_back_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Sandra_travelled_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Mary_went_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Sandra_went_back_to_the_bathroom(self):
        self.Sandra.location = "bathroom"
        for item in self.Sandra.inventory:
            item.location = "bathroom"
        
    def Sandra_discarded_the_football(self):
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        
    def Mary_journeyed_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        for item in self.Mary.inventory:
            item.location = "bedroom"
        
    def Sandra_picked_up_the_football_there(self):
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        
    def Mary_grabbed_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def Mary_discarded_the_milk(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Daniel_moved_to_the_bedroom(self):
        self.Daniel.location = "bedroom"
        for item in self.Daniel.inventory:
            item.location = "bedroom"
        
    def Mary_picked_up_the_milk_there(self):
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        
    def Mary_got_the_apple_there(self):
        self.Mary.inventory.append(self.apple)
        self.apple.carrier = self.Mary
        
    def Sandra_went_back_to_the_kitchen(self):
        self.Sandra.location = "kitchen"
        for item in self.Sandra.inventory:
            item.location = "kitchen"
        
    def Mary_discarded_the_apple_there(self):
        self.Mary.inventory.remove(self.apple)
        self.apple.carrier = None
        
    def Daniel_took_the_apple_there(self):
        self.Daniel.inventory.append(self.apple)
        self.apple.carrier = self.Daniel
        
    def Mary_put_down_the_milk_there(self):
        self.Mary.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Daniel_travelled_to_the_bathroom(self):
        self.Daniel.location = "bathroom"
        for item in self.Daniel.inventory:
            item.location = "bathroom"
        
    def Where_is_the_apple(self):
        print(self.apple.location)

world = World()
world.story()