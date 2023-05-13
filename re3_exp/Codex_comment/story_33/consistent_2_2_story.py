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

    def story(self):
        ## Charles Wilson sits in his office filling out reports.
        ## He's in his forties, in good shape, and has short black hair.
        self.Charles_Wilson.appearance.append('forties')
        self.Charles_Wilson.appearance.append('good shape')
        self.Charles_Wilson.appearance.append('short black hair')
        ## His wife is out shopping.
        self.Charles_Wilson.relations['wife'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['husband'] = 'Charles_Wilson'
        ## She thinks he's at work but instead he's sitting at his desk daydreaming about the girl he's been dating for the past few weeks.
        self.Nina_Peterson.relations['girlfriend'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['boyfriend'] = 'Charles_Wilson'
        ## She's a college student and is twenty years younger than him but Charles doesn't care.
        self.Nina_Peterson.age.append('college student')
        ## As long as she has a pulse she can have him.
        ## He fantasizes about taking her to dinner tomorrow night and ending up back at her place to have sex.
        ## He thinks about bending her over, putting it in doggy style, pounding away until she moans.
        ## He thinks about pounding her until she screams for mercy, begging him to stop with tears streaming down her face...  "Good afternoon Charles."
        ## His sergeant calls from the doorway of his office waking him from his fantasy.
        self.Charles_Wilson.relations['sergeant'] = 'Jeff_Foster'
        self.Jeff_Foster.relations['officer'] = 'Charles_Wilson'
        ## "Just wanted to let you know we just got a rape case down on the South side."
        ## "Great!"
        ## Charles said sarcastically with a sigh.
        ## "When do I get my vacation?"
        ## His sergeant laughs as he walks away leaving Charles alone with his fantasies again.

