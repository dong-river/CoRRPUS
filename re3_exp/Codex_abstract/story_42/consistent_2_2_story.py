## Carl Russo parked his car in front of the police station, excited to tell his coworker and friend, John Davis, about a television show he was watching.
## The show was called 'Police Intervention', and its goal was to catch police officers on camera during a routine traffic stop who were unfairly profiling.
## "Hey, Davis!"
## Carl shouted as he burst through the front door of the police station.
## John waved at Carl from across the room.
## He stopped talking to the other cops and turned around to face Carl as he approached him.
## "Hey Russo," John said with a big smile on his face.
## "You're in a good mood today!"
## Carl dropped his things on his desk and looked at John curiously.
## "I have good news!
## And I know you'll appreciate it."
## He nodded at one of the other cops nearby and laughed when that cop made fun of him for going to UCLA instead of California State University at Northridge.
## They all shared some good-natured laughs together before they turned back towards Carl and John when they heard Carl's next sentence; "I watched this great TV show last night called 'Police Intervention'."
## "What's that?"
## one of the young rookie cops asked.
## "Like COPS?"

## Create a world model state to track each character's appearance, personality, and relations with other characters.

class character:
    def __init__(self, name):
        self.name = name
        self.appearance = []
        self.occupation = []
        self.gender = []
        self.age = []
        self.relations = {}

class World:
    def __init__(self):
        self.Valerie_Russo = character('Valerie Russo')
        self.Carl_Russo = character('Carl Russo')
        self.Antoinette_Russo = character('Antoinette Russo')

    def set_appearance(self, character, appearance):
        character.appearance.append(appearance)
    
    def set_occupation(self, character, occupation):
        character.occupation.append(occupation)
    
    def set_gender(self, character, gender):
        character.gender.append(gender)
    
    def set_age(self, character, age):
        character.age.append(age)
    
    def set_relation(self, character, relation, other_character):
        character.relations[relation] = other_character.name
        
    def story(self):
        ## Carl Russo parked his car in front of the police station, excited to tell his coworker and friend, John Davis, about a television show he was watching.
        ## The show was called 'Police Intervention', and its goal was to catch police officers on camera during a routine traffic stop who were unfairly profiling.
        ## "Hey, Davis!"
        ## Carl shouted as he burst through the front door of the police station.
        ## John waved at Carl from across the room.
        ## He stopped talking to the other cops and turned around to face Carl as he approached him.
        ## "Hey Russo," John said with a big smile on his face.
        ## "You're in a good mood today!"
        ## Carl dropped his things on his desk and looked at John curiously.
        ## "I have good news!
        ## And I know you'll appreciate it."
        ## He nodded at one of the other cops nearby and laughed when that cop made fun of him for going to UCLA instead of California State University at Northridge.
        ## They all shared some good-natured laughs together before they turned back towards Carl and John when they heard Carl's next sentence; "I watched this great TV show last night called 'Police Intervention'."
        ## "What's that?"
        ## one of the young rookie cops asked.
        ## "Like COPS?"
        self.set_occupation(self.Carl_Russo, "police")
        self.set_occupation(self.Valerie_Russo, "police")
        self.set_occupation(self.Antoinette_Russo, "police")
        self.set_relation(self.Valerie_Russo, 'mother', self.Antoinette_Russo)
        self.set_relation(self.Antoinette_Russo, 'daughter', self.Valerie_Russo)
        self.set_relation(self.Carl_Russo, 'wife', self.Valerie_Russo)
        self.set_relation(self.Valerie_Russo, 'husband', self.Carl_Russo)
        self.set_gender(self.Carl_Russo, "male")
        self.set_gender(self.Valerie_Russo, "female")
        self.set_gender(self.Antoinette_Russo, "female")
        self.set_appearance(self.Carl_Russo, "dark brown hair")
        self.set_appearance(self.Valerie_Russo, "dark brown hair")
        self.set_appearance(self.Antoinette_Russo, "dark brown hair")
        self.set_age(self.Carl_Russo, "middle-aged")
        self.set_age(self.Valerie_Russo, "middle-aged")
        self.set_age(self.Antoinette_Russo, "old")
        self.set_age(self.Carl_Russo, "middle-aged")
        self.set_age(self.Valerie_Russo, "middle-aged")
        self.set_age(self.Antoinette_Russo, "old")
        self.set_appearance(self.Carl_Russo, "dark brown hair")
        self.set_appearance(self.Valerie_Russo, "dark brown hair")
        self.set_appearance(self.Antoinette_Russo, "dark brown hair")
        self.set_age(self.Carl_Russo, "middle-aged")
        self.set_age(self.Valerie_Russo, "middle-aged")
        self.set_age(self.Antoinette_Russo, "old")
