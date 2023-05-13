## John travelled to the bathroom.
## John travelled to the hallway.
## Mary picked up the milk there.
## Mary went back to the bedroom.
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
        self.milk = object("milk")

    def story(self):
        ## John travelled to the bathroom.
        self.John.location = "bathroom"
        ## John travelled to the hallway.
        self.John.location = "hallway"
        ## Mary picked up the milk there.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Mary went back to the bedroom.
        self.Mary.location = "bedroom"
        self.milk.location = "bedroom"
        ## Where is the milk?
        print(self.milk.location)
world = World()
world.story()