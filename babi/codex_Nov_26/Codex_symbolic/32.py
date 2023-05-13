## Daniel journeyed to the office.
## Daniel went back to the bedroom.
## Mary went back to the kitchen.
## Mary got the football there.
## Daniel travelled to the hallway.
## John journeyed to the bedroom.
## Daniel got the apple there.
## Sandra travelled to the garden.
## Daniel travelled to the garden.
## Daniel dropped the apple.
## Mary left the football.
## Mary journeyed to the bedroom.
## John moved to the hallway.
## John went back to the bedroom.
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
        self.apple = object("apple")
    
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

    def story(self):
        ## Daniel journeyed to the office.
        self.go(character = self.Daniel, location = "office")
        ## Daniel went back to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Mary went back to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary got the football there.
        self.pick_up(character = self.Mary, item = self.football)
        ## Daniel travelled to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## John journeyed to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Daniel got the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## Sandra travelled to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Daniel travelled to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel dropped the apple.
        self.drop(character = self.Daniel, item = self.apple)
        ## Mary left the football.
        self.drop(character = self.Mary, item = self.football)
        ## Mary journeyed to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## John moved to the hallway.
        self.go(character = self.John, location = "hallway")
        ## John went back to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## 
        ## Where is the football? 
        print(self.football.location)

world = World()
world.story()