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

    def story(self):
        ## After the loss of her father, Shannon is determined to follow in his footsteps and become a successful journalist.
        self.Shannon_Kincaid.relations['father'] = 'Jack_Kincaid'
        self.Jack_Kincaid.relations['daughter'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.occupation.append('journalist')
        self.Jack_Kincaid.occupation.append('journalist')
        ## However, when she lands her first big story, she quickly learns that the ugly reality of life in the city is far different from the dream she imagined.
        ## The story is set in a large city.
        ## Shannon Kincaid is a young woman in her early twenties.
        self.Shannon_Kincaid.age.append('young')
        self.Shannon_Kincaid.gender.append('female')
        ## She has long, brown hair and blue eyes.
        self.Shannon_Kincaid.appearance.append("long, brown hair")
        self.Shannon_Kincaid.appearance.append("blue eyes")
        ## She is of average height and build.
        ## Jack Kincaid is Shannon’s father.
        self.Jack_Kincaid.gender.append('male')
        ## He was a successful journalist before his untimely death.
        ## Mark Woodbury is Shannon’s boss at the newspaper where she works.
        self.Shannon_Kincaid.relations['boss'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['employee'] = 'Shannon_Kincaid'
        ## He is a middle-aged man with graying hair and a mustache.
        self.Mark_Woodbury.age.append('middle-aged')
        self.Mark_Woodbury.appearance.append("graying hair")
        self.Mark_Woodbury.appearance.append("mustache")
        self.Mark_Woodbury.gender.append('male')

