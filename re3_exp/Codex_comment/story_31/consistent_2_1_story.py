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
        ## He lives in a small town called Grandview, and he has been there for his entire life.
        self.Chase_Elliott.occupation.append('works at the local gas station')
        self.Chase_Elliott.age.append('average')
        self.Chase_Elliott.gender.append('male')
        self.Chase_Elliott.relations['lives in'] = 'Grandview'
        ## Jonas Harper was a rich man who owned his own business and drove a nice car.
        ## He came from a small town called Resting Ridge, and he loved to drive on country roads.
        self.Jonas_Harper.occupation.append('rich man')
        self.Jonas_Harper.occupation.append('owned his own business')
        self.Jonas_Harper.occupation.append('drove a nice car')
        self.Jonas_Harper.relations['came from'] = 'Resting Ridge'
        ## Jonas Harper died in a car accident.
        ## His daughter Riley lives far away from Grandview, but she comes for her father's funeral."
        self.Jonas_Harper.relations['father'] = 'Riley_Harper'
        self.Riley_Harper.relations['daughter'] = 'Jonas_Harper'
        self.Riley_Harper.relations['lives far away from'] = 'Grandview'
        self.Riley_Harper.relations['comes for her father funeral'] = 'Jonas_Harper'
        

