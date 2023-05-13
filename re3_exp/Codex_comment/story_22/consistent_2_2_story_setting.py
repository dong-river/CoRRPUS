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

    def story(self):
        ## The story is set in a gas station at night.
        ## Harold Martinez is a young Hispanic man who is the gas station attendant who is held up at gunpoint by a customer and is forced to give him all the money in the register
        self.Harold_Martinez.gender.append('male')
        self.Harold_Martinez.age.append('young')
        self.Harold_Martinez.occupation.append('gas station attendant')
        ## David Garcia is a young Hispanic man who is the customer who robs the gas station.
        self.David_Garcia.gender.append('male')
        self.David_Garcia.age.append('young')
        self.David_Garcia.occupation.append('gas station customer')
        ## He is armed and dangerous, and is clearly desperate.
        self.David_Garcia.appearance.append('armed and dangerous')

