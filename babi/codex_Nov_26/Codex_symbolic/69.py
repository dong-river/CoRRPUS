## Daniel journeyed to the hallway.
## Daniel journeyed to the garden.
## Mary went back to the kitchen.
## Daniel went back to the office.
## Mary journeyed to the bathroom.
## John moved to the hallway.
## Daniel grabbed the football there.
## Daniel went to the kitchen.
## Daniel discarded the football.
## John went to the bathroom.
## Daniel took the football there.
## John travelled to the kitchen.
## Mary travelled to the office.
## John travelled to the hallway.
## John went back to the office.
## Daniel journeyed to the bedroom.
## Daniel got the milk there.
## Daniel discarded the milk.
## Sandra went to the bathroom.
## Mary went back to the bedroom.
## Daniel took the apple there.
## Daniel dropped the football.
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
        self.apple = object("apple")
    
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
        ## Daniel journeyed to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel journeyed to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Mary went back to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Daniel went back to the office.
        self.go(character = self.Daniel, location = "office")
        ## Mary journeyed to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## John moved to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Daniel grabbed the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Daniel went to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Daniel discarded the football.
        self.drop(character = self.Daniel, item = self.football)
        ## John went to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Daniel took the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## John travelled to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary travelled to the office.
        self.go(character = self.Mary, location = "office")
        ## John travelled to the hallway.
        self.go(character = self.John, location = "hallway")
        ## John went back to the office.
        self.go(character = self.John, location = "office")
        ## Daniel journeyed to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel got the milk there.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## Daniel discarded the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## Sandra went to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Mary went back to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Daniel took the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## Daniel dropped the football.
        self.drop(character = self.Daniel, item = self.football)
        ## Where is the football?
        print(self.football.location)


world = World()
world.story()