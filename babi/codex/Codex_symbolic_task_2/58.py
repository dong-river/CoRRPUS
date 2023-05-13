## John went to the bathroom.
## Daniel travelled to the kitchen.
## John journeyed to the kitchen.
## Daniel journeyed to the hallway.
## Sandra travelled to the kitchen.
## Mary moved to the office.
## Daniel went back to the office.
## Sandra went back to the bathroom.
## John grabbed the milk there.
## John grabbed the apple there.
## Sandra journeyed to the office.
## Mary went to the hallway.
## John went to the bathroom.
## John discarded the apple.
## John put down the milk.
## John picked up the apple there.
## Daniel went back to the bathroom.
## John took the milk there.
## Daniel travelled to the garden.
## Sandra journeyed to the bathroom.
## John travelled to the kitchen.
## Mary went back to the office.
## Mary moved to the hallway.
## John left the milk.
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
        self.John = character("John")
        self.Daniel = character("Daniel")
        self.Sandra = character("Sandra")
        self.Mary = character("Mary")
        self.milk = object("milk")
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
        ## John went to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Daniel travelled to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## John journeyed to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Daniel journeyed to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Sandra travelled to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## Daniel went back to the office.
        self.go(character = self.Daniel, location = "office")
        ## Sandra went back to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John grabbed the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## John grabbed the apple there.
        self.pick_up(character = self.John, item = self.apple)
        ## Sandra journeyed to the office.
        self.go(character = self.Sandra, location = "office")
        ## Mary went to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John went to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John discarded the apple.
        self.drop(character = self.John, item = self.apple)
        ## John put down the milk.
        self.drop(character = self.John, item = self.milk)
        ## John picked up the apple there.
        self.pick_up(character = self.John, item = self.apple)
        ## Daniel went back to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## John took the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## Daniel travelled to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Sandra journeyed to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John travelled to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary went back to the office.
        self.go(character = self.Mary, location = "office")
        ## Mary moved to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John left the milk.
        self.drop(character = self.John, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()