## Sandra moved to the garden.
## Daniel took the apple there.
## Daniel dropped the apple.
## Sandra travelled to the office.
## John moved to the kitchen.
## Sandra moved to the garden.
## Daniel went back to the bathroom.
## Mary travelled to the hallway.
## Sandra went to the bathroom.
## John went back to the bedroom.
## Mary moved to the garden.
## John picked up the apple there.
## John went back to the kitchen.
## John went back to the garden.
## Mary went to the office.
## Daniel went to the bedroom.
## John went to the bathroom.
## John dropped the apple.
## 
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
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.Mary = character("Mary")
        self.John = character("John")
        self.apple = object("apple")
    
    def go(self, character, location):
        character.location = location
        for item in character.inventory:
            item.location = location

    def pick_up(self, character, item):
        character.inventory.append(item)
        item.carrier = character

    def drop(self, character, item):
        character.inventory.remove(item)
        item.carrier = None

    def story(self):
        ## Sandra moved to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Daniel took the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## Daniel dropped the apple.
        self.drop(character = self.Daniel, item = self.apple)
        ## Sandra travelled to the office.
        self.go(character = self.Sandra, location = "office")
        ## John moved to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Sandra moved to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Daniel went back to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Mary travelled to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Sandra went to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John went back to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Mary moved to the garden.
        self.go(character = self.Mary, location = "garden")
        ## John picked up the apple there.
        self.pick_up(character = self.John, item = self.apple)
        ## John went back to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## John went back to the garden.
        self.go(character = self.John, location = "garden")
        ## Mary went to the office.
        self.go(character = self.Mary, location = "office")
        ## Daniel went to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John went to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John dropped the apple.
        self.drop(character = self.John, item = self.apple)
        ## 
        ## Where is the apple? 
        print(self.apple.location)

world = World()
world.story()