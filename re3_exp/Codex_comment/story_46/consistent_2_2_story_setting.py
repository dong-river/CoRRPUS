## A young woman fresh out of college moves to New York City to start her dream job, but discovers that the reality of working in the fashion industry is far different from what she expected.
## The story is set in New York City.
## Jessica Campbell is a 22-year-old woman who has just graduated from college.
## She is tall and thin, with long blond hair and blue eyes.
## John Smith is a 26-year-old man who works as a model.
## He is tall and handsome, with short brown hair and blue eyes.
## Tina Sanchez is a 22-year- old woman who works as a model.
## She is short and thin, with long black hair and brown eyes.
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
        self.Jessica_Campbell = character('Jessica Campbell')
        self.John_Smith = character('John Smith')
        self.Tina_Sanchez = character('Tina Sanchez')

    def story(self):
        ## The story is set in New York City.
        ## Jessica Campbell is a 22-year-old woman who has just graduated from college.
        self.Jessica_Campbell.age.append('22')
        self.Jessica_Campbell.gender.append('female')
        ## She is tall and thin, with long blond hair and blue eyes.
        self.Jessica_Campbell.appearance.append("tall")
        self.Jessica_Campbell.appearance.append("thin")
        self.Jessica_Campbell.appearance.append("long blond hair")
        self.Jessica_Campbell.appearance.append("blue eyes")
        ## John Smith is a 26-year-old man who works as a model.
        self.John_Smith.age.append('26')
        self.John_Smith.gender.append('male')
        self.John_Smith.occupation.append('model')
        ## He is tall and handsome, with short brown hair and blue eyes.
        self.John_Smith.appearance.append("tall")
        self.John_Smith.appearance.append("handsome")
        self.John_Smith.appearance.append("short brown hair")
        self.John_Smith.appearance.append("blue eyes")
        ## Tina Sanchez is a 22-year- old woman who works as a model.
        self.Tina_Sanchez.age.append('22')
        self.Tina_Sanchez.gender.append('female')
        self.Tina_Sanchez.occupation.append('model')
        ## She is short and thin, with long black hair and brown eyes.
        self.Tina_Sanchez.appearance.append("short")
        self.Tina_Sanchez.appearance.append("thin")
        self.Tina_Sanchez.appearance.append("long black hair")
        self.Tina_Sanchez.appearance.append("brown eyes")

