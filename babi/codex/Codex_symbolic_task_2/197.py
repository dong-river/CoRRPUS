## Sandra got the milk there.
## John grabbed the apple there.
## John journeyed to the bathroom.
## John discarded the apple.
## John journeyed to the garden.
## Sandra travelled to the bedroom.
## Sandra went back to the garden.
## Sandra left the milk there.
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
        self.go(character = self.Sandra, location = "bathroom")
        self.pick_up(character = self.Sandra, item = self.milk)
        ## John grabbed the apple there.
        self.go(character = self.John, location = "bathroom")
        self.pick_up(character = self.John, item = self.apple)
        ## John journeyed to the bathroom.
        self.go(character = self.John, location = "kitchen")
        ## John discarded the apple.
        self.drop(character = self.John, item = self.apple)
        ## John journeyed to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra travelled to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Sandra went back to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Sandra left the milk there.
        self.drop(character = self.Sandra, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()