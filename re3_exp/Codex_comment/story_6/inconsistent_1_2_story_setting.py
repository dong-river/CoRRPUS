## After the loss of her father, Shannon is determined to follow in his footsteps and become a successful journalist.
## However, when she lands her first major assignment, she quickly discovers that the ugly reality of life in the city is far different from the dream she imagined.
## The story is set in a large city.
## Shannon Riley is a young woman in her early twenties.
## She has long, brown hair and blue eyes.
## She is of average height and build.
## Robert Riley is Shannon's father.
## He was a successful journalist who died suddenly of a heart attack.
## Jillian Riley is Shannon's mother.
## She is a stay-at-home mom who is struggling to cope with her husband's death.
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

    def story(self):
        ## The story is set in a large city.
        ## Shannon Riley is a young woman in her early twenties.
        self.Shannon_Riley.gender.append('female')
        self.Shannon_Riley.age.append('young')
        ## She has long, brown hair and blue eyes.
        self.Shannon_Riley.appearance.append('long, brown hair')
        self.Shannon_Riley.appearance.append('blue eyes')
        ## She is of average height and build.
        self.Shannon_Riley.appearance.append('average height')
        self.Shannon_Riley.appearance.append('average build')
        ## Robert Riley is Shannon's father.
        self.Shannon_Riley.relations['father'] = 'Robert_Riley'
        self.Robert_Riley.relations['daughter'] = 'Shannon_Riley'
        ## He was a successful journalist who died suddenly of a heart attack.
        self.Robert_Riley.occupation.append('journalist')
        ## Jillian Riley is Shannon's mother.
        self.Shannon_Riley.relations['mother'] = 'Jillian_Riley'
        self.Jillian_Riley.relations['daughter'] = 'Shannon_Riley'
        ## She is a stay-at-home mom who is struggling to cope with her husband's death.

