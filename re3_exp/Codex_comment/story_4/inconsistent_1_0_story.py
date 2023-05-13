## Mark Woodbury hurried down the sidewalk and crossed the street.
## He didn’t have time to be late for his date with Shannon Kincaid, and he wanted to arrive at the restaurant early so he could beat the rush.
## As he neared the entrance, he saw her waving at him from a table inside.
## “I’m sorry I’m late, Mark,” she said when he sat down.
## “I was held up in traffic on the way here.
## How are you?”  Mark leaned over and kissed her cheek.
## “That was quite a jolt you gave me when you called a few minutes ago and said you were running late.
## But I guess it’s good that I got here when I did.
## If we had set this thing for any later, we would have missed our reservation for sure.
## They were about to turn people away as I walked up here.”  Shannon laughed lightly.
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
        self.Shannon_Kincaid = character('Shannon Kincaid')
        self.Jack_Kincaid = character('Jack Kincaid')
        self.Mark_Woodbury = character('Mark Woodbury')

    def story(self):
        ## Mark Woodbury hurried down the sidewalk and crossed the street.
        ## He didn’t have time to be late for his date with Shannon Kincaid, and he wanted to arrive at the restaurant early so he could beat the rush.
        ## As he neared the entrance, he saw her waving at him from a table inside.
        ## “I’m sorry I’m late, Mark,” she said when he sat down.
        ## “I was held up in traffic on the way here.
        ## How are you?”  Mark leaned over and kissed her cheek.
        ## “That was quite a jolt you gave me when you called a few minutes ago and said you were running late.
        ## But I guess it’s good that I got here when I did.
        ## If we had set this thing for any later, we would have missed our reservation for sure.
        ## They were about to turn people away as I walked up here.”  Shannon laughed lightly.
        self.Shannon_Kincaid.relations['boyfriend'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['girlfriend'] = 'Shannon_Kincaid'
        self.Mark_Woodbury.gender.append('male')
        self.Shannon_Kincaid.gender.append('female')
        ## "I’m sorry I’m late, Mark," she said when he sat down.
        ## "I was held up in traffic on the way here.
        ## How are you?"
        self.Mark_Woodbury.relations['held_up'] = 'Shannon_Kincaid'
        ## Mark leaned over and kissed her cheek.
        self.Mark_Woodbury.relations['kissed'] = 'Shannon_Kincaid'
        ## "That was quite a jolt you gave me when you called a few minutes ago and said you were running late.
        ## But I guess it’s good that I got here when I did.
        ## If we had set this thing for any later, we would have missed our reservation for sure.
        ## They were about to turn people away as I walked up here."
        ## Shannon laughed lightly.
        
