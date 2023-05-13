## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the bathroom.
## John got the football there.
## Mary journeyed to the bathroom.
## Mary gave the milk to Sandra.
## How many objects is Mary carrying? 

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

    def give(self, character1, item, character2):
        character1.inventory.remove(item)
        character2.inventory.append(item)
        item.carrier = character2

    def story(self):
        ## Mary got the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## John moved to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra went back to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## Mary journeyed to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Mary gave the milk to Sandra.
        self.give(character1 = self.Mary, item = self.milk, character2 = self.Sandra)
        ## How many objects is Mary carrying? 
        print(len(self.Mary.inventory))

world = World()
world.story()