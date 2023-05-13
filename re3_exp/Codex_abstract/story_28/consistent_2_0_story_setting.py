## At thirty-six years old, Payton's biological clock is ticking, but she's never found the right person to have children with.
## She's always been a career woman, and she's not sure she's ready to give up her freedom.
## When her best friend from college dies unexpectedly, leaving behind a four-year-old daughter, Payton is faced with the decision of whether or not to take on the responsibility of raising her.
## The story is set in New York City.
## Payton Dupree is a 36-year-old successful businesswoman.
## She has never been married and does not have any children.
## She is fiercely independent and has always put her career first.
## Amanda Dupree is Payton's deceased best friend from college.
## She was a stay-at-home mom and died suddenly, leaving behind her 4-year-old daughter Olivia.
## Olivia Dupree is Payton's niece and Amanda's daughter.
## She is a 4-year-old girl who is shy and introverted.
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
        self.Payton_Dupree = character('Payton Dupree')
        self.Amanda_Dupree = character('Amanda Dupree')
        self.Olivia_Dupree = character('Olivia Dupree')

    def story(self):
        ## At thirty-six years old, Payton's biological clock is ticking, but she's never found the right person to have children with.
        self.Payton_Dupree.age.append('thirty-six')
        ## She's always been a career woman, and she's not sure she's ready to give up her freedom.
        self.Payton_Dupree.occupation.append('career woman')
        ## When her best friend from college dies unexpectedly, leaving behind a four-year-old daughter, Payton is faced with the decision of whether or not to take on the responsibility of raising her.
        self.Payton_Dupree.relations['best friend from college'] = 'Amanda_Dupree'
        self.Amanda_Dupree.relations['best friend from college'] = 'Payton_Dupree'
        self.Amanda_Dupree.relations['daughter'] = 'Olivia_Dupree'
        self.Olivia_Dupree.relations['mother'] = 'Amanda_Dupree'
        ## The story is set in New York City.
        ## Payton Dupree is a 36-year-old successful businesswoman.
        self.Payton_Dupree.age.append('thirty-six')
        self.Payton_Dupree.occupation.append('successful businesswoman')
        ## She has never been married and does not have any children.
        self.Payton_Dupree.relations['married'] = 'none'
        self.Payton_Dupree.relations['children'] = 'none'
        ## She is fiercely independent and has always put her career first.
        self.Payton_Dupree.appearance.append('fiercely independent')
        self.Payton_Dupree.appearance.append('put her career first')
        ## Amanda Dupree is Payton's deceased best friend from college.
        self.Amanda_Dupree.relations['best friend from college'] = 'Payton_Dupree'
        ## She was a stay-at-home mom and died suddenly, leaving behind her 4-year-old daughter Olivia.
        self.Amanda_Dupree.relations['mother'] = 'Olivia_Dupree'
        self.Amanda_Dupree.occupation.append('stay-at-home mom')
        ## Olivia Dupree is Payton's niece and Amanda's daughter.
        self.Olivia_Dupree.relations['mother'] = 'Amanda_Dupree'
        self.Olivia_Dupree.relations['aunt'] = 'Payton_Dupree'
        ## She is a 4-year-old girl who is shy and introverted.
        self.Olivia_Dupree.age.append('four')
        self.Olivia_Dupree.gender.append('female')
        self.Olivia_Dupree.appearance.append('shy')
        self.Olivia_Dupree.appearance.append('introverted')
