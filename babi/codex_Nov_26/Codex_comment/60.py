## Daniel moved to the office.
## Daniel travelled to the bedroom.
## John took the milk there.
## John travelled to the garden.
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
        self.Daniel = character("Daniel")
        self.John = character("John")
        self.milk = object("milk")

    def story(self):
        ## Daniel moved to the office.
        self.Daniel.location = "office"
        ## Daniel travelled to the bedroom.
        self.Daniel.location = "bedroom"
        ## John took the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        ## John travelled to the garden.
        self.John.location = "garden"
        ## 
        ## Where is the milk?
        print(self.milk.location)
 

world = World()
world.story()