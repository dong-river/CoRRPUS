## Daniel moved to the bathroom.
## John got the football.
## Sandra grabbed the milk.
## Sandra put down the milk.
## Daniel journeyed to the bedroom.
## Sandra took the milk.
## Sandra put down the milk there.
## John put down the football.
## Mary travelled to the hallway.
## John took the football.
## Sandra went back to the office.
## Mary moved to the garden.
## Daniel moved to the garden.
## Daniel went back to the office.
## Sandra journeyed to the hallway.
## Mary went to the office.
## Sandra went back to the office.
## Sandra moved to the bathroom.
## John dropped the football.
## Sandra got the football.
## Sandra left the football there.
## Daniel moved to the bedroom.
## Daniel journeyed to the office.
## John went back to the office.
## Sandra got the football.
## Sandra discarded the football.
## Mary travelled to the bathroom.
## Mary got the football.
## Mary went back to the kitchen.
## Mary journeyed to the garden.
## Mary journeyed to the bedroom.
## Mary took the milk.
## Where was the football before the garden? 

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
        ## Daniel moved to the bathroom.
        self.Daniel.location = "bathroom"
        ## John got the football.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Sandra grabbed the milk.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra put down the milk.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        ## Daniel journeyed to the bedroom.
        self.Daniel.location = "bedroom"
        ## Sandra took the milk.
        self.Sandra.inventory.append(self.milk)
        self.milk.carrier = self.Sandra
        ## Sandra put down the milk there.
        self.Sandra.inventory.remove(self.milk)
        self.milk.carrier = None
        self.milk.location = "bedroom"
        ## John put down the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"
        ## John took the football.
        self.John.inventory.append(self.football)
        self.football.carrier = self.John
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Mary moved to the garden.
        self.Mary.location = "garden"
        ## Daniel moved to the garden.
        self.Daniel.location = "garden"
        ## Daniel went back to the office.
        self.Daniel.location = "office"
        ## Sandra journeyed to the hallway.
        self.Sandra.location = "hallway"
        ## Mary went to the office.
        self.Mary.location = "office"
        ## Sandra went back to the office.
        self.Sandra.location = "office"
        ## Sandra moved to the bathroom.
        self.Sandra.location = "bathroom"
        ## John dropped the football.
        self.John.inventory.remove(self.football)
        self.football.carrier = None
        ## Sandra got the football.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Sandra left the football there.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        self.football.location = "bathroom"
        ## Daniel moved to the bedroom.
        self.Daniel.location = "bedroom"
        ## Daniel journeyed to the office.
        self.Daniel.location = "office"
        ## John went back to the office.
        self.John.location = "office"
        ## Sandra got the football.
        self.Sandra.inventory.append(self.football)
        self.football.carrier = self.Sandra
        ## Sandra discarded the football.
        self.Sandra.inventory.remove(self.football)
        self.football.carrier = None
        ## Mary travelled to the bathroom.
        self.Mary.location = "bathroom"
        ## Mary got the football.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        ## Mary journeyed to the garden.
        self.Mary.location = "garden"
        ## Mary journeyed to the bedroom.
        self.Mary.location = "bedroom"
        ## Mary took the milk.
        self.Mary.inventory.append(self.milk)
        self.milk.carrier = self.Mary
        ## Where was the football before the garden? 
        print(self.football.location)

world = World()
world.story()