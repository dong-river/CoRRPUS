## Daniel took the milk there.
## John journeyed to the garden.
## Daniel went back to the hallway.
## Daniel journeyed to the bathroom.
## Daniel dropped the milk.
## Daniel took the milk there.
## John grabbed the apple there.
## Sandra journeyed to the kitchen.
## John went to the hallway.
## Sandra went back to the garden.
## Daniel journeyed to the kitchen.
## Sandra journeyed to the bedroom.
## Daniel went back to the hallway.
## Sandra went back to the kitchen.
## Sandra went back to the bathroom.
## John went to the kitchen.
## Sandra got the football there.
## Sandra went to the kitchen.
## Daniel left the milk.
## Sandra put down the football.
## Sandra picked up the football there.
## Sandra put down the football.
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
        ## Daniel took the milk there.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## John journeyed to the garden.
        self.go(character = self.John, location = "garden")
        ## Daniel went back to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel journeyed to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Daniel dropped the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## Daniel took the milk there.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## John grabbed the apple there.
        self.pick_up(character = self.John, item = self.apple)
        ## Sandra journeyed to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## John went to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Sandra went back to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Daniel journeyed to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Sandra journeyed to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Daniel went back to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Sandra went back to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Sandra went back to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Sandra got the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Sandra went to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Daniel left the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## Sandra put down the football.
        self.drop(character = self.Sandra, item = self.football)
        ## Sandra picked up the football there.
        self.pick_up(character = self.Sandra, item = self.football)
        ## Sandra put down the football.
        self.drop(character = self.Sandra, item = self.football)
        ## 
        ## Where is the football? 
        print(self.football.location)

world = World()
world.story()