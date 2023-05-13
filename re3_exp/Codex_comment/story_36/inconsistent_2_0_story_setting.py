## The last thing Karen remembers before she blacks out is the sound of her daughter crying for help.
## When she comes to, she's in the hospital with no recollection of what happened.
## The police are at her bedside, telling her that her daughter is dead and that she is the prime suspect.
## The story is set in a hospital room.
## Karen Fletcher is a middle-aged woman with blonde hair and blue eyes.
## She is of average height and build.
## Kate Fletcher is Karen's teenage daughter.
## She is tall and slender with dark hair and brown eyes.
## Julia Fletcher is Karen's mother-in-law who is in her late 60s/early 70s, thin and frail with grey hair and blue eyes, Julia is bedridden and uses a wheelchair to get around.
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
        ## The story is set in a hospital room.
        ## Karen Fletcher is a middle-aged woman with blonde hair and blue eyes.
        self.Karen_Fletcher.gender.append('female')
        self.Karen_Fletcher.age.append('middle aged')
        self.Karen_Fletcher.appearance.append('blonde hair')
        self.Karen_Fletcher.appearance.append('blue eyes')
        ## She is of average height and build.
        ## Kate Fletcher is Karen's teenage daughter.
        self.Kate_Fletcher.relations['mother'] = 'Karen_Fletcher'
        self.Karen_Fletcher.relations['daughter'] = 'Kate_Fletcher'
        self.Kate_Fletcher.gender.append('female')
        self.Kate_Fletcher.age.append('teenage')
        ## She is tall and slender with dark hair and brown eyes.
        self.Kate_Fletcher.appearance.append('tall')
        self.Kate_Fletcher.appearance.append('slender')
        self.Kate_Fletcher.appearance.append('dark hair')
        self.Kate_Fletcher.appearance.append('brown eyes')
        ## Julia Fletcher is Karen's mother-in-law who is in her late 60s/early 70s, thin and frail with grey hair and blue eyes, Julia is bedridden and uses a wheelchair to get around.
        self.Julia_Fletcher.relations['mother_in_law'] = 'Karen_Fletcher'
        self.Karen_Fletcher.relations['mother_in_law'] = 'Julia_Fletcher'
        self.Julia_Fletcher.gender.append('female')
        self.Julia_Fletcher.age.append('late 60s')
        self.Julia_Fletcher.age.append('early 70s')
        self.Julia_Fletcher.appearance.append('thin')
        self.Julia_Fletcher.appearance.append('frail')
        self.Julia_Fletcher.appearance.append('grey hair')
        self.Julia_Fletcher.appearance.append('blue eyes')
        self.Julia_Fletcher.appearance.append('bedridden')
        self.Julia_Fletcher.appearance.append('wheelchair')

