## Beth Christensen walked into the living room, where her daughter Julie was sitting with her boyfriend Tommy.
## She could tell that the two were happy and carefree, and she instantly knew that something was up.
## "Julie," Beth said sternly.
## "What's going on?"
## "What do you mean?"
## Julie asked nervously.
## "You look too happy for something not to be going on," Beth replied, glaring at Tommy.
## "Is this about what I think it is?"
## Julie turned to Tommy for help, but he remained silent and looked away from her.
## "I'm pregnant," she said in a low voice after several moments of silence.
## She started to tear up as she finished speaking.
## "I'm sorry."
## Beth was shocked by what she had just heard.
## She went to her daughter and pulled her into a hug while scolding Tommy at the same time.
## "Tommy Foster!
## What did you do?
## When did this happen?
## Why didn't you stop this from happening?
## You're the one who is supposed to be responsible!
## Now I have to deal with you and your father's mistakes."

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
        self.Julie_Christensen = character('Julie Christensen')
        self.Tommy_Foster = character('Tommy Foster')
        self.Beth_Christensen = character('Beth Christensen')

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
        ## Beth Christensen walked into the living room, where her daughter Julie was sitting with her boyfriend Tommy.
        self.set_relation(self.Julie_Christensen, 'mother', self.Beth_Christensen)
        self.set_relation(self.Beth_Christensen, 'daughter', self.Julie_Christensen)
        self.set_gender(self.Beth_Christensen, "female")
        self.set_gender(self.Julie_Christensen, "female")
        self.set_relation(self.Julie_Christensen, 'boyfriend', self.Tommy_Foster)
        self.set_relation(self.Tommy_Foster, 'girlfriend', self.Julie_Christensen)
        self.set_gender(self.Tommy_Foster, "male")
        ## She could tell that the two were happy and carefree, and she instantly knew that something was up.
        ## "Julie," Beth said sternly.
        ## "What's going on?"
        ## "What do you mean?"
        ## Julie asked nervously.
        ## "You look too happy for something not to be going on," Beth replied, glaring at Tommy.
        ## "Is this about what I think it is?"
        ## Julie turned to Tommy for help, but he remained silent and looked away from her.
        ## "I'm pregnant," she said in a low voice after several moments of silence.
        ## She started to tear up as she finished speaking.
        ## "I'm sorry."
        ## Beth was shocked by what she had just heard.
        ## She went to her daughter and pulled her into a hug while scolding Tommy at the same time.
        ## "Tommy Foster!
        ## What did you do?
        ## When did this happen?
        ## Why didn't you stop this from happening?
        ## You're the one who is supposed to be responsible!
        ## Now I have to deal with you and your father's mistakes."
