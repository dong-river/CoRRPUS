## John travelled to the bathroom.
## John travelled to the hallway.
## Mary picked up the milk there.
## Mary went back to the bedroom.
## Sandra took the football there.
## Sandra moved to the office.
## Sandra went back to the bathroom.
## John journeyed to the bedroom.
## John went back to the bathroom.
## Sandra put down the football.
## Mary discarded the milk.
## Sandra moved to the kitchen.
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
        self.Mary = character("Mary")
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
        ## John travelled to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John travelled to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Mary picked up the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Mary went back to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Sandra took the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Sandra moved to the office.
        self.go(character = self.Sandra, location = "office")
        ## Sandra went back to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John journeyed to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## John went back to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Sandra put down the football.
        self.drop(character = self.Sandra, item = self.football)
        ## Mary discarded the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## Sandra moved to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()