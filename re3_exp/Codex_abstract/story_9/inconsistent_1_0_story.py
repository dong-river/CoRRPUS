## Beth Christensen sat down in a chair across from Julie and took her hand.
## "You have to listen to me," she said.
## "You're having the baby."
## "Beth, no, no, no!
## You don't understand," Julie protested.
## "It's impossible."
## "Why?"
## Beth replied.
## "Is it because you're still a virgin?"
## Julie looked at her friend with tears in her eyes and nodded.
## "How can I be pregnant?
## How can that happen?"
## "Because you had sex," Beth replied.
## "You know how it happens, right?
## The same way every time."
## She paused for a moment, and then asked softly, "Does he know?
## Has he spoken to you yet?"
## She then held up a hand to stop Julie from responding before continuing.
## "Listen, my advice is that you talk to him about this.
## Tell him what's going on and see what he says about it."

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
        ## Beth Christensen sat down in a chair across from Julie and took her hand.
        self.set_gender(self.Beth_Christensen, "female")
        self.set_relation(self.Beth_Christensen, 'friend', self.Julie_Christensen)
        self.set_relation(self.Julie_Christensen, 'friend', self.Beth_Christensen)
        ## "You have to listen to me," she said.
        ## "You're having the baby."
        ## "Beth, no, no, no!
        ## You don't understand," Julie protested.
        ## "It's impossible."
        ## "Why?"
        ## Beth replied.
        ## "Is it because you're still a virgin?"
        ## Julie looked at her friend with tears in her eyes and nodded.
        ## "How can I be pregnant?
        ## How can that happen?"
        ## "Because you had sex," Beth replied.
        ## "You know how it happens, right?
        ## The same way every time."
        ## She paused for a moment, and then asked softly, "Does he know?
        ## Has he spoken to you yet?"
        ## She then held up a hand to stop Julie from responding before continuing.
        ## "Listen, my advice is that you talk to him about this.
        ## Tell him what's going on and see what he says about it."
