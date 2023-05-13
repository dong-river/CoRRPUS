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
        ## He lives in a small town called Grandview, and he has been there for his entire life.
        self.set_appearance(self.Chase_Elliott, "small town")
        ## Jonas Harper was a rich man who owned his own business and drove a nice car.
        self.set_occupation(self.Jonas_Harper, "rich man")
        self.set_occupation(self.Jonas_Harper, "own business")
        self.set_appearance(self.Jonas_Harper, "nice car")
        ## He came from a small town called Resting Ridge, and he loved to drive on country roads.
        self.set_appearance(self.Jonas_Harper, "small town")
        self.set_appearance(self.Jonas_Harper, "country roads")
        ## Jonas Harper died in a car accident.
        ## His daughter Riley lives far away from Grandview, but she comes for her father's funeral.
        self.set_relation(self.Jonas_Harper, 'daughter', self.Riley_Harper)
        self.set_relation(self.Riley_Harper, 'father', self.Jonas_Harper)
        self.set_appearance(self.Riley_Harper, "far away from Grandview")
        self.set_appearance(self.Riley_Harper, "comes for father's funeral")
