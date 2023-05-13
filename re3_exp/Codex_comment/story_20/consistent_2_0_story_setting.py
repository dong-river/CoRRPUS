## The novel is set in a future in which the world is at war.
## The main character, a young girl, is drafted into the army.
## The story is set in a future world that is at war.
## Olivia Fria Spierings is a young girl who is drafted into the army.
## She is a small, skinny girl with long dark hair and blue eyes.
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
        ## Olivia Fria Spierings is a young girl who is drafted into the army.
        self.Olivia_Fria_Spierings.gender.append('female')
        self.Olivia_Fria_Spierings.age.append('young')
        ## She is a small, skinny girl with long dark hair and blue eyes.
        self.Olivia_Fria_Spierings.appearance.append('small')
        self.Olivia_Fria_Spierings.appearance.append('skinny')
        self.Olivia_Fria_Spierings.appearance.append('long dark hair')
        self.Olivia_Fria_Spierings.appearance.append('blue eyes')
        ## Colonel Damien Riggs is the commanding officer of Olivia's unit.
        self.Olivia_Fria_Spierings.relations['commanding officer'] = 'Colonel_Damien_Riggs'
        self.Colonel_Damien_Riggs.relations['commanding officer'] = 'Olivia_Fria_Spierings'
        ## He is a tall, muscular man in his early 40s with short graying hair and blue eyes.
        self.Colonel_Damien_Riggs.appearance.append('tall')
        self.Colonel_Damien_Riggs.appearance.append('muscular')
        self.Colonel_Damien_Riggs.appearance.append('early 40s')
        self.Colonel_Damien_Riggs.appearance.append('short graying hair')
        self.Colonel_Damien_Riggs.appearance.append('blue eyes')

