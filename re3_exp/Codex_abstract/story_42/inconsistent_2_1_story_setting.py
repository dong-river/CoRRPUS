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
        ## The story is set in the present day, in the small town of Valerie's childhood home.
        ## Valerie Russo is a young woman of Italian descent.
        ## She has dark hair and brown eyes.
        self.set_gender(self.Valerie_Russo, "female")
        self.set_appearance(self.Valerie_Russo, "dark hair")
        self.set_appearance(self.Valerie_Russo, "brown eyes")
        ## She is average height and build.
        ## Carl Russo is Valerie's father.
        self.set_relation(self.Valerie_Russo, 'father', self.Carl_Russo)
        self.set_relation(self.Carl_Russo, 'daughter', self.Valerie_Russo)
        ## He is a large man with dark hair and brown eyes.
        self.set_appearance(self.Carl_Russo, "dark hair")
        self.set_appearance(self.Carl_Russo, "brown eyes")
        ## He is a retired police officer who now works as a security guard at the local hospital.
        self.set_occupation(self.Carl_Russo, "security guard")
        ## Antoinette Russo is Valerie's mother.
        self.set_relation(self.Valerie_Russo, 'mother', self.Antoinette_Russo)
        self.set_relation(self.Antoinette_Russo, 'daughter', self.Valerie_Russo)
        ## She is a petite woman with dark hair and brown eyes.
        self.set_appearance(self.Antoinette_Russo, "dark hair")
        self.set_appearance(self.Antoinette_Russo, "brown eyes")
        ## She is a successful surgeon who owns her own practice.
        self.set_occupation(self.Antoinette_Russo, "surgeon")
        
