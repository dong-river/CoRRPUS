## John went to the hallway.
## John went back to the bathroom.
## John grabbed the milk there.
## Sandra went back to the office.
## Sandra journeyed to the kitchen.
## Sandra got the apple there.
## Sandra dropped the apple there.
## John dropped the milk.
## Mary went back to the garden.
## Sandra journeyed to the hallway.
## Sandra got the football there.
## Mary moved to the kitchen.
## Sandra journeyed to the bedroom.
## Mary grabbed the apple there.
## Sandra went back to the office.
## Mary discarded the apple.
## 
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
        self.apple = object("apple")
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
        ## Mary went back to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Sandra journeyed to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Sandra got the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Mary moved to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Sandra journeyed to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Mary grabbed the apple there.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Mary discarded the apple.
        self.drop(character = self.Mary, item = self.apple)
        ## 
        ## Where is the apple?
        print(self.apple.location)

world = World()
world.story()