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
## Sandra got the apple there.
## John went to the kitchen.
## Mary went to the bathroom.
## Mary journeyed to the garden.
## Sandra went back to the kitchen.
## Sandra put down the apple there.
## Mary went back to the bedroom.
## Mary went back to the kitchen.
## 
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
        ## Sandra got the apple there.
        self.pick_up(character = self.Sandra, item = self.apple)
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary went to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Mary journeyed to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Sandra went back to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Sandra put down the apple there.
        self.drop(character = self.Sandra, item = self.apple)
        ## Mary went back to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary went back to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## 
        ## Where is the apple? 
        print(self.apple.location)


world = World()
world.story()