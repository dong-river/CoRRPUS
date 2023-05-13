## A young woman finds out that she is pregnant and decides to abort the pregnancy even though it goes against her religious beliefs.
## The story is set in a small town in the Midwest.
## Julie Christensen is a young woman in her early twenties.
## She is pretty and blonde, and is the daughter of a prominent family in the town.
## Julie is a student at the local college, and is active in her church.
## Tommy Foster is a young man in his early twenties.
## He is the son of a poor family in the town, and has been involved in a lot of trouble in his life.
## Tommy is Julie's boyfriend, and the father of her unborn child.
## Beth Christensen is Julie's mother.
## She is a well-respected member of the community, and is very involved in her church.
## Beth is not happy about her daughter's situation, and is strongly opposed to the idea of abortion.
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
        self.Julie_Christensen.gender.append('female')
        self.Julie_Christensen.age.append('young')
        ## She is pretty and blonde, and is the daughter of a prominent family in the town.
        self.Julie_Christensen.appearance.append("pretty")
        self.Julie_Christensen.appearance.append("blonde")
        self.Julie_Christensen.relations['daughter'] = 'Beth_Christensen'
        self.Beth_Christensen.relations['daughter'] = 'Julie_Christensen'
        ## Julie is a student at the local college, and is active in her church.
        self.Julie_Christensen.occupation.append("student")
        self.Julie_Christensen.occupation.append("active in her church")
        ## Tommy Foster is a young man in his early twenties.
        self.Tommy_Foster.gender.append('male')
        self.Tommy_Foster.age.append('young')
        ## He is the son of a poor family in the town, and has been involved in a lot of trouble in his life.
        self.Tommy_Foster.relations['son'] = 'poor family'
        self.Tommy_Foster.relations['involved in a lot of trouble'] = 'his life'
        ## Tommy is Julie's boyfriend, and the father of her unborn child.
        self.Tommy_Foster.relations['boyfriend'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['boyfriend'] = 'Tommy_Foster'
        self.Tommy_Foster.relations['father'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['father'] = 'Tommy_Foster'
        ## Beth Christensen is Julie's mother.
        self.Julie_Christensen.relations['mother'] = 'Beth_Christensen'
        self.Beth_Christensen.relations['daughter'] = 'Julie_Christensen'
        ## She is a well-respected member of the community, and is very involved in her church.
        self.Beth_Christensen.relations['well-respected member of the community'] = 'her church'
        ## Beth is not happy about her daughter's situation, and is strongly opposed to the idea of abortion.
        self.Beth_Christensen.relations['not happy about her daughter'] = 'abortion'

