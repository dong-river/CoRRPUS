gpt3_example = """
Mary moved to the bathroom.
Sandra journeyed to the bedroom.
Mary got the football there.
John went to the kitchen.
Mary went back to the garden.
Question: Where is the football?
Answer: garden
###
"""

gpt3_example_long = """
Mary moved to the bathroom.
Sandra journeyed to the bedroom.
Mary got the football there.
John went to the kitchen.
Mary went back to the kitchen.
Mary went back to the garden.
Sandra went back to the office.
John moved to the office.
Sandra journeyed to the hallway.
Daniel went back to the kitchen.
Mary dropped the football.
John got the milk there.
Mary took the football there.
Sandra picked up the apple there.
Mary travelled to the hallway.
John journeyed to the kitchen.
Question: Where is the football? 	
Answer: hallway
"""

COT_example = """ 
Below are some stories about people moving objects between rooms. After each story you have to answer a question about where a particular object is. 
Story:
at t=0, Mary moved to the bathroom.
at t=1, Sandra journeyed to the bedroom.
at t=2, Mary got the football there.
at t=3, John went to the kitchen.
at t=4, Mary went back to the garden.
Question: Where is the football?
Reasoning: At t=2, Mary got the football there. We know that at t=4, Mary went back to the garden. Therefore, the football is in the garden.
###
"""

COT_example_long = """
Below are some stories about people moving objects between rooms. After each story you have to answer a question about where a particular object is. 
Story:
at t=0, Mary moved to the bathroom.
at t=1, Sandra journeyed to the bedroom.
at t=2, Mary got the football there.
at t=3, John went to the kitchen.
at t=4, Mary went back to the kitchen.
at t=5, Mary went back to the garden.
at t=6, Sandra went back to the office.
at t=7, John moved to the office.
at t=8, Sandra journeyed to the hallway.
at t=9, Daniel went back to the kitchen.
at t=10, Mary dropped the football.
at t=11, John got the milk there.
at t=12, Mary took the football there.
at t=13, Sandra picked up the apple there.
at t=14, Mary travelled to the hallway.
at t=15, John journeyed to the kitchen.
Question: Where is the football?
Answer: At t=12, Mary took the football there. We know that at t=14,  Mary travelled to the hallway. Therefore, the football is in the hallway.
"""


SI_example_selection = """
Here are a collection of stories about people carrying objects from one room to another. You will be asked where any object is. To answer this question you need to figure out who last had the object and which room they have the object in by the end of the story. Here are some examples:
Story:
at t=0, Mary moved to the bathroom.
at t=1, Sandra journeyed to the bedroom.
at t=2, Mary got the football there.
at t=3, John went to the kitchen.
at t=4, Mary went back to the garden.
Question: Where is the football? 
Reasoning: at t=2, Mary got the football there. at t=4, Mary went back to the garden.
"""

SI_example_inference = """
at t=2, Mary got the football there. at t=4, Mary went back to the garden. Therefore, the football is in the garden.
###
"""

babi_init = """
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
"""

babi_init_task_3 = """
class character:
    def __init__(self, name):
        self.name = name
        self.location = ""
        self.inventory = []
        self.history = []

class object:
    def __init__(self, name):
        self.name = name
        self.location = ""
        self.carrier = None
        self.history = []

class World:
    def __init__(self):
"""

Codex_command_example = """
## Mary moved to the bathroom.
## Sandra journeyed to the bedroom.
## Mary got the football there.
## John went to the kitchen.
## Mary went back to the garden.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.football = object("football")

    def story(self):
        self.Mary_moved_to_the_bathroom()
        self.Sandra_journeyed_to_the_bedroom()
        self.Mary_got_the_football_there()
        self.John_went_to_the_kitchen()
        self.Mary_went_back_to_the_garden()
        self.Where_is_the_football()

    def Mary_moved_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        
    def Mary_got_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Mary_went_back_to_the_garden(self):
        self.Mary.location = "garden"
        self.football.location = "garden"
        
    def Where_is_the_football(self):
        print(self.football.location)
###
"""

Codex_command_example = """
## Mary moved to the bathroom.
## Sandra journeyed to the bedroom.
## Mary got the football there.
## John went to the kitchen.
## Mary went back to the garden.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.football = object("football")

    def story(self):
        self.Mary_moved_to_the_bathroom()
        self.Sandra_journeyed_to_the_bedroom()
        self.Mary_got_the_football_there()
        self.John_went_to_the_kitchen()
        self.Mary_went_back_to_the_garden()
        self.Where_is_the_football()

    def Mary_moved_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        for item in self.Mary.inventory:
            item.location = "bathroom"
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        for item in self.Sandra.inventory:
            item.location = "bedroom"
        
    def Mary_got_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        for item in self.John.inventory:
            item.location = "bathroom"
        
    def Mary_went_back_to_the_garden(self):
        self.Mary.location = "garden"
        for item in self.Mary.inventory:
            item.location = "garden"
        
    def Where_is_the_football(self):
        print(self.football.location)
###
"""

Codex_command_example_long = """
## Mary moved to the bathroom.
## Sandra journeyed to the bedroom.
## Mary got the football there.
## John went to the kitchen.
## Mary went back to the kitchen.
## Mary went back to the garden.
## Sandra went back to the office.
## John moved to the office.
## Sandra journeyed to the hallway.
## Daniel went back to the kitchen.
## Mary dropped the football.
## John got the milk there.
## Mary took the football there.
## Sandra picked up the apple there.
## Mary travelled to the hallway.
## John journeyed to the kitchen.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        self.Mary_moved_to_the_bathroom()
        self.Sandra_journeyed_to_the_bedroom()
        self.Mary_got_the_football_there()
        self.John_went_to_the_kitchen()
        self.Mary_went_back_to_the_kitchen()
        self.Mary_went_back_to_the_garden()
        self.Sandra_went_back_to_the_office()
        self.John_moved_to_the_office()
        self.Sandra_journeyed_to_the_hallway()
        self.Daniel_went_back_to_the_kitchen()
        self.Mary_dropped_the_football()
        self.John_got_the_milk_there()
        self.Mary_took_the_football_there()
        self.Sandra_picked_up_the_apple_there()
        self.Mary_travelled_to_the_hallway()
        self.John_journeyed_to_the_kitchen()
        self.Where_is_the_football()

    def Mary_moved_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        
    def Mary_got_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Mary_went_back_to_the_kitchen(self):
        self.Mary.location = "kitchen"
        self.football.location = "kitchen "
        
    def Mary_went_back_to_the_garden(self):
        self.Mary.location = "garden"
        self.football.location = "garden"
        
    def Sandra_went_back_to_the_office(self):
        self.Sandra.location = "office"
        
    def John_moved_to_the_office(self):
        self.John.location = "office"
        
    def Sandra_journeyed_to_the_hallway(self):
        self.Sandra.location = "hallway"
        
    def Daniel_went_back_to_the_kitchen(self):
        self.Daniel.location = "kitchen"
        
    def Mary_dropped_the_football(self):
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None

    def John_got_the_milk_there(self):
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John
        
    def Mary_took_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        
    def Sandra_picked_up_the_apple_there(self):
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra
        
    def Mary_travelled_to_the_hallway(self):
        self.Mary.location = "hallway"
        
    def John_journeyed_to_the_kitchen(self):
        self.John.location = "kitchen"
        
    def Where_is_the_football(self):
        print(self.football.location)
"""

Codex_comment_example = """
## Mary moved to the bathroom.
## Sandra journeyed to the bedroom.
## Mary got the football there.
## John went to the kitchen.
## Mary went back to the garden.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.football = object("football")

    def story(self):
        ## Mary moved to the bathroom.
        self.Mary.location = "bathroom"
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        ## Mary got the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        ## John went to the kitchen.
        self.John.location = "kitchen"
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        self.football.location = "garden"
        ## Where is the football?
        print(self.football.location)
###
"""

Codex_comment_example_long = """
## Mary moved to the bathroom.
## Sandra journeyed to the bedroom.
## Mary got the football there.
## John went to the kitchen.
## Mary went back to the kitchen.
## Mary went back to the garden.
## Sandra went back to the office.
## John moved to the office.
## Sandra journeyed to the hallway.
## Daniel went back to the kitchen.
## Mary dropped the football.
## John got the milk there.
## Mary took the football there.
## Sandra picked up the apple there.
## Mary travelled to the hallway.
## John journeyed to the kitchen.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.Daniel = character("Daniel")
        self.football = object("football")
        self.milk = object("milk")
        self.apple = object("apple")

    def story(self):
        ## Mary moved to the bathroom.
        self.Mary.location = "bathroom"

        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"

        ## Mary got the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary

        ## John went to the kitchen.
        self.John.location = "kitchen"

        ## Mary went back to the kitchen.
        self.Mary.location = "kitchen"
        self.football.location = "kitchen "

        ## Mary went back to the garden.
        self.Mary.location = "garden"
        self.football.location = "garden"

        ## Sandra went back to the office.
        self.Sandra.location = "office"

        ## John moved to the office.
        self.John.location = "office"

        ## Sandra journeyed to the hallway.
        self.Sandra.location = "hallway"

        ## Daniel went back to the kitchen.
        self.Daniel.location = "kitchen"

        ## Mary dropped the football.
        self.Mary.inventory.remove(self.football)
        self.football.carrier = None

        ## John got the milk there.
        self.John.inventory.append(self.milk)
        self.milk.carrier = self.John

        ## Mary took the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary

        ## Sandra picked up the apple there.
        self.Sandra.inventory.append(self.apple)
        self.apple.carrier = self.Sandra

        ## Mary travelled to the hallway.
        self.Mary.location = "hallway"

        ## John journeyed to the kitchen.
        self.John.location = "kitchen"

        ## Where is the football? 	
        print(self.football.location)
"""

Codex_parsed_command_srl_example = """
## Mary moved to the bathroom.
## Sandra journeyed to the bedroom.
## Mary got the football there.
## John went to the kitchen.
## Mary went back to the garden.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.football = object("football")

    def story(self):
        ## Mary moved to the bathroom.
        self.move(character = self.Mary, destination = "bathroom")
        ## Sandra journeyed to the bedroom.
        self.journey(character = self.Sandra, destination = "bedroom")
        ## Mary got the football there.
        self.got(character = self.Mary, object = self.football)
        ## John went to the kitchen.
        self.go(character = self.John, destination = "kitchen")
        ## Mary went back to the garden.
        self.go(character = self.Mary, destination = "garden")
        ## Where is the football?
        print(self.football.location)
        
    def move(self, character, destination):
        character.location = destination
        for item in character.inventory:
            item.location = destination
            
    def journey(self, character, destination):
        character.location = destination
        for item in character.inventory:
            item.location = destination
            
    def got(self, character, object):
        object.carrier = character
        character.inventory.append(object)
        
    def go(self, character, destination):
        character.location = destination
        for item in character.inventory:
            item.location = destination
###
"""

Codex_symbolic_example = """
## Mary moved to the bathroom.
## Sandra journeyed to the bedroom.
## Mary got the football there.
## John went to the kitchen.
## Mary went back to the garden.
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
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.football = object("football")
    
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
===
"""

Codex_symbolic_example_task_3 = """
## Mary moved to the bathroom.
## Sandra journeyed to the bedroom.
## Mary got the football there.
## John went to the kitchen.
## Mary went back to the garden.
## Where is the football?

class character:
    def __init__(self, name):
        self.name = name
        self.location = ""
        self.inventory = []
        self.history = []
        
class object:
    def __init__(self, name):
        self.name = name
        self.location = ""
        self.carrier = None
        self.history = []

class World:
    def __init__(self):
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.football = object("football")
    
    def go(self, character, location):
        character.location = location
        character.history.append(location)
        for item in character.inventory:
            item.location = location
            item.history.append(location)

    def pick_up(self, character, item):
        character.inventory.append(item)
        item.location = character.location
        item.carrier = character
        item.history.append(character.location)

    def drop(self, character, item):
        character.inventory.remove(item)
        item.location = character.location
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
        ## Where is the football before library?
        print("football's location history: ", self.football.history)
===
"""

Codex_command_example_task_3 = """
## Mary moved to the bathroom.
## Sandra journeyed to the bedroom.
## Mary got the football there.
## John went to the kitchen.
## Mary went back to the garden.
## Where is the football before garden?

class character:
    def __init__(self, name):
        self.name = name
        self.location = ""
        self.inventory = []
        self.history = []

class object:
    def __init__(self, name):
        self.name = name
        self.location = ""
        self.carrier = None
        self.history = []

class World:
    def __init__(self):
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.football = object("football")

    def story(self):
        self.Mary_moved_to_the_bathroom()
        self.Sandra_journeyed_to_the_bedroom()
        self.Mary_got_the_football_there()
        self.John_went_to_the_kitchen()
        self.Mary_went_back_to_the_garden()
        self.Where_is_the_football_before_garden()

    def Mary_moved_to_the_bathroom(self):
        self.Mary.location = "bathroom"
        self.Mary.history.append("bathroom")
        for item in self.Mary.inventory:
            item.location = "bathroom"
            item.history.append("bathroom")
        
    def Sandra_journeyed_to_the_bedroom(self):
        self.Sandra.location = "bedroom"
        self.Sandra.history.append("bedroom")
        for item in self.Sandra.inventory:
            item.location = "bedroom"
            item.history.append("bedroom")
        
    def Mary_got_the_football_there(self):
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        self.football.history.append("bedroom")
        
    def John_went_to_the_kitchen(self):
        self.John.location = "kitchen"
        self.John.history.append("kitchen")
        for item in self.John.inventory:
            item.location = "bathroom"
            item.history.append("bathroom")
        
    def Mary_went_back_to_the_garden(self):
        self.Mary.location = "garden"
        self.Mary.history.append("garden")
        for item in self.Mary.inventory:
            item.location = "garden"
            item.history.append("garden")
        
    def Where_is_the_football_before_library(self):
        print("football's location history: ", self.football.history)
===
"""

Codex_comment_example_task_3 = """
## Mary moved to the bathroom.
## Sandra journeyed to the bedroom.
## Mary got the football there.
## John went to the kitchen.
## Mary went back to the garden.
## Where is the football before garden?

class character:
    def __init__(self, name):
        self.name = name
        self.location = ""
        self.inventory = []
        self.history = []

class object:
    def __init__(self, name):
        self.name = name
        self.location = ""
        self.carrier = None
        self.history = []

class World:
    def __init__(self):
        self.Mary = character("Mary")
        self.John = character("John")
        self.Sandra = character("Sandra")
        self.football = object("football")

    def story(self):
        ## Mary moved to the bathroom.
        self.Mary.location = "bathroom"
        self.Mary.history.append("bathroom")
        ## Sandra journeyed to the bedroom.
        self.Sandra.location = "bedroom"
        self.Sandra.history.append("bedroom")
        ## Mary got the football there.
        self.Mary.inventory.append(self.football)
        self.football.carrier = self.Mary
        self.football.history.append("bedroom")
        ## John went to the kitchen.
        self.John.location = "kitchen"
        self.John.history.append("kitchen")
        ## Mary went back to the garden.
        self.Mary.location = "garden"
        self.Mary.history.append("garden")
        self.football.location = "garden"
        self.football.history.append("garden")
        ## Where is the football before garden?
        print("football's location history: ", self.football.history)
===
"""

gpt3_example_task_3 = """
Mary moved to the bathroom.
Sandra journeyed to the bedroom.
Mary got the football there.
John went to the kitchen.
Mary went back to the garden.
Question: Where is the football before garden?
Answer: bathroom
"""

prompt_dic = {
    '1': {"Codex_comment": Codex_comment_example, "Codex_command": Codex_command_example, "Codex_symbolic": Codex_symbolic_example, "GPT-3": gpt3_example, "COT": COT_example},
    '2': {"Codex_comment": Codex_comment_example, "Codex_command": Codex_command_example, "Codex_symbolic": Codex_symbolic_example, "GPT-3": gpt3_example, "COT": COT_example},
    '3': {"Codex_comment": Codex_comment_example_task_3, "Codex_command": Codex_command_example_task_3, "Codex_symbolic": Codex_symbolic_example_task_3, "GPT-3": gpt3_example_task_3, "COT": COT_example},
}