## Mary journeyed to the bathroom.
## Sandra went to the garden.
## Daniel went back to the garden.
## Daniel went to the office.
## Sandra grabbed the milk there.
## Sandra put down the milk there.
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
        self.milk = object("milk")

    def story(self):
        ## Mary journeyed to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra went to the garden.
        self.Sandra.location = "garden"
        ## Daniel went back to the garden.
        self.Daniel.location = "garden"
        ## Daniel went to the office.
        self.Daniel.location = "office"
        ## Sandra grabbed the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra put down the milk there.
        self.milk.location = "office"
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()