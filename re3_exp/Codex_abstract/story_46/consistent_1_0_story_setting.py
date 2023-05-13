## A young woman fresh out of college moves to New York City to start her dream job, but discovers that the reality of working in the fashion industry is far different from what she expected.
## The story is set in New York City.
## Jessica Campbell is a 22-year-old woman who has just graduated from college.
## She is tall and thin, with long blond hair and blue eyes.
## John Smith is a 26-year-old man who works as a model.
## He is tall and handsome, with short brown hair and blue eyes.
## Tina Sanchez is a 28-year-old Latina who works as a stylist.
## She is short and curvaceous, with long dark hair and brown eyes.

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
        ## The story is set in New York City.
        ## Jessica Campbell is a 22-year-old woman who has just graduated from college.
        self.set_gender(self.Jessica_Campbell, "female")
        self.set_age(self.Jessica_Campbell, "22")
        self.set_occupation(self.Jessica_Campbell, "college graduate")
        ## She is tall and thin, with long blond hair and blue eyes.
        self.set_appearance(self.Jessica_Campbell, "tall")
        self.set_appearance(self.Jessica_Campbell, "thin")
        self.set_appearance(self.Jessica_Campbell, "long blond hair")
        self.set_appearance(self.Jessica_Campbell, "blue eyes")
        ## John Smith is a 26-year-old man who works as a model.
        self.set_gender(self.John_Smith, "male")
        self.set_age(self.John_Smith, "26")
        self.set_occupation(self.John_Smith, "model")
        ## He is tall and handsome, with short brown hair and blue eyes.
        self.set_appearance(self.John_Smith, "tall")
        self.set_appearance(self.John_Smith, "handsome")
        self.set_appearance(self.John_Smith, "short brown hair")
        self.set_appearance(self.John_Smith, "blue eyes")
        ## Tina Sanchez is a 28-year-old Latina who works as a stylist.
        self.set_gender(self.Tina_Sanchez, "female")
        self.set_age(self.Tina_Sanchez, "28")
        self.set_occupation(self.Tina_Sanchez, "stylist")
        ## She is short and curvaceous, with long dark hair and brown eyes.
        self.set_appearance(self.Tina_Sanchez, "short")
        self.set_appearance(self.Tina_Sanchez, "curvaceous")
        self.set_appearance(self.Tina_Sanchez, "long dark hair")
        self.set_appearance(self.Tina_Sanchez, "brown eyes")
