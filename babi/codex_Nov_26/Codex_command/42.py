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
## 
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Daniel = character("Daniel")
        self.milk = object("milk")

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
        self.Where_is_the_milk()

    def Daniel_moved_to_the_hallway(self):
        self.Daniel.location = "hallway"
        
    def Mary_went_back_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        
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
        
    def John_went_back_to_the_bedroom(self):
        self.John.location = "bedroom"
        
    def Mary_picked_up_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def John_went_to_the_office(self):
        self.John.location = "office"
        
    def John_left_the_milk(self):
        self.John.inventory.remove(self.milk)
        self.milk.carrier = None
        
    def Mary_went_to_the_bedroom(self):
        self.Mary.location = "bedroom"
        
    def John_went_to_the_bedroom(self):
        self.John.location = "bedroom"
        
    def Where_is_the_milk(self):
        if self.milk.carrier is not None:
            print(self.milk.carrier.name)
        else:
            print(self.milk.location)

world = World()
world.story()