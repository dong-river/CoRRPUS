## Daniel moved to the bedroom.
## Daniel went to the bathroom.
## John moved to the garden.
## Mary travelled to the bedroom.
## Sandra travelled to the garden.
## Daniel journeyed to the garden.
## Sandra travelled to the hallway.
## John got the football there.
## John moved to the bathroom.
## Sandra travelled to the bathroom.
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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.Mary = character("Mary")
        self.Sandra = character("Sandra")
        self.football = object("football")
    
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
        ## Daniel moved to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel went to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## John moved to the garden.
        self.go(character = self.John, location = "garden")
        ## Mary travelled to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Sandra travelled to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Daniel journeyed to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Sandra travelled to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John moved to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Sandra travelled to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()