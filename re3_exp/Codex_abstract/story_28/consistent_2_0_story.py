## Olivia Dupree's cheeks were stained with tears as she approached the boarding area for the plane to New York.
## Her arms were wrapped around her guardian's waist, and she was clutching her new backpack to her chest.
## She was only four years old, but she had never been away from home before and didn't know why she had to go on this trip.
## "I don't want to go," Olivia whimpered, looking up at her mother's face.
## Amanda knelt down on one knee and embraced her daughter in a tight hug.
## "Olivia, you have to go.
## Your Aunt Payton is very busy and can't take care of you right now," Amanda said softly.
## "I know you're going to like New York."
## Olivia released a loud sob and buried her face in Amanda's shoulder.
## "It'll be okay," Amanda promised her daughter again.
## "You'll stay with your aunt for a few days, get some rest, eat good food-the works!
## I bet it'll be really fun."
## Olivia looked at Amanda and wiped a tear away from the corner of her eye with the back of her hand.
## "Are you coming back?"

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
        ## Olivia Dupree's cheeks were stained with tears as she approached the boarding area for the plane to New York.
        self.set_appearance(self.Olivia_Dupree, "cheeks stained with tears")
        ## Her arms were wrapped around her guardian's waist, and she was clutching her new backpack to her chest.
        self.set_relation(self.Olivia_Dupree, 'guardian', self.Amanda_Dupree)
        self.set_relation(self.Amanda_Dupree, 'child', self.Olivia_Dupree)
        ## She was only four years old, but she had never been away from home before and didn't know why she had to go on this trip.
        self.set_age(self.Olivia_Dupree, "four")
        ## "I don't want to go," Olivia whimpered, looking up at her mother's face.
        ## Amanda knelt down on one knee and embraced her daughter in a tight hug.
        self.set_relation(self.Olivia_Dupree, 'mother', self.Amanda_Dupree)
        self.set_relation(self.Amanda_Dupree, 'daughter', self.Olivia_Dupree)
        ## "Olivia, you have to go.
        ## Your Aunt Payton is very busy and can't take care of you right now," Amanda said softly.
        self.set_relation(self.Olivia_Dupree, 'aunt', self.Payton_Dupree)
        self.set_relation(self.Payton_Dupree, 'niece', self.Olivia_Dupree)
        ## "I know you're going to like New York."
        ## Olivia released a loud sob and buried her face in Amanda's shoulder.
        ## "It'll be okay," Amanda promised her daughter again.
        ## "You'll stay with your aunt for a few days, get some rest, eat good food-the works!
        ## I bet it'll be really fun."
        ## Olivia looked at Amanda and wiped a tear away from the corner of her eye with the back of her hand.
        ## "Are you coming back?"
