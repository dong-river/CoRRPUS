## Connor Riley sat in the shuttle craft, feeling uneasy.
## He was scheduled to be the pilot of the Mars expedition and should have been excited about that, but he wasn't.
## He had not been consulted about the makeup of the rest of the team, and he didn't know why he felt so uneasy about that either.
## The mission was all about searching for signs of life on Mars, and Dr. Harper was a plant biologist.
## There was no point having a doctor if they weren't going to look for signs of life there.
## And he knew from his own research that any planets that had enough water would also support life on them at some point in their history.
## "The Earth isn't an exception," Connor told himself quietly while tapping his fingers on his thigh nervously.
## He really wasn't looking forward to being stuck in a small space with four other people for a six-month flight to Mars, but one person in particular worried him even more than anyone else on the team: Nadia Kaminski.
## Nadia's field of expertise was astrobiology, so why had she been chosen?
## Unless someone knew something she didn't know!
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
        self.Nadia_Kaminski = character('Nadia Kaminski')
        self.Connor_Riley = character('Connor Riley')
        self.Abigail_Harper = character('Abigail Harper')

    def story(self):
        ## Connor Riley sat in the shuttle craft, feeling uneasy.
        ## He was scheduled to be the pilot of the Mars expedition and should have been excited about that, but he wasn't.
        self.Connor_Riley.occupation.append('pilot')
        ## He had not been consulted about the makeup of the rest of the team, and he didn't know why he felt so uneasy about that either.
        ## The mission was all about searching for signs of life on Mars, and Dr. Harper was a plant biologist.
        self.Abigail_Harper.occupation.append('plant biologist')
        ## There was no point having a doctor if they weren't going to look for signs of life there.
        ## And he knew from his own research that any planets that had enough water would also support life on them at some point in their history.
        ## "The Earth isn't an exception," Connor told himself quietly while tapping his fingers on his thigh nervously.
        ## He really wasn't looking forward to being stuck in a small space with four other people for a six-month flight to Mars, but one person in particular worried him even more than anyone else on the team: Nadia Kaminski.
        self.Connor_Riley.relations['Nadia Kaminski'] = 'worried'
        ## Nadia's field of expertise was astrobiology, so why had she been chosen?
        self.Nadia_Kaminski.occupation.append('astrobiology')
        ## Unless someone knew something she didn't know!

