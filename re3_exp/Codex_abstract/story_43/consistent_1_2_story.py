## Shannon Mulaney looked out her bedroom window at the dark sky.
## A storm was coming and Shannon knew that there would be a tornado warning in her town tomorrow.
## She also knew that her mom wasn't going to listen to the warning and stay home.
## Shannon turned away from the window and sighed as she looked around her room.
## She was about to turn 20 years old and here she was still living with her mom in a small town in upstate New York.
## Her mom hadn't let go of life after losing Shannon's dad when Shannon was 9, so she kept busy, going here and there until late at night, rarely taking care of Shannon.
## There were days that Shannon felt like nobody wanted her around except for Jess Abernathy, who had been appointed as an official university staff member at XYZ University to be assigned as an RA (resident assistant) in a dormitory suite named "Sky House".
## While Jess had barely known this girl, she seemed so lonely but just not willing to talk about it or anything else really...  As a friend it was tough to watch your best friend face the loss of their parent over many years go by without doing anything about it or trying to change things...

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
        self.Shannon_Mulaney = character('Shannon Mulaney')
        self.Jess_Abernathy = character('Jess Abernathy')
        self.Olivia_Kendall = character('Olivia Kendall')

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
        ## Shannon Mulaney looked out her bedroom window at the dark sky.
        ## A storm was coming and Shannon knew that there would be a tornado warning in her town tomorrow.
        ## She also knew that her mom wasn't going to listen to the warning and stay home.
        self.set_relation(self.Shannon_Mulaney, 'mother', self.Olivia_Kendall)
        self.set_relation(self.Olivia_Kendall, 'daughter', self.Shannon_Mulaney)
        self.set_gender(self.Olivia_Kendall, "female")
        ## Shannon turned away from the window and sighed as she looked around her room.
        ## She was about to turn 20 years old and here she was still living with her mom in a small town in upstate New York.
        self.set_age(self.Shannon_Mulaney, "20")
        self.set_age(self.Olivia_Kendall, "40")
        ## Her mom hadn't let go of life after losing Shannon's dad when Shannon was 9, so she kept busy, going here and there until late at night, rarely taking care of Shannon.
        self.set_age(self.Shannon_Mulaney, "9")
        ## There were days that Shannon felt like nobody wanted her around except for Jess Abernathy, who had been appointed as an official university staff member at XYZ University to be assigned as an RA (resident assistant) in a dormitory suite named "Sky House".
        self.set_relation(self.Shannon_Mulaney, 'friend', self.Jess_Abernathy)
        self.set_relation(self.Jess_Abernathy, 'friend', self.Shannon_Mulaney)
        self.set_occupation(self.Jess_Abernathy, "RA")
        ## While Jess had barely known this girl, she seemed so lonely but just not willing to talk about it or anything else really...  As a friend it was tough to watch your best friend face the loss of their parent over many years go by without doing anything about it or trying to change things...
        self.set_age(self.Jess_Abernathy, "25")
        self.set_gender(self.Jess_Abernathy, "female")
