## John went to the hallway.
## John went back to the bathroom.
## John grabbed the milk there.
## Sandra went back to the office.
## Sandra journeyed to the kitchen.
## Sandra got the apple there.
## Sandra dropped the apple there.
## John dropped the milk.
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
        self.John = character("John")
        self.Sandra = character("Sandra")
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
        ## John went to the hallway.
        self.go(character = self.John, location = "hallway")
        ## John went back to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John grabbed the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Sandra journeyed to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Sandra got the apple there.
        self.pick_up(character = self.Sandra, item = self.apple)
        ## Sandra dropped the apple there.
        self.drop(character = self.Sandra, item = self.apple)
        ## John dropped the milk.
        self.drop(character = self.John, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()