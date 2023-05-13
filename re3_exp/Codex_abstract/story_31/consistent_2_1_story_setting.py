## After the death of her father, a young woman moves to a small town to start a new life.
## She quickly learns that the town is full of secrets, and that her father's death may not have been an accident.
## The story is set in a small town in the middle of nowhere.
## Riley Harper is a young woman in her early twenties.
## She has long, dark hair and hazel eyes.
## She is of average height and build.
## Chase Elliott is a young man in his early twenties who works at the local gas station.
## He has dark hair and brown eyes and is of average height and build."
## Jonas Harper is Riley's late father.
## He was a successful businessman who died suddenly in a car accident.

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
        self.Riley_Harper = character('Riley Harper')
        self.Chase_Elliott = character('Chase Elliott')
        self.Jonas_Harper = character('Jonas Harper')

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
        ## After the death of her father, a young woman moves to a small town to start a new life.
        self.set_relation(self.Riley_Harper, 'father', self.Jonas_Harper)
        self.set_relation(self.Jonas_Harper, 'daughter', self.Riley_Harper)
        self.set_age(self.Riley_Harper, "young")
        self.set_gender(self.Riley_Harper, "female")
        ## She quickly learns that the town is full of secrets, and that her father's death may not have been an accident.
        ## The story is set in a small town in the middle of nowhere.
        ## Riley Harper is a young woman in her early twenties.
        self.set_age(self.Riley_Harper, "early twenties")
        ## She has long, dark hair and hazel eyes.
        self.set_appearance(self.Riley_Harper, "long, dark hair and hazel eyes")
        ## She is of average height and build.
        self.set_appearance(self.Riley_Harper, "average height and build")
        ## Chase Elliott is a young man in his early twenties who works at the local gas station.
        self.set_age(self.Chase_Elliott, "early twenties")
        self.set_occupation(self.Chase_Elliott, "local gas station")
        ## He has dark hair and brown eyes and is of average height and build."
        self.set_appearance(self.Chase_Elliott, "dark hair and brown eyes")
        self.set_appearance(self.Chase_Elliott, "average height and build")
        ## Jonas Harper is Riley's late father.
        self.set_age(self.Jonas_Harper, "late")
        ## He was a successful businessman who died suddenly in a car accident.
        self.set_occupation(self.Jonas_Harper, "successful businessman")
        self.set_appearance(self.Jonas_Harper, "car accident")
        self.set_appearance(self.Jonas_Harper, "sudden death")
