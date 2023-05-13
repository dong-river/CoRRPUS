## At thirty-six years old, Payton's biological clock is ticking, but she's never found the right person to have children with.
## She's always been a career woman, and she's not sure she's ready to give up her freedom.
## When her best friend from college dies unexpectedly, leaving behind a four-year-old daughter, Payton is faced with the decision of whether or not to take on the responsibility of raising her.
## The story is set in New York City.
## Payton Dupree is a 36-year-old successful businesswoman.
## She has never been married and does not have any children.
## She is fiercely independent and has always put her career first.
## Amanda Dupree is Payton's deceased best friend from college.
## She was a stay-at-home mom and died suddenly, leaving behind her 4-year-old daughter Olivia.
## Olivia Dupree is Payton's niece and Amanda's daughter.
## She is a 4-year-old girl who is shy and introverted.

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
        self.Payton_Dupree = character('Payton Dupree')
        self.Amanda_Dupree = character('Amanda Dupree')
        self.Olivia_Dupree = character('Olivia Dupree')

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
        ## The story is set in New York City.
        ## Payton Dupree is a 36-year-old successful businesswoman.
        self.set_occupation(self.Payton_Dupree, "successful businesswoman")
        self.set_age(self.Payton_Dupree, "36")
        ## She has never been married and does not have any children.
        self.set_relation(self.Payton_Dupree, 'married', self.Amanda_Dupree)
        self.set_relation(self.Amanda_Dupree, 'wife', self.Payton_Dupree)
        self.set_relation(self.Payton_Dupree, 'children', self.Olivia_Dupree)
        self.set_relation(self.Olivia_Dupree, 'mother', self.Payton_Dupree)
        self.set_relation(self.Olivia_Dupree, 'father', self.Amanda_Dupree)
        self.set_relation(self.Amanda_Dupree, 'children', self.Olivia_Dupree)
        ## She is fiercely independent and has always put her career first.
        self.set_appearance(self.Payton_Dupree, "fiercely independent")
        ## Amanda Dupree is Payton's deceased best friend from college.
        self.set_relation(self.Payton_Dupree, 'best friend', self.Amanda_Dupree)
        self.set_relation(self.Amanda_Dupree, 'best friend', self.Payton_Dupree)
        ## She was a stay-at-home mom and died suddenly, leaving behind her 4-year-old daughter Olivia.
        self.set_occupation(self.Amanda_Dupree, "stay-at-home mom")
        self.set_age(self.Amanda_Dupree, "died suddenly")
        ## Olivia Dupree is Payton's niece and Amanda's daughter.
        self.set_relation(self.Payton_Dupree, 'niece', self.Olivia_Dupree)
        self.set_relation(self.Olivia_Dupree, 'aunt', self.Payton_Dupree)
        self.set_relation(self.Amanda_Dupree, 'daughter', self.Olivia_Dupree)
        self.set_relation(self.Olivia_Dupree, 'mother', self.Amanda_Dupree)
        ## She is a 4-year-old girl who is shy and introverted.
        self.set_age(self.Olivia_Dupree, "4")
        self.set_gender(self.Olivia_Dupree, "girl")
        self.set_appearance(self.Olivia_Dupree, "shy and introverted")
