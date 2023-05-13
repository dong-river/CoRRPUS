## Mary moved to the kitchen.
## Mary travelled to the office.
## Daniel grabbed the football there.
## Mary moved to the hallway.
## Sandra moved to the bedroom.
## Mary went back to the bedroom.
## John grabbed the milk there.
## John put down the milk.
## Daniel journeyed to the bathroom.
## Sandra journeyed to the bathroom.
## John got the milk there.
## Mary took the apple there.
## Mary left the apple.
## John journeyed to the bedroom.
## Mary travelled to the office.
## Daniel put down the football.
## John went back to the kitchen.
## Sandra got the football there.
## John travelled to the hallway.
## Sandra discarded the football there.
## John left the milk.
## John grabbed the milk there.
## Mary went to the hallway.
## John moved to the bedroom.
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
        ## Mary moved to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary travelled to the office.
        self.go(character = self.Mary, location = "office")
        ## Daniel grabbed the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Mary moved to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Sandra moved to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Mary went back to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## John grabbed the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## John put down the milk.
        self.drop(character = self.John, item = self.milk)
        ## Daniel journeyed to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Sandra journeyed to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John got the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## Mary took the apple there.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Mary left the apple.
        self.drop(character = self.Mary, item = self.apple)
        ## John journeyed to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Mary travelled to the office.
        self.go(character = self.Mary, location = "office")
        ## Daniel put down the football.
        self.drop(character = self.Daniel, item = self.football)
        ## John went back to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Sandra got the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## John travelled to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Sandra discarded the football there.
        self.drop(character = self.Sandra, item = self.football)
        ## John left the milk.
        self.drop(character = self.John, item = self.milk)
        ## John grabbed the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## Mary went to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John moved to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()