## John got the football there.
## John left the football.
## Daniel went back to the bathroom.
## Mary went back to the bathroom.
## Sandra travelled to the office.
## Daniel got the apple there.
## John got the football there.
## John left the football.
## Daniel journeyed to the kitchen.
## John moved to the bathroom.
## John went to the office.
## Mary took the milk there.
## John journeyed to the garden.
## Sandra went to the garden.
## Daniel grabbed the football there.
## Mary discarded the milk.
## Sandra moved to the office.
## Mary got the milk there.
## Mary moved to the garden.
## Mary left the milk.
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
        self.Mary = character("Mary")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
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
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John left the football.
        self.drop(character = self.John, item = self.football)
        ## Daniel went back to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Mary went back to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Sandra travelled to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel got the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John left the football.
        self.drop(character = self.John, item = self.football)
        ## Daniel journeyed to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## John moved to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John went to the office.
        self.go(character = self.John, location = "office")
        ## Mary took the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## John journeyed to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra went to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Daniel grabbed the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Mary discarded the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## Sandra moved to the office.
        self.go(character = self.Sandra, location = "office")
        ## Mary got the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Mary moved to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Mary left the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()