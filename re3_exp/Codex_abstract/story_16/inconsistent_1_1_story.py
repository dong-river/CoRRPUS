## Jennifer Ann Smith is a 27 year old woman who has just moved into a new apartment and started a new job as a receptionist at an office building downtown Chicago, Illinois, United States of America.
## Jennifer was excited about her new apartment.
## She didn't know anybody there and had no friends in the city, but she decided it was time to leave her family behind and become independent.
## She spent her days calling friends from college and sending emails to her family in other states.
## She found herself to be very busy with work and keeping in touch with people so she never even had time to meet anybody outside of work.
## It seemed as if everybody else were settling down while she was working herself to death in the big city.
## It had been almost two months since Jennifer moved into her new apartment when one day she found that she wasn't really satisfied with it anymore, which caught her by surprise as she had never even thought of moving out yet.

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
        self.Jennifer_Ann_Smith = character('Jennifer Ann Smith')
        self.Clara_Smith = character('Clara Smith')
        self.Robert_Smith = character('Robert Smith')

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
        ## Jennifer Ann Smith is a 27 year old woman who has just moved into a new apartment and started a new job as a receptionist at an office building downtown Chicago, Illinois, United States of America.
        self.set_gender(self.Jennifer_Ann_Smith, "female")
        self.set_age(self.Jennifer_Ann_Smith, "27 years old")
        self.set_occupation(self.Jennifer_Ann_Smith, "receptionist")
        ## Jennifer was excited about her new apartment.
        ## She didn't know anybody there and had no friends in the city, but she decided it was time to leave her family behind and become independent.
        self.set_relation(self.Jennifer_Ann_Smith, 'family', self.Clara_Smith)
        self.set_relation(self.Jennifer_Ann_Smith, 'family', self.Robert_Smith)
        self.set_relation(self.Clara_Smith, 'daughter', self.Jennifer_Ann_Smith)
        self.set_relation(self.Robert_Smith, 'daughter', self.Jennifer_Ann_Smith)
        ## She spent her days calling friends from college and sending emails to her family in other states.
        ## She found herself to be very busy with work and keeping in touch with people so she never even had time to meet anybody outside of work.
        ## It seemed as if everybody else were settling down while she was working herself to death in the big city.
        ## It had been almost two months since Jennifer moved into her new apartment when one day she found that she wasn't really satisfied with it anymore, which caught her by surprise as she had never even thought of moving out yet.
        ## Jennifer had been living in her new apartment for almost two months when she realized that she was not satisfied with it anymore.
        ## She had never even thought of moving out yet.
        ## She was surprised by this realization.
