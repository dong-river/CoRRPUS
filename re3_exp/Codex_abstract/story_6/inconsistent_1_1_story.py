## Jillian Riley couldn't believe her sister was actually moving to the city.
## "I've finally found my dream job," said Shannon.
## "I'm going to be a journalist."
## "That's great, sis," said Jillian, smiling.
## "But how are you going to pay the rent?
## I hope you know you don't have a job lined up yet.
## There are no newspapers in town, so it won't be easy finding a job."
## "But I have found a job!"
## exclaimed Shannon.
## "Robert Riley hired me."
## Jillian choked on her soup.
## "What?"
## she asked incredulously when she'd recovered herself.
## "You're not going to work for Robert Riley!"
## Jillian knew her father had moved back to the city about three months ago, but she didn't know he'd gotten back into journalism after retiring many years ago.
## Apparently, Shannon hadn't known either.
## She just assumed that Robert had moved back to the city and was living off his retirement fund while taking care of his two granddaughters full-time.

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
        self.Shannon_Riley = character('Shannon Riley')
        self.Robert_Riley = character('Robert Riley')
        self.Jillian_Riley = character('Jillian Riley')

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
        ## Jillian Riley couldn't believe her sister was actually moving to the city.
        ## "I've finally found my dream job," said Shannon.
        ## "I'm going to be a journalist."
        self.set_relation(self.Shannon_Riley, 'sister', self.Jillian_Riley)
        self.set_relation(self.Jillian_Riley, 'sister', self.Shannon_Riley)
        self.set_occupation(self.Shannon_Riley, 'journalist')
        ## "That's great, sis," said Jillian, smiling.
        ## "But how are you going to pay the rent?
        ## I hope you know you don't have a job lined up yet.
        ## There are no newspapers in town, so it won't be easy finding a job."
        ## "But I have found a job!"
        ## exclaimed Shannon.
        ## "Robert Riley hired me."
        self.set_relation(self.Shannon_Riley, 'father', self.Robert_Riley)
        self.set_relation(self.Robert_Riley, 'daughter', self.Shannon_Riley)
        ## Jillian choked on her soup.
        ## "What?"
        ## she asked incredulously when she'd recovered herself.
        ## "You're not going to work for Robert Riley!"
        ## Jillian knew her father had moved back to the city about three months ago, but she didn't know he'd gotten back into journalism after retiring many years ago.
        ## Apparently, Shannon hadn't known either.
        ## She just assumed that Robert had moved back to the city and was living off his retirement fund while taking care of his two granddaughters full-time.
