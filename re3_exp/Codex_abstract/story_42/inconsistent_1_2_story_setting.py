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
        ## Valerie is a high school senior who has always been a good student.
        self.set_age(self.Valerie_Russo, "high school senior")
        ## She's been told her whole life that she's going to be a great doctor, just like her mother.
        self.set_occupation(self.Valerie_Russo, "doctor")
        self.set_relation(self.Valerie_Russo, "mother", self.Antoinette_Russo)
        self.set_occupation(self.Antoinette_Russo, "surgeon")
        ## But when she starts to doubt her abilities, she decides to take a gap year to travel the world and find herself.
        ## The story is set in the present day, in the small town of Valerie's childhood home.
        ## Valerie Russo is a young woman of Italian descent.
        self.set_gender(self.Valerie_Russo, "female")
        ## She has dark hair and brown eyes.
        self.set_appearance(self.Valerie_Russo, "dark hair")
        self.set_appearance(self.Valerie_Russo, "brown eyes")
        ## She is average height and build.
        self.set_appearance(self.Valerie_Russo, "average height")
        self.set_appearance(self.Valerie_Russo, "average build")
        ## Carl Russo is Valerie's father.
        self.set_relation(self.Valerie_Russo, "father", self.Carl_Russo)
        self.set_relation(self.Carl_Russo, "daughter", self.Valerie_Russo)
        ## He is a tall man of average build with salt and pepper hair.
        self.set_appearance(self.Carl_Russo, "tall")
        self.set_appearance(self.Carl_Russo, "average build")
        self.set_appearance(self.Carl_Russo, "salt and pepper hair")
        ## He is a successful businessman who owns his own company.
        self.set_occupation(self.Carl_Russo, "businessman")
        ## Antoinette Russo is Valerie's mother.
        self.set_relation(self.Valerie_Russo, "mother", self.Antoinette_Russo)
        self.set_relation(self.Antoinette_Russo, "daughter", self.Valerie_Russo)
        ## She is a petite woman with dark hair and brown eyes.
        self.set_appearance(self.Antoinette_Russo, "petite")
        self.set_appearance(self.Antoinette_Russo, "dark hair")
        self.set_appearance(self.Antoinette_Russo, "brown eyes")
        ## She is a successful surgeon who owns her own practice.
        self.set_occupation(self.Antoinette_Russo, "surgeon")
