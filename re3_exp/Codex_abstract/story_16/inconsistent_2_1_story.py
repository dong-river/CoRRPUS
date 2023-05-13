## Jennifer Ann Smith is a tired-looking woman in her mid-30s.
## She has shoulder-length brown hair that is starting to show some gray at the temples.
## Jennifer's right hand clutches the phone, while her left hand clenches a cigarette between her thumb and forefinger.
## Her eyes are narrowed with annoyance as she listens to her mother ranting on the other end of the line.
## "Where have you been?"
## demands Clara Smith, once she realizes that Jennifer has finally picked up the phone.
## "I've been trying to call you for hours!"
## "I was at work," says Jennifer, letting out a sigh.
## "You know I don't get off until eight."
## "Are you going to invite me over?"
## asks Clara.
## Jennifer's stomach does a flip as she lets out another sigh and glances down at her boyfriend Robert lying in bed beside her.
## The last thing she wanted was for her mother to barge into their apartment and intrude on their sex life again, but there wasn't much she could do about it now.
## If she turned down Clara's invitation, she knew that Clara would just continue calling back all night until she agreed to meet with her mother for lunch tomorrow or something like that.

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
        ## Jennifer Ann Smith is a tired-looking woman in her mid-30s.
        self.set_gender(self.Jennifer_Ann_Smith, "female")
        self.set_age(self.Jennifer_Ann_Smith, "mid-30s")
        ## She has shoulder-length brown hair that is starting to show some gray at the temples.
        self.set_appearance(self.Jennifer_Ann_Smith, "shoulder-length brown hair")
        ## Jennifer's right hand clutches the phone, while her left hand clenches a cigarette between her thumb and forefinger.
        self.set_occupation(self.Jennifer_Ann_Smith, "clutches the phone")
        ## Her eyes are narrowed with annoyance as she listens to her mother ranting on the other end of the line.
        ## "Where have you been?"
        ## demands Clara Smith, once she realizes that Jennifer has finally picked up the phone.
        self.set_relation(self.Jennifer_Ann_Smith, 'mother', self.Clara_Smith)
        self.set_relation(self.Clara_Smith, 'daughter', self.Jennifer_Ann_Smith)
        self.set_gender(self.Clara_Smith, "female")
        ## "I've been trying to call you for hours!"
        ## "I was at work," says Jennifer, letting out a sigh.
        ## "You know I don't get off until eight."
        ## "Are you going to invite me over?"
        ## asks Clara.
        ## Jennifer's stomach does a flip as she lets out another sigh and glances down at her boyfriend Robert lying in bed beside her.
        self.set_relation(self.Jennifer_Ann_Smith, 'boyfriend', self.Robert_Smith)
        self.set_relation(self.Robert_Smith, 'girlfriend', self.Jennifer_Ann_Smith)
        self.set_gender(self.Robert_Smith, "male")
        ## The last thing she wanted was for her mother to barge into their apartment and intrude on their sex life again, but there wasn't much she could do about it now.
        ## If she turned down Clara's invitation, she knew that Clara would just continue calling back all night until she agreed to meet with her mother for lunch tomorrow or something like that.
