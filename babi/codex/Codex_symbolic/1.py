## Mary got the milk.
## John moved to the bedroom.
## Daniel journeyed to the office.
## John grabbed the apple there.
## John got the football.
## John journeyed to the garden.
## Mary left the milk.
## John left the football.
## Daniel moved to the garden.
## Daniel grabbed the football.
## Mary moved to the hallway.
## Mary went to the kitchen.
## John put down the apple there.
## John picked up the apple.
## Sandra moved to the hallway.
## Daniel left the football there.
## Daniel took the football.
## John travelled to the kitchen.
## Daniel dropped the football.
## John dropped the apple.
## John grabbed the apple.
## John went to the office.
## Sandra went back to the bedroom.
## Sandra took the milk.
## John journeyed to the bathroom.
## John travelled to the office.
## Sandra left the milk.
## Mary went to the bedroom.
## Mary moved to the office.
## John travelled to the hallway.
## Sandra moved to the garden.
## Mary moved to the kitchen.
## Daniel took the football.
## Mary journeyed to the bedroom.
## Mary grabbed the milk there.
## Mary discarded the milk.
## John went to the garden.
## John discarded the apple there.
## Sandra travelled to the bedroom.
## Daniel moved to the bathroom.
## Where was the apple before the hallway? 

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
        self.Daniel = character("Daniel")
        self.Sandra = character("Sandra")
        self.milk = object("milk")
        self.apple = object("apple")
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

    def story(self):
        ## Mary got the milk.
        self.pick_up(character = self.Mary, item = self.milk)
        ## John moved to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Daniel journeyed to the office.
        self.go(character = self.Daniel, location = "office")
        ## John grabbed the apple there.
        self.pick_up(character = self.John, item = self.apple)
        ## John got the football.
        self.pick_up(character = self.John, item = self.football)
        ## John journeyed to the garden.
        self.go(character = self.John, location = "garden")
        ## Mary left the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## John left the football.
        self.drop(character = self.John, item = self.football)
        ## Daniel moved to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel grabbed the football.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Mary moved to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Mary went to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## John put down the apple there.
        self.drop(character = self.John, item = self.apple)
        ## John picked up the apple.
        self.pick_up(character = self.John, item = self.apple)
        ## Sandra moved to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Daniel left the football there.
        self.drop(character = self.Daniel, item = self.football)
        ## Daniel took the football.
        self.pick_up(character = self.Daniel, item = self.football)
        ## John travelled to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Daniel dropped the football.
        self.drop(character = self.Daniel, item = self.football)
        ## John dropped the apple.
        self.drop(character = self.John, item = self.apple)
        ## John grabbed the apple.
        self.pick_up(character = self.John, item = self.apple)
        ## John went to the office.
        self.go(character = self.John, location = "office")
        ## Sandra went back to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Sandra took the milk.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## John journeyed to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## Sandra left the milk.
        self.drop(character = self.Sandra, item = self.milk)
        ## Mary went to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## John travelled to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Sandra moved to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Mary moved to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Daniel took the football.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Mary journeyed to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary grabbed the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Mary discarded the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## John went to the garden.
        self.go(character = self.John, location = "garden")
        ## John discarded the apple there.
        self.drop(character = self.John, item = self.apple)
        ## Sandra travelled to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Daniel moved to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Where was the apple before the hallway?
        print(self.apple.location)

world = World()
world.story()