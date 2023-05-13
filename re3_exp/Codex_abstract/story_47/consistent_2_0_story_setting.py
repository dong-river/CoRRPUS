## After the loss of her father, Shannon is determined to follow in his footsteps and become a successful journalist.
## However, when she lands her first major assignment, she quickly discovers that the ugly reality of life in the city is far different from the dream she imagined.
## The story is set in a large city.
## Shannon Burke is a young woman in her early twenties.
## She is of average height and build, with shoulder-length brown hair and hazel eyes.
## Charles Burke is Shannon's father.
## He was a successful journalist who died unexpectedly a few years ago.
## Maxine Carter is Shannon's mother, who works as a secretary to support Shannon and her sister, Jenna.

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
        self.Shannon_Burke = character('Shannon Burke')
        self.Charles_Burke = character('Charles Burke')
        self.Maxine_Carter = character('Maxine Carter')

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
        ## The story is set in a large city.
        ## Shannon Burke is a young woman in her early twenties.
        self.set_age(self.Shannon_Burke, "early twenties")
        self.set_gender(self.Shannon_Burke, "female")
        ## She is of average height and build, with shoulder-length brown hair and hazel eyes.
        self.set_appearance(self.Shannon_Burke, "average height and build")
        self.set_appearance(self.Shannon_Burke, "shoulder-length brown hair")
        self.set_appearance(self.Shannon_Burke, "hazel eyes")
        ## Charles Burke is Shannon's father.
        self.set_relation(self.Shannon_Burke, 'father', self.Charles_Burke)
        self.set_relation(self.Charles_Burke, 'daughter', self.Shannon_Burke)
        ## He was a successful journalist who died unexpectedly a few years ago.
        self.set_occupation(self.Charles_Burke, "journalist")
        ## Maxine Carter is Shannon's mother, who works as a secretary to support Shannon and her sister, Jenna.
        self.set_relation(self.Shannon_Burke, 'mother', self.Maxine_Carter)
        self.set_relation(self.Maxine_Carter, 'daughter', self.Shannon_Burke)
        self.set_occupation(self.Maxine_Carter, "secretary")
