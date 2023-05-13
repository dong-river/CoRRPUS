## After the loss of her father, Shannon is determined to follow in his footsteps and become a successful journalist.
## However, when she lands her first big story, she quickly learns that the ugly reality of life in the city is far different from the dream she imagined.
## The story is set in a large city.
## Shannon Kincaid is a young woman in her early twenties.
## She has long, brown hair and blue eyes.
## She is of average height and build.
## Jack Kincaid is Shannon’s father.
## He was a successful journalist before his untimely death.
## Mark Woodbury is Shannon’s boss at the newspaper where she works.
## He is a middle-aged man with graying hair and a mustache.

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
        self.Shannon_Kincaid = character('Shannon Kincaid')
        self.Jack_Kincaid = character('Jack Kincaid')
        self.Mark_Woodbury = character('Mark Woodbury')

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
        ## After the loss of her father, Shannon is determined to follow in his footsteps and become a successful journalist.
        self.set_occupation(self.Shannon_Kincaid, "journalist")
        self.set_relation(self.Shannon_Kincaid, 'father', self.Jack_Kincaid)
        self.set_relation(self.Jack_Kincaid, 'daughter', self.Shannon_Kincaid)
        self.set_occupation(self.Jack_Kincaid, "journalist")
        ## However, when she lands her first big story, she quickly learns that the ugly reality of life in the city is far different from the dream she imagined.
        self.set_relation(self.Shannon_Kincaid, 'boss', self.Mark_Woodbury)
        self.set_relation(self.Mark_Woodbury, 'employee', self.Shannon_Kincaid)
        ## The story is set in a large city.
        ## Shannon Kincaid is a young woman in her early twenties.
        self.set_age(self.Shannon_Kincaid, "young")
        self.set_gender(self.Shannon_Kincaid, "female")
        ## She has long, brown hair and blue eyes.
        self.set_appearance(self.Shannon_Kincaid, "long, brown hair")
        self.set_appearance(self.Shannon_Kincaid, "blue eyes")
        ## She is of average height and build.
        ## Jack Kincaid is Shannon’s father.
        ## He was a successful journalist before his untimely death.
        ## Mark Woodbury is Shannon’s boss at the newspaper where she works.
        ## He is a middle-aged man with graying hair and a mustache.
