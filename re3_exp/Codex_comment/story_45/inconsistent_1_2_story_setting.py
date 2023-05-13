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

    def story(self):
        ## Nina, an unassuming pre-teen, discovers she has the ability to astral project outside of her body.
        self.Nina_Harman.gender.append('female')
        self.Nina_Harman.age.append('pre-teen')
        ## She soon learns that she is not the only one with this ability and that there are others who would use this power for evil.
        ## Nina must use her new found abilities to stop them.
        ## The story is set in a small town in the United States.
        ## Nina Harman is a small, delicate looking pre-teen with long dark hair and brown eyes.
        self.Nina_Harman.appearance.append('long dark hair')
        self.Nina_Harman.appearance.append('brown eyes')
        ## She is shy and withdrawn, but has a kind heart.
        ## Jake Ryan is a handsome teenage boy who is popular at school.
        self.Jake_Ryan.gender.append('male')
        self.Jake_Ryan.age.append('teenage')
        self.Jake_Ryan.appearance.append('handsome')
        ## He is athletic and outgoing, but can be arrogant at times.
        ## He is also Nina's crush.
        self.Nina_Harman.relations['crush'] = 'Jake_Ryan'
        ## Karen Hartman is Nina's mother.
        self.Nina_Harman.relations['mother'] = 'Karen_Hartman'
        ## She is a kind and loving woman who is always supportive of her daughter.

