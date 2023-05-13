## After the death of her father, a young woman moves to a small town to start a new life.
## She quickly learns that the town is full of secrets, and that her father's death may not have been an accident.
## The story is set in a small town in the middle of nowhere.
## Riley Harper is a young woman in her early twenties.
## She has long, dark hair and hazel eyes.
## She is of average height and build.
## Chase Elliott is a tall, handsome man in his early thirties.
## He has dark hair and blue eyes.
## He is the chief of police in the small town where Riley has moved to.
## Jonas Harper is Riley's late father.
## He was a successful businessman who died suddenly in a car accident.
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
        self.Riley_Harper = character('Riley Harper')
        self.Chase_Elliott = character('Chase Elliott')
        self.Jonas_Harper = character('Jonas Harper')

    def story(self):
        ## After the death of her father, a young woman moves to a small town to start a new life.
        self.Jonas_Harper.relations['father'] = 'Riley_Harper'
        self.Riley_Harper.relations['daughter'] = 'Jonas_Harper'
        self.Riley_Harper.age.append('young')
        self.Riley_Harper.gender.append('female')
        ## She quickly learns that the town is full of secrets, and that her father's death may not have been an accident.
        ## The story is set in a small town in the middle of nowhere.
        ## Riley Harper is a young woman in her early twenties.
        self.Riley_Harper.age.append('early twenties')
        ## She has long, dark hair and hazel eyes.
        self.Riley_Harper.appearance.append('long, dark hair')
        self.Riley_Harper.appearance.append('hazel eyes')
        ## She is of average height and build.
        self.Riley_Harper.appearance.append('average height and build')
        ## Chase Elliott is a tall, handsome man in his early thirties.
        self.Chase_Elliott.age.append('early thirties')
        self.Chase_Elliott.appearance.append('tall, handsome')
        ## He has dark hair and blue eyes.
        self.Chase_Elliott.appearance.append('dark hair')
        self.Chase_Elliott.appearance.append('blue eyes')
        ## He is the chief of police in the small town where Riley has moved to.
        self.Chase_Elliott.occupation.append('chief of police')
        ## Jonas Harper is Riley's late father.
        self.Jonas_Harper.relations['father'] = 'Riley_Harper'
        self.Riley_Harper.relations['daughter'] = 'Jonas_Harper'
        ## He was a successful businessman who died suddenly in a car accident.
        self.Jonas_Harper.occupation.append('successful businessman')
        self.Jonas_Harper.gender.append('male')

