## Sandra grabbed the football there.
## Sandra put down the football.
## John grabbed the apple there.
## Sandra went to the hallway.
## John journeyed to the hallway.
## Mary grabbed the milk there.
## John journeyed to the garden.
## Sandra moved to the bathroom.
## Mary journeyed to the bedroom.
## John picked up the football there.
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
        self.apple = object("apple")
        self.milk = object("milk")

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
        ## Sandra grabbed the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Sandra put down the football.
        self.drop(character = self.Sandra, item = self.football)
        ## John grabbed the apple there.
        self.pick_up(character = self.John, item = self.apple)
        ## Sandra went to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## John journeyed to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Mary grabbed the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## John journeyed to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra moved to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Mary journeyed to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## John picked up the football there.
        self.pick_up(character = self.John, item = self.football)
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()