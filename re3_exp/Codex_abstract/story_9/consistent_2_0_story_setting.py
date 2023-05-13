## A young woman finds out that she is pregnant and decides to abort the pregnancy even though it goes against her religious beliefs.
## The story is set in a small town in the Midwest.
## Julie Christensen is a young woman in her early twenties.
## She is pretty and blonde, and is the daughter of a prominent family in the town.
## Julie is a student at the local college, and is active in her church.
## Tommy Foster is a young man in his early twenties.
## He is the son of a poor family in the town, and has been involved in a lot of trouble in his life.
## Tommy is Julie's boyfriend, and the father of her unborn child.
## Beth Christensen is Julie's best friend since childhood and her confidante in this matter.

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
        self.Julie_Christensen = character('Julie Christensen')
        self.Tommy_Foster = character('Tommy Foster')
        self.Beth_Christensen = character('Beth Christensen')

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
        ## A young woman finds out that she is pregnant and decides to abort the pregnancy even though it goes against her religious beliefs.
        self.set_gender(self.Julie_Christensen, "female")
        self.set_age(self.Julie_Christensen, "young")
        self.set_gender(self.Tommy_Foster, "male")
        self.set_age(self.Tommy_Foster, "young")
        self.set_relation(self.Julie_Christensen, "boyfriend", self.Tommy_Foster)
        self.set_relation(self.Tommy_Foster, "girlfriend", self.Julie_Christensen)
        ## The story is set in a small town in the Midwest.
        ## Julie Christensen is a young woman in her early twenties.
        ## She is pretty and blonde, and is the daughter of a prominent family in the town.
        self.set_appearance(self.Julie_Christensen, "pretty")
        self.set_appearance(self.Julie_Christensen, "blonde")
        self.set_relation(self.Julie_Christensen, "daughter", self.Beth_Christensen)
        self.set_relation(self.Beth_Christensen, "father", self.Julie_Christensen)
        ## Julie is a student at the local college, and is active in her church.
        self.set_occupation(self.Julie_Christensen, "student")
        ## Tommy Foster is a young man in his early twenties.
        ## He is the son of a poor family in the town, and has been involved in a lot of trouble in his life.
        self.set_relation(self.Tommy_Foster, "son", self.Beth_Christensen)
        self.set_relation(self.Beth_Christensen, "father", self.Tommy_Foster)
        ## Tommy is Julie's boyfriend, and the father of her unborn child.
        ## Beth Christensen is Julie's best friend since childhood and her confidante in this matter.
        self.set_relation(self.Julie_Christensen, "best friend", self.Beth_Christensen)
        self.set_relation(self.Beth_Christensen, "best friend", self.Julie_Christensen)

