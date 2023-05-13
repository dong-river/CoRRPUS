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

    def story(self):
        ## Karen Hanson sat in the kitchen of her home and wondered if there was anything that could snap her out of her depression.
        ## She had just lost her husband, and it seemed as if everything she had ever known was gone.
        self.Karen_Hanson.relations['husband'] = 'Bob_Hanson'
        self.Bob_Hanson.relations['wife'] = 'Karen_Hanson'
        self.Karen_Hanson.gender.append('female')
        ## Lettie, her mother, was also suffering from grief because she had lost the one person she loved more than anything else in the world.
        self.Karen_Hanson.relations['mother'] = 'Lettie_Hanson'
        self.Lettie_Hanson.relations['daughter'] = 'Karen_Hanson'
        self.Lettie_Hanson.gender.append('female')
        ## Lettie would have been one hundred years old next week.
        self.Lettie_Hanson.age.append('one hundred years old')
        ## She had lived a long life, but Bob's death felt like the last thing left to live for.
        self.Lettie_Hanson.relations['husband'] = 'Bob_Hanson'
        self.Bob_Hanson.relations['wife'] = 'Lettie_Hanson'
        self.Bob_Hanson.gender.append('male')
        ## Lettie cried often, especially when Karen took Andrew and Robbie to visit their graves every Sunday.
        self.Lettie_Hanson.relations['grandson'] = 'Andrew_Hanson'
        self.Andrew_Hanson.relations['grandmother'] = 'Lettie_Hanson'
        self.Andrew_Hanson.gender.append('male')
        self.Lettie_Hanson.relations['grandson'] = 'Robbie_Hanson'
        self.Robbie_Hanson.relations['grandmother'] = 'Lettie_Hanson'
        self.Robbie_Hanson.gender.append('male')
        ## That morning Karen woke up to see that it was a beautiful day outside, as usual.
        ## It always seemed as if the sky above their town was unendingly blue with white puffy clouds floating around in it.
        ## They rarely got rainy days or snowy days; there never seemed to be any threat of harsh weather at all.
        ## This perfect weather only served to make Lettie feel even worse about how everything worked out for them both being alive without Bob.
        ## Karen felt herself sink into despair every time she looked out of her window and realized how awful life was without Bob there to share it with them all.

