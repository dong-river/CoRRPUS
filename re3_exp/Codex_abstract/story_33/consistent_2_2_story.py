## Charles Wilson sits in his office filling out reports.
## He's in his forties, in good shape, and has short black hair.
## His wife is out shopping.
## She thinks he's at work but instead he's sitting at his desk daydreaming about the girl he's been dating for the past few weeks.
## She's a college student and is twenty years younger than him but Charles doesn't care.
## As long as she has a pulse she can have him.
## He fantasizes about taking her to dinner tomorrow night and ending up back at her place to have sex.
## He thinks about bending her over, putting it in doggy style, pounding away until she moans.
## He thinks about pounding her until she screams for mercy, begging him to stop with tears streaming down her face...  "Good afternoon Charles."
## His sergeant calls from the doorway of his office waking him from his fantasy.
## "Just wanted to let you know we just got a rape case down on the South side."
## "Great!"
## Charles said sarcastically with a sigh.
## "When do I get my vacation?"
## His sergeant laughs as he walks away leaving Charles alone with his fantasies again.

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
        self.Charles_Wilson = character('Charles Wilson')
        self.Nina_Peterson = character('Nina Peterson')
        self.Jeff_Foster = character('Jeff Foster')

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
        ## Charles Wilson sits in his office filling out reports.
        self.set_occupation(self.Charles_Wilson, "office")
        ## He's in his forties, in good shape, and has short black hair.
        self.set_age(self.Charles_Wilson, "forties")
        self.set_appearance(self.Charles_Wilson, "short black hair")
        ## His wife is out shopping.
        self.set_relation(self.Charles_Wilson, 'wife', self.Nina_Peterson)
        self.set_relation(self.Nina_Peterson, 'husband', self.Charles_Wilson)
        ## She thinks he's at work but instead he's sitting at his desk daydreaming about the girl he's been dating for the past few weeks.
        self.set_relation(self.Charles_Wilson, 'girlfriend', self.Nina_Peterson)
        self.set_relation(self.Nina_Peterson, 'boyfriend', self.Charles_Wilson)
        ## She's a college student and is twenty years younger than him but Charles doesn't care.
        self.set_age(self.Nina_Peterson, "twenty")
        self.set_occupation(self.Nina_Peterson, "college student")
        ## As long as she has a pulse she can have him.
        self.set_gender(self.Nina_Peterson, "female")
        ## He fantasizes about taking her to dinner tomorrow night and ending up back at her place to have sex.
        ## He thinks about bending her over, putting it in doggy style, pounding away until she moans.
        ## He thinks about pounding her until she screams for mercy, begging him to stop with tears streaming down her face...  "Good afternoon Charles."
        ## His sergeant calls from the doorway of his office waking him from his fantasy.
        self.set_relation(self.Charles_Wilson, 'sergeant', self.Jeff_Foster)
        self.set_relation(self.Jeff_Foster, 'officer', self.Charles_Wilson)
        ## "Just wanted to let you know we just got a rape case down on the South side."
        ## "Great!"
        ## Charles said sarcastically with a sigh.
        ## "When do I get my vacation?"
        ## His sergeant laughs as he walks away leaving Charles alone with his fantasies again.

## Create a world model state to track each character's appearance, personality, and relations with other characters.

