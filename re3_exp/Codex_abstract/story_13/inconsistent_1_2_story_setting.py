## Sherry had the perfect life--three healthy children, a loving wife, and a job to support them; until she discovers what was happening right in front of her.
## Sherry's wife has been cheating on her with her brother ever since they've been married.
## A panic attack at work forces Sherry to deal with her personal life head on.
## After gaining some closure, she moves out of state with her children to start afresh.
## The story is set in the present day in a small town in the midwest.
## Sherry Hellinger is a middle-aged woman with short brown hair and green eyes.
## She is of average height and build.
## Emily Hellinger is Sherry's wife of ten years.
## She is a tall woman with long blond hair and blue eyes.
## She is in her early 40s.
## John Hellinger is Sherry's older brother.
## He is a tall man with short brown hair and blue eyes.
## He is in his early 40s.

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
        self.Sherry_Hellinger = character('Sherry Hellinger')
        self.Emily_Hellinger = character('Emily Hellinger')
        self.John_Hellinger = character('John Hellinger')

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
        ## Sherry had the perfect life--three healthy children, a loving wife, and a job to support them; until she discovers what was happening right in front of her.
        ## Sherry's wife has been cheating on her with her brother ever since they've been married.
        self.set_relation(self.Sherry_Hellinger, 'wife', self.Emily_Hellinger)
        self.set_relation(self.Sherry_Hellinger, 'brother', self.John_Hellinger)
        self.set_relation(self.Emily_Hellinger, 'husband', self.Sherry_Hellinger)
        self.set_relation(self.John_Hellinger, 'sister', self.Sherry_Hellinger)
        ## A panic attack at work forces Sherry to deal with her personal life head on.
        ## After gaining some closure, she moves out of state with her children to start afresh.
        ## The story is set in the present day in a small town in the midwest.
        ## Sherry Hellinger is a middle-aged woman with short brown hair and green eyes.
        self.set_appearance(self.Sherry_Hellinger, "middle-aged")
        self.set_appearance(self.Sherry_Hellinger, "short brown hair")
        self.set_appearance(self.Sherry_Hellinger, "green eyes")
        ## She is of average height and build.
        ## Emily Hellinger is Sherry's wife of ten years.
        self.set_relation(self.Sherry_Hellinger, 'wife', self.Emily_Hellinger)
        self.set_relation(self.Emily_Hellinger, 'husband', self.Sherry_Hellinger)
        ## She is a tall woman with long blond hair and blue eyes.
        self.set_appearance(self.Emily_Hellinger, "tall")
        self.set_appearance(self.Emily_Hellinger, "long blond hair")
        self.set_appearance(self.Emily_Hellinger, "blue eyes")
        ## She is in her early 40s.
        self.set_age(self.Emily_Hellinger, "early 40s")
        self.set_gender(self.Emily_Hellinger, "female")
        ## John Hellinger is Sherry's older brother.
        self.set_relation(self.Sherry_Hellinger, 'brother', self.John_Hellinger)
        self.set_relation(self.John_Hellinger, 'sister', self.Sherry_Hellinger)
        ## He is a tall man with short brown hair and blue eyes.
        self.set_appearance(self.John_Hellinger, "tall")
        self.set_appearance(self.John_Hellinger, "short brown hair")
        self.set_appearance(self.John_Hellinger, "blue eyes")
        ## He is in his early 40s.
        self.set_age(self.John_Hellinger, "early 40s")
        self.set_gender(self.John_Hellinger, "male")
