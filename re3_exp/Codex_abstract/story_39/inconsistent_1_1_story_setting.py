## When the last of the world's trees are gone, the humans are forced to find alternative sources of oxygen.
## They build giant machines to simulate the trees, but the air is still not clean enough.
## The government decides to send a team of scientists to Mars to see if there is any possibility of life there.
## If they can find a way to terraform Mars, maybe the humans can have a chance at survival.
## The story is set in a future world where the last of the trees have been wiped out and the humans are struggling to find a way to survive.
## Nadia Kaminski is a scientist who specializes in astrobiology.
## She is chosen to be part of the team that is sent to Mars to investigate the possibility of life there.
## Connor Riley is an engineer who is responsible for the design and construction of the machines that will be used to simulate the trees on Mars.
## Abigail Harper is a doctor who is chosen to be part of the medical team that will be responsible for the health of the astronauts during their stay on Mars.

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
        self.Nadia_Kaminski = character('Nadia Kaminski')
        self.Connor_Riley = character('Connor Riley')
        self.Abigail_Harper = character('Abigail Harper')

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
        ## The story is set in a future world where the last of the trees have been wiped out and the humans are struggling to find a way to survive.
        ## Nadia Kaminski is a scientist who specializes in astrobiology.
        self.set_occupation(self.Nadia_Kaminski, "scientist")
        ## She is chosen to be part of the team that is sent to Mars to investigate the possibility of life there.
        self.set_occupation(self.Nadia_Kaminski, "astrobiology")
        ## Connor Riley is an engineer who is responsible for the design and construction of the machines that will be used to simulate the trees on Mars.
        self.set_occupation(self.Connor_Riley, "engineer")
        ## Abigail Harper is a doctor who is chosen to be part of the medical team that will be responsible for the health of the astronauts during their stay on Mars.
        self.set_occupation(self.Abigail_Harper, "doctor")
