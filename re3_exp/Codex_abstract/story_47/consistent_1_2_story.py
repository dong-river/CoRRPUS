## Maxine Carter looked over at her latest hire, Shannon Burke, with a puzzled expression.
## Shannon had a wild look in her eyes as she paced back and forth across the floor of Maxine's office.
## She kept checking her watch while jumping up every so often to peek through the blinds at the news station beyond.
## Maxine found it difficult to understand why this woman was so edgy when they were due to start filming in a few minutes.
## It wasn't like she was an inexperienced intern.
## For that matter, it wasn't like she hadn't been out on assignments before.
## "Okay, Shan," said Maxine breaking into the young woman's monologue of nervous babble.
## "What's the big deal?
## The camera is in position and everything is ready to go."
## Shannon whipped around with a surprised look on her face and smiled broadly at Maxine as if suddenly realizing where she was.
## "Oh!
## Right!"
## She laughed nervously.
## "Sorry, Max."
## Maxine smiled but did not respond to Shannon's apology or explanation for her strange behavior.
## The woman needed no prompting to continue where she had left off moments before.
## "I have been thinking about what you said about your reporting strategy for this case."

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
        self.Shannon_Burke = character('Shannon Burke')
        self.Charles_Burke = character('Charles Burke')
        self.Maxine_Carter = character('Maxine Carter')

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
        ## Maxine Carter looked over at her latest hire, Shannon Burke, with a puzzled expression.
        self.set_relation(self.Shannon_Burke, 'employer', self.Maxine_Carter)
        self.set_relation(self.Maxine_Carter, 'employee', self.Shannon_Burke)
        self.set_gender(self.Maxine_Carter, "female")
        self.set_gender(self.Shannon_Burke, "female")
        ## Shannon had a wild look in her eyes as she paced back and forth across the floor of Maxine's office.
        ## She kept checking her watch while jumping up every so often to peek through the blinds at the news station beyond.
        ## Maxine found it difficult to understand why this woman was so edgy when they were due to start filming in a few minutes.
        ## It wasn't like she was an inexperienced intern.
        ## For that matter, it wasn't like she hadn't been out on assignments before.
        ## "Okay, Shan," said Maxine breaking into the young woman's monologue of nervous babble.
        ## "What's the big deal?
        ## The camera is in position and everything is ready to go."
        ## Shannon whipped around with a surprised look on her face and smiled broadly at Maxine as if suddenly realizing where she was.
        ## "Oh!
        ## Right!"
        ## She laughed nervously.
        ## "Sorry, Max."
        ## Maxine smiled but did not respond to Shannon's apology or explanation for her strange behavior.
        ## The woman needed no prompting to continue where she had left off moments before.
        ## "I have been thinking about what you said about your reporting strategy for this case."
