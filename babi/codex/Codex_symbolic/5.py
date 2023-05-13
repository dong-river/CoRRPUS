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
## Where was the apple before the bathroom? 

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
        self.history = []

    def go(self, character, location):
        character.location = location
        for item in character.inventory:
            item.location = location
        self.history.append(character.name + " moved to the " + location + ".")

    def pick_up(self, character, item):
        character.inventory.append(item)
        item.location = character.location
        item.carrier = character
        self.history.append(character.name + " picked up the " + item.name + ".")

    def drop(self, character, item):
        character.inventory.remove(item)
        item.location = character.location
        item.carrier = None
        self.history.append(character.name + " dropped the " + item.name + ".")

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
        ## Where was the apple before the bathroom?
        for event in reversed(self.history):
            if "apple" in event:
                print(event)
                break


world = World()
world.story()