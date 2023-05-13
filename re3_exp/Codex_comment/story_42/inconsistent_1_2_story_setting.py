## Valerie is a high school senior who has always been a good student.
## She's been told her whole life that she's going to be a great doctor, just like her mother.
## But when she starts to doubt her abilities, she decides to take a gap year to travel the world and find herself.
## The story is set in the present day, in the small town of Valerie's childhood home.
## Valerie Russo is a young woman of Italian descent.
## She has dark hair and brown eyes.
## She is average height and build.
## Carl Russo is Valerie's father.
## He is a tall man of average build with salt and pepper hair.
## He is a successful businessman who owns his own company.
## Antoinette Russo is Valerie's mother.
## She is a petite woman with dark hair and brown eyes.
## She is a successful surgeon who owns her own practice.
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
        self.Valerie_Russo = character('Valerie Russo')
        self.Carl_Russo = character('Carl Russo')
        self.Antoinette_Russo = character('Antoinette Russo')

    def story(self):
        ## Valerie is a high school senior who has always been a good student.
        ## She's been told her whole life that she's going to be a great doctor, just like her mother.
        ## But when she starts to doubt her abilities, she decides to take a gap year to travel the world and find herself.
        self.Valerie_Russo.age.append('high school senior')
        self.Valerie_Russo.occupation.append('student')
        self.Valerie_Russo.relations['mother'] = 'Antoinette_Russo'
        self.Antoinette_Russo.occupation.append('surgeon')
        ## The story is set in the present day, in the small town of Valerie's childhood home.
        ## Valerie Russo is a young woman of Italian descent.
        self.Valerie_Russo.gender.append('female')
        ## She has dark hair and brown eyes.
        self.Valerie_Russo.appearance.append('dark hair')
        self.Valerie_Russo.appearance.append('brown eyes')
        ## She is average height and build.
        self.Valerie_Russo.appearance.append('average height')
        self.Valerie_Russo.appearance.append('average build')
        ## Carl Russo is Valerie's father.
        self.Valerie_Russo.relations['father'] = 'Carl_Russo'
        self.Carl_Russo.relations['daughter'] = 'Valerie_Russo'
        ## He is a tall man of average build with salt and pepper hair.
        self.Carl_Russo.appearance.append('tall')
        self.Carl_Russo.appearance.append('average build')
        self.Carl_Russo.appearance.append('salt and pepper hair')
        ## He is a successful businessman who owns his own company.
        self.Carl_Russo.occupation.append('businessman')
        self.Carl_Russo.occupation.append('owns his own company')
        ## Antoinette Russo is Valerie's mother.
        self.Valerie_Russo.relations['mother'] = 'Antoinette_Russo'
        self.Antoinette_Russo.relations['daughter'] = 'Valerie_Russo'
        ## She is a petite woman with dark hair and brown eyes.
        self.Antoinette_Russo.appearance.append('petite')
        self.Antoinette_Russo.appearance.append('dark hair')
        self.Antoinette_Russo.appearance.append('brown eyes')
        ## She is a successful surgeon who owns her own practice.
        self.Antoinette_Russo.occupation.append('successful surgeon')
        self.Antoinette_Russo.occupation.append('owns her own practice')


