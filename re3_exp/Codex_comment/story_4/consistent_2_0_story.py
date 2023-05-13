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
        self.Shannon_Kincaid.gender.append('female')
        self.Mark_Woodbury.gender.append('male')
        ## Shannon Kincaid is a beautiful woman with long black hair, dark brown eyes, and an athletic build.
        self.Shannon_Kincaid.appearance.append('beautiful')
        self.Shannon_Kincaid.appearance.append('long black hair')
        self.Shannon_Kincaid.appearance.append('dark brown eyes')
        self.Shannon_Kincaid.appearance.append('athletic build')
        ## She is a nurse at the local hospital, and she works long hours.
        self.Shannon_Kincaid.occupation.append('nurse')
        ## She is divorced and has a son named Jack.
        self.Shannon_Kincaid.relations['ex-husband'] = 'Jack Kincaid'
        self.Shannon_Kincaid.relations['son'] = 'Jack Kincaid'
        ## Jack is a high school student who is struggling with the divorce.
        self.Jack_Kincaid.relations['mother'] = 'Shannon Kincaid'
        self.Jack_Kincaid.age.append('high school student')
        ## Mark Woodbury is a handsome man with short brown hair, blue eyes, and a muscular build.
        self.Mark_Woodbury.appearance.append('handsome')
        self.Mark_Woodbury.appearance.append('short brown hair')
        self.Mark_Woodbury.appearance.append('blue eyes')
        self.Mark_Woodbury.appearance.append('muscular build')
        ## He is an accountant at a local firm, and he has a steady income.
        self.Mark_Woodbury.occupation.append('accountant')
        ## He is divorced and has no children.
        self.Mark_Woodbury.relations['ex-wife'] = 'Shannon Kincaid'
        ## Mark and Shannon met at a party a few weeks ago, and they have been dating ever since.
        self.Mark_Woodbury.relations['girlfriend'] = 'Shannon Kincaid'
        self.Shannon_Kincaid.relations['boyfriend'] = 'Mark Woodbury'
        ## Mark and Shannon have a lot in common, and they have been enjoying each other’s company.
        ## Mark and Shannon have been dating for a few weeks, and they are enjoying each other’s company.
        ## They have a lot in common, and they have been talking about moving in together.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## They have been dating for a few weeks, and they are enjoying each other’s company.
        ## They have a lot in common, and they have been talking about moving in together.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner at a local restaurant.
        ## Mark has been working long hours at his job, and he is tired.
        ## He has been talking about taking a vacation, and he has been looking forward to this evening out with Shannon.
        ## Shannon has been working long hours at the hospital, and she is tired.
        ## She has been talking about taking a vacation, and she has been looking forward to this evening out with Mark.
        ## Mark and Shannon are enjoying a romantic dinner