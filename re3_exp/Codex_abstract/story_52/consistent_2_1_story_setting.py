## The grass is always greener on the other side.
## This is a lesson that John learns the hard way when he cheated on his wife with her best friend.
## When he tries to reconcile with his wife, he realizes that she has been cheating on him with her best friend's husband.
## The story is set in a small town in the midwest.
## Sarah Mason is a beautiful woman with long blond hair and blue eyes.
## She is the wife of John Mason and the mother of two children.
## Rachel Stephenson is Sarah's best friend and the wife of Richard Stevenson.
## John Mason is Sarah's husband and the father of two children.
## He is a successful businessman who has a wandering eye.

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
        self.Sarah_Mason = character('Sarah Mason')
        self.Rachel_Stephenson = character('Rachel Stephenson')
        self.John_Mason = character('John Mason')

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
        ## The story is set in a small town in the midwest.
        ## Sarah Mason is a beautiful woman with long blond hair and blue eyes.
        self.set_appearance(self.Sarah_Mason, "beautiful")
        self.set_appearance(self.Sarah_Mason, "long blond hair")
        self.set_appearance(self.Sarah_Mason, "blue eyes")
        ## She is the wife of John Mason and the mother of two children.
        self.set_relation(self.Sarah_Mason, 'wife', self.John_Mason)
        self.set_relation(self.John_Mason, 'husband', self.Sarah_Mason)
        ## Rachel Stephenson is Sarah's best friend and the wife of Richard Stevenson.
        self.set_relation(self.Rachel_Stephenson, 'best_friend', self.Sarah_Mason)
        self.set_relation(self.Sarah_Mason, 'best_friend', self.Rachel_Stephenson)
        self.set_relation(self.Rachel_Stephenson, 'wife', self.John_Mason)
        self.set_relation(self.John_Mason, 'husband', self.Rachel_Stephenson)
        ## John Mason is Sarah's husband and the father of two children.
        self.set_relation(self.John_Mason, 'wife', self.Sarah_Mason)
        self.set_relation(self.Sarah_Mason, 'husband', self.John_Mason)
        ## He is a successful businessman who has a wandering eye.
        self.set_occupation(self.John_Mason, "successful businessman")
        self.set_appearance(self.John_Mason, "wandering eye")
