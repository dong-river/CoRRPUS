## Landon Shaw, the handsome mechanic, was just climbing into bed when his sister Maggie barged in without knocking.
## "What is it?"
## he asked irritably.
## He was exhausted and was hoping to get a full eight hours of sleep tonight, but that seemed unlikely now.
## "I need to talk to you," she said insistently.
## Landon didn't want to talk, he wanted to sleep but Maggie looked so desperate that he couldn't say no.
## "Fine," he said in an irritated tone, "what do you want?"
## Maggie sat down on the edge of her brother's bed and took a deep breath.
## "I need your help."
## Her words sounded thick with tears.
## "You are my only hope."
## She had waited until she knew her brother would be home before she came over and now it was already after midnight; there wasn't much time left to make him change his mind about her plan.
## "What are you talking about?"
## Landon replied harshly.
## "Just spit it out already."
## He rolled over and turned off the light by his side of the bed before settling down to go back to sleep for just another few minutes before his alarm clock would go off in a couple of hours anyway.
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
        self.Payton_Parskin = character('Payton Parskin')
        self.Landon_Shaw = character('Landon Shaw')
        self.Maggie_Shaw = character('Maggie Shaw')

    def story(self):
        ## Landon Shaw, the handsome mechanic, was just climbing into bed when his sister Maggie barged in without knocking.
        self.Landon_Shaw.gender.append('male')
        self.Landon_Shaw.occupation.append('mechanic')
        self.Landon_Shaw.relations['sister'] = 'Maggie_Shaw'
        self.Maggie_Shaw.relations['brother'] = 'Landon_Shaw'
        ## "What is it?"
        ## he asked irritably.
        ## He was exhausted and was hoping to get a full eight hours of sleep tonight, but that seemed unlikely now.
        ## "I need to talk to you," she said insistently.
        ## Landon didn't want to talk, he wanted to sleep but Maggie looked so desperate that he couldn't say no.
        ## "Fine," he said in an irritated tone, "what do you want?"
        ## Maggie sat down on the edge of her brother's bed and took a deep breath.
        ## "I need your help."
        ## Her words sounded thick with tears.
        ## "You are my only hope."
        ## She had waited until she knew her brother would be home before she came over and now it was already after midnight; there wasn't much time left to make him change his mind about her plan.
        ## "What are you talking about?"
        ## Landon replied harshly.
        ## "Just spit it out already."
        ## He rolled over and turned off the light by his side of the bed before settling down to go back to sleep for just another few minutes before his alarm clock would go off in a couple of hours anyway.

