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

    def story(self):
        ## After the loss of her father, Shannon is determined to follow in his footsteps and become a successful journalist.
        self.Shannon_Burke.relations['father'] = 'Charles_Burke'
        self.Charles_Burke.relations['daughter'] = 'Shannon_Burke'
        self.Shannon_Burke.occupation.append('journalist')
        ## However, when she lands her first major assignment, she quickly discovers that the ugly reality of life in the city is far different from the dream she imagined.
        ## The story is set in a large city.
        ## Shannon Burke is a young woman in her early twenties.
        self.Shannon_Burke.age.append('early twenties')
        self.Shannon_Burke.gender.append('female')
        ## She is of average height and build, with shoulder-length brown hair and hazel eyes.
        self.Shannon_Burke.appearance.append('average height')
        self.Shannon_Burke.appearance.append('average build')
        self.Shannon_Burke.appearance.append('shoulder-length brown hair')
        self.Shannon_Burke.appearance.append('hazel eyes')
        ## Charles Burke is Shannon's father.
        self.Charles_Burke.gender.append('male')
        ## He was a successful journalist who died unexpectedly a few years ago.
        self.Charles_Burke.occupation.append('journalist')
        ## Maxine Carter is Shannon's mother, who works as a secretary to support Shannon and her sister, Jenna.
        self.Shannon_Burke.relations['mother'] = 'Maxine_Carter'
        self.Maxine_Carter.relations['daughter'] = 'Shannon_Burke'
        self.Maxine_Carter.gender.append('female')
        self.Maxine_Carter.occupation.append('secretary')

