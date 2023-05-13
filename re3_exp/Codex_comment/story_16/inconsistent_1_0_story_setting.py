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

    def story(self):
        ## The story is set in Jennifer's home, after she has gotten off from work.
        ## Jennifer Ann Smith is a tired-looking woman in her mid-30s.
        self.Jennifer_Ann_Smith.age.append('mid-30s')
        ## She has shoulder-length brown hair that is starting to show some gray at the temples.
        self.Jennifer_Ann_Smith.appearance.append("shoulder-length brown hair")
        ## Clara Smith is Jennifer's mother.
        self.Jennifer_Ann_Smith.relations['mother'] = 'Clara_Smith'
        self.Clara_Smith.relations['daughter'] = 'Jennifer_Ann_Smith'
        ## She is a heavyset woman in her late 50s with graying hair that she often dyes blonde.
        self.Clara_Smith.gender.append('female')
        self.Clara_Smith.age.append('late 50s')
        self.Clara_Smith.appearance.append("graying hair")
        ## Robert Smith is Jennifer's father.
        self.Jennifer_Ann_Smith.relations['father'] = 'Robert_Smith'
        self.Robert_Smith.relations['daughter'] = 'Jennifer_Ann_Smith'
        ## He is a tall man in his early 60s with thinning gray hair and a mustache.
        self.Robert_Smith.gender.append('male')
        self.Robert_Smith.age.append('early 60s')
        self.Robert_Smith.appearance.append("thinning gray hair")
        self.Robert_Smith.appearance.append("mustache")

