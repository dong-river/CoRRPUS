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
        self.Charles_Wilson.age.append('forties')
        self.Charles_Wilson.relations['wife'] = 'wife'
        self.Charles_Wilson.relations['kids'] = 'kids'
        self.Charles_Wilson.occupation.append('police detective')
        ## Nina Peterson is a young woman in her early twenties.
        ## She's about 5'4 with long blonde hair and blue eyes.
        ## She's a bit shy and introverted but generally a good person.
        self.Nina_Peterson.age.append('early twenties')
        self.Nina_Peterson.appearance.append('5\'4 with long blonde hair and blue eyes')
        self.Nina_Peterson.gender.append('female')
        ## Jeff Foster is the man who Nina meets at the bar and brings home with her.
        ## He's in his early thirties and is of average height with dark hair and eyes.
        self.Jeff_Foster.age.append('early thirties')
        self.Jeff_Foster.appearance.append('average height with dark hair and eyes')
        self.Jeff_Foster.gender.append('male')

## The story is set in a fantasy world.
## The world is in a state of chaos.
## The king was killed by an assassin and the kingdom is in turmoil.
## The queen is struggling to keep the kingdom together.
## The queen is in her forties and has long blonde hair and blue eyes.
## She's a kind and loving woman who cares deeply for her people.
## She's also a powerful sorceress who wields dark magic.
## The queen is trying to find the person responsible for killing her husband.
## The queen's son is a young man who is struggling to cope with his father's death.
## He's about 6'2 with short brown hair and green eyes.
## He's a kind and compassionate man who cares deeply for his mother.
## He's also a skilled swordsman and is training to become a knight.
## The queen's son is trying to find the person responsible for killing his father.
## Create a world model state to track each character's appearance, personality, and relations with other characters.

