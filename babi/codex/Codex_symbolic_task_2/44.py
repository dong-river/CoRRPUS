## Daniel moved to the hallway.
## Mary went back to the kitchen.
## John got the milk there.
## John put down the milk.
## John got the milk there.
## Mary went back to the garden.
## John went back to the bedroom.
## Mary picked up the football there.
## John went to the office.
## John left the milk.
## Mary went to the bedroom.
## John went to the bedroom.
## John went to the bathroom.
## Mary moved to the bathroom.
## Mary went to the kitchen.
## Mary travelled to the office.
## Sandra moved to the kitchen.
## Daniel picked up the apple there.
## Sandra travelled to the garden.
## Mary travelled to the bedroom.
## Daniel went to the kitchen.
## Mary put down the football.
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
        self.football = object("football")
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
        ## Daniel moved to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Mary went back to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## John got the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## John put down the milk.
        self.drop(character = self.John, item = self.milk)
        ## John got the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## Mary went back to the garden.
        self.go(character = self.Mary, location = "garden")
        ## John went back to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Mary picked up the football there.
        self.pick_up(character = self.Mary, item = self.football)
        ## John went to the office.
        self.go(character = self.John, location = "office")
        ## John left the milk.
        self.drop(character = self.John, item = self.milk)
        ## Mary went to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## John went to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## John went to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Mary moved to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Mary went to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary travelled to the office.
        self.go(character = self.Mary, location = "office")
        ## Sandra moved to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Daniel picked up the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## Sandra travelled to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Mary travelled to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Daniel went to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Mary put down the football.
        self.drop(character = self.Mary, item = self.football)
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()