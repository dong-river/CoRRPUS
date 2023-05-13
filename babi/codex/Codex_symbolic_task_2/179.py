## Mary went back to the bathroom.
## Daniel went back to the bathroom.
## Mary got the milk there.
## Mary journeyed to the kitchen.
## Mary got the apple there.
## Mary moved to the hallway.
## Mary went back to the bedroom.
## Mary moved to the kitchen.
## John journeyed to the bathroom.
## John went back to the hallway.
## John moved to the bedroom.
## Mary journeyed to the garden.
## Daniel travelled to the office.
## Daniel picked up the football there.
## Mary journeyed to the office.
## John journeyed to the bathroom.
## Daniel discarded the football.
## Mary discarded the milk.
## Mary grabbed the football there.
## Sandra went back to the bathroom.
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
        self.apple = object("apple")
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
        ## Mary went back to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Daniel went back to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Mary got the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Mary journeyed to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary got the apple there.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Mary moved to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Mary went back to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Mary moved to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## John journeyed to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John went back to the hallway.
        self.go(character = self.John, location = "hallway")
        ## John moved to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Mary journeyed to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Daniel travelled to the office.
        self.go(character = self.Daniel, location = "office")
        ## Daniel picked up the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Mary journeyed to the office.
        self.go(character = self.Mary, location = "office")
        ## John journeyed to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Daniel discarded the football.
        self.drop(character = self.Daniel, item = self.football)
        ## Mary discarded the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## Mary grabbed the football there.
        self.pick_up(character = self.Mary, item = self.football)
        ## Sandra went back to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()