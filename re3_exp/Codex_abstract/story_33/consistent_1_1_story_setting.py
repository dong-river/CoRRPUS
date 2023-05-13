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
        ## Charles Wilson is a young man in his early twenties.
        self.set_age(self.Charles_Wilson, "early twenties")
        self.set_gender(self.Charles_Wilson, "male")
        ## He's of average height with brown hair and eyes.
        self.set_appearance(self.Charles_Wilson, "average height")
        self.set_appearance(self.Charles_Wilson, "brown hair")
        self.set_appearance(self.Charles_Wilson, "brown eyes")
        ## He's generally a good guy but he has a bit of a temper.
        ## Nina Peterson is a young woman in her early twenties.
        self.set_age(self.Nina_Peterson, "early twenties")
        self.set_gender(self.Nina_Peterson, "female")
        ## She's about 5'4 with long blonde hair and blue eyes.
        self.set_appearance(self.Nina_Peterson, "5'4")
        self.set_appearance(self.Nina_Peterson, "long blonde hair")
        self.set_appearance(self.Nina_Peterson, "blue eyes")
        ## She's a bit shy and introverted but generally a good person.
        ## Jeff Foster is the man who Nina meets at the bar and brings home with her.
        ## He's in his early thirties and is of average height with dark hair and eyes.
        self.set_age(self.Jeff_Foster, "early thirties")
        self.set_appearance(self.Jeff_Foster, "average height")
        self.set_appearance(self.Jeff_Foster, "dark hair")
        self.set_appearance(self.Jeff_Foster, "dark eyes")
        self.set_gender(self.Jeff_Foster, "male")
        ## Nina, a college student, is studying for her final exams and is struggling to stay focused.
        self.set_occupation(self.Nina_Peterson, "college student")
        ## She takes a break from studying to go for a walk and ends up at a bar.
        ## She has a few drinks and starts chatting with the guy next to her.
        ## They hit it off and end up back at his place.
        ## Nina wakes up the next morning naked in his bed with no recollection of what happened.
        ## She panics and quickly leaves.
        ## The guy tries to stop her but she's out the door before he can say anything.
        ## Nina doesn't want to believe she was raped but she can't remember what happened.
