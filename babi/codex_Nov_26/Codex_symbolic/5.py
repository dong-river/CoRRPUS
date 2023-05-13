## Mary journeyed to the bathroom.
## Sandra went to the garden.
## Daniel went back to the garden.
## Daniel went to the office.
## Sandra grabbed the milk there.
## Sandra put down the milk there.
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
        self.Mary = character("Mary")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
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
        ## Mary journeyed to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Sandra went to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Daniel went back to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel went to the office.
        self.go(character = self.Daniel, location = "office")
        ## Sandra grabbed the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Sandra put down the milk there.
        self.drop(character = self.Sandra, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()