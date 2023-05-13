## Daniel moved to the bathroom.
## John got the football.
## Sandra grabbed the milk.
## Sandra put down the milk.
## Daniel journeyed to the bedroom.
## Sandra took the milk.
## Sandra put down the milk there.
## John put down the football.
## Mary travelled to the hallway.
## John took the football.
## Sandra went back to the office.
## Mary moved to the garden.
## Daniel moved to the garden.
## Daniel went back to the office.
## Sandra journeyed to the hallway.
## Mary went to the office.
## Sandra went back to the office.
## Sandra moved to the bathroom.
## John dropped the football.
## Sandra got the football.
## Sandra left the football there.
## Daniel moved to the bedroom.
## Daniel journeyed to the office.
## John went back to the office.
## Sandra got the football.
## Sandra discarded the football.
## Mary travelled to the bathroom.
## Mary got the football.
## Mary went back to the kitchen.
## Mary journeyed to the garden.
## Mary journeyed to the bedroom.
## Mary took the milk.
## John went to the kitchen.
## Mary travelled to the garden.
## John grabbed the apple.
## John discarded the apple.
## John travelled to the garden.
## Mary went to the bedroom.
## Mary discarded the milk.
## John went back to the office.
## Mary went back to the bathroom.
## Mary journeyed to the garden.
## Where was the milk before the bedroom? 

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
        self.Daniel = character("Daniel")
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
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
        ## Daniel moved to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## John got the football.
        self.pick_up(character = self.John, item = self.football)
        ## Sandra grabbed the milk.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Sandra put down the milk.
        self.drop(character = self.Sandra, item = self.milk)
        ## Daniel journeyed to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Sandra took the milk.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Sandra put down the milk there.
        self.drop(character = self.Sandra, item = self.milk)
        ## John put down the football.
        self.drop(character = self.John, item = self.football)
        ## Mary travelled to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John took the football.
        self.pick_up(character = self.John, item = self.football)
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Mary moved to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Daniel moved to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel went back to the office.
        self.go(character = self.Daniel, location = "office")
        ## Sandra journeyed to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Mary went to the office.
        self.go(character = self.Mary, location = "office")
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Sandra moved to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John dropped the football.
        self.drop(character = self.John, item = self.football)
        ## Sandra got the football.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Sandra left the football there.
        self.drop(character = self.Sandra, item = self.football)
        ## Daniel moved to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel journeyed to the office.
        self.go(character = self.Daniel, location = "office")
        ## John went back to the office.
        self.go(character = self.John, location = "office")
        ## Sandra got the football.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Sandra discarded the football.
        self.drop(character = self.Sandra, item = self.football)
        ## Mary travelled to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Mary got the football.
        self.pick_up(character = self.Mary, item = self.football)
        ## Mary went back to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary journeyed to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Mary journeyed to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary took the milk.
        self.pick_up(character = self.Mary, item = self.milk)
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary travelled to the garden.
        self.go(character = self.Mary, location = "garden")
        ## John grabbed the apple.
        self.pick_up(character = self.John, item = self.apple)
        ## John discarded the apple.
        self.drop(character = self.John, item = self.apple)
        ## John travelled to the garden.
        self.go(character = self.John, location = "garden")
        ## Mary went to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary discarded the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## John went back to the office.
        self.go(character = self.John, location = "office")
        ## Mary went back to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Mary journeyed to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Where was the milk before the bedroom?
        print(self.milk.location)

world = World()
world.story()