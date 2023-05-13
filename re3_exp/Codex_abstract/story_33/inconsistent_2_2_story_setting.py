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

    def set_appearance(self, character, appearance):
        character.appearance.append(appearance)
    
    def set_occupation(self, character, occupation):
        character.occupation.append(occupation)
    
    def set_gender(self, character, gender):
        character.gender.append(gender)
    
    def set_age(self, character, age):
        character.age.append(age)
    
    def set_relation(self, character, relation, other_character):
        character.relations[relation] = other_character.name
        
    def story(self):
        ## The story is set in a college town.
        ## Charles Wilson is a police detective who is assigned to investigate Nina's case.
        self.set_occupation(self.Charles_Wilson, 'police detective')
        self.set_relation(self.Charles_Wilson, 'assigned to investigate', self.Nina_Peterson)
        ## He's in his forties and has a wife and two kids at home.
        self.set_age(self.Charles_Wilson, 'forties')
        self.set_relation(self.Charles_Wilson, 'wife', self.Charles_Wilson)
        self.set_relation(self.Charles_Wilson, 'kids', self.Charles_Wilson)
        ## He's a good cop but he's also a bit of a ladies man and has a tendency to flirt with the women he meets on the job.
        self.set_occupation(self.Charles_Wilson, 'good cop')
        self.set_occupation(self.Charles_Wilson, 'ladies man')
        ## Nina Peterson is a young woman in her early twenties.
        self.set_age(self.Nina_Peterson, 'early twenties')
        self.set_gender(self.Nina_Peterson, 'woman')
        ## She's about 5'4 with long blonde hair and blue eyes.
        self.set_appearance(self.Nina_Peterson, '5\'4')
        self.set_appearance(self.Nina_Peterson, 'long blonde hair')
        self.set_appearance(self.Nina_Peterson, 'blue eyes')
        ## She's a bit shy and introverted but generally a good person.
        self.set_appearance(self.Nina_Peterson, 'shy')
        self.set_appearance(self.Nina_Peterson, 'introverted')
        self.set_appearance(self.Nina_Peterson, 'good person')
        ## Jeff Foster is the man who Nina meets at the bar and brings home with her.
        self.set_relation(self.Jeff_Foster, 'met', self.Nina_Peterson)
        self.set_relation(self.Nina_Peterson, 'met', self.Jeff_Foster)
        self.set_relation(self.Jeff_Foster, 'brought home', self.Nina_Peterson)
        self.set_relation(self.Nina_Peterson, 'brought home', self.Jeff_Foster)
        ## He's in his early thirties and is of average height with dark hair and eyes.
        self.set_age(self.Jeff_Foster, 'early thirties')
        self.set_appearance(self.Jeff_Foster, 'average height')
        self.set_appearance(self.Jeff_Foster, 'dark hair')
        self.set_appearance(self.Jeff_Foster, 'dark eyes')
