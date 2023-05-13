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
        self.Karen_Fletcher.appearance.append('blonde hair')
        self.Karen_Fletcher.appearance.append('blue eyes')
        self.Karen_Fletcher.age.append('middle-aged')
        ## She is of average height and build.
        ## Kate Fletcher is Karen's teenage daughter.
        self.Karen_Fletcher.relations['daughter'] = 'Kate_Fletcher'
        self.Kate_Fletcher.relations['mother'] = 'Karen_Fletcher'
        self.Kate_Fletcher.age.append('teenage')
        ## She is tall and slender with dark hair and brown eyes.
        self.Kate_Fletcher.appearance.append('tall and slender')
        self.Kate_Fletcher.appearance.append('dark hair')
        self.Kate_Fletcher.appearance.append('brown eyes')
        ## Julia Fletcher is Karen's mother-in-law who is in her late 60s/early 70s, thin and frail with grey hair and blue eyes, Julia is bedridden and uses a wheelchair to get around.
        self.Karen_Fletcher.relations['mother-in-law'] = 'Julia_Fletcher'
        self.Julia_Fletcher.relations['daughter-in-law'] = 'Karen_Fletcher'
        self.Julia_Fletcher.age.append('late 60s/early 70s')
        self.Julia_Fletcher.appearance.append('thin and frail')
        self.Julia_Fletcher.appearance.append('grey hair')
        self.Julia_Fletcher.appearance.append('blue eyes')
        self.Julia_Fletcher.appearance.append('bedridden')
        self.Julia_Fletcher.appearance.append('uses a wheelchair')
