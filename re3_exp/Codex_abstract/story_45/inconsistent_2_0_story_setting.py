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

    def story(self):
        ## The story is set in a small town in the United States.
        ## Nina Harman is a small, delicate looking pre-teen with long dark hair and brown eyes.
        self.Nina_Harman.appearance.append('dark hair')
        self.Nina_Harman.appearance.append('brown eyes')
        self.Nina_Harman.age.append('pre-teen')
        ## She is shy and withdrawn, but has a kind heart.
        self.Nina_Harman.personality.append('shy')
        self.Nina_Harman.personality.append('withdrawn')
        self.Nina_Harman.personality.append('kind')
        ## Jake Ryan is a handsome teenage boy who is popular at school.
        self.Jake_Ryan.appearance.append('handsome')
        self.Jake_Ryan.age.append('teenage')
        self.Jake_Ryan.personality.append('popular')
        ## He is athletic and outgoing, but can be arrogant at times.
        self.Jake_Ryan.personality.append('athletic')
        self.Jake_Ryan.personality.append('outgoing')
        self.Jake_Ryan.personality.append('arrogant')
        ## He is also Nina's crush.
        self.Nina_Harman.relations['crush'] = 'Jake_Ryan'
        ## Karen Hartman is Nina's best friend who is outgoing and energetic with a quick wit and sharp tongue.
        self.Nina_Harman.relations['best_friend'] = 'Karen_Hartman'
        self.Karen_Hartman.relations['best_friend'] = 'Nina_Harman'
        self.Karen_Hartman.personality.append('outgoing')
        self.Karen_Hartman.personality.append('energetic')
        self.Karen_Hartman.personality.append('quick_wit')
        self.Karen_Hartman.personality.append('sharp_tongue')

