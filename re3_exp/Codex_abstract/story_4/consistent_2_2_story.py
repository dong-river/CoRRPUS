## Mark Woodbury hurried down the sidewalk and crossed the street.
## He didn’t have time to be late for his date with Shannon Kincaid, and he wanted to arrive at the restaurant early so he could beat the rush.
## As he neared the entrance, he saw her waving at him from a table inside.
## “I’m sorry I’m late, Mark,” she said when he sat down.
## “I was held up in traffic on the way here.
## How are you?”  Mark leaned over and kissed her cheek.
## “That was quite a jolt you gave me when you called a few minutes ago and said you were running late.
## But I guess it’s good that I got here when I did.
## If we had set this thing for any later, we would have missed our reservation for sure.
## They were about to turn people away as I walked up here.”  Shannon laughed lightly.

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
        self.Shannon_Kincaid = character('Shannon Kincaid')
        self.Jack_Kincaid = character('Jack Kincaid')
        self.Mark_Woodbury = character('Mark Woodbury')

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
        ## Mark Woodbury hurried down the sidewalk and crossed the street.
        ## He didn’t have time to be late for his date with Shannon Kincaid, and he wanted to arrive at the restaurant early so he could beat the rush.
        self.set_gender(self.Mark_Woodbury, "male")
        self.set_relation(self.Mark_Woodbury, "date", self.Shannon_Kincaid)
        ## As he neared the entrance, he saw her waving at him from a table inside.
        ## “I’m sorry I’m late, Mark,” she said when he sat down.
        ## “I was held up in traffic on the way here.
        ## How are you?”  Mark leaned over and kissed her cheek.
        self.set_relation(self.Shannon_Kincaid, "date", self.Mark_Woodbury)
        self.set_gender(self.Shannon_Kincaid, "female")
        ## “That was quite a jolt you gave me when you called a few minutes ago and said you were running late.
        ## But I guess it’s good that I got here when I did.
        ## If we had set this thing for any later, we would have missed our reservation for sure.
        ## They were about to turn people away as I walked up here.”  Shannon laughed lightly.
