## John grabbed the football there.
## John journeyed to the office.
## John went back to the garden.
## John went to the hallway.
## John dropped the football.
## John grabbed the football there.
## Sandra travelled to the bathroom.
## Sandra picked up the milk there.
## Sandra went to the office.
## John moved to the bathroom.
## John grabbed the apple there.
## Sandra travelled to the bedroom.
## John discarded the apple.
## Mary went back to the hallway.
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
        ## John grabbed the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John journeyed to the office.
        self.go(character = self.John, location = "office")
        ## John went back to the garden.
        self.go(character = self.John, location = "garden")
        ## John went to the hallway.
        self.go(character = self.John, location = "hallway")
        ## John dropped the football.
        self.drop(character = self.John, item = self.football)
        ## John grabbed the football there.
        self.pick_up(character = self.John, item = self.football)
        ## Sandra travelled to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Sandra picked up the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Sandra went to the office.
        self.go(character = self.Sandra, location = "office")
        ## John moved to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John grabbed the apple there.
        self.pick_up(character = self.John, item = self.apple)
        ## Sandra travelled to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## John discarded the apple.
        self.drop(character = self.John, item = self.apple)
        ## Mary went back to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Where is the apple?
        print(self.apple.location)

world = World()
world.story()