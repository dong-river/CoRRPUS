## The townspeople of a small town in the middle of nowhere are constantly being terrorized by a serial killer who only comes out at night.
## They're all too scared to leave their homes after dark, so they've hired a group of mercenaries to help them protect themselves.
## The mercenaries are good at their jobs, but they're not prepared for the sheer brutality of the killer.
## The story is set in a remote, rural town that is plagued by a relentless and brutal serial killer.
## Will Trenton is a former soldier who now works as a mercenary.
## He's a tough and experienced fighter who is not afraid of the killer.
## Amanda Wilkinson is a local woman who is terrified of the serial killer.
## She's been living in fear for months and is ready to do whatever it takes to protect herself.
## Thomas Watkins is the leader of the mercenary team that has been hired to protect the town.
## He's a no-nonsense type of guy who is determined to stop the killer.

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
        self.Will_Trenton = character('Will Trenton')
        self.Amanda_Wilkinson = character('Amanda Wilkinson')
        self.Thomas_Watkins = character('Thomas Watkins')

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
        ## The townspeople of a small town in the middle of nowhere are constantly being terrorized by a serial killer who only comes out at night.
        ## They're all too scared to leave their homes after dark, so they've hired a group of mercenaries to help them protect themselves.
        ## The mercenaries are good at their jobs, but they're not prepared for the sheer brutality of the killer.
        ## The story is set in a remote, rural town that is plagued by a relentless and brutal serial killer.
        ## Will Trenton is a former soldier who now works as a mercenary.
        self.set_occupation(self.Will_Trenton, "mercenary")
        ## He's a tough and experienced fighter who is not afraid of the killer.
        self.set_appearance(self.Will_Trenton, "tough and experienced")
        ## Amanda Wilkinson is a local woman who is terrified of the serial killer.
        self.set_appearance(self.Amanda_Wilkinson, "terrified")
        self.set_relation(self.Amanda_Wilkinson, 'local', self.Will_Trenton)
        self.set_relation(self.Will_Trenton, 'local', self.Amanda_Wilkinson)
        ## She's been living in fear for months and is ready to do whatever it takes to protect herself.
        self.set_appearance(self.Amanda_Wilkinson, "living in fear")
        ## Thomas Watkins is the leader of the mercenary team that has been hired to protect the town.
        self.set_relation(self.Thomas_Watkins, 'leader', self.Will_Trenton)
        self.set_relation(self.Will_Trenton, 'leader', self.Thomas_Watkins)
        ## He's a no-nonsense type of guy who is determined to stop the killer.
        self.set_appearance(self.Thomas_Watkins, "no-nonsense")
        self.set_appearance(self.Thomas_Watkins, "determined")
