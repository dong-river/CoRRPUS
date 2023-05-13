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

    def story(self):
        ## After losing her mom to cancer, Shannon is really struggling in her first year of college.
        self.Shannon_Mulaney.relations['mom'] = 'deceased'
        self.Shannon_Mulaney.relations['cancer'] = 'deceased'
        self.Shannon_Mulaney.age.append('18')
        ## She's failing all her classes and is ready to give up when she meets her RA, Jess.
        self.Shannon_Mulaney.relations['RA'] = 'Jess_Abernathy'
        self.Jess_Abernathy.relations['student'] = 'Shannon_Mulaney'
        ## Jess is really easy to talk to and has been through a lot in her life.
        self.Jess_Abernathy.relations['life'] = 'tough'
        ## Through their talks and late night study sessions, Shannon starts to turn her life around.
        self.Shannon_Mulaney.relations['life'] = 'turning around'
        ## The story is set in Shannon's college dorm room and the common areas of the dorm building.
        ## Shannon Mulaney is an 18 year old from Michigan and is attending XYZ university in Boston, Massachusetts on a full softball scholarship (XYZ being a large Division 1 universities in Boston with over 30,000 students).
        self.Shannon_Mulaney.relations['Michigan'] = 'home'
        self.Shannon_Mulaney.relations['Boston'] = 'school'
        ## Shannon is 5'10" with wavy brown/blonde ombre/roots (which she dyes herself), blue eyes, pale skin, and an athletic build (somewhat muscular, especially in legs/thighs).
        self.Shannon_Mulaney.appearance.append('5\'10"')
        self.Shannon_Mulaney.appearance.append('wavy brown/blonde ombre/roots')
        self.Shannon_Mulaney.appearance.append('blue eyes')
        self.Shannon_Mulaney.appearance.append('pale skin')
        self.Shannon_Mulaney.appearance.append('athletic build')
        ## Jess Abernathy is a 21-year-old student at XYZ University and Shannon's RA.
        self.Jess_Abernathy.relations['XYZ University'] = 'school'
        self.Jess_Abernathy.age.append('21')
        ## Jess is tall and has straight blond hair that she often wears in a ponytail.
        self.Jess_Abernathy.appearance.append('tall')
        self.Jess_Abernathy.appearance.append('straight blond hair')
        self.Jess_Abernathy.appearance.append('ponytail')
        ## She is originally from California and is the oldest of three sisters.
        self.Jess_Abernathy.relations['California'] = 'home'
        self.Jess_Abernathy.relations['oldest sister'] = '3'
        ## Olivia Kendall is Shannon's best friend from high school who is also attending XYZ University with her.
        self.Shannon_Mulaney.relations['best friend'] = 'Olivia_Kendall'
        self.Olivia_Kendall.relations['best friend'] = 'Shannon_Mulaney'
        ## Olivia is of average height with wavy brown hair and hazel eyes.
        self.Olivia_Kendall.appearance.append('average height')
        self.Olivia_Kendall.appearance.append('wavy brown hair')
        self.Olivia_Kendall.appearance.append('hazel eyes')

