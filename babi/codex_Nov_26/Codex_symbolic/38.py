## John went back to the office.
## Mary went back to the hallway.
## Daniel journeyed to the bedroom.
## Mary went back to the bathroom.
## Sandra went back to the hallway.
## Sandra got the milk there.
## Mary moved to the office.
## Mary went to the hallway.
## Daniel went to the bathroom.
## Sandra went to the office.
## John journeyed to the garden.
## Sandra journeyed to the hallway.
## Daniel moved to the office.
## Mary went back to the office.
## John moved to the kitchen.
## Sandra journeyed to the bedroom.
## Sandra went back to the office.
## Daniel moved to the kitchen.
## John took the football there.
## John left the football.
## Sandra went back to the bedroom.
## Sandra went back to the hallway.
## John grabbed the football there.
## Daniel went to the bathroom.
## John left the football.
## Sandra went back to the bedroom.
## 
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
        item.carrier = character

    def drop(self, character, item):
        character.inventory.remove(item)
        item.carrier = None

    def story(self):
        ## John went back to the office.
        self.go(character = self.John, location = "office")
        ## Mary went back to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Daniel journeyed to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Mary went back to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Sandra went back to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Sandra got the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## Mary went to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Daniel went to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Sandra went to the office.
        self.go(character = self.Sandra, location = "office")
        ## John journeyed to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra journeyed to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Daniel moved to the office.
        self.go(character = self.Daniel, location = "office")
        ## Mary went back to the office.
        self.go(character = self.Mary, location = "office")
        ## John moved to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Sandra journeyed to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel moved to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## John took the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John left the football.
        self.drop(character = self.John, item = self.football)
        ## Sandra went back to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Sandra went back to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## John grabbed the football there.
        self.pick_up(character = self.John, item = self.football)
        ## Daniel went to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## John left the football.
        self.drop(character = self.John, item = self.football)
        ## Sandra went back to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Where is the football?
        print(self.football.location)

world = World()
world.story()