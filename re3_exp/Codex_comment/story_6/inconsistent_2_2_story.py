## Jillian Riley always wanted to be a writer.
## Her husband, Robert, had always been an artist at heart.
## When they married and began their life together, they believed they would both achieve their dreams.
## Instead, Robert lived his life vicariously through his wife's stories and articles.
## He died before he had the chance to be published himself.
## Jillian's first story was published in a national newspaper shortly after his death.
## She took on part-time work as a sales assistant at a small bookshop to help support herself and her daughter.
## With money tight, Jillian relied on her writing skills to pay for Shannon's education and living expenses.
## She taught Shannon how to appreciate the printed word and provided a broad range of reading material, from romance novels to classics such as Shakespeare and Dickens.
## As Shannon grew older, she began writing her own stories for her mother to read each night before bedtime.
## The story is set in a small city in New England where an exciting artistic environment exists beside an old mill that was converted into shops selling various art supplies.
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

    def story(self):
        ## Jillian Riley always wanted to be a writer.
        self.Jillian_Riley.occupation.append("writer")
        ## Her husband, Robert, had always been an artist at heart.
        self.Jillian_Riley.relations['husband'] = 'Robert_Riley'
        self.Robert_Riley.relations['wife'] = 'Jillian_Riley'
        self.Robert_Riley.occupation.append("artist")
        ## When they married and began their life together, they believed they would both achieve their dreams.
        ## Instead, Robert lived his life vicariously through his wife's stories and articles.
        ## He died before he had the chance to be published himself.
        ## Jillian's first story was published in a national newspaper shortly after his death.
        ## She took on part-time work as a sales assistant at a small bookshop to help support herself and her daughter.
        ## With money tight, Jillian relied on her writing skills to pay for Shannon's education and living expenses.
        ## She taught Shannon how to appreciate the printed word and provided a broad range of reading material, from romance novels to classics such as Shakespeare and Dickens.
        ## As Shannon grew older, she began writing her own stories for her mother to read each night before bedtime.
        ## The story is set in a small city in New England where an exciting artistic environment exists beside an old mill that was converted into shops selling various art supplies.

