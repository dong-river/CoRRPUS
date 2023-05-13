## Julia Fletcher had been the only person to witness the murder of her daughter-in-law Karen on that fateful day in February.
## Ever since then, she has been on a constant watch for Karen's ghost and sees her shadow sometimes.
## The doctors say that she is suffering from hallucinations due to her condition.
## But every time she sees it, her health seems to worsen drastically.
## On one fine day when she started convulsing, no one could do anything about it except for the nurse who has been working with Julia for the past four years.
## “She might be seeing things!”  “I can see my daughter in this mirror!
## Why is my body shaking?
## Is this a fit?
## It feels like I am shaking all over and I can't control myself!
## Why am I talking like this?
## Am I speaking without a tongue or without feeling a mouth?” She sobbed while clutching her chest at the same time.
## A jolt of fear ran through everyone who was witnessing Julia's state at that time, including Karen's daughter Kate who was trying to give comfort to her mother-in-law.
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
        self.Karen_Fletcher = character('Karen Fletcher')
        self.Kate_Fletcher = character('Kate Fletcher')
        self.Julia_Fletcher = character('Julia Fletcher')

    def story(self):
        ## Julia Fletcher had been the only person to witness the murder of her daughter-in-law Karen on that fateful day in February.
        self.Julia_Fletcher.relations['daughter-in-law'] = 'Karen_Fletcher'
        self.Karen_Fletcher.relations['mother-in-law'] = 'Julia_Fletcher'
        ## Ever since then, she has been on a constant watch for Karen's ghost and sees her shadow sometimes.
        ## The doctors say that she is suffering from hallucinations due to her condition.
        ## But every time she sees it, her health seems to worsen drastically.
        ## On one fine day when she started convulsing, no one could do anything about it except for the nurse who has been working with Julia for the past four years.
        self.Julia_Fletcher.relations['nurse'] = 'Kate_Fletcher'
        ## “She might be seeing things!”  “I can see my daughter in this mirror!
        self.Julia_Fletcher.relations['daughter'] = 'Kate_Fletcher'
        ## Why is my body shaking?
        ## Is this a fit?
        ## It feels like I am shaking all over and I can't control myself!
        ## Why am I talking like this?
        ## Am I speaking without a tongue or without feeling a mouth?” She sobbed while clutching her chest at the same time.
        ## A jolt of fear ran through everyone who was witnessing Julia's state at that time, including Karen's daughter Kate who was trying to give comfort to her mother-in-law.

