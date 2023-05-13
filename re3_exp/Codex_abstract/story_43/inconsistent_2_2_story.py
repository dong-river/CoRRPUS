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
        self.set_appearance(self.Shannon_Mulaney, "dark sky")
        ## She also knew that her mom wasn't going to listen to the warning and stay home.
        self.set_relation(self.Shannon_Mulaney, 'mom', self.Olivia_Kendall)
        self.set_relation(self.Olivia_Kendall, 'daughter', self.Shannon_Mulaney)
        ## Shannon turned away from the window and sighed as she looked around her room.
        ## She was about to turn 20 years old and here she was still living with her mom in a small town in upstate New York.
        self.set_age(self.Shannon_Mulaney, "20")
        ## Her mom hadn't let go of life after losing Shannon's dad when Shannon was 9, so she kept busy, going here and there until late at night, rarely taking care of Shannon.
        self.set_relation(self.Shannon_Mulaney, 'dad', self.Olivia_Kendall)
        self.set_age(self.Shannon_Mulaney, "9")
        ## There were days that Shannon felt like nobody wanted her around except for Jess Abernathy, who had been appointed as an official university staff member at XYZ University to be assigned as an RA (resident assistant) in a dormitory suite named "Sky House".
        self.set_relation(self.Shannon_Mulaney, 'friend', self.Jess_Abernathy)
        self.set_relation(self.Jess_Abernathy, 'friend', self.Shannon_Mulaney)
        self.set_occupation(self.Jess_Abernathy, "RA")
        ## While Jess had barely known this girl, she seemed so lonely but just not willing to talk about it or anything else really...  As a friend it was tough to watch your best friend face the loss of their parent over many years go by without doing anything about it or trying to change things...
        self.set_relation(self.Jess_Abernathy, 'best friend', self.Shannon_Mulaney)
        self.set_relation(self.Shannon_Mulaney, 'best friend', self.Jess_Abernathy)
        self.set_relation(self.Shannon_Mulaney, 'parent', self.Olivia_Kendall)
        self.set_relation(self.Olivia_Kendall, 'child', self.Shannon_Mulaney)
##
## The story is set in the present day and takes place in the United States.
## Joan Westfall is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind.
## Brent Westfall is Joan's husband. He is a kind and loving man who is struggling to cope with his wife's death.
## Jason Westfall is Joan's son. He is a young boy who is struggling to understand his mother's death.
## Jason Westfall sits on the floor, looking at the empty box that used to hold his sister-in-law's belongings. 
## His gaze is unfocused. his dark blue eyes brimming with tears.
## He cries for hours, eventually falling asleep from exhaustion.
## When he wakes up, he feels dazed and ill.
## Joan died in a car accident on a rainy day several weeks ago.
## Jason has been carrying on with life ever since as best he can manage, but he still doesn't really know how to cope with Joan's death.
## Create a world model state to track each character's appearance, personality, and relations with other characters.

