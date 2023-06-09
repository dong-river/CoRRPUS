## Daniel journeyed to the office.
## John took the football there.
## John discarded the football.
## John travelled to the garden.
## Daniel travelled to the garden.
## Sandra went to the garden.
## Daniel travelled to the kitchen.
## Daniel moved to the office.
## Mary grabbed the milk there.
## Daniel journeyed to the bedroom.
## John travelled to the office.
## Daniel travelled to the bathroom.
## John travelled to the kitchen.
## Mary travelled to the garden.
## Mary dropped the milk.
## John went back to the garden.
## Sandra got the milk there.
## Sandra put down the milk.
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
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Mary = character("Mary")
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
        ## Daniel journeyed to the office.
        self.go(character = self.Daniel, location = "office")
        ## John took the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John discarded the football.
        self.drop(character = self.John, item = self.football)
        ## John travelled to the garden.
        self.go(character = self.John, location = "garden")
        ## Daniel travelled to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Sandra went to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Daniel travelled to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Daniel moved to the office.
        self.go(character = self.Daniel, location = "office")
        ## Mary grabbed the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Daniel journeyed to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John travelled to the office.
        self.go(character = self.John, location = "office")
        ## Daniel travelled to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## John travelled to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary travelled to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Mary dropped the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## John went back to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra got the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Sandra put down the milk.
        self.drop(character = self.Sandra, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()