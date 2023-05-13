## Sandra took the milk there.
## Sandra journeyed to the garden.
## Sandra dropped the milk there.
## Sandra journeyed to the bathroom.
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
        self.Sandra = character("Sandra")
        self.milk = object("milk")

    def story(self):
        ## Sandra took the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra journeyed to the garden.
        self.Sandra.location = "garden"
        ## Sandra dropped the milk there.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "garden"
        ## Sandra journeyed to the bathroom.
        self.Sandra.location = "bathroom"
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()