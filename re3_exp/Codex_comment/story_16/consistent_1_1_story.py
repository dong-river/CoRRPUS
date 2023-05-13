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

    def story(self):
        ## Jennifer Ann Smith is a tired-looking woman in her mid-30s.
        self.Jennifer_Ann_Smith.age.append('mid-30s')
        self.Jennifer_Ann_Smith.appearance.append('tired-looking')
        self.Jennifer_Ann_Smith.gender.append('female')
        ## She has shoulder-length brown hair that is starting to show some gray at the temples.
        self.Jennifer_Ann_Smith.appearance.append('shoulder-length brown hair')
        self.Jennifer_Ann_Smith.appearance.append('gray at the temples')
        ## Jennifer's right hand clutches the phone, while her left hand clenches a cigarette between her thumb and forefinger.
        self.Jennifer_Ann_Smith.appearance.append('right hand clutches the phone')
        self.Jennifer_Ann_Smith.appearance.append('left hand clenches a cigarette between her thumb and forefinger')
        ## Her eyes are narrowed with annoyance as she listens to her mother ranting on the other end of the line.
        self.Jennifer_Ann_Smith.appearance.append('narrowed eyes')
        self.Jennifer_Ann_Smith.relations['mother'] = 'Clara_Smith'
        self.Clara_Smith.relations['daughter'] = 'Jennifer_Ann_Smith'
        ## "Where have you been?"
        ## demands Clara Smith, once she realizes that Jennifer has finally picked up the phone.
        self.Clara_Smith.appearance.append('demands Clara Smith')
        ## "I've been trying to call you for hours!"
        ## "I was at work," says Jennifer, letting out a sigh.
        ## "You know I don't get off until eight."
        ## "Are you going to invite me over?"
        ## asks Clara.
        ## Jennifer's stomach does a flip as she lets out another sigh and glances down at her boyfriend Robert lying in bed beside her.
        self.Jennifer_Ann_Smith.relations['boyfriend'] = 'Robert_Smith'
        self.Robert_Smith.relations['girlfriend'] = 'Jennifer_Ann_Smith'
        ## The last thing she wanted was for her mother to barge into their apartment and intrude on their sex life again, but there wasn't much she could do about it now.
        ## If she turned down Clara's invitation, she knew that Clara would just continue calling back all night until she agreed to meet with her mother for lunch tomorrow or something like that.

