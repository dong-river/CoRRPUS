## After the loss of her father, Shannon is determined to follow in his footsteps and become a successful journalist.
## However, when she lands her first big story, she quickly learns that the ugly reality of life in the city is far different from the dream she imagined.
## The story is set in a large city.
## Shannon Kincaid is a young woman in her early twenties.
## She has long, brown hair and blue eyes.
## She is of average height and build.
## Jack Kincaid is Shannon’s father.
## He was a successful journalist before his untimely death.
## Mark Woodbury is Shannon’s boyfriend.
## He is a student at the local college.
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

    def story(self):
        ## The story is set in a large city.
        ## Shannon Kincaid is a young woman in her early twenties.
        self.Shannon_Kincaid.age.append('young')
        self.Shannon_Kincaid.gender.append('female')
        ## She has long, brown hair and blue eyes.
        self.Shannon_Kincaid.appearance.append('long brown hair')
        self.Shannon_Kincaid.appearance.append('blue eyes')
        ## She is of average height and build.
        ## Jack Kincaid is Shannon’s father.
        self.Shannon_Kincaid.relations['father'] = 'Jack_Kincaid'
        self.Jack_Kincaid.relations['daughter'] = 'Shannon_Kincaid'
        ## He was a successful journalist before his untimely death.
        self.Jack_Kincaid.occupation.append('successful journalist')
        ## Mark Woodbury is Shannon’s boyfriend.
        self.Shannon_Kincaid.relations['boyfriend'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['girlfriend'] = 'Shannon_Kincaid'
        ## He is a student at the local college.
        self.Mark_Woodbury.occupation.append('student')

