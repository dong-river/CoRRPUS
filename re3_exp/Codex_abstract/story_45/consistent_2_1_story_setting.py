## Nina, an unassuming pre-teen, discovers she has the ability to astral project outside of her body.
## She soon learns that she is not the only one with this ability and that there are others who would use this power for evil.
## Nina must use her new found abilities to stop them.
## The story is set in a small town in the United States.
## Nina Harman is a small, delicate looking pre-teen with long dark hair and brown eyes.
## She is shy and withdrawn, but has a kind heart.
## Jake Ryan is a handsome teenage boy who is popular at school.
## He is athletic and outgoing, but can be arrogant at times.
## He is also Nina's crush.
## Karen Hartman is Nina's best friend who is outgoing and energetic with a quick wit and sharp tongue.

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
        ## The story is set in a small town in the United States.
        ## Nina Harman is a small, delicate looking pre-teen with long dark hair and brown eyes.
        self.set_appearance(self.Nina_Harman, "small, delicate looking pre-teen with long dark hair and brown eyes")
        self.set_age(self.Nina_Harman, "pre-teen")
        self.set_gender(self.Nina_Harman, "female")
        ## She is shy and withdrawn, but has a kind heart.
        ## Jake Ryan is a handsome teenage boy who is popular at school.
        self.set_appearance(self.Jake_Ryan, "handsome teenage boy")
        self.set_age(self.Jake_Ryan, "teenage boy")
        self.set_gender(self.Jake_Ryan, "male")
        ## He is athletic and outgoing, but can be arrogant at times.
        ## He is also Nina's crush.
        self.set_relation(self.Nina_Harman, 'crush', self.Jake_Ryan)
        self.set_relation(self.Jake_Ryan, 'crush', self.Nina_Harman)
        ## Karen Hartman is Nina's best friend who is outgoing and energetic with a quick wit and sharp tongue.
        self.set_relation(self.Nina_Harman, 'best friend', self.Karen_Hartman)
        self.set_relation(self.Karen_Hartman, 'best friend', self.Nina_Harman)
        self.set_appearance(self.Karen_Hartman, "outgoing and energetic with a quick wit and sharp tongue")
        self.set_gender(self.Karen_Hartman, "female")
        ## Nina, an unassuming pre-teen, discovers she has the ability to astral project outside of her body.
        self.set_occupation(self.Nina_Harman, "unassuming pre-teen, discovers she has the ability to astral project outside of her body")
        ## She soon learns that she is not the only one with this ability and that there are others who would use this power for evil.
        ## Nina must use her new found abilities to stop them.
