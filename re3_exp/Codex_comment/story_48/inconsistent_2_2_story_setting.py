## After the loss of her mother, Shannon is determined to keep her promise and finish her degree.
## But with mounting bills and a full-time job, Shannon is struggling to make ends meet.
## When she's offered a position as a live-in nanny for a wealthy family, Shannon jumps at the chance.
## But she soon discovers that the family's secrets are far more dangerous than she could have imagined.
## The story is set in a small town in the United States.
## Shannon Fitzgerald is a young woman in her early twenties.
## She is of average height and build, with shoulder-length brown hair and brown eyes.
## Shannon is a diligent student, working hard to earn her degree despite the challenges she faces.
## Olivia Kane is a woman in her thirties.
## She is the wife of a wealthy man and the mother of two children.
## Olivia is a beautiful woman, with long blonde hair and blue eyes.
## Richard Kane is a man in his forties.
## He is the wealthy owner of a large company and the brother of Olivia Kane.
## Richard is a tall man with dark hair and blue eyes
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
        self.Shannon_Fitzgerald = character('Shannon Fitzgerald')
        self.Olivia_Kane = character('Olivia Kane')
        self.Richard_Kane = character('Richard Kane')

    def story(self):
        ## The story is set in a small town in the United States.
        ## Shannon Fitzgerald is a young woman in her early twenties.
        self.Shannon_Fitzgerald.age.append('young')
        self.Shannon_Fitzgerald.gender.append('female')
        ## She is of average height and build, with shoulder-length brown hair and brown eyes.
        self.Shannon_Fitzgerald.appearance.append('average height')
        self.Shannon_Fitzgerald.appearance.append('average build')
        self.Shannon_Fitzgerald.appearance.append('shoulder-length brown hair')
        self.Shannon_Fitzgerald.appearance.append('brown eyes')
        ## Shannon is a diligent student, working hard to earn her degree despite the challenges she faces.
        self.Shannon_Fitzgerald.occupation.append('student')
        ## Olivia Kane is a woman in her thirties.
        self.Olivia_Kane.age.append('thirties')
        self.Olivia_Kane.gender.append('female')
        ## She is the wife of a wealthy man and the mother of two children.
        self.Olivia_Kane.relations['husband'] = 'Richard_Kane'
        self.Olivia_Kane.relations['children'] = 'two'
        ## Olivia is a beautiful woman, with long blonde hair and blue eyes.
        self.Olivia_Kane.appearance.append('beautiful')
        self.Olivia_Kane.appearance.append('long blonde hair')
        self.Olivia_Kane.appearance.append('blue eyes')
        ## Richard Kane is a man in his forties.
        self.Richard_Kane.age.append('forties')
        self.Richard_Kane.gender.append('male')
        ## He is the wealthy owner of a large company and the brother of Olivia Kane.
        self.Richard_Kane.occupation.append('owner of a large company')
        self.Richard_Kane.relations['brother'] = 'Olivia_Kane'
        ## Richard is a tall man with dark hair and blue eyes
        self.Richard_Kane.appearance.append('tall')
        self.Richard_Kane.appearance.append('dark hair')
        self.Richard_Kane.appearance.append('blue eyes')

