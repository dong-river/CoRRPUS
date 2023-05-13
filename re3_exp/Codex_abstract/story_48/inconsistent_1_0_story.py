## Richard Kane glanced at his watch, frowning.
## His daughter's bedtime was rapidly approaching, and he had yet to settle the kid down.
## When she wasn't having trouble falling asleep, she was up before dawn and running through the house.
## She and her brother had little interest in television.
## He suspected that their mother was mostly responsible for that.
## Olivia rarely watched any shows with them in front of the screen, and their father didn't bother trying to convince her otherwise.
## He rose from his seat at the table with a sigh and glanced around the room.
## He spotted his wife by one of the large picture windows, staring out at the backyard with a pensive expression on her face.
## She hadn't moved since he had last spoken to her, an hour ago at least.
## He moved towards her and touched her shoulder, then turned towards their youngest child.
## "Bring Jack into your room," he said quietly before returning his attention to Olivia.
## She turned to him slowly, nodding without a word before heading towards their son's bedroom with Jack trotting behind her cheerfully.

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
        self.Shannon_Fitzgerald = character('Shannon Fitzgerald')
        self.Olivia_Kane = character('Olivia Kane')
        self.Richard_Kane = character('Richard Kane')

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
        ## Richard Kane glanced at his watch, frowning.
        ## His daughter's bedtime was rapidly approaching, and he had yet to settle the kid down.
        self.set_relation(self.Richard_Kane, 'daughter', self.Shannon_Fitzgerald)
        self.set_relation(self.Shannon_Fitzgerald, 'father', self.Richard_Kane)
        self.set_age(self.Shannon_Fitzgerald, "child")
        self.set_gender(self.Shannon_Fitzgerald, "female")
        ## When she wasn't having trouble falling asleep, she was up before dawn and running through the house.
        ## She and her brother had little interest in television.
        ## He suspected that their mother was mostly responsible for that.
        self.set_relation(self.Shannon_Fitzgerald, 'brother', self.Olivia_Kane)
        self.set_relation(self.Olivia_Kane, 'sister', self.Shannon_Fitzgerald)
        ## Olivia rarely watched any shows with them in front of the screen, and their father didn't bother trying to convince her otherwise.
        self.set_relation(self.Olivia_Kane, 'father', self.Richard_Kane)
        self.set_relation(self.Richard_Kane, 'daughter', self.Olivia_Kane)
        self.set_age(self.Olivia_Kane, "child")
        self.set_gender(self.Olivia_Kane, "female")
        ## He rose from his seat at the table with a sigh and glanced around the room.
        ## He spotted his wife by one of the large picture windows, staring out at the backyard with a pensive expression on her face.
        ## She hadn't moved since he had last spoken to her, an hour ago at least.
        ## He moved towards her and touched her shoulder, then turned towards their youngest child.
        ## "Bring Jack into your room," he said quietly before returning his attention to Olivia.
        ## She turned to him slowly, nodding without a word before heading towards their son's bedroom with Jack trotting behind her cheerfully.
