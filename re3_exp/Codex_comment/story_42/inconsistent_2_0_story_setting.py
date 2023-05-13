## Valerie is a high school senior who has always been a good student.
## She's been told her whole life that she's going to be a great doctor, just like her mother.
## But when she starts to doubt her abilities, she decides to take a gap year to travel the world and find herself.
## The story is set in the present day, in the small town of Valerie's childhood home.
## Valerie Russo is a young woman of Italian descent.
## She has dark hair and brown eyes.
## She is average height and build.
## Carl Russo is Valerie's father.
## He is a large man with dark hair and brown eyes.
## He is a retired police officer who now works as a security guard at the local hospital.
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
        self.Valerie_Russo.age.append('high school senior')
        ## She's been told her whole life that she's going to be a great doctor, just like her mother.
        self.Valerie_Russo.occupation.append('doctor')
        self.Antoinette_Russo.occupation.append('doctor')
        self.Valerie_Russo.relations['mother'] = 'Antoinette_Russo'
        self.Antoinette_Russo.relations['daughter'] = 'Valerie_Russo'
        ## But when she starts to doubt her abilities, she decides to take a gap year to travel the world and find herself.
        ## The story is set in the present day, in the small town of Valerie's childhood home.
        ## Valerie Russo is a young woman of Italian descent.
        ## She has dark hair and brown eyes.
        self.Valerie_Russo.appearance.append('dark hair')
        self.Valerie_Russo.appearance.append('brown eyes')
        ## She is average height and build.
        self.Valerie_Russo.appearance.append('average height')
        self.Valerie_Russo.appearance.append('average build')
        ## Carl Russo is Valerie's father.
        self.Valerie_Russo.relations['father'] = 'Carl_Russo'
        self.Carl_Russo.relations['daughter'] = 'Valerie_Russo'
        ## He is a large man with dark hair and brown eyes.
        self.Carl_Russo.appearance.append('large')
        self.Carl_Russo.appearance.append('dark hair')
        self.Carl_Russo.appearance.append('brown eyes')
        ## He is a retired police officer who now works as a security guard at the local hospital.
        self.Carl_Russo.occupation.append('retired police officer')
        self.Carl_Russo.occupation.append('security guard')
        ## Antoinette Russo is Valerie's mother.
        self.Valerie_Russo.relations['mother'] = 'Antoinette_Russo'
        self.Antoinette_Russo.relations['daughter'] = 'Valerie_Russo'
        ## She is a petite woman with dark hair and brown eyes.
        self.Antoinette_Russo.appearance.append('petite')
        self.Antoinette_Russo.appearance.append('dark hair')
        self.Antoinette_Russo.appearance.append('brown eyes')
        ## She is a successful surgeon who owns her own practice.
        self.Antoinette_Russo.occupation.append('surgeon')
        self.Antoinette_Russo.occupation.append('owns own practice')

