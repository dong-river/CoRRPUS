## Richard Kane is a very successful businessman.
## He owns many restaurants and businesses all over the city, bringing in millions of dollars in revenue every year.
## But business alone cannot satisfy Richard.
## He has a strong thirst for the thrill of the game and enjoys gambling, always striving to push his luck with each new venture.
## Richard is married to Olivia Kane, a beautiful woman who never failed to meet his high expectations.
## Olivia was always stylish and popular, but she married into money, which made her even more popular among the upper class of society.
## Despite their wealth and popularity, Richard and Olivia wanted children, which would ensure that they passed on their status into the next generation.
## They spent several years trying to conceive but were unable to do so until one day, Olivia became pregnant.
## A son was born first but died shortly after birth.
## It was only then that a daughter came along two years later; but this child also did not survive past infancy despite their desperate efforts to save her life.
## Despite these crushing losses and failing health for both of them, Olivia loved her husband dearly despite his weaknesses for gambling and foolish risks in business dealings.

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
        self.Shannon_Fitzgerald = character('Shannon Fitzgerald')
        self.Olivia_Kane = character('Olivia Kane')
        self.Richard_Kane = character('Richard Kane')

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
        ## Richard Kane is a very successful businessman.
        self.set_occupation(self.Richard_Kane, "successful businessman")
        ## He owns many restaurants and businesses all over the city, bringing in millions of dollars in revenue every year.
        ## But business alone cannot satisfy Richard.
        ## He has a strong thirst for the thrill of the game and enjoys gambling, always striving to push his luck with each new venture.
        ## Richard is married to Olivia Kane, a beautiful woman who never failed to meet his high expectations.
        self.set_relation(self.Richard_Kane, 'wife', self.Olivia_Kane)
        self.set_relation(self.Olivia_Kane, 'husband', self.Richard_Kane)
        ## Olivia was always stylish and popular, but she married into money, which made her even more popular among the upper class of society.
        self.set_appearance(self.Olivia_Kane, "stylish")
        ## Despite their wealth and popularity, Richard and Olivia wanted children, which would ensure that they passed on their status into the next generation.
        ## They spent several years trying to conceive but were unable to do so until one day, Olivia became pregnant.
        ## A son was born first but died shortly after birth.
        ## It was only then that a daughter came along two years later; but this child also did not survive past infancy despite their desperate efforts to save her life.
        ## Despite these crushing losses and failing health for both of them, Olivia loved her husband dearly despite his weaknesses for gambling and foolish risks in business dealings.
