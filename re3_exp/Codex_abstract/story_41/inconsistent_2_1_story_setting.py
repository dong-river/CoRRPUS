## After a car crash, a woman starts seeing ghosts.
## The ghosts tell her she has to right the wrongs they did in life in order to move on.
## She's not sure if she's going crazy or if this is really happening.
## The story is set in a small town in the United States.
## Jennie Mayfield is a young woman in her early twenties.
## She has long dark hair and brown eyes.
## She is of average height and build.
## Aaron Mayfield is Jennie's older brother.
## He is in his late twenties and has short blond hair and blue eyes.
## He is taller than Jennie and has a muscular build.
## Alex Preston is a young man in his early twenties, who is Jennie's boyfriend and Aaron's best friend.
## He has short dark hair and brown eyes, and is of average height and build.

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
        self.Jennie_Mayfield = character('Jennie Mayfield')
        self.Aaron_Mayfield = character('Aaron Mayfield')
        self.Alex_Preston = character('Alex Preston')

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
        ## The story is set in a small town in the United States.
        ## Jennie Mayfield is a young woman in her early twenties.
        self.set_age(self.Jennie_Mayfield, "early twenties")
        self.set_gender(self.Jennie_Mayfield, "female")
        ## She has long dark hair and brown eyes.
        self.set_appearance(self.Jennie_Mayfield, "long dark hair")
        self.set_appearance(self.Jennie_Mayfield, "brown eyes")
        ## She is of average height and build.
        self.set_appearance(self.Jennie_Mayfield, "average height")
        self.set_appearance(self.Jennie_Mayfield, "average build")
        ## Aaron Mayfield is Jennie's older brother.
        self.set_relation(self.Jennie_Mayfield, 'brother', self.Aaron_Mayfield)
        self.set_relation(self.Aaron_Mayfield, 'sister', self.Jennie_Mayfield)
        ## He is in his late twenties and has short blond hair and blue eyes.
        self.set_age(self.Aaron_Mayfield, "late twenties")
        self.set_appearance(self.Aaron_Mayfield, "short blond hair")
        self.set_appearance(self.Aaron_Mayfield, "blue eyes")
        ## He is taller than Jennie and has a muscular build.
        self.set_appearance(self.Aaron_Mayfield, "taller than Jennie")
        self.set_appearance(self.Aaron_Mayfield, "muscular build")
        ## Alex Preston is a young man in his early twenties, who is Jennie's boyfriend and Aaron's best friend.
        self.set_age(self.Alex_Preston, "early twenties")
        self.set_gender(self.Alex_Preston, "male")
        self.set_relation(self.Jennie_Mayfield, 'boyfriend', self.Alex_Preston)
        self.set_relation(self.Alex_Preston, 'girlfriend', self.Jennie_Mayfield)
        self.set_relation(self.Aaron_Mayfield, 'best_friend', self.Alex_Preston)
        self.set_relation(self.Alex_Preston, 'best_friend', self.Aaron_Mayfield)
        ## He has short dark hair and brown eyes, and is of average height and build.
        self.set_appearance(self.Alex_Preston, "short dark hair")
        self.set_appearance(self.Alex_Preston, "brown eyes")
        self.set_appearance(self.Alex_Preston, "average height")
        self.set_appearance(self.Alex_Preston, "average build")
