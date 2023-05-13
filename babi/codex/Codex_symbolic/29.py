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
## Sandra grabbed the football.
## John took the apple.
## Mary travelled to the hallway.
## Mary journeyed to the office.
## Sandra discarded the football.
## John put down the apple there.
## Mary went to the bathroom.
## Daniel picked up the football.
## Daniel travelled to the bathroom.
## Mary moved to the kitchen.
## John took the apple.
## John moved to the kitchen.
## Daniel went back to the office.
## John left the apple there.
## Mary picked up the apple there.
## Mary dropped the apple.
## Daniel went back to the bedroom.
## John moved to the hallway.
## Mary went back to the garden.
## Mary travelled to the bedroom.
## Mary travelled to the kitchen.
## John journeyed to the bedroom.
## Daniel journeyed to the kitchen.
## Daniel got the apple there.
## Sandra moved to the office.
## Sandra journeyed to the bedroom.
## Daniel went to the garden.
## John went back to the bathroom.
## Mary moved to the hallway.
## Mary journeyed to the kitchen.
## Sandra moved to the office.
## Daniel journeyed to the office.
## Mary travelled to the bedroom.
## Daniel put down the football there.
## Sandra journeyed to the bathroom.
## Daniel left the apple there.
## John moved to the bedroom.
## Sandra journeyed to the office.
## Sandra got the football.
## Mary went back to the hallway.
## Where was the apple before the office? 

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
        self.football = object("football")
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
        self.go(character = self.John, location = "hallway")
        self.go(character = self.Mary, location = "office")
        self.pick_up(character = self.Mary, item = self.milk)
        self.go(character = self.John, location = "garden")
        self.go(character = self.Daniel, location = "kitchen")
        self.drop(character = self.Mary, item = self.milk)
        self.go(character = self.John, location = "bathroom")
        self.go(character = self.Daniel, location = "hallway")
        self.pick_up(character = self.John, item = self.apple)
        self.go(character = self.Daniel, location = "office")
        self.pick_up(character = self.Daniel, item = self.milk)
        self.drop(character = self.John, item = self.apple)
        self.go(character = self.Daniel, location = "garden")
        self.drop(character = self.Daniel, item = self.milk)
        self.go(character = self.Mary, location = "garden")
        self.go(character = self.Daniel, location = "office")
        self.go(character = self.Mary, location = "bedroom")
        self.go(character = self.Mary, location = "garden")
        self.pick_up(character = self.John, item = self.football)
        self.pick_up(character = self.John, item = self.apple)
        self.drop(character = self.John, item = self.football)
        self.go(character = self.John, location = "office")
        self.go(character = self.Sandra, location = "bathroom")
        self.pick_up(character = self.Sandra, item = self.football)
        self.go(character = self.Sandra, location = "office")
        self.go(character = self.Daniel, location = "bedroom")
        self.go(character = self.Mary, location = "hallway")
        self.go(character = self.Daniel, location = "hallway")
        self.go(character = self.Sandra, location = "bedroom")
        self.drop(character = self.Sandra, item = self.football)
        self.drop(character = self.John, item = self.apple)
        self.pick_up(character = self.Sandra, item = self.football)
        self.pick_up(character = self.John, item = self.apple)
        self.go(character = self.Mary, location = "bedroom")
        self.go(character = self.Sandra, location = "bedroom")
        self.drop(character = self.Sandra, item = self.football)
        self.go(character = self.John, location = "bathroom")
        self.go(character = self.Mary, location = "bathroom")
        self.pick_up(character = self.Daniel, item = self.football)
        self.go(character = self.Daniel, location = "bathroom")
        self.go(character = self.Mary, location = "kitchen")
        self.pick_up(character = self.John, item = self.apple)
        self.go(character = self.John, location = "kitchen")
        self.go(character = self.Daniel, location = "office")
        self.drop(character = self.John, item = self.apple)
        self.go(character = self.Mary, location = "hallway")
        self.go(character = self.Mary, location = "kitchen")
        self.go(character = self.Sandra, location = "office")
        self.go(character = self.Daniel, location = "kitchen")
        self.pick_up(character = self.Daniel, item = self.apple)
        self.go(character = self.Sandra, location = "bedroom")
        self.go(character = self.Daniel, location = "office")
        self.go(character = self.Mary, location = "bedroom")
        self.go(character = self.Daniel, location = "garden")
        self.drop(character = self.Daniel, item = self.football)
        self.go(character = self.Sandra, location = "bathroom")
        self.go(character = self.Daniel, location = "office")
        self.drop(character = self.Daniel, item = self.apple)
        self.go(character = self.John, location = "bedroom")
        self.go(character = self.Sandra, location = "office")
        self.pick_up(character = self.Sandra, item = self.football)
        self.go(character = self.Mary, location = "hallway")
        print(self.apple.location)

world = World()
world.story()