## Emma is your typical high school girl, until she starts seeing ghosts.
## At first she think she's going crazy, but she soon realizes that the ghosts are trying to tell her something.
## With the help of her new ghost friends, Emma has to uncover a dark secret that is haunting her school.
## The story is set in a small town in the United States.
## Emma Saunders is a teenage girl with long curly hair and brown eyes.
## She's of average height and build.
## Jackson Cooper is a teenage boy with short brown hair and blue eyes.
## He's of average height and build.
## Olivia Saunders is Emma's mother.
## She's a tall woman with blonde hair and green eyes.
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
        self.Emma_Saunders = character('Emma Saunders')
        self.Jackson_Cooper = character('Jackson Cooper')
        self.Olivia_Saunders = character('Olivia Saunders')

    def story(self):
        ## The story is set in a small town in the United States.
        ## Emma Saunders is a teenage girl with long curly hair and brown eyes.
        self.Emma_Saunders.gender.append('female')
        self.Emma_Saunders.age.append('teen')
        self.Emma_Saunders.appearance.append('long curly hair')
        self.Emma_Saunders.appearance.append('brown eyes')
        ## She's of average height and build.
        ## Jackson Cooper is a teenage boy with short brown hair and blue eyes.
        self.Jackson_Cooper.gender.append('male')
        self.Jackson_Cooper.age.append('teen')
        self.Jackson_Cooper.appearance.append('short brown hair')
        self.Jackson_Cooper.appearance.append('blue eyes')
        ## He's of average height and build.
        ## Olivia Saunders is Emma's mother.
        self.Emma_Saunders.relations['mother'] = 'Olivia_Saunders'
        self.Olivia_Saunders.relations['daughter'] = 'Emma_Saunders'
        ## She's a tall woman with blonde hair and green eyes.
        self.Olivia_Saunders.gender.append('female')
        self.Olivia_Saunders.appearance.append('tall')
        self.Olivia_Saunders.appearance.append('blonde hair')
        self.Olivia_Saunders.appearance.append('green eyes')

