## Mary travelled to the bathroom.
## John took the milk there.
## Sandra moved to the hallway.
## Sandra grabbed the football there.
## Daniel went back to the bedroom.
## Daniel travelled to the kitchen.
## Sandra put down the football.
## John moved to the bedroom.
## Mary journeyed to the hallway.
## John dropped the milk.
## Mary travelled to the bathroom.
## Mary moved to the kitchen.
## Daniel travelled to the bedroom.
## Daniel travelled to the bathroom.
## Sandra grabbed the football there.
## Sandra left the football.
## Where is the football? 

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
        ## Mary travelled to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## John took the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## Sandra moved to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Sandra grabbed the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Daniel went back to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel travelled to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Sandra put down the football.
        self.drop(character = self.Sandra, item = self.football)
        ## John moved to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Mary journeyed to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## John dropped the milk.
        self.drop(character = self.John, item = self.milk)
        ## Mary travelled to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Mary moved to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Daniel travelled to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel travelled to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Sandra grabbed the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Sandra left the football.
        self.drop(character = self.Sandra, item = self.football)
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()