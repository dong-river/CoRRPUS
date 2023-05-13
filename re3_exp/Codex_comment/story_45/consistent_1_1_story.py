## Karen Hartman was worried about her daughter, Nina.
## She was worried because the child was becoming increasingly withdrawn and moody.
## It all started a few months ago when she would wake up in the middle of the night sobbing and thrashing wildly around in her bed.
## Every time she was questioned about it, she would give the same answer, "I don't know."
## Karen decided to put it out of her mind as her daughter began school this year.
## But she started having problems there too, showing unusual interest in anything that resembled ghost stories or movies with lots of special effects.
## She even began asking questions about ghosts in everyday life to both her teachers and the students around her at school.
## Some of the other students had heard rumors about a house on Charlotte Street that supposedly haunted and laughed at Nina's questions and rumors went through the school about Nina having a crush on a cute boy that lived there named Jake Ryan.
## "Do you know who I am talking about?"
## asked Nina anxiously as she continued pacing back and forth from one end of Karen's living room to another, stopping every so often to look at something intently out one of the windows or shake her head slowly side to side like someone in deep thought.
## Karen shook her head no in response.
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
        self.Nina_Harman = character('Nina Harman')
        self.Jake_Ryan = character('Jake Ryan')
        self.Karen_Hartman = character('Karen Hartman')

    def story(self):
        ## Karen Hartman was worried about her daughter, Nina.
        self.Karen_Hartman.relations['daughter'] = 'Nina_Harman'
        self.Nina_Harman.relations['mother'] = 'Karen_Hartman'
        ## She was worried because the child was becoming increasingly withdrawn and moody.
        self.Nina_Harman.appearance.append('withdrawn')
        self.Nina_Harman.appearance.append('moody')
        ## It all started a few months ago when she would wake up in the middle of the night sobbing and thrashing wildly around in her bed.
        ## Every time she was questioned about it, she would give the same answer, "I don't know."
        ## Karen decided to put it out of her mind as her daughter began school this year.
        ## But she started having problems there too, showing unusual interest in anything that resembled ghost stories or movies with lots of special effects.
        self.Nina_Harman.occupation.append('student')
        ## She even began asking questions about ghosts in everyday life to both her teachers and the students around her at school.
        ## Some of the other students had heard rumors about a house on Charlotte Street that supposedly haunted and laughed at Nina's questions and rumors went through the school about Nina having a crush on a cute boy that lived there named Jake Ryan.
        self.Jake_Ryan.appearance.append('cute')
        self.Nina_Harman.relations['crush'] = 'Jake_Ryan'
        ## "Do you know who I am talking about?"
        ## asked Nina anxiously as she continued pacing back and forth from one end of Karen's living room to another, stopping every so often to look at something intently out one of the windows or shake her head slowly side to side like someone in deep thought.
        ## Karen shook her head no in response.

