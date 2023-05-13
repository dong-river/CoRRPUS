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
        ## Where is the milk? 
        print(self.milk.location)

world = World()
world.story()