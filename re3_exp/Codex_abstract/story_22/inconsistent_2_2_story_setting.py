## It was supposed to be a quiet night shift at the gas station, but when a disheveled man walks in and demands all the money in the register, it turns into a nightmare.
## The man is armed and clearly desperate, and the clerk has no choice but to complied.
## But when the police arrive minutes later, the customer is long gone - leaving the clerk as the only suspect.
## The story is set in a gas station at night.
## Harold Martinez is a young Hispanic man who is the gas station attendant who is held up at gunpoint by a customer and is forced to give him all the money in the register  David Garcia is a young Hispanic man who is the customer who robs the gas station.
## He is armed and dangerous, and is clearly desperate.

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
        ## It was supposed to be a quiet night shift at the gas station, but when a disheveled man walks in and demands all the money in the register, it turns into a nightmare.
        ## The man is armed and clearly desperate, and the clerk has no choice but to complied.
        self.set_appearance(self.David_Garcia, "disheveled")
        self.set_occupation(self.David_Garcia, "gas station attendant")
        self.set_gender(self.David_Garcia, "male")
        self.set_age(self.David_Garcia, "young")
        self.set_appearance(self.Harold_Martinez, "disheveled")
        self.set_occupation(self.Harold_Martinez, "customer")
        self.set_gender(self.Harold_Martinez, "male")
        self.set_age(self.Harold_Martinez, "young")
        ## But when the police arrive minutes later, the customer is long gone - leaving the clerk as the only suspect.
        ## The story is set in a gas station at night.
        ## Harold Martinez is a young Hispanic man who is the gas station attendant who is held up at gunpoint by a customer and is forced to give him all the money in the register  David Garcia is a young Hispanic man who is the customer who robs the gas station.
        ## He is armed and dangerous, and is clearly desperate.
