## After the death of her father, a young woman moves to a small town to start a new life.
## She quickly learns that the town is full of secrets, and that her father's death may not have been an accident.
## The story is set in a small town in the middle of nowhere.
## Riley Harper is a young woman in her early twenties.
## She has long, dark hair and hazel eyes.
## She is of average height and build.
## Chase Elliott is a young man in his early twenties who works at the local gas station.
## He has dark hair and brown eyes and is of average height and build."
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
        self.Riley_Harper.gender.append('female')
        self.Riley_Harper.age.append('young')
        self.Jonas_Harper.gender.append('male')
        self.Jonas_Harper.age.append('old')
        self.Jonas_Harper.relations['daughter'] = 'Riley_Harper'
        self.Riley_Harper.relations['father'] = 'Jonas_Harper'
        ## She quickly learns that the town is full of secrets, and that her father's death may not have been an accident.
        ## The story is set in a small town in the middle of nowhere.
        ## Riley Harper is a young woman in her early twenties.
        ## She has long, dark hair and hazel eyes.
        ## She is of average height and build.
        self.Riley_Harper.appearance.append('long dark hair')
        self.Riley_Harper.appearance.append('hazel eyes')
        ## Chase Elliott is a young man in his early twenties who works at the local gas station.
        self.Chase_Elliott.gender.append('male')
        self.Chase_Elliott.age.append('young')
        ## He has dark hair and brown eyes and is of average height and build."
        self.Chase_Elliott.appearance.append('dark hair')
        self.Chase_Elliott.appearance.append('brown eyes')
        ## Jonas Harper is Riley's late father.
        ## He was a successful businessman who died suddenly in a car accident.

