## After a year of being together, John andabegan to notice the cracks in their relationship.
## With jobs and school pulling them in different directions, they began to grow apart.
## However, when John loses his job and Abby is diagnosed with cancer, they are forced to lean on each other for support.
## Through their difficult journey, they realize that they still have feelings for each other and their relationship is stronger than ever.
## The story is set in a small town in the US.
## John Doe is a man in his early 30s with brown hair and brown eyes.
## He is a construction worker who has recently lost his job completion of a construction project he was working on in the town he lives in .
## Abby Mills is a beautiful woman in her early 30s.
## She has blonde hair and blue eyes.
## She is a teacher at a local elementary school.
## Mike Benson is Abby's ex-boyfriend.
## He is in his early 30s and is also a teacher at the same elementary school as Abby.

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
        self.John_Doe = character('John Doe')
        self.Abby_Mills = character('Abby Mills')
        self.Mike_Benson = character('Mike Benson')

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
        ## The story is set in a small town in the US.
        ## John Doe is a man in his early 30s with brown hair and brown eyes.
        self.set_appearance(self.John_Doe, "brown hair")
        self.set_appearance(self.John_Doe, "brown eyes")
        self.set_age(self.John_Doe, "early 30s")
        self.set_gender(self.John_Doe, "male")
        ## He is a construction worker who has recently lost his job completion of a construction project he was working on in the town he lives in .
        self.set_occupation(self.John_Doe, "construction worker")
        ## Abby Mills is a beautiful woman in her early 30s.
        self.set_appearance(self.Abby_Mills, "beautiful")
        self.set_age(self.Abby_Mills, "early 30s")
        self.set_gender(self.Abby_Mills, "female")
        ## She has blonde hair and blue eyes.
        self.set_appearance(self.Abby_Mills, "blonde hair")
        self.set_appearance(self.Abby_Mills, "blue eyes")
        ## She is a teacher at a local elementary school.
        self.set_occupation(self.Abby_Mills, "teacher")
        ## Mike Benson is Abby's ex-boyfriend.
        self.set_relation(self.Abby_Mills, 'ex-boyfriend', self.Mike_Benson)
        self.set_relation(self.Mike_Benson, 'ex-girlfriend', self.Abby_Mills)
        ## He is in his early 30s and is also a teacher at the same elementary school as Abby.
        self.set_age(self.Mike_Benson, "early 30s")
        self.set_gender(self.Mike_Benson, "male")
        self.set_occupation(self.Mike_Benson, "teacher")
