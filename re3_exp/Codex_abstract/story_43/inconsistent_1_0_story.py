## Shannon Mulaney walked into her dorm room and flopped down on her bed.
## She had just gotten off the phone with her mom and they'd argued again.
## The bad grades she'd been getting all semester were affecting her softball scholarship, so Shannon knew that her mom was upset.
## They hadn't spoken in two weeks, though, and Shannon still felt hurt by the fight they'd had before she left Michigan.
## Her whole life she had felt like the odd one out in the family, with both of her sisters being more popular than she was, and now it seemed that her mom was starting to see it too.
## As she lay there waiting for Olivia to come back from class, Shannon closed her eyes and fell asleep.
## "So when did your mom get cancer?"
## Jess asked as she set down a few books on top of some envelopes that were stacked on the small desk across from Shannon's bed.
## "She didn't," Shannon answered without looking up from the book open in front of her.
## "What do you mean?
## She's been sick for a year."
## Jess sounded confused.

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
        self.Shannon_Mulaney = character('Shannon Mulaney')
        self.Jess_Abernathy = character('Jess Abernathy')
        self.Olivia_Kendall = character('Olivia Kendall')

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
        ## Shannon Mulaney walked into her dorm room and flopped down on her bed.
        ## She had just gotten off the phone with her mom and they'd argued again.
        self.set_relation(self.Shannon_Mulaney, 'mother', self.Olivia_Kendall)
        self.set_relation(self.Olivia_Kendall, 'daughter', self.Shannon_Mulaney)
        ## The bad grades she'd been getting all semester were affecting her softball scholarship, so Shannon knew that her mom was upset.
        self.set_occupation(self.Shannon_Mulaney, "softball scholarship")
        ## They hadn't spoken in two weeks, though, and Shannon still felt hurt by the fight they'd had before she left Michigan.
        self.set_relation(self.Shannon_Mulaney, 'Michigan', self.Olivia_Kendall)
        self.set_relation(self.Olivia_Kendall, 'Michigan', self.Shannon_Mulaney)
        ## Her whole life she had felt like the odd one out in the family, with both of her sisters being more popular than she was, and now it seemed that her mom was starting to see it too.
        self.set_relation(self.Shannon_Mulaney, 'sisters', self.Olivia_Kendall)
        self.set_relation(self.Olivia_Kendall, 'daughters', self.Shannon_Mulaney)
        ## As she lay there waiting for Olivia to come back from class, Shannon closed her eyes and fell asleep.
        ## "So when did your mom get cancer?"
        ## Jess asked as she set down a few books on top of some envelopes that were stacked on the small desk across from Shannon's bed.
        ## "She didn't," Shannon answered without looking up from the book open in front of her.
        ## "What do you mean?
        ## She's been sick for a year."
        ## Jess sounded confused.
