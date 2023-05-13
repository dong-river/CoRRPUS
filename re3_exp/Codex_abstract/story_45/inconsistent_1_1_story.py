## Karen Hartman sat on her bed, absentmindedly picking at a loose thread in the bedspread.
## She watched Nina work away on a school project, scowling at the pieces of paper Nina was spread out on her bed.
## It was late afternoon, and Karen wanted to just lay back and relax for a few minutes before she went home.
## Instead, she was stuck in her room helping her friend who wasn't exactly an expert when it came to organization.
## Nina paused in her work and looked up at Karen.
## "Is something wrong?"
## "No.
## I'm fine."
## Karen lied.
## Nina didn't fall for it.
## "Don't lie to me."
## She said flatly before getting up and turning away from Karen so that she couldn't see the hurt in her eyes.
## "It's about the fifth time you've gotten off my bed today."
## There was a long silence before Nina continued to speak again without turning around.
## "If you want me to leave you alone, just say so."
## Her voice was barely above a whisper as tears stung her eyes.

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
        self.Nina_Harman = character('Nina Harman')
        self.Jake_Ryan = character('Jake Ryan')
        self.Karen_Hartman = character('Karen Hartman')

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
        ## Karen Hartman sat on her bed, absentmindedly picking at a loose thread in the bedspread.
        self.set_relation(self.Karen_Hartman, 'friend', self.Nina_Harman)
        self.set_relation(self.Karen_Hartman, 'boyfriend', self.Jake_Ryan)
        self.set_relation(self.Nina_Harman, 'friend', self.Karen_Hartman)
        self.set_relation(self.Jake_Ryan, 'girlfriend', self.Karen_Hartman)
        ## She watched Nina work away on a school project, scowling at the pieces of paper Nina was spread out on her bed.
        self.set_occupation(self.Nina_Harman, "student")
        ## It was late afternoon, and Karen wanted to just lay back and relax for a few minutes before she went home.
        ## Instead, she was stuck in her room helping her friend who wasn't exactly an expert when it came to organization.
        self.set_appearance(self.Karen_Hartman, "wanted to relax")
        ## Nina paused in her work and looked up at Karen.
        ## "Is something wrong?"
        ## "No.
        ## I'm fine."
        ## Karen lied.
        ## Nina didn't fall for it.
        ## "Don't lie to me."
        ## She said flatly before getting up and turning away from Karen so that she couldn't see the hurt in her eyes.
        ## "It's about the fifth time you've gotten off my bed today."
        ## There was a long silence before Nina continued to speak again without turning around.
        ## "If you want me to leave you alone, just say so."
        ## Her voice was barely above a whisper as tears stung her eyes.
