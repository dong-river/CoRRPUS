## Mary moved to the hallway.
## Mary journeyed to the kitchen.
## Sandra moved to the office.
## Daniel journeyed to the office.
## Mary travelled to the bedroom.
## Mary went back to the garden.
## Sandra moved to the kitchen.
## Daniel went back to the bedroom.
## Mary went to the office.
## Mary moved to the garden.
## John moved to the hallway.
## John travelled to the bedroom.
## John moved to the office.
## Daniel journeyed to the bathroom.
## Sandra picked up the milk there.
## Sandra moved to the office.
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
        ## Mary moved to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Mary journeyed to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Sandra moved to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel journeyed to the office.
        self.go(character = self.Daniel, location = "office")
        ## Mary travelled to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary went back to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Sandra moved to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Daniel went back to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Mary went to the office.
        self.go(character = self.Mary, location = "office")
        ## Mary moved to the garden.
        self.go(character = self.Mary, location = "garden")
        ## John moved to the hallway.
        self.go(character = self.John, location = "hallway")
        ## John travelled to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## John moved to the office.
        self.go(character = self.John, location = "office")
        ## Daniel journeyed to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Sandra picked up the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Sandra moved to the office.
        self.go(character = self.Sandra, location = "office")
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()