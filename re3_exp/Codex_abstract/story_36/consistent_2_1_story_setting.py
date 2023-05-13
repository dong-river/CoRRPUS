## The last thing Karen remembers before she blacks out is the sound of her daughter crying for help.
## When she comes to, she's in the hospital with no recollection of what happened.
## The police are at her bedside, telling her that her daughter is dead and that she is the prime suspect.
## The story is set in a hospital room.
## Karen Fletcher is a middle-aged woman with blonde hair and blue eyes.
## She is of average height and build.
## Kate Fletcher is Karen's teenage daughter.
## She is tall and slender with dark hair and brown eyes.
## Julia Fletcher is Karen's mother-in-law who is in her late 60s/early 70s, thin and frail with grey hair and blue eyes, Julia is bedridden and uses a wheelchair to get around.

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
        self.set_relation(self.Karen_Fletcher, 'daughter', self.Kate_Fletcher)
        self.set_relation(self.Kate_Fletcher, 'mother', self.Karen_Fletcher)
        ## The story is set in a hospital room.
        ## Karen Fletcher is a middle-aged woman with blonde hair and blue eyes.
        self.set_age(self.Karen_Fletcher, "middle-aged")
        self.set_appearance(self.Karen_Fletcher, "blonde hair")
        self.set_appearance(self.Karen_Fletcher, "blue eyes")
        self.set_gender(self.Karen_Fletcher, "female")
        ## She is of average height and build.
        self.set_appearance(self.Karen_Fletcher, "average height")
        self.set_appearance(self.Karen_Fletcher, "average build")
        ## Kate Fletcher is Karen's teenage daughter.
        self.set_age(self.Kate_Fletcher, "teenage")
        ## She is tall and slender with dark hair and brown eyes.
        self.set_appearance(self.Kate_Fletcher, "tall")
        self.set_appearance(self.Kate_Fletcher, "slender")
        self.set_appearance(self.Kate_Fletcher, "dark hair")
        self.set_appearance(self.Kate_Fletcher, "brown eyes")
        self.set_gender(self.Kate_Fletcher, "female")
        ## Julia Fletcher is Karen's mother-in-law who is in her late 60s/early 70s, thin and frail with grey hair and blue eyes, Julia is bedridden and uses a wheelchair to get around.
        self.set_relation(self.Karen_Fletcher, 'mother_in_law', self.Julia_Fletcher)
        self.set_relation(self.Julia_Fletcher, 'daughter_in_law', self.Karen_Fletcher)
        self.set_age(self.Julia_Fletcher, "late 60s/early 70s")
        self.set_appearance(self.Julia_Fletcher, "thin")
        self.set_appearance(self.Julia_Fletcher, "frail")
        self.set_appearance(self.Julia_Fletcher, "grey hair")
        self.set_appearance(self.Julia_Fletcher, "blue eyes")
        self.set_appearance(self.Julia_Fletcher, "bedridden")
        self.set_appearance(self.Julia_Fletcher, "uses a wheelchair to get around")
        self.set_gender(self.Julia_Fletcher, "female")
