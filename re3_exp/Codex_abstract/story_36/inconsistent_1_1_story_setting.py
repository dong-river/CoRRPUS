## The last thing Karen remembers before she blacks out is the sound of her daughter crying for help.
## When she comes to, she's in the hospital with no recollection of what happened.
## The police are at her bedside, telling her that her daughter is dead and that she is the prime suspect.
## The story is set in a hospital room.
## Karen Fletcher is a middle-aged woman with blonde hair and blue eyes.
## She is of average height and build.
## Kate Fletcher is Karen's teenage daughter.
## She is tall and slender with dark hair and brown eyes.
## Julia Fletcher is Karen's younger sister.
## She is shorter than Karen with light brown hair and green eyes.

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
        self.Karen_Fletcher = character('Karen Fletcher')
        self.Kate_Fletcher = character('Kate Fletcher')
        self.Julia_Fletcher = character('Julia Fletcher')

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
        ## The last thing Karen remembers before she blacks out is the sound of her daughter crying for help.
        ## When she comes to, she's in the hospital with no recollection of what happened.
        ## The police are at her bedside, telling her that her daughter is dead and that she is the prime suspect.
        ## The story is set in a hospital room.
        ## Karen Fletcher is a middle-aged woman with blonde hair and blue eyes.
        self.set_appearance(self.Karen_Fletcher, "middle-aged")
        self.set_appearance(self.Karen_Fletcher, "blonde hair")
        self.set_appearance(self.Karen_Fletcher, "blue eyes")
        ## She is of average height and build.
        self.set_appearance(self.Karen_Fletcher, "average height")
        self.set_appearance(self.Karen_Fletcher, "average build")
        ## Kate Fletcher is Karen's teenage daughter.
        self.set_relation(self.Karen_Fletcher, 'daughter', self.Kate_Fletcher)
        self.set_relation(self.Kate_Fletcher, 'mother', self.Karen_Fletcher)
        ## She is tall and slender with dark hair and brown eyes.
        self.set_appearance(self.Kate_Fletcher, "tall")
        self.set_appearance(self.Kate_Fletcher, "slender")
        self.set_appearance(self.Kate_Fletcher, "dark hair")
        self.set_appearance(self.Kate_Fletcher, "brown eyes")
        ## Julia Fletcher is Karen's younger sister.
        self.set_relation(self.Karen_Fletcher, 'younger sister', self.Julia_Fletcher)
        self.set_relation(self.Julia_Fletcher, 'older sister', self.Karen_Fletcher)
        ## She is shorter than Karen with light brown hair and green eyes.
        self.set_appearance(self.Julia_Fletcher, "shorter than Karen")
        self.set_appearance(self.Julia_Fletcher, "light brown hair")
        self.set_appearance(self.Julia_Fletcher, "green eyes")
