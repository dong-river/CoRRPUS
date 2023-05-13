## Daniel moved to the bathroom.
## Sandra went back to the kitchen.
## John moved to the bathroom.
## Mary picked up the milk there.
## John travelled to the garden.
## Mary dropped the milk there.
## Sandra journeyed to the bedroom.
## John journeyed to the bathroom.
## Daniel went back to the office.
## John moved to the hallway.
## Mary got the milk there.
## Daniel took the apple there.
## John picked up the football there.
## Mary went to the kitchen.
## Mary dropped the milk.
## Daniel travelled to the bedroom.
## John journeyed to the office.
## Daniel went to the garden.
## Mary picked up the milk there.
## Mary left the milk.
## John travelled to the garden.
## Mary travelled to the office.
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
        ## Daniel moved to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## Sandra went back to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## John moved to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Mary picked up the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## John travelled to the garden.
        self.go(character = self.John, location = "garden")
        ## Mary dropped the milk there.
        self.drop(character = self.Mary, item = self.milk)
        ## Sandra journeyed to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## John journeyed to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Daniel went back to the office.
        self.go(character = self.Daniel, location = "office")
        ## John moved to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Mary got the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Daniel took the apple there.
        self.pick_up(character = self.Daniel, item = self.apple)
        ## John picked up the football there.
        self.pick_up(character = self.John, item = self.football)
        ## Mary went to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary dropped the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## Daniel travelled to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John journeyed to the office.
        self.go(character = self.John, location = "office")
        ## Daniel went to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Mary picked up the milk there.
        self.pick_up(character = self.Mary, item = self.milk)
        ## Mary left the milk.
        self.drop(character = self.Mary, item = self.milk)
        ## John travelled to the garden.
        self.go(character = self.John, location = "garden")
        ## Mary travelled to the office.
        self.go(character = self.Mary, location = "office")
        ## 
        ## Where is the milk? 
        print(self.milk.location)

world = World()
world.story()