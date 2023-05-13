## Sandra got the milk there.
## John grabbed the apple there.
## John journeyed to the bathroom.
## John discarded the apple.
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
        self.Sandra = character("Sandra")
        self.John = character("John")
        self.milk = object("milk")
        self.apple = object("apple")

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
        ## Sandra got the milk there.
        self.go(character = self.Sandra, location = "kitchen")
        self.pick_up(character = self.Sandra, item = self.milk)
        ## John grabbed the apple there.
        self.go(character = self.John, location = "kitchen")
        self.pick_up(character = self.John, item = self.apple)
        ## John journeyed to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John discarded the apple.
        self.drop(character = self.John, item = self.apple)
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()