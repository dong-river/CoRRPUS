## Sandra journeyed to the garden.
## Sandra travelled to the bathroom.
## Daniel went back to the garden.
## Sandra got the apple there.
## Mary travelled to the bedroom.
## John went to the hallway.
## Sandra travelled to the office.
## Mary grabbed the milk there.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.apple = object("apple")
        self.milk = object("milk")
        
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
        ## Sandra journeyed to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Sandra travelled to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Daniel went back to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Sandra got the apple there.
        self.pick_up(character = self.Sandra, item = self.apple)
        ## Mary travelled to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## John went to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Sandra travelled to the office.
        self.go(character = self.Sandra, location = "office")
        ## Mary grabbed the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Where is the apple?
        print(self.apple.location)
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()