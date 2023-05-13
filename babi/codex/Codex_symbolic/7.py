## John went back to the kitchen.
## Daniel picked up the milk.
## Sandra went back to the bedroom.
## Mary moved to the garden.
## Sandra got the apple.
## Mary journeyed to the office.
## Mary journeyed to the garden.
## Sandra went to the hallway.
## Daniel moved to the bedroom.
## Sandra grabbed the football.
## Daniel discarded the milk.
## John journeyed to the garden.
## John went to the hallway.
## Mary journeyed to the office.
## John journeyed to the bedroom.
## Sandra moved to the garden.
## John travelled to the garden.
## Daniel grabbed the milk.
## Mary journeyed to the bathroom.
## Daniel dropped the milk.
## Daniel went to the office.
## Daniel travelled to the garden.
## John went back to the bedroom.
## Sandra discarded the football.
## Mary went back to the hallway.
## John journeyed to the garden.
## Daniel went back to the hallway.
## John went to the bedroom.
## Sandra travelled to the bathroom.
## John moved to the hallway.
## Daniel travelled to the kitchen.
## Daniel journeyed to the bedroom.
## John journeyed to the office.
## Mary travelled to the garden.
## Daniel went to the hallway.
## Daniel went to the garden.
## Daniel travelled to the hallway.
## Mary journeyed to the bathroom.
## John travelled to the kitchen.
## Sandra dropped the apple.
## Sandra grabbed the apple there.
## Mary went to the office.
## Sandra left the apple there.
## Daniel went to the bedroom.
## Sandra went back to the bedroom.
## Mary travelled to the hallway.
## Mary went to the office.
## Sandra took the milk.
## Mary went to the bathroom.
## John moved to the bathroom.
## Daniel moved to the kitchen.
## Mary grabbed the apple.
## Daniel moved to the office.
## Sandra went to the kitchen.
## Sandra went back to the office.
## Mary dropped the apple.
## Sandra dropped the milk.
## John went to the kitchen.
## Daniel grabbed the milk.
## Mary picked up the apple.
## Sandra went back to the hallway.
## Daniel journeyed to the hallway.
## John moved to the bedroom.
## John went to the bathroom.
## Daniel discarded the milk there.
## Mary moved to the kitchen.
## Mary journeyed to the office.
## Daniel got the milk.
## John moved to the garden.
## Sandra travelled to the kitchen.
## Mary put down the apple.
## John took the football.
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
        ## John went back to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Daniel picked up the milk.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## Sandra went back to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Mary moved to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Sandra got the apple.
        self.pick_up(character = self.Sandra, item = self.apple)
        ## Mary journeyed to the office.
        self.go(character = self.Mary, location = "office")
        ## Mary journeyed to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Sandra went to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Daniel moved to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Sandra grabbed the football.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Daniel discarded the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## John journeyed to the garden.
        self.go(character = self.John, location = "garden")
        ## John went to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Mary journeyed to the office.
        self.go(character = self.Mary, location = "office")
        ## John journeyed to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra moved to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## John travelled to the garden.
        self.go(character = self.John, location = "garden")
        ## Daniel grabbed the milk.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## Mary journeyed to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Daniel dropped the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## Daniel went to the office.
        self.go(character = self.Daniel, location = "office")
        ## Daniel travelled to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## John went back to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra discarded the football.
        self.drop(character = self.Sandra, item = self.football)
        ## Mary went back to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John journeyed to the garden.
        self.go(character = self.John, location = "garden")
        ## Daniel went back to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## John went to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra travelled to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John moved to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Daniel travelled to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Daniel journeyed to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John journeyed to the office.
        self.go(character = self.John, location = "office")
        ## Mary travelled to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Daniel went to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel travelled to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Mary journeyed to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## John travelled to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Sandra dropped the apple.
        self.drop(character = self.Sandra, item = self.apple)
        ## Sandra grabbed the apple there.
        self.pick_up(character = self.Sandra, item = self.apple)
        ## Mary went to the office.
        self.go(character = self.Mary, location = "office")
        ## Sandra left the apple there.
        self.drop(character = self.Sandra, item = self.apple)
        ## Daniel went to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Sandra went back to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Mary travelled to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Mary went to the office.
        self.go(character = self.Mary, location = "office")
        ## Sandra took the milk.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Mary went to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## John moved to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Daniel moved to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Mary grabbed the apple.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Daniel moved to the office.
        self.go(character = self.Daniel, location = "office")
        ## Sandra went to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Mary dropped the apple.
        self.drop(character = self.Mary, item = self.apple)
        ## Sandra dropped the milk.
        self.drop(character = self.Sandra, item = self.milk)
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Daniel grabbed the milk.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## Mary picked up the apple.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Sandra went back to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Daniel journeyed to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## John moved to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## John went to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Daniel discarded the milk there.
        self.drop(character = self.Daniel, item = self.milk)
        ## Mary moved to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary journeyed to the office.
        self.go(character = self.Mary, location = "office")
        ## Daniel got the milk.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## John moved to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra travelled to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Mary put down the apple.
        self.drop(character = self.Mary, item = self.apple)
        ## John took the football.
        self.pick_up(character = self.John, item = self.football)
        ## Where was the apple before the office? 
        print(self.apple.location)

world = World()
world.story()