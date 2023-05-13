## Sandra took the milk there.
## Sandra journeyed to the garden.
## Sandra dropped the milk there.
## Sandra journeyed to the bathroom.
## John travelled to the garden.
## John went to the kitchen.
## John got the apple there.
## Daniel moved to the bathroom.
## John dropped the apple.
## Daniel moved to the hallway.
## John picked up the apple there.
## Mary went back to the office.
## Mary journeyed to the kitchen.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
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
        ## Sandra took the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Sandra journeyed to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Sandra dropped the milk there.
        self.drop(character = self.Sandra, item = self.milk)
        ## Sandra journeyed to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John travelled to the garden.
        self.go(character = self.John, location = "garden")
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## John got the apple there.
        self.pick_up(character = self.John, item = self.apple)
        ## Daniel moved to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## John dropped the apple.
        self.drop(character = self.John, item = self.apple)
        ## Daniel moved to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## John picked up the apple there.
        self.pick_up(character = self.John, item = self.apple)
        ## Mary went back to the office.
        self.go(character = self.Mary, location = "office")
        ## Mary journeyed to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## John discarded the apple.
        self.drop(character = self.John, item = self.apple)
        ## Where is the apple?
        print(self.apple.location)

world = World()
world.story()