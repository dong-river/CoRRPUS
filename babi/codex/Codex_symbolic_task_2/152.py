## Daniel travelled to the garden.
## Sandra went back to the bedroom.
## John travelled to the bedroom.
## Sandra grabbed the apple there.
## Daniel travelled to the kitchen.
## Sandra left the apple.
## Sandra travelled to the office.
## Sandra went back to the bathroom.
## John travelled to the bathroom.
## Daniel went back to the hallway.
## Where is the apple? 

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
        self.Sandra = character("Sandra")
        self.John = character("John")
        self.apple = object("apple")
    
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
        ## Daniel travelled to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Sandra went back to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## John travelled to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra grabbed the apple there.
        self.pick_up(character = self.Sandra, item = self.apple)
        ## Daniel travelled to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Sandra left the apple.
        self.drop(character = self.Sandra, item = self.apple)
        ## Sandra travelled to the office.
        self.go(character = self.Sandra, location = "office")
        ## Sandra went back to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John travelled to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Daniel went back to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Where is the apple?
        print(self.apple.location)
world = World()
world.story()