## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the bathroom.
## John got the football there.
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
        ## Mary got the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## John moved to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra went back to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## How many objects is Mary carrying?
        print(len(self.Mary.inventory))

world = World()
world.story()