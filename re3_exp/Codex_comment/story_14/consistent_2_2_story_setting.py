## Jenny's life changed forever the day she discovered her ability to turn invisible.
## At first, it was a fun game to play with her friends, but soon Jenny realized that she could use her power for more than just pranks.
## When she starts using it to take the town's corrupt mayor down, she realizes that being invisible is more than just a gift--it's a way of life.
## The story is set in the small town of Shepherdstown.
## Jenny Anderson is a young girl with blonde hair and blue eyes.
## She is small for her age, and is often rebel without a cause.
## Jimmy Jackson is Jenny's boyfriend and the star quarterback of the football team at their school..
## Principal Stevens is the principal of Jenny's school.
## He is a middle-aged man with graying hair and glasses.
## He is a fair and just man, but is also very strict.
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
        self.Jenny_Anderson = character('Jenny Anderson')
        self.Jimmy_Jackson = character('Jimmy Jackson')
        self.Principal_Stevens = character('Principal Stevens')

    def story(self):
        ## Jenny's life changed forever the day she discovered her ability to turn invisible.
        ## At first, it was a fun game to play with her friends, but soon Jenny realized that she could use her power for more than just pranks.
        ## When she starts using it to take the town's corrupt mayor down, she realizes that being invisible is more than just a gift--it's a way of life.
        ## The story is set in the small town of Shepherdstown.
        ## Jenny Anderson is a young girl with blonde hair and blue eyes.
        self.Jenny_Anderson.appearance.append('blonde hair')
        self.Jenny_Anderson.appearance.append('blue eyes')
        self.Jenny_Anderson.age.append('young')
        self.Jenny_Anderson.gender.append('female')
        ## She is small for her age, and is often rebel without a cause.
        self.Jenny_Anderson.appearance.append('small')
        ## Jimmy Jackson is Jenny's boyfriend and the star quarterback of the football team at their school..
        self.Jenny_Anderson.relations['boyfriend'] = 'Jimmy_Jackson'
        self.Jimmy_Jackson.relations['girlfriend'] = 'Jenny_Anderson'
        self.Jimmy_Jackson.occupation.append('star quarterback of the football team at their school')
        self.Jimmy_Jackson.gender.append('male')
        ## Principal Stevens is the principal of Jenny's school.
        self.Principal_Stevens.occupation.append('principal of Jenny\'s school')
        ## He is a middle-aged man with graying hair and glasses.
        self.Principal_Stevens.appearance.append('graying hair')
        self.Principal_Stevens.appearance.append('glasses')
        self.Principal_Stevens.age.append('middle-aged')
        self.Principal_Stevens.gender.append('male')
        ## He is a fair and just man, but is also very strict.
        self.Principal_Stevens.occupation.append('fair and just man')
        self.Principal_Stevens.occupation.append('very strict')

