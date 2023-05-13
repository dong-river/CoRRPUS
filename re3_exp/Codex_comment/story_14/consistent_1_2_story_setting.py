## Jenny's life changed forever the day she discovered her ability to turn invisible.
## At first, it was a fun game to play with her friends, but soon Jenny realized that she could use her power for more than just pranks.
## When she starts using it to take the town's corrupt mayor down, she realizes that being invisible is more than just a gift--it's a way of life.
## The story is set in the small town of Shepherdstown.
## Jenny Anderson is a young girl with blonde hair and blue eyes.
## She is small for her age, and is often rebel without a cause.
## Jimmy Jackson is Jenny's best friend.
## He is a lanky boy with dark hair and brown eyes.
## He is always up for a good time, and is always trying to get Jenny into trouble.
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
        self.Jenny_Anderson.appearance.append('blonde hair')
        self.Jenny_Anderson.appearance.append('blue eyes')
        self.Jenny_Anderson.age.append('young')
        self.Jenny_Anderson.gender.append('female')
        ## At first, it was a fun game to play with her friends, but soon Jenny realized that she could use her power for more than just pranks.
        self.Jenny_Anderson.relations['friend'] = 'Jimmy_Jackson'
        self.Jimmy_Jackson.relations['friend'] = 'Jenny_Anderson'
        ## When she starts using it to take the town's corrupt mayor down, she realizes that being invisible is more than just a gift--it's a way of life.
        ## The story is set in the small town of Shepherdstown.
        ## Jenny Anderson is a young girl with blonde hair and blue eyes.
        ## She is small for her age, and is often rebel without a cause.
        self.Jenny_Anderson.appearance.append('blonde hair')
        self.Jenny_Anderson.appearance.append('blue eyes')
        self.Jenny_Anderson.age.append('young')
        self.Jenny_Anderson.gender.append('female')
        ## Jimmy Jackson is Jenny's best friend.
        ## He is a lanky boy with dark hair and brown eyes.
        ## He is always up for a good time, and is always trying to get Jenny into trouble.
        self.Jimmy_Jackson.appearance.append('dark hair')
        self.Jimmy_Jackson.appearance.append('brown eyes')
        self.Jimmy_Jackson.age.append('young')
        self.Jimmy_Jackson.gender.append('male')
        ## Principal Stevens is the principal of Jenny's school.
        ## He is a middle-aged man with graying hair and glasses.
        ## He is a fair and just man, but is also very strict.
        self.Principal_Stevens.appearance.append('gray hair')
        self.Principal_Stevens.appearance.append('glasses')
        self.Principal_Stevens.age.append('middle-aged')
        self.Principal_Stevens.gender.append('male')
        self.Principal_Stevens.occupation.append('principal')
        self.Principal_Stevens.relations['school'] = 'Jenny_Anderson'
        self.Jenny_Anderson.relations['school'] = 'Principal_Stevens'

