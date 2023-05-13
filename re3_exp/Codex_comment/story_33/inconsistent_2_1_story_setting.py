## Nina, a college student, is studying for her final exams and is struggling to stay focused.
## She takes a break from studying to go for a walk and ends up at a bar.
## She has a few drinks and starts chatting with the guy next to her.
## They hit it off and end up back at his place.
## Nina wakes up the next morning naked in his bed with no recollection of what happened.
## She panics and quickly leaves.
## The guy tries to stop her but she's out the door before he can say anything.
## Nina doesn't want to believe she was raped but she can't remember what happened.
## The story is set in a college town.
## Charles Wilson is a police detective who is assigned to investigate Nina's case.
## He's in his forties and has a wife and two kids at home.
## He's a good cop but he's also a bit of a ladies man and has a tendency to flirt with the women he meets on the job.
## Nina Peterson is a young woman in her early twenties.
## She's about 5'4 with long blonde hair and blue eyes.
## She's a bit shy and introverted but generally a good person.
## Jeff Foster is the man who Nina meets at the bar and brings home with her.
## He's in his early thirties and is of average height with dark hair and eyes.
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
        self.Charles_Wilson = character('Charles Wilson')
        self.Nina_Peterson = character('Nina Peterson')
        self.Jeff_Foster = character('Jeff Foster')

    def story(self):
        ## The story is set in a college town.
        ## Charles Wilson is a police detective who is assigned to investigate Nina's case.
        self.Charles_Wilson.occupation.append('police detective')
        self.Charles_Wilson.relations['investigate'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['investigate'] = 'Charles_Wilson'
        ## He's in his forties and has a wife and two kids at home.
        self.Charles_Wilson.age.append('forties')
        self.Charles_Wilson.relations['wife'] = 'wife'
        self.Charles_Wilson.relations['kids'] = 'kids'
        ## He's a good cop but he's also a bit of a ladies man and has a tendency to flirt with the women he meets on the job.
        self.Charles_Wilson.occupation.append('good cop')
        self.Charles_Wilson.occupation.append('ladies man')
        self.Charles_Wilson.occupation.append('flirt')
        ## Nina Peterson is a young woman in her early twenties.
        self.Nina_Peterson.age.append('early twenties')
        self.Nina_Peterson.gender.append('female')
        ## She's about 5'4 with long blonde hair and blue eyes.
        self.Nina_Peterson.appearance.append('5\'4')
        self.Nina_Peterson.appearance.append('long blonde hair')
        self.Nina_Peterson.appearance.append('blue eyes')
        ## She's a bit shy and introverted but generally a good person.
        self.Nina_Peterson.appearance.append('shy')
        self.Nina_Peterson.appearance.append('introverted')
        self.Nina_Peterson.appearance.append('good person')
        ## Jeff Foster is the man who Nina meets at the bar and brings home with her.
        self.Jeff_Foster.relations['Nina_Peterson'] = 'meets at the bar'
        self.Jeff_Foster.relations['Nina_Peterson'] = 'brings home'
        ## He's in his early thirties and is of average height with dark hair and eyes.
        self.Jeff_Foster.age.append('early thirties')
        self.Jeff_Foster.appearance.append('average height')
        self.Jeff_Foster.appearance.append('dark hair')
        self.Jeff_Foster.appearance.append('dark eyes')

