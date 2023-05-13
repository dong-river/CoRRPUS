## Rachel Stephenson was a happy person.
## She had her best friend, Sarah Mason, her perfect husband, Mark Stephenson, and two perfect children.
## She woke up at six every morning.
## As soon as she got out of bed, she did fifteen minutes of yoga to loosen her muscles and help them relax.
## After the yoga routine, she went downstairs to make breakfast for herself and her husband.
## While they ate breakfast in the kitchen, they discussed their plans for the day.
## After breakfast was done, she headed upstairs to give each of their two kids a bath while Mark took out the trash and checked his email on his computer in the den.
## Their kids were like little angels because they never caused any trouble; they were quiet when they were eating; they were always dressed in impeccable outfits when they left the house; and there was no yelling in their household because everyone was kind to one another.
## They would go out for walks after breakfast but by eight thirty am, Rachel already had her work clothes on as well as her makeup done; at nine am, she was usually working on a canvas or painting at one of three coffee shops that all opened at eight am in Lake Bloomfield, Illinois where she lived with her family.

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
        self.Sarah_Mason = character('Sarah Mason')
        self.Rachel_Stephenson = character('Rachel Stephenson')
        self.John_Mason = character('John Mason')

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
        self.set_relation(self.Rachel_Stephenson, 'best friend', self.Sarah_Mason)
        self.set_relation(self.Sarah_Mason, 'best friend', self.Rachel_Stephenson)
        self.set_gender(self.Sarah_Mason, "female")
        self.set_relation(self.Rachel_Stephenson, 'husband', self.John_Mason)
        self.set_relation(self.John_Mason, 'wife', self.Rachel_Stephenson)
        self.set_gender(self.John_Mason, "male")
        ## She woke up at six every morning.
        ## As soon as she got out of bed, she did fifteen minutes of yoga to loosen her muscles and help them relax.
        ## After the yoga routine, she went downstairs to make breakfast for herself and her husband.
        ## While they ate breakfast in the kitchen, they discussed their plans for the day.
        ## After breakfast was done, she headed upstairs to give each of their two kids a bath while Mark took out the trash and checked his email on his computer in the den.
        ## Their kids were like little angels because they never caused any trouble; they were quiet when they were eating; they were always dressed in impeccable outfits when they left the house; and there was no yelling in their household because everyone was kind to one another.
        ## They would go out for walks after breakfast but by eight thirty am, Rachel already had her work clothes on as well as her makeup done; at nine am, she was usually working on a canvas or painting at one of three coffee shops that all opened at eight am in Lake Bloomfield, Illinois where she lived with her family.


 

## Create a world model state to track each character's appearance, personality, and relations with other characters.

