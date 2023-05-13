## Sandra took the football there.
## Mary travelled to the kitchen.
## John went to the office.
## Daniel travelled to the bedroom.
## Daniel journeyed to the bathroom.
## Mary went back to the bedroom.
## Sandra travelled to the kitchen.
## Mary went to the bathroom.
## Sandra went back to the bathroom.
## Sandra discarded the football.
## Mary journeyed to the bedroom.
## Sandra picked up the football there.
## Mary grabbed the milk there.
## Mary discarded the milk.
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

    def story(self):
        ## Sandra took the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Mary travelled to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## John went to the office.
        self.go(character = self.John, location = "office")
        ## Daniel travelled to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel journeyed to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Mary went back to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Sandra travelled to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Mary went to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Sandra went back to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Sandra discarded the football.
        self.drop(character = self.Sandra, item = self.football)
        ## Mary journeyed to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Sandra picked up the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Mary grabbed the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Mary discarded the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()