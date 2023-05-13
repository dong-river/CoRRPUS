## Sandra got the milk there.
## John grabbed the apple there.
## John journeyed to the bathroom.
## John discarded the apple.
## John journeyed to the garden.
## Sandra travelled to the bedroom.
## Sandra went back to the garden.
## Sandra left the milk there.
## John grabbed the milk there.
## John went back to the kitchen.
## Daniel went to the garden.
## Sandra journeyed to the kitchen.
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
        self.milk = object("milk")
        self.apple = object("apple")
        self.Daniel = character("Daniel")

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
        self.pick_up(character = self.Sandra, item = self.milk)
        ## John grabbed the apple there.
        self.pick_up(character = self.John, item = self.apple)
        ## John journeyed to the bathroom.
        self.go(character = self.John, location = "bathroom")
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
        ## John grabbed the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## John went back to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Sandra journeyed to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()