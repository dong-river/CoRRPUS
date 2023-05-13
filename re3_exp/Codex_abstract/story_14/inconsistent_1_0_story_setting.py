## Jenny's life changed forever the day she discovered her ability to turn invisible.
## At first, it was a fun game to play with her friends, but soon Jenny realized that she could use her power for more than just pranks.
## When she starts using it to take the town's corrupt mayor down, she realizes that being invisible is more than just a gift--it's a way of life.
## The story is set in the small town of Shepherdstown.
## Jenny Anderson is a young girl with blonde hair and blue eyes.
## She is small for her age, and is often rebel without a cause.
## Jimmy Jackson is Jenny's best friend.
## He is a lanky boy with dark hair and brown eyes.
## He is always up for a good time, and is always trying to get Jenny into trouble.
## Principal Stevens is the principal of Jenny's school.
## He is a middle-aged man with graying hair and glasses.
## He is a fair and just man, but is also very strict.

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
        self.Jenny_Anderson = character('Jenny Anderson')
        self.Jimmy_Jackson = character('Jimmy Jackson')
        self.Principal_Stevens = character('Principal Stevens')

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
        ## The story is set in the small town of Shepherdstown.
        ## Jenny Anderson is a young girl with blonde hair and blue eyes.
        self.set_age(self.Jenny_Anderson, "young")
        self.set_gender(self.Jenny_Anderson, "female")
        self.set_appearance(self.Jenny_Anderson, "blonde hair and blue eyes")
        ## She is small for her age, and is often rebel without a cause.
        ## Jimmy Jackson is Jenny's best friend.
        self.set_relation(self.Jenny_Anderson, 'best friend', self.Jimmy_Jackson)
        self.set_relation(self.Jimmy_Jackson, 'best friend', self.Jenny_Anderson)
        ## He is a lanky boy with dark hair and brown eyes.
        self.set_gender(self.Jimmy_Jackson, "male")
        self.set_appearance(self.Jimmy_Jackson, "dark hair and brown eyes")
        ## He is always up for a good time, and is always trying to get Jenny into trouble.
        ## Principal Stevens is the principal of Jenny's school.
        self.set_relation(self.Jimmy_Jackson, 'principal', self.Principal_Stevens)
        self.set_relation(self.Jenny_Anderson, 'principal', self.Principal_Stevens)
        self.set_occupation(self.Principal_Stevens, "principal")
        ## He is a middle-aged man with graying hair and glasses.
        self.set_age(self.Principal_Stevens, "middle-aged")
        self.set_gender(self.Principal_Stevens, "male")
        self.set_appearance(self.Principal_Stevens, "graying hair and glasses")
        ## He is a fair and just man, but is also very strict.
