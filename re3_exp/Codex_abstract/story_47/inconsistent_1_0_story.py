## Maxine Carter knocked on the apartment door and waited.
## She hated doing this—she much preferred dropping off the food that she cooked for Shannon's boyfriend, but he had insisted.
## A minute later, she heard steps coming down the hall, and a moment later, Shannon opened the door.
## Maxine smiled at her daughter.
## "Is everything all right?
## He didn't hit you again, did he?"
## Shannon rolled her eyes.
## "No, Mom, he didn't hit me again."
## Then she grinned mischievously.
## "We had a great time!
## We went to bed early—and I can tell you that neither of us was asleep when we got up."
## Maxine tried to suppress a smile as she realized what her daughter meant.
## The young man who had asked Shannon out a few weeks ago seemed too good to be true: smart and charming with just enough edge in his personality to make him mysterious.
## But although Maxine had always been wary of men like that, Shannon was of legal age and had no intention of listening to her mother's advice about dating anyone less than perfect—or even only nearly perfect.
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
        self.Shannon_Burke = character('Shannon Burke')
        self.Charles_Burke = character('Charles Burke')
        self.Maxine_Carter = character('Maxine Carter')

    def story(self):
        ## Maxine Carter knocked on the apartment door and waited.
        ## She hated doing this—she much preferred dropping off the food that she cooked for Shannon's boyfriend, but he had insisted.
        ## A minute later, she heard steps coming down the hall, and a moment later, Shannon opened the door.
        self.Shannon_Burke.relations['mother'] = 'Maxine_Carter'
        self.Maxine_Carter.relations['daughter'] = 'Shannon_Burke'
        ## Maxine smiled at her daughter.
        ## "Is everything all right?
        ## He didn't hit you again, did he?"
        ## Shannon rolled her eyes.
        ## "No, Mom, he didn't hit me again."
        ## Then she grinned mischievously.
        ## "We had a great time!
        ## We went to bed early—and I can tell you that neither of us was asleep when we got up."
        ## Maxine tried to suppress a smile as she realized what her daughter meant.
        ## The young man who had asked Shannon out a few weeks ago seemed too good to be true: smart and charming with just enough edge in his personality to make him mysterious.
        ## But although Maxine had always been wary of men like that, Shannon was of legal age and had no intention of listening to her mother's advice about dating anyone less than perfect—or even only nearly perfect.

