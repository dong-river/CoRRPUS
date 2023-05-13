## The novel is set in a future in which the world is at war.
## The main character, a young girl, is drafted into the army.
## The story is set in a future world that is at war.
## Olivia Fria Spierings is a 15-year-old girl who is drafted into the army.
## She is of average height and build with brown hair and eyes.
## Colonel Damien Riggs is the commanding officer of Olivia's unit.
## He is a tall, muscular man in his early 40s with short graying hair and blue eyes.
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
        self.Olivia_Fria_Spierings = character('Olivia Fria Spierings')
        self.Colonel_Damien_Riggs = character('Colonel Damien Riggs')

    def story(self):
        ## The novel is set in a future in which the world is at war.
        ## The main character, a young girl, is drafted into the army.
        ## The story is set in a future world that is at war.
        ## Olivia Fria Spierings is a 15-year-old girl who is drafted into the army.
        self.Olivia_Fria_Spierings.age.append('15')
        self.Olivia_Fria_Spierings.gender.append('female')
        ## She is of average height and build with brown hair and eyes.
        self.Olivia_Fria_Spierings.appearance.append('average height and build')
        self.Olivia_Fria_Spierings.appearance.append('brown hair and eyes')
        ## Colonel Damien Riggs is the commanding officer of Olivia's unit.
        self.Colonel_Damien_Riggs.relations['commander'] = 'Olivia_Fria_Spierings'
        self.Olivia_Fria_Spierings.relations['commanded'] = 'Colonel_Damien_Riggs'
        self.Colonel_Damien_Riggs.occupation.append('commander')
        ## He is a tall, muscular man in his early 40s with short graying hair and blue eyes.
        self.Colonel_Damien_Riggs.appearance.append('tall')
        self.Colonel_Damien_Riggs.appearance.append('muscular')
        self.Colonel_Damien_Riggs.appearance.append('short graying hair')
        self.Colonel_Damien_Riggs.appearance.append('blue eyes')
        self.Colonel_Damien_Riggs.age.append('40s')
        self.Colonel_Damien_Riggs.gender.append('male')

