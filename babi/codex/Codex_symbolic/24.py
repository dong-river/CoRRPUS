## John took the football.
## Daniel went back to the garden.
## Mary moved to the bathroom.
## Mary went to the bedroom.
## Mary went to the hallway.
## John dropped the football.
## Daniel journeyed to the hallway.
## Sandra grabbed the football.
## John moved to the office.
## Sandra put down the football.
## Sandra took the football.
## Daniel went to the bedroom.
## Mary moved to the office.
## Mary journeyed to the bedroom.
## Mary grabbed the apple there.
## Sandra went back to the kitchen.
## Sandra picked up the milk there.
## Mary discarded the apple.
## John went back to the bathroom.
## Mary got the apple.
## Mary left the apple.
## Mary took the apple.
## Mary put down the apple.
## Sandra put down the milk.
## Daniel went to the kitchen.
## Sandra journeyed to the office.
## Sandra journeyed to the bedroom.
## John moved to the garden.
## Sandra journeyed to the garden.
## Mary got the apple.
## Mary discarded the apple.
## Mary travelled to the hallway.
## Daniel went to the garden.
## Sandra went back to the hallway.
## Sandra travelled to the garden.
## Sandra went back to the office.
## Daniel went to the bathroom.
## Sandra dropped the football.
## Mary went back to the kitchen.
## Mary went back to the hallway.
## Sandra went back to the hallway.
## Mary journeyed to the bathroom.
## John travelled to the bathroom.
## Sandra journeyed to the office.
## John went to the bedroom.
## Sandra went back to the bedroom.
## John took the apple.
## John went to the office.
## Sandra travelled to the kitchen.
## John put down the apple.
## Daniel travelled to the bedroom.
## John journeyed to the bedroom.
## John went to the garden.
## Daniel went to the hallway.
## Daniel went to the office.
## Sandra grabbed the milk there.
## Mary went to the garden.
## Sandra went back to the office.
## John travelled to the office.
## Sandra journeyed to the kitchen.
## Daniel went to the garden.
## John grabbed the football.
## Sandra went to the bedroom.
## John grabbed the apple.
## Daniel went back to the bathroom.
## Daniel went back to the office.
## Mary moved to the hallway.
## Mary travelled to the kitchen.
## John discarded the football.
## John dropped the apple.
## Mary went to the hallway.
## John grabbed the apple.
## John got the football.
## Sandra put down the milk.
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
        ## John took the football.
        self.pick_up(character = self.John, item = self.football)
        ## Daniel went back to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Mary moved to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Mary went to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary went to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John dropped the football.
        self.drop(character = self.John, item = self.football)
        ## Daniel journeyed to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Sandra grabbed the football.
        self.pick_up(character = self.Sandra, item = self.football)
        ## John moved to the office.
        self.go(character = self.John, location = "office")
        ## Sandra put down the football.
        self.drop(character = self.Sandra, item = self.football)
        ## Sandra took the football.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Daniel went to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## Mary journeyed to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary grabbed the apple there.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Sandra went back to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Sandra picked up the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Mary discarded the apple.
        self.drop(character = self.Mary, item = self.apple)
        ## John went back to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Mary got the apple.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Mary left the apple.
        self.drop(character = self.Mary, item = self.apple)
        ## Mary took the apple.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Mary put down the apple.
        self.drop(character = self.Mary, item = self.apple)
        ## Sandra put down the milk.
        self.drop(character = self.Sandra, item = self.milk)
        ## Daniel went to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Sandra journeyed to the office.
        self.go(character = self.Sandra, location = "office")
        ## Sandra journeyed to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## John moved to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra journeyed to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Mary got the apple.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Mary discarded the apple.
        self.drop(character = self.Mary, item = self.apple)
        ## Mary travelled to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Sandra went back to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Sandra travelled to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel went to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Sandra dropped the football.
        self.drop(character = self.Sandra, item = self.football)
        ## Mary went back to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary went back to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Sandra went back to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Mary journeyed to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## John travelled to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Sandra journeyed to the office.
        self.go(character = self.Sandra, location = "office")
        ## John went to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra went back to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## John took the apple.
        self.pick_up(character = self.John, item = self.apple)
        ## John went to the office.
        self.go(character = self.John, location = "office")
        ## Sandra travelled to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## John put down the apple.
        self.drop(character = self.John, item = self.apple)
        ## Daniel travelled to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John journeyed to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## John went to the garden.
        self.go(character = self.John, location = "garden")
        ## Daniel went to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel went to the office.
        self.go(character = self.Daniel, location = "office")
        ## Sandra grabbed the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Mary went to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## Sandra journeyed to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## John grabbed the football.
        self.pick_up(character = self.John, item = self.football)
        ## Sandra went to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## John grabbed the apple.
        self.pick_up(character = self.John, item = self.apple)
        ## Daniel went back to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Daniel went back to the office.
        self.go(character = self.Daniel, location = "office")
        ## Mary moved to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Mary travelled to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## John discarded the football.
        self.drop(character = self.John, item = self.football)
        ## John dropped the apple.
        self.drop(character = self.John, item = self.apple)
        ## Mary went to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John grabbed the apple.
        self.pick_up(character = self.John, item = self.apple)
        ## John got the football.
        self.pick_up(character = self.John, item = self.football)
        ## Sandra put down the milk.
        self.drop(character = self.Sandra, item = self.milk)
        ## Where was the milk before the bedroom? 
        print(self.milk.location)

world = World()
world.story()