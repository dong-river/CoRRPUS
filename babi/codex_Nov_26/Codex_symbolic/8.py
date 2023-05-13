## Mary journeyed to the bathroom.
## Sandra went to the garden.
## Daniel went back to the garden.
## Daniel went to the office.
## Sandra grabbed the milk there.
## Sandra put down the milk there.
## Daniel went to the hallway.
## Sandra got the milk there.
## Daniel went to the garden.
## Daniel journeyed to the kitchen.
## Daniel journeyed to the bedroom.
## Mary journeyed to the garden.
## Daniel took the football there.
## Mary moved to the office.
## Sandra travelled to the bedroom.
## Daniel dropped the football.
## Sandra left the milk there.
## Daniel grabbed the football there.
## Sandra grabbed the milk there.
## Daniel went to the kitchen.
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
        self.Daniel = character("Daniel")
        self.Sandra = character("Sandra")
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
        ## Mary journeyed to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Sandra went to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Daniel went back to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel went to the office.
        self.go(character = self.Daniel, location = "office")
        ## Sandra grabbed the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Sandra put down the milk there.
        self.drop(character = self.Sandra, item = self.milk)
        ## Daniel went to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Sandra got the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Daniel journeyed to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Daniel journeyed to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Mary journeyed to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Daniel took the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## Sandra travelled to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Daniel dropped the football.
        self.drop(character = self.Daniel, item = self.football)
        ## Sandra left the milk there.
        self.drop(character = self.Sandra, item = self.milk)
        ## Daniel grabbed the football there.
        self.pick_up(character = self.Daniel, item = self.football)
        ## Sandra grabbed the milk there.
        self.pick_up(character = self.Sandra, item = self.milk)
        ## Daniel went to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## 
        ## Where is the football? 
        print(self.football.location)

world = World()
world.story()