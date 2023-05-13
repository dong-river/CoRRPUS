## Mary picked up the apple there.
## Mary dropped the apple.
## Daniel went back to the garden.
## Mary journeyed to the office.
## John got the football there.
## Mary went back to the kitchen.
## Daniel picked up the milk there.
## John travelled to the bedroom.
## John moved to the hallway.
## John discarded the football.
## Daniel dropped the milk.
## John got the football there.
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
        self.football = object("football")
        self.apple = object("apple")
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
        ## Mary moved to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Sandra journeyed to the bedroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Mary got the football there.
        self.pick_up(character = self.Mary, item = self.football)
        ## John went to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary went back to the garden.
        self.go(character = self.Mary, location = "garden")
        ## Where is the football?
        print(self.football.location)
        ## Mary picked up the apple there.
        self.pick_up(character = self.Mary, item = self.apple)
        ## Mary dropped the apple.
        self.drop(character = self.Mary, item = self.apple)
        ## Daniel went back to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Mary journeyed to the office.
        self.go(character = self.Mary, location = "office")
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## Mary went back to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Daniel picked up the milk there.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## John travelled to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## John moved to the hallway.
        self.go(character = self.John, location = "hallway")
        ## John discarded the football.
        self.drop(character = self.John, item = self.football)
        ## Daniel dropped the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## Where is the milk?
        print(self.milk.location)
 


world = World()
world.story()