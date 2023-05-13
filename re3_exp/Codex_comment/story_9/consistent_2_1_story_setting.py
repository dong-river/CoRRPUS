## A young woman finds out that she is pregnant and decides to abort the pregnancy even though it goes against her religious beliefs.
## The story is set in a small town in the Midwest.
## Julie Christensen is a young woman in her early twenties.
## She is pretty and blonde, and is the daughter of a prominent family in the town.
## Julie is a student at the local college, and is active in her church.
## Tommy Foster is a young man in his early twenties.
## He is the son of a poor family in the town, and has been involved in a lot of trouble in his life.
## Tommy is Julie's boyfriend, and the father of her unborn child.
## Beth Christensen is Julie's best friend since childhood and her confidante in this matter.
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
        self.Julie_Christensen = character('Julie Christensen')
        self.Tommy_Foster = character('Tommy Foster')
        self.Beth_Christensen = character('Beth Christensen')

    def story(self):
        ## The story is set in a small town in the Midwest.
        ## Julie Christensen is a young woman in her early twenties.
        self.Julie_Christensen.age.append('early twenties')
        self.Julie_Christensen.gender.append('female')
        ## She is pretty and blonde, and is the daughter of a prominent family in the town.
        self.Julie_Christensen.appearance.append('pretty')
        self.Julie_Christensen.appearance.append('blonde')
        ## Julie is a student at the local college, and is active in her church.
        self.Julie_Christensen.occupation.append('student')
        self.Julie_Christensen.occupation.append('church')
        ## Tommy Foster is a young man in his early twenties.
        self.Tommy_Foster.age.append('early twenties')
        self.Tommy_Foster.gender.append('male')
        ## He is the son of a poor family in the town, and has been involved in a lot of trouble in his life.
        self.Tommy_Foster.occupation.append('poor')
        self.Tommy_Foster.occupation.append('trouble')
        ## Tommy is Julie's boyfriend, and the father of her unborn child.
        self.Tommy_Foster.relations['boyfriend'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['boyfriend'] = 'Tommy_Foster'
        self.Tommy_Foster.relations['father'] = 'unborn child'
        ## Beth Christensen is Julie's best friend since childhood and her confidante in this matter.
        self.Beth_Christensen.relations['Julie_Christensen'] = 'best friend'
        self.Julie_Christensen.relations['Beth_Christensen'] = 'best friend'
        self.Beth_Christensen.relations['Julie_Christensen'] = 'confidante'
        self.Julie_Christensen.relations['Beth_Christensen'] = 'confidante'
        self.Beth_Christensen.gender.append('female')
        ## A young woman finds out that she is pregnant and decides to abort the pregnancy even though it goes against her religious beliefs.
        self.Julie_Christensen.occupation.append('pregnancy')
        self.Julie_Christensen.occupation.append('abortion')
        self.Julie_Christensen.occupation.append('religious beliefs')

