## John went back to the garden.
## Daniel went to the bathroom.
## Daniel went to the hallway.
## Daniel grabbed the football there.
## Daniel travelled to the bathroom.
## Daniel went to the garden.
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
        self.John = character("John")
        self.Daniel = character("Daniel")
        self.football = object("football")

    def go(self, character, location):
        character.location = location
        for item in character.inventory:
            item.location = location

    def pick_up(self, character, item):
        character.inventory.append(item)
        item.location = character.location
        item.carrier = character

    def drop(self, character, item):
        character.inventory.remove(item)
        item.location = character.location
        item.carrier = None

    def story(self):
        ## John went back to the garden.
        self.go(character = self.John, location = "garden")
        ## Daniel went to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Daniel went to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel grabbed the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Daniel travelled to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Where is the football?
        print(self.football.location)
world = World()
world.story()