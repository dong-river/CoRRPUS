## After a woman's husband dies, she realizes that she is now invisible to the world.
## She tries to go on with her life, but finds that without anyone acknowledging her existence, she might as well not exist at all.
## The story is set in a small town in the United States.
## Lettie Hanson is a middle-aged woman who is struggling to cope with the death of her husband.
## She is kind-hearted and gentle, but feels lost and alone in the world without him.
## Bob Hanson is Lettie's late husband.
## He was a kind and loving man who was always there for her.
## Karen Hanson is Lettie's niece who comes to visit her after Bob's death.

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
        self.Lettie_Hanson = character('Lettie Hanson')
        self.Bob_Hanson = character('Bob Hanson')
        self.Karen_Hanson = character('Karen Hanson')

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
        ## The story is set in a small town in the United States.
        ## Lettie Hanson is a middle-aged woman who is struggling to cope with the death of her husband.
        self.set_gender(self.Lettie_Hanson, "female")
        self.set_age(self.Lettie_Hanson, "middle-aged")
        self.set_relation(self.Lettie_Hanson, 'husband', self.Bob_Hanson)
        self.set_relation(self.Bob_Hanson, 'wife', self.Lettie_Hanson)
        ## She is kind-hearted and gentle, but feels lost and alone in the world without him.
        self.set_appearance(self.Lettie_Hanson, "kind-hearted")
        self.set_appearance(self.Lettie_Hanson, "gentle")
        ## Bob Hanson is Lettie's late husband.
        self.set_gender(self.Bob_Hanson, "male")
        self.set_age(self.Bob_Hanson, "middle-aged")
        ## He was a kind and loving man who was always there for her.
        self.set_appearance(self.Bob_Hanson, "kind")
        self.set_appearance(self.Bob_Hanson, "loving")
        ## Karen Hanson is Lettie's niece who comes to visit her after Bob's death.
        self.set_relation(self.Lettie_Hanson, 'niece', self.Karen_Hanson)
        self.set_relation(self.Karen_Hanson, 'aunt', self.Lettie_Hanson)
        self.set_gender(self.Karen_Hanson, "female")
        self.set_age(self.Karen_Hanson, "young")
