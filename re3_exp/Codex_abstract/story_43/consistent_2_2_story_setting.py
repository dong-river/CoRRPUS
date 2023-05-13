## After losing her mom to cancer, Shannon is really struggling in her first year of college.
## She's failing all her classes and is ready to give up when she meets her RA, Jess.
## Jess is really easy to talk to and has been through a lot in her life.
## Through their talks and late night study sessions, Shannon starts to turn her life around.
## The story is set in Shannon's college dorm room and the common areas of the dorm building.
## Shannon Mulaney is an 18 year old from Michigan and is attending XYZ university in Boston, Massachusetts on a full softball scholarship (XYZ being a large Division 1 universities in Boston with over 30,000 students).
## Shannon is 5'10" with wavy brown/blonde ombre/roots (which she dyes herself), blue eyes, pale skin, and an athletic build (somewhat muscular, especially in legs/thighs).
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
        ## After losing her mom to cancer, Shannon is really struggling in her first year of college.
        ## She's failing all her classes and is ready to give up when she meets her RA, Jess.
        ## Jess is really easy to talk to and has been through a lot in her life.
        ## Through their talks and late night study sessions, Shannon starts to turn her life around.
        ## The story is set in Shannon's college dorm room and the common areas of the dorm building.
        ## Shannon Mulaney is an 18 year old from Michigan and is attending XYZ university in Boston, Massachusetts on a full softball scholarship (XYZ being a large Division 1 universities in Boston with over 30,000 students).
        self.set_age(self.Shannon_Mulaney, '18')
        self.set_occupation(self.Shannon_Mulaney, 'student')
        self.set_gender(self.Shannon_Mulaney, 'female')
        ## Shannon is 5'10" with wavy brown/blonde ombre/roots (which she dyes herself), blue eyes, pale skin, and an athletic build (somewhat muscular, especially in legs/thighs).
        self.set_appearance(self.Shannon_Mulaney, '5\'10"')
        self.set_appearance(self.Shannon_Mulaney, 'wavy brown/blonde ombre/roots')
        self.set_appearance(self.Shannon_Mulaney, 'blue eyes')
        self.set_appearance(self.Shannon_Mulaney, 'pale skin')
        self.set_appearance(self.Shannon_Mulaney, 'athletic build')
        ## Jess Abernathy is a 21-year-old student at XYZ University and Shannon's RA.
        self.set_age(self.Jess_Abernathy, '21')
        self.set_occupation(self.Jess_Abernathy, 'student')
        self.set_gender(self.Jess_Abernathy, 'female')
        ## Jess is tall and has straight blond hair that she often wears in a ponytail.
        self.set_appearance(self.Jess_Abernathy, 'tall')
        self.set_appearance(self.Jess_Abernathy, 'straight blond hair')
        ## She is originally from California and is the oldest of three sisters.
        ## Olivia Kendall is Shannon's best friend from high school who is also attending XYZ University with her.
        ## Olivia is of average height with wavy brown hair and hazel eyes.
        
        self.set_age(self.Olivia_Kendall, '18')
        self.set_occupation(self.Olivia_Kendall, 'student')
        self.set_gender(self.Olivia_Kendall, 'female')
        self.set_appearance(self.Olivia_Kendall, 'average height')
        self.set_appearance(self.Olivia_Kendall, 'wavy brown hair')
        self.set_appearance(self.Olivia_Kendall, 'hazel eyes')
        
        
 
        
## Create a world model state to track each character's appearance, personality, and relations with other characters.

