## Daniel moved to the office.
## Daniel travelled to the bedroom.
## John took the milk there.
## John travelled to the garden.
## Sandra moved to the office.
## Daniel went back to the office.
## 
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
        self.Daniel = character("Daniel")
        self.Sandra = character("Sandra")
        self.John = character("John")
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
        ## Daniel moved to the office.
        self.go(character = self.Daniel, location = "office")
        ## Daniel travelled to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John took the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## John travelled to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra moved to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel went back to the office.
        self.go(character = self.Daniel, location = "office")
        ## Where is the milk? 
        print(self.milk.location)

world = World()
world.story()