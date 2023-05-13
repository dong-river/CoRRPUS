## John travelled to the bathroom.
## John travelled to the hallway.
## Mary picked up the milk there.
## Mary went back to the bedroom.
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
        ## John travelled to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John travelled to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Mary picked up the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Mary went back to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ##
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()