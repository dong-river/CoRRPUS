## Chase Elliott is your average guy who works at the local gas station.
## He lives in a small town called Grandview, and he has been there for his entire life.
## Jonas Harper was a rich man who owned his own business and drove a nice car.
## He came from a small town called Resting Ridge, and he loved to drive on country roads.
## Jonas Harper died in a car accident.
## His daughter Riley lives far away from Grandview, but she comes for her father's funeral."
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
        ## Chase Elliott is your average guy who works at the local gas station.
        self.Chase_Elliott.occupation.append('gas station')
        ## He lives in a small town called Grandview, and he has been there for his entire life.
        self.Chase_Elliott.relations['town'] = 'Grandview'
        ## Jonas Harper was a rich man who owned his own business and drove a nice car.
        self.Jonas_Harper.occupation.append('business')
        self.Jonas_Harper.relations['car'] = 'car'
        ## He came from a small town called Resting Ridge, and he loved to drive on country roads.
        self.Jonas_Harper.relations['town'] = 'Resting Ridge'
        ## Jonas Harper died in a car accident.
        self.Jonas_Harper.relations['death'] = 'car accident'
        ## His daughter Riley lives far away from Grandview, but she comes for her father's funeral."
        self.Riley_Harper.relations['father'] = 'Jonas Harper'
        self.Riley_Harper.relations['town'] = 'Grandview'
        self.Riley_Harper.relations['death'] = 'funeral'

