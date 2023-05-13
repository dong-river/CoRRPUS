## After a long day at work, the last thing Jennifer wanted was to deal with her phone ringing off the hook.
## She thought about ignoring it, but she knew her mother would just keep calling back until she answered.
## Jennifer sure wasn't in the mood to listen to her mother complain about her life, but she didn't have a choice.
## The story is set in Jennifer's home, after she has gotten off from work.
## Jennifer Ann Smith is a 27 year old woman who has just moved into a new apartment and started a new job as a receptionist at an office building downtown Chicago, Illinois, United States of America  Clara Smith is Jennifer's mother.
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
        ## Jennifer Ann Smith is a 27 year old woman who has just moved into a new apartment and started a new job as a receptionist at an office building downtown Chicago, Illinois, United States of America  Clara Smith is Jennifer's mother.
        self.Jennifer_Ann_Smith.age.append('27')
        self.Jennifer_Ann_Smith.gender.append('female')
        self.Jennifer_Ann_Smith.relations['mother'] = 'Clara_Smith'
        self.Clara_Smith.relations['daughter'] = 'Jennifer_Ann_Smith'
        self.Clara_Smith.gender.append('female')
        ## She is a heavyset woman in her late 50s with graying hair that she often dyes blonde.
        self.Clara_Smith.appearance.append('heavyset')
        self.Clara_Smith.appearance.append('graying hair')
        self.Clara_Smith.appearance.append('late 50s')
        ## Robert Smith is Jennifer's father.
        self.Jennifer_Ann_Smith.relations['father'] = 'Robert_Smith'
        self.Robert_Smith.relations['daughter'] = 'Jennifer_Ann_Smith'
        self.Robert_Smith.gender.append('male')
        ## He is a tall man in his early 60s with thinning gray hair and a mustache.
        self.Robert_Smith.appearance.append('tall')
        self.Robert_Smith.appearance.append('thin')
        self.Robert_Smith.appearance.append('gray hair')
        self.Robert_Smith.appearance.append('mustache')
        self.Robert_Smith.appearance.append('early 60s')
        
