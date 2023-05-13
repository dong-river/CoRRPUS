## Karen Hanson sat in the kitchen of her home and wondered if there was anything that could snap her out of her depression.
## She had just lost her husband, and it seemed as if everything she had ever known was gone.
## Lettie, her mother, was also suffering from grief because she had lost the one person she loved more than anything else in the world.
## Lettie would have been one hundred years old next week.
## She had lived a long life, but Bob's death felt like the last thing left to live for.
## Lettie cried often, especially when Karen took Andrew and Robbie to visit their graves every Sunday.
## That morning Karen woke up to see that it was a beautiful day outside, as usual.
## It always seemed as if the sky above their town was unendingly blue with white puffy clouds floating around in it.
## They rarely got rainy days or snowy days; there never seemed to be any threat of harsh weather at all.
## This perfect weather only served to make Lettie feel even worse about how everything worked out for them both being alive without Bob.
## Karen felt herself sink into despair every time she looked out of her window and realized how awful life was without Bob there to share it with them all.

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
        ## Karen Hanson sat in the kitchen of her home and wondered if there was anything that could snap her out of her depression.
        ## She had just lost her husband, and it seemed as if everything she had ever known was gone.
        self.set_gender(self.Karen_Hanson, "female")
        self.set_relation(self.Karen_Hanson, 'husband', self.Bob_Hanson)
        self.set_relation(self.Bob_Hanson, 'wife', self.Karen_Hanson)
        self.set_gender(self.Bob_Hanson, "male")
        ## Lettie, her mother, was also suffering from grief because she had lost the one person she loved more than anything else in the world.
        self.set_relation(self.Lettie_Hanson, 'daughter', self.Karen_Hanson)
        self.set_relation(self.Karen_Hanson, 'mother', self.Lettie_Hanson)
        self.set_relation(self.Lettie_Hanson, 'husband', self.Bob_Hanson)
        self.set_relation(self.Bob_Hanson, 'wife', self.Lettie_Hanson)
        ## Lettie would have been one hundred years old next week.
        self.set_age(self.Lettie_Hanson, "old")
        self.set_gender(self.Lettie_Hanson, "female")
        ## She had lived a long life, but Bob's death felt like the last thing left to live for.
        self.set_relation(self.Lettie_Hanson, 'husband', self.Bob_Hanson)
        self.set_relation(self.Bob_Hanson, 'wife', self.Lettie_Hanson)
        self.set_gender(self.Bob_Hanson, "male")
        ## Lettie cried often, especially when Karen took Andrew and Robbie to visit their graves every Sunday.
        ## That morning Karen woke up to see that it was a beautiful day outside, as usual.
        ## It always seemed as if the sky above their town was unendingly blue with white puffy clouds floating around in it.
        ## They rarely got rainy days or snowy days; there never seemed to be any threat of harsh weather at all.
        ## This perfect weather only served to make Lettie feel even worse about how everything worked out for them both being alive without Bob.
        ## Karen felt herself sink into despair every time she looked out of her window and realized how awful life was without Bob there to share it with them all.


