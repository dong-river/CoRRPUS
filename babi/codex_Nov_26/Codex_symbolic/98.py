## Mary went to the garden.
## John picked up the milk there.
## Mary journeyed to the bedroom.
## Sandra went back to the hallway.
## John discarded the milk.
## John journeyed to the bedroom.
## John got the football there.
## John moved to the bathroom.
## Sandra went to the office.
## Daniel went back to the hallway.
## John put down the football.
## Mary journeyed to the kitchen.
## Mary picked up the milk there.
## Mary moved to the hallway.
## 
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
    
    def go(self, character, location):
        character.location = location
        for item in character.inventory:
            item.location = location

    def pick_up(self, character, item):
        character.inventory.append(item)
        item.carrier = character

    def drop(self, character, item):
        character.inventory.remove(item)
        item.carrier = None
        
    def put_down(self, character, item):
        character.inventory.remove(item)
        item.carrier = None
        item.location = character.location
    
    def story(self):
        ## Mary went to the garden.
        self.go(character = self.Mary, location = "garden")
        ## John picked up the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## Mary journeyed to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Sandra went back to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## John discarded the milk.
        self.drop(character = self.John, item = self.milk)
        ## John journeyed to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John moved to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Sandra went to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel went back to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## John put down the football.
        self.put_down(character = self.John, item = self.football)
        ## Mary journeyed to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary picked up the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Mary moved to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## 
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()