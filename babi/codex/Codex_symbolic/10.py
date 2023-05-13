## Sandra moved to the bathroom.
## John picked up the football.
## John dropped the football.
## Daniel went to the kitchen.
## Daniel got the apple.
## John went to the kitchen.
## Mary went back to the hallway.
## Daniel travelled to the office.
## John travelled to the garden.
## John journeyed to the kitchen.
## Mary moved to the kitchen.
## Daniel moved to the garden.
## Mary journeyed to the bathroom.
## Daniel grabbed the milk.
## Mary went to the hallway.
## Mary got the football there.
## Mary dropped the football.
## Sandra moved to the bedroom.
## Mary went back to the office.
## John travelled to the office.
## Mary went back to the bathroom.
## John moved to the hallway.
## Sandra went to the office.
## Mary journeyed to the kitchen.
## Sandra travelled to the garden.
## John went back to the garden.
## Sandra went back to the office.
## Mary went to the hallway.
## Daniel went to the bedroom.
## Mary picked up the football there.
## John travelled to the kitchen.
## Mary moved to the bedroom.
## Sandra went to the bathroom.
## Daniel put down the milk.
## Daniel discarded the apple.
## Mary took the milk.
## Where was the apple before the bedroom? 

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
        ## Sandra moved to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John picked up the football.
        self.pick_up(character = self.John, item = self.football)
        ## John dropped the football.
        self.drop(character = self.John, item = self.football)
        ## Daniel went to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Daniel got the apple.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary went back to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Daniel travelled to the office.
        self.go(character = self.Daniel, location = "office")
        ## John travelled to the garden.
        self.go(character = self.John, location = "garden")
        ## John journeyed to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary moved to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Daniel moved to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Mary journeyed to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Daniel grabbed the milk.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## Mary went to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Mary got the football there.
        self.pick_up(character = self.Mary, item = self.football)
        ## Mary dropped the football.
        self.drop(character = self.Mary, item = self.football)
        ## Sandra moved to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Mary went back to the office.
        self.go(character = self.Mary, location = "office")
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## Mary went back to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## John moved to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Sandra went to the office.
        self.go(character = self.Sandra, location = "office")
        ## Mary journeyed to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Sandra travelled to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## John went back to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Mary went to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Daniel went to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Mary picked up the football there.
        self.pick_up(character = self.Mary, item = self.football)
        ## John travelled to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary moved to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Sandra went to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Daniel put down the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## Daniel discarded the apple.
        self.drop(character = self.Daniel, item = self.apple)
        ## Mary took the milk.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Where was the apple before the bedroom? 
        print(self.apple.location)

world = World()
world.story()