## Mark Woodbury, a middle-aged man with graying hair and a mustache, smiled at Shannon as she walked into his office.
## “Well, if it isn’t my little investigative reporter,” he said.
## Shannon smiled back.
## “Hello Mark,” she said cheerfully.
## “You have to admit that I do have a knack for getting good stories.”  Mark laughed.
## “That you do, young lady.
## That you do.
## And there’s no one better at getting to the bottom of a story than you are.
## Unfortunately…” He took off his glasses and began cleaning them with his handkerchief as he spoke.
## “Unfortunately, I’m going to have to turn down your latest assignment request—and it is an unusual request at that.”  Shannon put her hands on her hips and frowned angrily at him in reply.
## “What?!?
## You can’t turn me down!
## You know how long I worked on this story—how many interviews I did…how many people I asked questions of!
## This is my ticket out of the boring little old city pages—a big exclusive front page story…for real this time!
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
        ## Mark Woodbury, a middle-aged man with graying hair and a mustache, smiled at Shannon as she walked into his office.
        self.Mark_Woodbury.age.append('middle-aged')
        self.Mark_Woodbury.appearance.append('graying hair')
        self.Mark_Woodbury.appearance.append('mustache')
        self.Mark_Woodbury.relations['smiles at'] = 'Shannon_Kincaid'
        ## Shannon smiled back.
        self.Shannon_Kincaid.relations['smiles at'] = 'Mark_Woodbury'
        ## “Hello Mark,” she said cheerfully.
        ## “You have to admit that I do have a knack for getting good stories.”  Mark laughed.
        self.Mark_Woodbury.relations['laughs at'] = 'Shannon_Kincaid'
        ## “That you do, young lady.
        ## That you do.
        ## And there’s no one better at getting to the bottom of a story than you are.
        ## Unfortunately…” He took off his glasses and began cleaning them with his handkerchief as he spoke.
        ## “Unfortunately, I’m going to have to turn down your latest assignment request—and it is an unusual request at that.”  Shannon put her hands on her hips and frowned angrily at him in reply.
        self.Shannon_Kincaid.relations['frowns angrily at'] = 'Mark_Woodbury'
        ## “What?!?
        ## You can’t turn me down!
        ## You know how long I worked on this story—how many interviews I did…how many people I asked questions of!
        ## This is my ticket out of the boring little old city pages—a big exclusive front page story…for real this time!

