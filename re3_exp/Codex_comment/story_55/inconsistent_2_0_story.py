## Olivia Saunders pulled her car into the school parking lot, and turned off the engine.
## "Don't forget that the assignments are due by tomorrow, Emma," she said, looking at her daughter.
## "I know mom, I won't forget," Emma replied.
## "I told you I've been studying like crazy."
## "Alright," Olivia said, opening the door and getting out of the car.
## "Good luck sweetie."
## Emma sighed.
## Her mother was being overly protective of her, but she knew why.
## She had struggled at school since third grade, when all of a sudden her grades plummeted and teachers began to complain about her behavior in class.
## All this time she had thought that something was wrong with her brain, but doctors never found anything.
## They simply diagnosed it as ADD.
## In high school it got worse; none of her teachers were interested in helping her anymore and she was struggling more than ever to pass even one class in English class that she could barely read now because of dyslexia and ADHD.
## She's stopped trying to be a good girl in school, because they weren't helping anyway so why not be what they thought she already was?
## It gave them more reason to hate on you right?
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
        self.Emma_Saunders = character('Emma Saunders')
        self.Jackson_Cooper = character('Jackson Cooper')
        self.Olivia_Saunders = character('Olivia Saunders')

    def story(self):
        ## Olivia Saunders pulled her car into the school parking lot, and turned off the engine.
        self.Olivia_Saunders.occupation.append('mother')
        self.Olivia_Saunders.relations['daughter'] = 'Emma_Saunders'
        self.Emma_Saunders.relations['mother'] = 'Olivia_Saunders'
        self.Emma_Saunders.age.append('teenage')
        self.Olivia_Saunders.gender.append('female')
        ## "Don't forget that the assignments are due by tomorrow, Emma," she said, looking at her daughter.
        ## "I know mom, I won't forget," Emma replied.
        ## "I told you I've been studying like crazy."
        ## "Alright," Olivia said, opening the door and getting out of the car.
        ## "Good luck sweetie."
        ## Emma sighed.
        ## Her mother was being overly protective of her, but she knew why.
        ## She had struggled at school since third grade, when all of a sudden her grades plummeted and teachers began to complain about her behavior in class.
        ## All this time she had thought that something was wrong with her brain, but doctors never found anything.
        ## They simply diagnosed it as ADD.
        self.Emma_Saunders.relations['diagnosis'] = 'ADD'
        ## In high school it got worse; none of her teachers were interested in helping her anymore and she was struggling more than ever to pass even one class in English class that she could barely read now because of dyslexia and ADHD.
        self.Emma_Saunders.relations['diagnosis'] = 'ADD'
        self.Emma_Saunders.relations['diagnosis'] = 'dyslexia'
        self.Emma_Saunders.relations['diagnosis'] = 'ADHD'
        ## She's stopped trying to be a good girl in school, because they weren't helping anyway so why not be what they thought she already was?
        ## It gave them more reason to hate on you right?

