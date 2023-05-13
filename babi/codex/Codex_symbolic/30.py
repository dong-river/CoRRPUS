## Mary went back to the garden.
## John went back to the hallway.
## Daniel went back to the bedroom.
## Daniel got the milk.
## Daniel put down the milk.
## Daniel got the milk.
## Daniel dropped the milk.
## Mary picked up the apple.
## Daniel went to the hallway.
## John went back to the office.
## John moved to the bedroom.
## Daniel travelled to the office.
## Mary discarded the apple.
## John took the milk.
## Mary went to the office.
## Sandra went to the bathroom.
## Sandra went back to the office.
## Sandra moved to the garden.
## Sandra grabbed the apple there.
## John travelled to the hallway.
## Daniel went back to the garden.
## Sandra moved to the bathroom.
## John grabbed the football.
## Daniel went to the hallway.
## Sandra went to the hallway.
## Sandra moved to the office.
## Sandra moved to the kitchen.
## Sandra left the apple there.
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

    def story(self):
        ## Mary went back to the garden.
        self.go(character = self.Mary, location = "garden")
        ## John went back to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Daniel went back to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel got the milk.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## Daniel put down the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## Daniel got the milk.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## Daniel dropped the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## Mary picked up the apple.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Daniel went to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## John went back to the office.
        self.go(character = self.John, location = "office")
        ## John moved to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Daniel travelled to the office.
        self.go(character = self.Daniel, location = "office")
        ## Mary discarded the apple.
        self.drop(character = self.Mary, item = self.apple)
        ## John took the milk.
        self.pick_up(character = self.John, item = self.milk)
        ## Mary went to the office.
        self.go(character = self.Mary, location = "office")
        ## Sandra went to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Sandra moved to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Sandra grabbed the apple there.
        self.pick_up(character = self.Sandra, item = self.apple)
        ## John travelled to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Daniel went back to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Sandra moved to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John grabbed the football.
        self.pick_up(character = self.John, item = self.football)
        ## Daniel went to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Sandra went to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Sandra moved to the office.
        self.go(character = self.Sandra, location = "office")
        ## Sandra moved to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Sandra left the apple there.
        self.drop(character = self.Sandra, item = self.apple)
        ## Where was the apple before the hallway? 
        print(self.apple.location)

world = World()
world.story()