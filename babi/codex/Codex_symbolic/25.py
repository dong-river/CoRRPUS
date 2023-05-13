## John went to the hallway.
## Mary went back to the office.
## Mary got the milk.
## John journeyed to the garden.
## Daniel went to the kitchen.
## Mary put down the milk.
## John travelled to the bathroom.
## Daniel went back to the hallway.
## John took the apple.
## Daniel journeyed to the office.
## Daniel grabbed the milk.
## John discarded the apple.
## Daniel went to the garden.
## Daniel dropped the milk.
## Mary travelled to the garden.
## Daniel travelled to the office.
## Mary travelled to the bedroom.
## Mary moved to the garden.
## John picked up the football.
## John picked up the apple.
## John left the football.
## John moved to the office.
## Sandra travelled to the bathroom.
## Sandra got the football.
## Sandra travelled to the office.
## Daniel went back to the bedroom.
## Mary went back to the office.
## Daniel travelled to the hallway.
## Mary went back to the hallway.
## Sandra moved to the bedroom.
## Daniel moved to the bedroom.
## Sandra moved to the bathroom.
## John dropped the apple.
## John picked up the apple.
## Mary went back to the bedroom.
## Sandra went to the bedroom.
## Sandra dropped the football there.
## John dropped the apple.
## Where was the football before the bedroom? 

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
        ## John went to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Mary went back to the office.
        self.go(character = self.Mary, location = "office")
        ## Mary got the milk.
        self.pick_up(character = self.Mary, item = self.milk)
        ## John journeyed to the garden.
        self.go(character = self.John, location = "garden")
        ## Daniel went to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Mary put down the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## John travelled to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Daniel went back to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## John took the apple.
        self.pick_up(character = self.John, item = self.apple)
        ## Daniel journeyed to the office.
        self.go(character = self.Daniel, location = "office")
        ## Daniel grabbed the milk.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## John discarded the apple.
        self.drop(character = self.John, item = self.apple)
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel dropped the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## Mary travelled to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Daniel travelled to the office.
        self.go(character = self.Daniel, location = "office")
        ## Mary travelled to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary moved to the garden.
        self.go(character = self.Mary, location = "garden")
        ## John picked up the football.
        self.pick_up(character = self.John, item = self.football)
        ## John picked up the apple.
        self.pick_up(character = self.John, item = self.apple)
        ## John left the football.
        self.drop(character = self.John, item = self.football)
        ## John moved to the office.
        self.go(character = self.John, location = "office")
        ## Sandra travelled to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Sandra got the football.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Sandra travelled to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel went back to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Mary went back to the office.
        self.go(character = self.Mary, location = "office")
        ## Daniel travelled to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Mary went back to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Sandra moved to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Daniel moved to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Sandra moved to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John dropped the apple.
        self.drop(character = self.John, item = self.apple)
        ## John picked up the apple.
        self.pick_up(character = self.John, item = self.apple)
        ## Mary went back to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Sandra went to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Sandra dropped the football there.
        self.drop(character = self.Sandra, item = self.football)
        ## John dropped the apple.
        self.drop(character = self.John, item = self.apple)
        ## Where was the football before the bedroom?
        print(self.football.location)

world = World()
world.story()