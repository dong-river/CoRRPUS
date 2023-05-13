## Sandra went back to the hallway.
## Mary travelled to the hallway.
## Mary picked up the football there.
## John travelled to the bathroom.
## Daniel moved to the bedroom.
## Sandra moved to the bedroom.
## Sandra travelled to the hallway.
## Sandra travelled to the office.
## Mary moved to the office.
## Mary put down the football.
## Sandra grabbed the milk there.
## Sandra left the milk.
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
        self.milk = object("milk")

    def story(self):
        ## Sandra went back to the hallway.
        self.Sandra.location = "hallway"
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        ## Mary picked up the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## John travelled to the bathroom.
        self.John.location = "bathroom"
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## Sandra moved to the bedroom.
        self.Sandra.location = "bedroom"
        ## Sandra travelled to the hallway.
        self.Sandra.location = "hallway"
        ## Sandra travelled to the office.
        self.Sandra.location = "office"
        ## Mary moved to the office.
        self.Mary.location = "office"
        ## Mary put down the football.
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "office"
        ## Sandra grabbed the milk there.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra left the milk.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "office"
        ## Where is the milk?
        print(self.milk.location)

world = World()
world.story()