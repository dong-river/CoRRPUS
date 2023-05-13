## The last thing Karen remembers before she blacks out is the sound of her daughter crying for help.
## When she comes to, she's in the hospital with no recollection of what happened.
## The police are at her bedside, telling her that her daughter is dead and that she is the prime suspect.
## The story is set in a hospital room.
## Karen Fletcher is a middle-aged woman with blonde hair and blue eyes.
## She is of average height and build.
## Kate Fletcher is Karen's teenage daughter.
## She is tall and slender with dark hair and brown eyes.
## Julia Fletcher is Karen's younger sister.
## She is shorter than Karen with light brown hair and green eyes.
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
        self.Karen_Fletcher = character('Karen Fletcher')
        self.Kate_Fletcher = character('Kate Fletcher')
        self.Julia_Fletcher = character('Julia Fletcher')

    def story(self):
        ## The last thing Karen remembers before she blacks out is the sound of her daughter crying for help.
        ## When she comes to, she's in the hospital with no recollection of what happened.
        ## The police are at her bedside, telling her that her daughter is dead and that she is the prime suspect.
        ## The story is set in a hospital room.
        ## Karen Fletcher is a middle-aged woman with blonde hair and blue eyes.
        self.Karen_Fletcher.gender.append('female')
        self.Karen_Fletcher.age.append('middle-aged')
        self.Karen_Fletcher.appearance.append('blonde hair')
        self.Karen_Fletcher.appearance.append('blue eyes')
        ## She is of average height and build.
        self.Karen_Fletcher.appearance.append('average height')
        self.Karen_Fletcher.appearance.append('average build')
        ## Kate Fletcher is Karen's teenage daughter.
        self.Karen_Fletcher.relations['daughter'] = 'Kate_Fletcher'
        self.Kate_Fletcher.relations['mother'] = 'Karen_Fletcher'
        self.Kate_Fletcher.age.append('teenage')
        self.Kate_Fletcher.gender.append('female')
        ## She is tall and slender with dark hair and brown eyes.
        self.Kate_Fletcher.appearance.append('tall')
        self.Kate_Fletcher.appearance.append('slender')
        self.Kate_Fletcher.appearance.append('dark hair')
        self.Kate_Fletcher.appearance.append('brown eyes')
        ## Julia Fletcher is Karen's younger sister.
        self.Karen_Fletcher.relations['sister'] = 'Julia_Fletcher'
        self.Julia_Fletcher.relations['sister'] = 'Karen_Fletcher'
        self.Julia_Fletcher.age.append('younger')
        self.Julia_Fletcher.gender.append('female')
        ## She is shorter than Karen with light brown hair and green eyes.
        self.Julia_Fletcher.appearance.append('shorter than Karen')
        self.Julia_Fletcher.appearance.append('light brown hair')
        self.Julia_Fletcher.appearance.append('green eyes')

