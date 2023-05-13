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
        ## The story is set in a small town in the United States.
        ## Shannon Fitzgerald is a young woman in her early twenties.
        self.set_age(self.Shannon_Fitzgerald, "early twenties")
        self.set_gender(self.Shannon_Fitzgerald, "female")
        ## She is of average height and build, with shoulder-length brown hair and brown eyes.
        self.set_appearance(self.Shannon_Fitzgerald, "average height")
        self.set_appearance(self.Shannon_Fitzgerald, "build")
        self.set_appearance(self.Shannon_Fitzgerald, "shoulder-length brown hair")
        self.set_appearance(self.Shannon_Fitzgerald, "brown eyes")
        ## Shannon is a diligent student, working hard to earn her degree despite the challenges she faces.
        self.set_occupation(self.Shannon_Fitzgerald, "student")
        ## Olivia Kane is a woman in her thirties.
        self.set_age(self.Olivia_Kane, "thirties")
        self.set_gender(self.Olivia_Kane, "female")
        ## She is the wife of a wealthy man and the mother of two children.
        self.set_relation(self.Olivia_Kane, 'wife', self.Richard_Kane)
        self.set_relation(self.Richard_Kane, 'husband', self.Olivia_Kane)
        self.set_relation(self.Olivia_Kane, 'mother', self.Shannon_Fitzgerald)
        self.set_relation(self.Shannon_Fitzgerald, 'daughter', self.Olivia_Kane)
        ## Olivia is a beautiful woman, with long blonde hair and blue eyes.
        self.set_appearance(self.Olivia_Kane, "beautiful")
        self.set_appearance(self.Olivia_Kane, "long blonde hair")
        self.set_appearance(self.Olivia_Kane, "blue eyes")
        ## Richard Kane is a man in his forties.
        self.set_age(self.Richard_Kane, "forties")
        self.set_gender(self.Richard_Kane, "male")
        ## He is the wealthy owner of a large company and the brother of Olivia Kane.
        self.set_relation(self.Richard_Kane, 'brother', self.Olivia_Kane)
        self.set_relation(self.Olivia_Kane, 'sister', self.Richard_Kane)
        self.set_occupation(self.Richard_Kane, "owner of a large company")
        ## Richard is a tall man with dark hair and blue eyes.
        self.set_appearance(self.Richard_Kane, "tall")
        self.set_appearance(self.Richard_Kane, "dark hair")
        self.set_appearance(self.Richard_Kane, "blue eyes")

