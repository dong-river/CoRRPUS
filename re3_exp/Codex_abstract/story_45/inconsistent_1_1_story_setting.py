## Nina, an unassuming pre-teen, discovers she has the ability to astral project outside of her body.
## She soon learns that she is not the only one with this ability and that there are others who would use this power for evil.
## Nina must use her new found abilities to stop them.
## The story is set in a small town in the United States.
## Nina Harman is a small, delicate looking pre-teen with long dark hair and brown eyes.
## She is shy and withdrawn, but has a kind heart.
## Jake Ryan is a handsome teenage boy who is popular at school.
## He is athletic and outgoing, but can be arrogant at times.
## He is also Nina's crush.
## Karen Hartman is Nina's mother.
## She is a kind and loving woman who is always supportive of her daughter.

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
        self.set_appearance(self.Nina_Harman, "small")
        self.set_appearance(self.Nina_Harman, "delicate looking")
        self.set_appearance(self.Nina_Harman, "long dark hair")
        self.set_appearance(self.Nina_Harman, "brown eyes")
        self.set_age(self.Nina_Harman, "pre-teen")
        ## She is shy and withdrawn, but has a kind heart.
        ## Jake Ryan is a handsome teenage boy who is popular at school.
        self.set_appearance(self.Jake_Ryan, "handsome")
        self.set_age(self.Jake_Ryan, "teenage")
        ## He is athletic and outgoing, but can be arrogant at times.
        ## He is also Nina's crush.
        self.set_relation(self.Nina_Harman, 'crush', self.Jake_Ryan)
        self.set_relation(self.Jake_Ryan, 'crush', self.Nina_Harman)
        ## Karen Hartman is Nina's mother.
        self.set_relation(self.Nina_Harman, 'mother', self.Karen_Hartman)
        self.set_relation(self.Karen_Hartman, 'daughter', self.Nina_Harman)
        ## She is a kind and loving woman who is always supportive of her daughter.
