## Daniel moved to the bedroom.
## Daniel went to the bathroom.
## John moved to the garden.
## Mary travelled to the bedroom.
## Sandra travelled to the garden.
## Daniel journeyed to the garden.
## Sandra travelled to the hallway.
## John got the football there.
## John moved to the bathroom.
## Sandra travelled to the bathroom.
## Daniel moved to the bedroom.
## Daniel travelled to the kitchen.
## Mary moved to the hallway.
## Sandra travelled to the office.
## Daniel moved to the hallway.
## Daniel went back to the kitchen.
## John went back to the hallway.
## Daniel went back to the hallway.
## Daniel went to the bedroom.
## John moved to the kitchen.
## Mary moved to the office.
## John went back to the garden.
## Sandra took the apple there.
## Daniel went to the office.
## Mary went back to the kitchen.
## Mary went to the bedroom.
## John journeyed to the bathroom.
## Sandra went back to the hallway.
## Sandra moved to the bedroom.
## Daniel moved to the garden.
## John went back to the bedroom.
## Mary went back to the office.
## John moved to the kitchen.
## John grabbed the milk there.
## Daniel journeyed to the bedroom.
## John discarded the football.
## John left the milk.
## John took the milk there.
## John picked up the football there.
## John put down the football.
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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.Mary = character("Mary")
        self.Sandra = character("Sandra")
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
        ## Daniel moved to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel went to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## John moved to the garden.
        self.go(character = self.John, location = "garden")
        ## Mary travelled to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## Sandra travelled to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Daniel journeyed to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Sandra travelled to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## John got the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John moved to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Sandra travelled to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## Daniel moved to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## Daniel travelled to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## Mary moved to the hallway.
        self.go(character = self.Mary, location = "hallway")
        ## Sandra travelled to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel moved to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel went back to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## John went back to the hallway.
        self.go(character = self.John, location = "hallway")
        ## Daniel went back to the hallway.
        self.go(character = self.Daniel, location = "hallway")
        ## Daniel went to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John moved to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## John went back to the garden.
        self.go(character = self.John, location = "garden")
        ## Sandra took the apple there.
        self.pick_up(character = self.Sandra, item = self.apple)
        ## Daniel went to the office.
        self.go(character = self.Daniel, location = "office")
        ## Mary went back to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary went to the bedroom.
        self.go(character = self.Mary, location = "bedroom")
        ## John journeyed to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## Sandra went back to the hallway.
        self.go(character = self.Sandra, location = "hallway")
        ## Sandra moved to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## Daniel moved to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## John went back to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Mary went back to the office.
        self.go(character = self.Mary, location = "office")
        ## John moved to the kitchen.
        self.go(character = self.John, location = "kitchen")
        ## John grabbed the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## Daniel journeyed to the bedroom.
        self.go(character = self.Daniel, location = "bedroom")
        ## John discarded the football.
        self.drop(character = self.John, item = self.football)
        ## John left the milk.
        self.drop(character = self.John, item = self.milk)
        ## John took the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## John picked up the football there.
        self.pick_up(character = self.John, item = self.football)
        ## John put down the football.
        self.drop(character = self.John, item = self.football)

        ## Where is the football?
        print(self.football.location)
world = World()
world.story()

## Daniel moved to the bedroom.
## Daniel went to the bathroom.
## John moved to the garden.
## Mary travelled to the bedroom.
## Sandra travelled to the garden.
## Daniel journeyed to the garden.
## Sandra travelled to the hallway.
## John got the football there.
## John moved to the bathroom.
## Sandra travelled to the bathroom.
## Daniel moved to the bedroom.
## Daniel travelled to the kitchen.
## Mary moved to the hallway.
## Sandra travelled to the office.
## Daniel moved to the hallway.
## Daniel went back to the kitchen.
## John went back to the hallway.
## Daniel went back to the hallway.
## Daniel went to the bedroom.
## John moved to the kitchen.
## Mary moved to the office.
## John went back to the garden.
## Sandra took the apple there.
## Daniel went to the office.
## Mary went back to the kitchen.
## Mary went to the bedroom.
## John journeyed to the bathroom.
## Sandra went back to the hallway.
## Sandra moved to the bedroom.
## Daniel moved to the garden.
## John went back to the bedroom.
## Mary went back to the office.
## John moved to the kitchen.
## John grabbed the milk there.
## Daniel journeyed to the bedroom.
## John discarded the football.
## John left the milk.
## John took the milk there.
## John picked up the football there.
## John put down the football.
## 
## Where is the football? 


world = World()
world.story()