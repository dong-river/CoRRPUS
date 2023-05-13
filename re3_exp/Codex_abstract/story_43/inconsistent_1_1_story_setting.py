## After losing her mom to cancer, Shannon is really struggling in her first year of college.
## She's failing all her classes and is ready to give up when she meets her RA, Jess.
## Jess is really easy to talk to and has been through a lot in her life.
## Through their talks and late night study sessions, Shannon starts to turn her life around.
## The story is set in Shannon's college dorm room and the common areas of the dorm building.
## Shannon Mulaney is a 20-year-old student at XYZ University.
## She is petite and has long curly red hair.
## Shannon is from a small town in upstate New York and is the only child of her parents.
## Jess Abernathy is a 21-year-old student at XYZ University and Shannon's RA.
## Jess is tall and has straight blond hair that she often wears in a ponytail.
## She is originally from California and is the oldest of three sisters.
## Olivia Kendall is Shannon's best friend from high school who is also attending XYZ University with her.
## Olivia is of average height with wavy brown hair and hazel eyes.

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
        self.Shannon_Mulaney = character('Shannon Mulaney')
        self.Jess_Abernathy = character('Jess Abernathy')
        self.Olivia_Kendall = character('Olivia Kendall')

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
        ## The story is set in Shannon's college dorm room and the common areas of the dorm building.
        ## Shannon Mulaney is a 20-year-old student at XYZ University.
        self.set_age(self.Shannon_Mulaney, "20")
        self.set_occupation(self.Shannon_Mulaney, "student")
        ## She is petite and has long curly red hair.
        self.set_appearance(self.Shannon_Mulaney, "petite")
        self.set_appearance(self.Shannon_Mulaney, "long curly red hair")
        ## Shannon is from a small town in upstate New York and is the only child of her parents.
        self.set_occupation(self.Shannon_Mulaney, "only child")
        ## Jess Abernathy is a 21-year-old student at XYZ University and Shannon's RA.
        self.set_age(self.Jess_Abernathy, "21")
        self.set_occupation(self.Jess_Abernathy, "student")
        self.set_occupation(self.Jess_Abernathy, "RA")
        self.set_relation(self.Jess_Abernathy, 'student', self.Shannon_Mulaney)
        ## Jess is tall and has straight blond hair that she often wears in a ponytail.
        self.set_appearance(self.Jess_Abernathy, "tall")
        self.set_appearance(self.Jess_Abernathy, "straight blond hair")
        ## She is originally from California and is the oldest of three sisters.
        self.set_occupation(self.Jess_Abernathy, "oldest of three sisters")
        ## Olivia Kendall is Shannon's best friend from high school who is also attending XYZ University with her.
        self.set_relation(self.Shannon_Mulaney, 'best friend', self.Olivia_Kendall)
        self.set_relation(self.Olivia_Kendall, 'best friend', self.Shannon_Mulaney)
        ## Olivia is of average height with wavy brown hair and hazel eyes.
        self.set_appearance(self.Olivia_Kendall, "wavy brown hair")
        self.set_appearance(self.Olivia_Kendall, "hazel eyes")
        ## After losing her mom to cancer, Shannon is really struggling in her first year of college.
        ## She's failing all her classes and is ready to give up when she meets her RA, Jess.
        ## Jess is really easy to talk to and has been through a lot in her life.
        ## Through their talks and late night study sessions, Shannon starts to turn her life around.
