## After a long day at work, the last thing Jennifer wanted was to deal with her phone ringing off the hook.
## She thought about ignoring it, but she knew her mother would just keep calling back until she answered.
## Jennifer sure wasn't in the mood to listen to her mother complain about her life, but she didn't have a choice.
## The story is set in Jennifer's home, after she has gotten off from work.
## Jennifer Ann Smith is a tired-looking woman in her mid-30s.
## She has shoulder-length brown hair that is starting to show some gray at the temples.
## Clara Smith is Jennifer's mother.
## She is a heavyset woman in her late 50s with graying hair that she often dyes blonde.
## Robert Smith is Jennifer's father.
## He is a tall man in his early 60s with thinning gray hair and a mustache.

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
        self.Jennifer_Ann_Smith = character('Jennifer Ann Smith')
        self.Clara_Smith = character('Clara Smith')
        self.Robert_Smith = character('Robert Smith')

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
        ## The story is set in Jennifer's home, after she has gotten off from work.
        ## Jennifer Ann Smith is a tired-looking woman in her mid-30s.
        self.set_gender(self.Jennifer_Ann_Smith, "female")
        self.set_age(self.Jennifer_Ann_Smith, "mid-30s")
        ## She has shoulder-length brown hair that is starting to show some gray at the temples.
        self.set_appearance(self.Jennifer_Ann_Smith, "shoulder-length brown hair")
        self.set_appearance(self.Jennifer_Ann_Smith, "gray at the temples")
        ## Clara Smith is Jennifer's mother.
        self.set_relation(self.Jennifer_Ann_Smith, 'mother', self.Clara_Smith)
        self.set_relation(self.Clara_Smith, 'daughter', self.Jennifer_Ann_Smith)
        ## She is a heavyset woman in her late 50s with graying hair that she often dyes blonde.
        self.set_gender(self.Clara_Smith, "female")
        self.set_age(self.Clara_Smith, "late 50s")
        self.set_appearance(self.Clara_Smith, "heavyset woman")
        self.set_appearance(self.Clara_Smith, "graying hair")
        self.set_appearance(self.Clara_Smith, "often dyes blonde")
        ## Robert Smith is Jennifer's father.
        self.set_relation(self.Jennifer_Ann_Smith, 'father', self.Robert_Smith)
        self.set_relation(self.Robert_Smith, 'daughter', self.Jennifer_Ann_Smith)
        ## He is a tall man in his early 60s with thinning gray hair and a mustache.
        self.set_gender(self.Robert_Smith, "male")
        self.set_age(self.Robert_Smith, "early 60s")
        self.set_appearance(self.Robert_Smith, "tall man")
        self.set_appearance(self.Robert_Smith, "thinning gray hair")
        self.set_appearance(self.Robert_Smith, "mustache")
