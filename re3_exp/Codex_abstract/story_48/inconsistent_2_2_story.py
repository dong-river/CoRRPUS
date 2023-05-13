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
        self.set_occupation(self.Richard_Kane, "businessman")
        ## He owns many restaurants and businesses all over the city, bringing in millions of dollars in revenue every year.
        ## But business alone cannot satisfy Richard.
        ## He has a strong thirst for the thrill of the game and enjoys gambling, always striving to push his luck with each new venture.
        self.set_appearance(self.Richard_Kane, "gambling")
        ## Richard is married to Olivia Kane, a beautiful woman who never failed to meet his high expectations.
        self.set_relation(self.Richard_Kane, 'wife', self.Olivia_Kane)
        self.set_relation(self.Olivia_Kane, 'husband', self.Richard_Kane)
        self.set_gender(self.Olivia_Kane, "female")
        self.set_appearance(self.Olivia_Kane, "beautiful")
        ## Olivia was always stylish and popular, but she married into money, which made her even more popular among the upper class of society.
        self.set_appearance(self.Olivia_Kane, "stylish")
        ## Despite their wealth and popularity, Richard and Olivia wanted children, which would ensure that they passed on their status into the next generation.
        ## They spent several years trying to conceive but were unable to do so until one day, Olivia became pregnant.
        ## A son was born first but died shortly after birth.
        ## It was only then that a daughter came along two years later; but this child also did not survive past infancy despite their desperate efforts to save her life.
        ## Despite these crushing losses and failing health for both of them, Olivia loved her husband dearly despite his weaknesses for gambling and foolish risks in business dealings.
        ## Shannon Fitzgerald is a young woman who works as a waitress at the restaurant owned by Richard Kane.
        self.set_occupation(self.Shannon_Fitzgerald, "waitress")
        self.set_age(self.Shannon_Fitzgerald, "young")
        self.set_gender(self.Shannon_Fitzgerald, "female")
        ## Shannon lives with her mother, who is a single parent struggling to make ends meet.
        self.set_relation(self.Shannon_Fitzgerald, 'mother', self.Olivia_Kane)
        ## Shannon has been working at the restaurant for a few months now and is hoping to save up enough money to move out on her own.
        ## She gets along well with her coworkers, who are all young women in their twenties like herself.
        ## Shannon is a hard worker who always does her best, even when things get stressful or hectic at times.
        ## Her positive attitude makes her popular among the customers as well, who often leave generous tips for her.
        ## She has been saving up these tips in order to move out soon.
        ## Shannon has been working at the restaurant for a few months now and is hoping to save up enough money to move out on her own.
        ## She gets along well with her coworkers, who are all young women in their twenties like herself.
        ## Shannon is a hard worker who always does her best, even when things get stressful or hectic at times.
        ## Her positive attitude makes her popular among the customers as well, who often leave generous tips for her.
        ## She has been saving up these tips in order to move out soon.
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
        ## Shannon Fitzgerald is a young woman who works as a waitress at the restaurant owned by Richard Kane.
        ## Shannon lives with her mother, who is a single parent struggling to make ends meet.
        ## Shannon has been working at the restaurant for a few months now and is hoping to save up enough money to move out on her own.
        ## She gets along well with her coworkers, who are all young women in their twenties like herself.
        ## Shannon is a hard worker who always does her best, even when things get stressful or hectic at times.
        ## Her positive attitude makes her popular among the customers as well, who often leave generous tips for her.
        ## She has been saving up these tips in order to move out soon.
        ## Shannon has been working at the restaurant for a few months now and is hoping to save up enough money to move out on her own.
        ## She gets along well with her coworkers, who are all young women in their twenties like herself.
        ## Shannon is a hard worker who always does her best, even when things get stressful or hectic at times.
        ## Her positive attitude makes her popular among the customers as well, who often leave generous tips for her.
        ## She has been saving up these tips in order to move out soon.
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
        ## Shannon Fitzgerald is a young woman who works as a waitress at the restaurant owned by Richard Kane.
        ## Shannon lives with her mother, who is a single parent struggling to make ends meet.
        ## Shannon has been working at the restaurant for a few months now and is hoping to save up enough money to move out on her own.
        ## She gets along well with her coworkers, who are all young women in their twenties like herself.
        ## Shannon is a hard worker who always does her best, even when things get stressful or hectic at times.
        ## Her positive attitude makes her popular among the customers as well, who often leave generous tips for her.
        ## She has been saving up these tips in order to move out soon.
        ## Shannon has been working at the restaurant for a few months now and is hoping to save up enough money to move out on her own.
        ## She gets along well with her coworkers, who are all young women in their twenties like herself.
        ## Shannon is a hard worker who always does her best, even when things get stressful or hectic at times.
        ## Her positive attitude makes her popular among the customers as well, who often leave generous tips for her.
        ## She has been saving up these tips in order to move out soon.
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
        ## Shannon Fitzgerald is a young woman who works as a waitress at the restaurant owned by Richard Kane.
        ## Shannon lives with her mother, who is a single parent struggling to make ends meet.
        ## Shannon has been working at the restaurant for a few months now and is hoping to save up enough money to move out on her own.
        ## She gets along well with her coworkers, who are all young women in their twenties like herself.
        ## Shannon is a hard worker who always does her best, even when things get stressful or hectic at times.
        ## Her positive attitude makes her popular among the customers as well, who often leave generous tips for her.
        ## She has been saving up these tips in order to move out soon.
        ## Shannon has been working at the restaurant for a few months now and is hoping to save up enough money to move out on her own.
        ## She gets along well with her coworkers, who are all young women in their twenties like herself.
        ## Shannon is a hard worker who always does her best, even when things get stressful or hectic at times.
        ## Her positive attitude makes her popular among the customers as well, who often leave generous tips for her.
        ## She has been saving up these tips in order to move out soon.
        ## Richard Kane is a very successful businessman.
        ## He owns many restaurants and businesses all over the city, bringing in millions of dollars in revenue every year.
        ## But business alone cannot satisfy Richard.
        ## He has a strong thirst for the thrill of the game and enjoys gambling, always striving to push his luck with each new venture.
        ## Richard is married to Olivia Kane, a beautiful woman who never failed to meet his high expectations.
        ## Olivia was always stylish and popular, but she married into money, which made her