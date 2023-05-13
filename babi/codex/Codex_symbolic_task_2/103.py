## Mary moved to the bathroom.
## Sandra went to the kitchen.
## John travelled to the bedroom.
## Mary journeyed to the kitchen.
## Mary moved to the office.
## Sandra travelled to the bathroom.
## John travelled to the bathroom.
## John journeyed to the office.
## John took the milk there.
## Daniel travelled to the garden.
## Mary went to the kitchen.
## Daniel journeyed to the bathroom.
## John discarded the milk.
## Sandra went back to the kitchen.
## Daniel journeyed to the office.
## Sandra went back to the office.
## Daniel picked up the milk there.
## Sandra went back to the bedroom.
## John went to the garden.
## Daniel travelled to the kitchen.
## John journeyed to the bedroom.
## Sandra journeyed to the garden.
## Sandra moved to the kitchen.
## Daniel discarded the milk.
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
        ## Mary moved to the bathroom.
        self.go(character = self.Mary, location = "bathroom")
        ## Sandra journeyed to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## John travelled to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Mary journeyed to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Mary moved to the office.
        self.go(character = self.Mary, location = "office")
        ## Sandra travelled to the bathroom.
        self.go(character = self.Sandra, location = "bathroom")
        ## John travelled to the bathroom.
        self.go(character = self.John, location = "bathroom")
        ## John journeyed to the office.
        self.go(character = self.John, location = "office")
        ## John took the milk there.
        self.pick_up(character = self.John, item = self.milk)
        ## Daniel travelled to the garden.
        self.go(character = self.Daniel, location = "garden")
        ## Mary went to the kitchen.
        self.go(character = self.Mary, location = "kitchen")
        ## Daniel journeyed to the bathroom.
        self.go(character = self.Daniel, location = "bathroom")
        ## John discarded the milk.
        self.drop(character = self.John, item = self.milk)
        ## Sandra went back to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Daniel journeyed to the office.
        self.go(character = self.Daniel, location = "office")
        ## Sandra went back to the office.
        self.go(character = self.Sandra, location = "office")
        ## Daniel picked up the milk there.
        self.pick_up(character = self.Daniel, item = self.milk)
        ## Sandra went back to the bedroom.
        self.go(character = self.Sandra, location = "bedroom")
        ## John went to the garden.
        self.go(character = self.John, location = "garden")
        ## Daniel travelled to the kitchen.
        self.go(character = self.Daniel, location = "kitchen")
        ## John journeyed to the bedroom.
        self.go(character = self.John, location = "bedroom")
        ## Sandra journeyed to the garden.
        self.go(character = self.Sandra, location = "garden")
        ## Sandra moved to the kitchen.
        self.go(character = self.Sandra, location = "kitchen")
        ## Daniel discarded the milk.
        self.drop(character = self.Daniel, item = self.milk)
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()