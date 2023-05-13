## Harold Martinez, a 19 year old Hispanic boy, was working at the gas station when he noticed a customer, who looked like he needed some help.
## The man had a gun in his hand and looked pretty desperate.
## "Hey you!"
## The customer yelled.
## "Don't move!"
## Harold stepped out from behind the counter and got on his knees.
## The customer grabbed him by the collar of his shirt and pulled him close to him.
## "Listen very carefully," He said in a whisper that was almost a growl, "Give me all the money from the register and nobody gets hurt."
## He pulled out a stack of twenty dollar bills from his pocket and set them on the counter.
## He had some long greasy hair that stuck out everywhere on his head.
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
        self.Harold_Martinez = character('Harold Martinez')
        self.David_Garcia = character('David Garcia')

    def story(self):
        ## Harold Martinez, a 19 year old Hispanic boy, was working at the gas station when he noticed a customer, who looked like he needed some help.
        self.Harold_Martinez.age.append('19 year old')
        self.Harold_Martinez.gender.append('male')
        self.Harold_Martinez.occupation.append('gas station')
        ## The man had a gun in his hand and looked pretty desperate.
        self.David_Garcia.appearance.append('gun')
        ## "Hey you!"
        ## The customer yelled.
        ## "Don't move!"
        ## Harold stepped out from behind the counter and got on his knees.
        self.David_Garcia.appearance.append('desperate')
        ## The customer grabbed him by the collar of his shirt and pulled him close to him.
        self.David_Garcia.appearance.append('greasy hair')
        ## "Listen very carefully," He said in a whisper that was almost a growl, "Give me all the money from the register and nobody gets hurt."
        ## He pulled out a stack of twenty dollar bills from his pocket and set them on the counter.
        ## He had some long greasy hair that stuck out everywhere on his head.

