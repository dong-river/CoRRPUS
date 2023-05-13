## Sandra journeyed to the bathroom.
## Mary took the apple there.
## Sandra went back to the kitchen.
## Mary went back to the office.
## Sandra took the milk there.
## Mary discarded the apple.
## Mary got the apple there.
## Daniel moved to the bedroom.
## John went to the bedroom.
## Sandra dropped the milk there.
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
        self.Daniel = character("Daniel")
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

    def discard(self, character, item):
        character.inventory.remove(item)

    def story(self):
        ## Sandra journeyed to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Mary took the apple there.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Sandra went back to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Mary went back to the office.
        self.go(character = self.Mary, location = "office")
        ## Sandra took the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Mary discarded the apple.
        self.discard(character = self.Mary, item = self.apple)
        ## Mary got the apple there.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Daniel moved to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John went to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra dropped the milk there.
        self.drop(character = self.Sandra, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()