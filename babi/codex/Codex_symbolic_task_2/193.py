## Mary travelled to the bedroom.
## Daniel grabbed the apple there.
## Daniel went to the garden.
## John travelled to the office.
## Daniel left the apple.
## John travelled to the hallway.
## Sandra went to the office.
## Daniel journeyed to the hallway.
## Daniel went to the kitchen.
## John journeyed to the kitchen.
## Mary moved to the office.
## Mary went back to the garden.
## Mary moved to the office.
## John went back to the bathroom.
## John travelled to the office.
## Daniel went back to the garden.
## John travelled to the kitchen.
## Mary went to the bedroom.
## Daniel moved to the bathroom.
## Daniel picked up the football there.
## Sandra travelled to the hallway.
## Daniel picked up the milk there.
## Daniel dropped the milk.
## Daniel took the milk there.
## Daniel moved to the bedroom.
## Sandra went to the garden.
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
        self.football = object("football")

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

    def take(self, character, item, location):
        self.pick_up(character, item)
        self.go(character, location)
        self.drop(character, item)

    def story(self):
        ## Mary travelled to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Daniel grabbed the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## Daniel left the apple.
        self.drop(character = self.Daniel, item = self.apple)
        ## John travelled to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Sandra went to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel journeyed to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel went to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## John journeyed to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## Mary went back to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## John went back to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## Daniel went back to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## John travelled to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary went to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Daniel moved to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Daniel picked up the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Sandra travelled to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Daniel picked up the milk there.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## Daniel dropped the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## Daniel took the milk there.
        self.take(character = self.Daniel, item = self.milk, location = "hallway")
        ## Daniel moved to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Sandra went to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()