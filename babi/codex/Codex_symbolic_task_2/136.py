## Sandra went back to the hallway.
## Mary travelled to the hallway.
## Mary picked up the football there.
## John travelled to the bathroom.
## Daniel moved to the bedroom.
## Sandra moved to the bedroom.
## Sandra travelled to the hallway.
## Sandra travelled to the office.
## Mary moved to the office.
## Mary put down the football.
## Sandra grabbed the milk there.
## Sandra left the milk.
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
        ## Sandra went back to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Mary travelled to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Mary picked up the football there.
        self.pick_up(character = self.Mary, item = self.football)
        ## John travelled to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Daniel moved to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Sandra moved to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Sandra travelled to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Sandra travelled to the office.
        self.go(character = self.Sandra, location = "office")
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## Mary put down the football.
        self.drop(character = self.Mary, item = self.football)
        ## Sandra grabbed the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Sandra left the milk.
        self.drop(character = self.Sandra, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()