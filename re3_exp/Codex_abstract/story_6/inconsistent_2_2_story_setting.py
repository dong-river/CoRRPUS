## After the loss of her father, Shannon is determined to follow in his footsteps and become a successful journalist.
## However, when she lands her first major assignment, she quickly discovers that the ugly reality of life in the city is far different from the dream she imagined.
## The story is set in a large city.
## Shannon Riley is a young woman in her early twenties.
## She has long, brown hair and blue eyes.
## She is of average height and build.
## Robert Riley is Shannon's father.
## He was a successful journalist who died suddenly of a heart attack.
## Jillian Riley is Shannon's older sister by three years.
## She is a successful corporate lawyer who lives and works in the city.

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
        self.Shannon_Riley = character('Shannon Riley')
        self.Robert_Riley = character('Robert Riley')
        self.Jillian_Riley = character('Jillian Riley')

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
        self.set_relation(self.Shannon_Riley, 'father', self.Robert_Riley)
        self.set_relation(self.Robert_Riley, 'daughter', self.Shannon_Riley)
        self.set_occupation(self.Robert_Riley, "successful journalist")
        self.set_occupation(self.Shannon_Riley, "successful journalist")
        ## However, when she lands her first major assignment, she quickly discovers that the ugly reality of life in the city is far different from the dream she imagined.
        ## The story is set in a large city.
        ## Shannon Riley is a young woman in her early twenties.
        self.set_gender(self.Shannon_Riley, "female")
        self.set_age(self.Shannon_Riley, "young")
        ## She has long, brown hair and blue eyes.
        self.set_appearance(self.Shannon_Riley, "long brown hair")
        self.set_appearance(self.Shannon_Riley, "blue eyes")
        ## She is of average height and build.
        ## Robert Riley is Shannon's father.
        ## He was a successful journalist who died suddenly of a heart attack.
        self.set_occupation(self.Robert_Riley, "successful journalist")
        ## Jillian Riley is Shannon's older sister by three years.
        self.set_relation(self.Shannon_Riley, 'older sister', self.Jillian_Riley)
        self.set_relation(self.Jillian_Riley, 'younger sister', self.Shannon_Riley)
        ## She is a successful corporate lawyer who lives and works in the city.
        self.set_occupation(self.Jillian_Riley, "successful corporate lawyer")
