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

    def story(self):
        ## Shannon Mulaney is a 20-year-old student at XYZ University.
        self.Shannon_Mulaney.age.append('20')
        self.Shannon_Mulaney.occupation.append('student')
        self.Shannon_Mulaney.gender.append('female')
        ## She is petite and has long curly red hair.
        self.Shannon_Mulaney.appearance.append('petite')
        self.Shannon_Mulaney.appearance.append('long curly red hair')
        ## Shannon is from a small town in upstate New York and is the only child of her parents.
        self.Shannon_Mulaney.relations['parents'] = 'parents'
        ## Jess Abernathy is a 21-year-old student at XYZ University and Shannon's RA.
        self.Jess_Abernathy.age.append('21')
        self.Jess_Abernathy.occupation.append('student')
        self.Jess_Abernathy.occupation.append('RA')
        self.Jess_Abernathy.gender.append('female')
        ## Jess is tall and has straight blond hair that she often wears in a ponytail.
        self.Jess_Abernathy.appearance.append('tall')
        self.Jess_Abernathy.appearance.append('straight blond hair')
        self.Jess_Abernathy.appearance.append('ponytail')
        ## She is originally from California and is the oldest of three sisters.
        self.Jess_Abernathy.relations['sisters'] = 'sisters'
        ## Olivia Kendall is Shannon's best friend from high school who is also attending XYZ University with her.
        self.Shannon_Mulaney.relations['best friend'] = 'Olivia_Kendall'
        self.Olivia_Kendall.relations['best friend'] = 'Shannon_Mulaney'
        self.Olivia_Kendall.occupation.append('student')
        ## Olivia is of average height with wavy brown hair and hazel eyes.
        self.Olivia_Kendall.appearance.append('average height')
        self.Olivia_Kendall.appearance.append('wavy brown hair')
        self.Olivia_Kendall.appearance.append('hazel eyes')
        self.Olivia_Kendall.gender.append('female')
        
