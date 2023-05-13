## It was supposed to be a quiet night shift at the gas station, but when a disheveled man walks in and demands all the money in the register, it turns into a nightmare.
## The man is armed and clearly desperate, and the clerk has no choice but to complied.
## But when the police arrive minutes later, the customer is long gone - leaving the clerk as the only suspect.
## The story is set in a gas station at night.
## Harold Martinez is a middle-aged Hispanic man who works as a gas station clerk.
## He is a hardworking and honest man who has been working at the gas station for years.
## David Garcia is a young Hispanic man who is the customer who robs the gas station.
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
        self.set_appearance(self.David_Garcia, "disheveled")
        self.set_occupation(self.David_Garcia, "customer")
        ## The man is armed and clearly desperate, and the clerk has no choice but to complied.
        self.set_appearance(self.Harold_Martinez, "clerk")
        ## But when the police arrive minutes later, the customer is long gone - leaving the clerk as the only suspect.
        ## The story is set in a gas station at night.
        ## Harold Martinez is a middle-aged Hispanic man who works as a gas station clerk.
        self.set_age(self.Harold_Martinez, "middle-aged")
        ## He is a hardworking and honest man who has been working at the gas station for years.
        self.set_occupation(self.Harold_Martinez, "clerk")
        ## David Garcia is a young Hispanic man who is the customer who robs the gas station.
        self.set_age(self.David_Garcia, "young")
        ## He is armed and dangerous, and is clearly desperate.
        self.set_appearance(self.David_Garcia, "armed")
