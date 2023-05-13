## Chase Elliott is your average guy who works at the local gas station.
## He lives in a small town called Grandview, and he has been there for his entire life.
## Jonas Harper was a rich man who owned his own business and drove a nice car.
## He came from a small town called Resting Ridge, and he loved to drive on country roads.
## Jonas Harper died in a car accident.
## His daughter Riley lives far away from Grandview, but she comes for her father's funeral."

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
        ## Chase Elliott is your average guy who works at the local gas station.
        self.set_occupation(self.Chase_Elliott, "gas station")
        self.set_gender(self.Chase_Elliott, "male")
        ## He lives in a small town called Grandview, and he has been there for his entire life.
        self.set_appearance(self.Chase_Elliott, "Grandview")
        ## Jonas Harper was a rich man who owned his own business and drove a nice car.
        self.set_occupation(self.Jonas_Harper, "business")
        self.set_appearance(self.Jonas_Harper, "car")
        self.set_gender(self.Jonas_Harper, "male")
        ## He came from a small town called Resting Ridge, and he loved to drive on country roads.
        self.set_appearance(self.Jonas_Harper, "Resting Ridge")
        ## Jonas Harper died in a car accident.
        ## His daughter Riley lives far away from Grandview, but she comes for her father's funeral."
        self.set_relation(self.Jonas_Harper, 'daughter', self.Riley_Harper)
        self.set_relation(self.Riley_Harper, 'father', self.Jonas_Harper)
        self.set_gender(self.Riley_Harper, "female")
        self.set_appearance(self.Riley_Harper, "Grandview")
        self.set_appearance(self.Riley_Harper, "Resting Ridge")
