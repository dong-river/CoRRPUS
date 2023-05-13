## Harold Martinez, a 19 year old Hispanic boy, was working at the gas station when he noticed a customer, who looked like he needed some help.
## The man had a gun in his hand and looked pretty desperate.
## "Hey you!"
## The customer yelled.
## "Don't move!"
## Harold stepped out from behind the counter and got on his knees.
## The customer grabbed him by the collar of his shirt and pulled him close to him.
## "Listen very carefully," He said in a whisper that was almost a growl, "Give me all the money from the register and nobody gets hurt."
## He pulled out a stack of twenty dollar bills from his pocket and set them on the counter.
## He had some long greasy hair that stuck out everywhere on his head.

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
        self.Harold_Martinez = character('Harold Martinez')
        self.David_Garcia = character('David Garcia')

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
        self.set_age(self.Harold_Martinez, "19")
        self.set_gender(self.Harold_Martinez, "male")
        self.set_age(self.David_Garcia, "desperate")
        self.set_gender(self.David_Garcia, "male")
        self.set_relation(self.Harold_Martinez, 'boss', self.David_Garcia)
        self.set_relation(self.David_Garcia, 'employee', self.Harold_Martinez)
        self.set_appearance(self.David_Garcia, "long greasy hair")
        self.set_appearance(self.Harold_Martinez, "Hispanic")
