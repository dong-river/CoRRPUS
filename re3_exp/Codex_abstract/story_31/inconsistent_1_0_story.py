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
        self.Chase_Elliott.relations['hometown'] = 'Grandview'
        ## Jonas Harper was a rich man who owned his own business and drove a nice car.
        self.Jonas_Harper.occupation.append('business')
        self.Jonas_Harper.relations['car'] = 'nice'
        ## He came from a small town called Resting Ridge, and he loved to drive on country roads.
        self.Jonas_Harper.relations['hometown'] = 'Resting Ridge'
        self.Jonas_Harper.relations['driving'] = 'country roads'
        ## Jonas Harper died in a car accident.
        ## His daughter Riley lives far away from Grandview, but she comes for her father's funeral."
        self.Jonas_Harper.relations['daughter'] = 'Riley_Harper'
        self.Riley_Harper.relations['father'] = 'Jonas_Harper'
        self.Riley_Harper.relations['hometown'] = 'far away from Grandview'
        self.Riley_Harper.relations['visit'] = 'funeral'
        
