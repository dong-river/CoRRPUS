## Daniel took the milk there.
## John journeyed to the garden.
## Daniel went back to the hallway.
## Daniel journeyed to the bathroom.
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
        self.Sandra = character("Sandra")
        self.football = object("football")
        self.Daniel = character("Daniel")
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

    def story(self):
        ## Mary moved to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Sandra journeyed to the bedroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Mary got the football there.
        self.pick_up(character = self.Mary, item = self.football)
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary went back to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Where is the football?
        print(self.football.location)
        ## Daniel took the milk there.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## John journeyed to the garden.
        self.go(character = self.John, location = "garden")
        ## Daniel went back to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel journeyed to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Where is the milk? 
        print(self.milk.location)

world = World()
world.story()