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

    def story(self):
        ## Shannon Mulaney looked out her bedroom window at the dark sky.
        ## A storm was coming and Shannon knew that there would be a tornado warning in her town tomorrow.
        ## She also knew that her mom wasn't going to listen to the warning and stay home.
        self.Shannon_Mulaney.relations['mother'] = 'Olivia_Kendall'
        self.Olivia_Kendall.relations['daughter'] = 'Shannon_Mulaney'
        ## Shannon turned away from the window and sighed as she looked around her room.
        ## She was about to turn 20 years old and here she was still living with her mom in a small town in upstate New York.
        self.Shannon_Mulaney.age.append('20')
        self.Shannon_Mulaney.appearance.append('upstate New York')
        ## Her mom hadn't let go of life after losing Shannon's dad when Shannon was 9, so she kept busy, going here and there until late at night, rarely taking care of Shannon.
        self.Olivia_Kendall.relations['husband'] = 'Shannon_Mulaney'
        self.Shannon_Mulaney.age.append('9')
        ## There were days that Shannon felt like nobody wanted her around except for Jess Abernathy, who had been appointed as an official university staff member at XYZ University to be assigned as an RA (resident assistant) in a dormitory suite named "Sky House".
        self.Shannon_Mulaney.relations['friend'] = 'Jess_Abernathy'
        self.Jess_Abernathy.relations['friend'] = 'Shannon_Mulaney'
        self.Jess_Abernathy.appearance.append('XYZ University')
        self.Jess_Abernathy.occupation.append('RA')
        self.Jess_Abernathy.appearance.append('Sky House')
        ## While Jess had barely known this girl, she seemed so lonely but just not willing to talk about it or anything else really...  As a friend it was tough to watch your best friend face the loss of their parent over many years go by without doing anything about it or trying to change things...

