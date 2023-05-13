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

    def set_appearance(self, character, appearance):
        character.appearance.append(appearance)
    
    def set_occupation(self, character, occupation):
        character.occupation.append(occupation)
    
    def set_gender(self, character, gender):
        character.gender.append(gender)
    
    def set_age(self, character, age):
        character.age.append(age)
    
    def set_relation(self, character, relation, other_character):
        character.relations[relation] = other_character.name
        
    def story(self):
        ## The novel is set in a future in which the world is at war.
        ## The main character, a young girl, is drafted into the army.
        self.set_gender(self.Olivia_Fria_Spierings, "female")
        self.set_age(self.Olivia_Fria_Spierings, "young")
        ## The story is set in a future world that is at war.
        ## Olivia Fria Spierings is a young girl who is drafted into the army.
        ## She is a small, skinny girl with long dark hair and blue eyes.
        self.set_appearance(self.Olivia_Fria_Spierings, "long dark hair")
        self.set_appearance(self.Olivia_Fria_Spierings, "blue eyes")
        ## Colonel Damien Riggs is the commanding officer of Olivia's unit.
        self.set_relation(self.Olivia_Fria_Spierings, 'commanding officer', self.Colonel_Damien_Riggs)
        self.set_relation(self.Colonel_Damien_Riggs, 'unit', self.Olivia_Fria_Spierings)
        ## He is a tall, muscular man in his early 40s with short graying hair and blue eyes.
        self.set_appearance(self.Colonel_Damien_Riggs, "short graying hair")
        self.set_appearance(self.Colonel_Damien_Riggs, "blue eyes")
        self.set_gender(self.Colonel_Damien_Riggs, "male")
        self.set_age(self.Colonel_Damien_Riggs, "early 40s")
 
## Create a world model state to track each character's appearance, personality, and relations with other characters.

