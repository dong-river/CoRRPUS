## Thomas Watkins squinted as he surveyed the darkness surrounding the small town.
## He and his team had been in place for almost twenty-four hours, so they were all getting tired.
## They'd searched the town thoroughly, but they hadn't been able to find any sign of the killer.
## It was driving them crazy, but there wasn't much they could do except watch and wait.
## Thomas was a big man with brown hair and brown eyes.
## He stood at 6'2" and had a muscular build.
## He normally worked as a construction worker, but he also moonlighted as a mercenary on nights like this one.
## His skills were in high demand among local towns that needed help protecting themselves from violent criminals or people that wanted to invade their territory or business interests.
## Thomas was armed with a .357 Magnum revolver, an M-16 machine gun, grenades, and an Uzi machine pistol.
## He looked over at his young partner Will Trenton and nodded toward the main street of town in front of them.
## "We should probably start taking shifts."
## He let out a frustrated sigh.
## "There's no way we're going to get any sleep tonight."
## Will nodded his agreement.
## "Okay."

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
        ## Thomas Watkins squinted as he surveyed the darkness surrounding the small town.
        ## He and his team had been in place for almost twenty-four hours, so they were all getting tired.
        ## They'd searched the town thoroughly, but they hadn't been able to find any sign of the killer.
        ## It was driving them crazy, but there wasn't much they could do except watch and wait.
        ## Thomas was a big man with brown hair and brown eyes.
        ## He stood at 6'2" and had a muscular build.
        ## He normally worked as a construction worker, but he also moonlighted as a mercenary on nights like this one.
        ## His skills were in high demand among local towns that needed help protecting themselves from violent criminals or people that wanted to invade their territory or business interests.
        self.set_occupation(self.Thomas_Watkins, "construction worker")
        self.set_occupation(self.Thomas_Watkins, "mercenary")
        ## Thomas was armed with a .357 Magnum revolver, an M-16 machine gun, grenades, and an Uzi machine pistol.
        ## He looked over at his young partner Will Trenton and nodded toward the main street of town in front of them.
        self.set_relation(self.Thomas_Watkins, 'partner', self.Will_Trenton)
        self.set_relation(self.Will_Trenton, 'partner', self.Thomas_Watkins)
        ## "We should probably start taking shifts."
        ## He let out a frustrated sigh.
        ## "There's no way we're going to get any sleep tonight."
        ## Will nodded his agreement.
        ## "Okay."
