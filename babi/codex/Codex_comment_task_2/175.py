## Mary went back to the bathroom.
## Daniel went back to the bathroom.
## Mary got the milk there.
## Mary journeyed to the kitchen.
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
        self.Daniel = character("Daniel")
        self.milk = object("milk")

    def story(self):
        ## Mary went back to the bathroom.
        self.Mary.location = "bathroom"
        ## Daniel went back to the bathroom.
        self.Daniel.location = "bathroom"
        ## Mary got the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Mary journeyed to the kitchen.
        self.Mary.location = "kitchen"
        self.milk.location = "kitchen"
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()