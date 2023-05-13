## Nina, a college student, is studying for her final exams and is struggling to stay focused.
## She takes a break from studying to go for a walk and ends up at a bar.
## She has a few drinks and starts chatting with the guy next to her.
## They hit it off and end up back at his place.
## Nina wakes up the next morning naked in his bed with no recollection of what happened.
## She panics and quickly leaves.
## The guy tries to stop her but she's out the door before he can say anything.
## Nina doesn't want to believe she was raped but she can't remember what happened.
## The story is set in a college town.
## Charles Wilson is a young man in his early twenties.
## He's of average height with brown hair and eyes.
## He's generally a good guy but he has a bit of a temper.
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
        ## Charles Wilson is a young man in his early twenties.
        self.Charles_Wilson.gender.append('male')
        self.Charles_Wilson.age.append('young')
        ## He's of average height with brown hair and eyes.
        self.Charles_Wilson.appearance.append('brown hair')
        self.Charles_Wilson.appearance.append('brown eyes')
        ## He's generally a good guy but he has a bit of a temper.
        ## Nina Peterson is a young woman in her early twenties.
        self.Nina_Peterson.gender.append('female')
        self.Nina_Peterson.age.append('young')
        ## She's about 5'4 with long blonde hair and blue eyes.
        self.Nina_Peterson.appearance.append('long blonde hair')
        self.Nina_Peterson.appearance.append('blue eyes')
        ## She's a bit shy and introverted but generally a good person.
        ## Jeff Foster is the man who Nina meets at the bar and brings home with her.
        self.Nina_Peterson.relations['met_at_bar'] = 'Jeff_Foster'
        ## He's in his early thirties and is of average height with dark hair and eyes.
        self.Jeff_Foster.age.append('early thirties')
        self.Jeff_Foster.appearance.append('dark hair')
        self.Jeff_Foster.appearance.append('dark eyes')

