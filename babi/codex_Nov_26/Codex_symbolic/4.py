## Mary got the milk there.
## John moved to the bedroom.
## Sandra went back to the kitchen.
## Mary travelled to the hallway.
## John got the football there.
## John went to the hallway.
## John put down the football.
## Mary went to the garden.
## John went to the kitchen.
## Sandra travelled to the hallway.
## Daniel went to the hallway.
## Mary discarded the milk.
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
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.milk = object("milk")
        self.football = object("football")

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
        ## Mary got the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## John moved to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra went back to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Mary travelled to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John went to the hallway.
        self.go(character = self.John, location = "hallway")
        ## John put down the football.
        self.drop(character = self.John, item = self.football)
        ## Mary went to the garden.
        self.go(character = self.Mary, location = "garden")
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Sandra travelled to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Daniel went to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Mary discarded the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)


world = World()
world.story()