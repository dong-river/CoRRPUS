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
        self.Mark_Woodbury.appearance.append('middle-aged')
        self.Mark_Woodbury.appearance.append('graying hair')
        self.Mark_Woodbury.appearance.append('mustache')
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
        self.Shannon_Kincaid.occupation.append('investigative reporter')
        self.Mark_Woodbury.occupation.append('editor')
        self.Shannon_Kincaid.relations['editor'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['reporter'] = 'Shannon_Kincaid'
        ## “I’m sorry Shannon,” Mark said.
        ## “But it’s just not a good idea.
        ## You know how the paper’s been doing lately…” “But…” Shannon protested.
        ## “It’s a great idea!
        ## It’s a story that will bring in a lot of readers!
        ## And it’s not like we’re going to print it right away—we’ll wait until the right moment to publish it.”  “It’s not that,” Mark said.
        ## “It’s just…” He paused for a moment.
        ## “Well, it’s just that you’re not the best person to be writing about this kind of thing.
        ## You’re too…emotionally involved.” Shannon’s eyes widened in surprise.
        ## “What?” She asked.
        ## “What are you talking about?
        ## I’m not emotionally involved in this story at all!”  “Oh really?” Mark asked.
        ## “Then why did you bring your husband along with you when you came to see me?” Shannon looked at Jack, who was standing behind her.
        ## “Jack?” She asked.
        ## “What are you doing here?” “I thought you might want me to come along,” Jack said.
        ## “I know how much this story means to you…and I wanted to support you.” “Oh.” Shannon said, her voice suddenly quiet.
        ## “I…I didn’t know.”  “Well, now you do,” Mark said.
        ## “And I think it would be best if you stepped aside for this one.
        ## I’ll find someone else to write the story.”  “But…” Shannon began to protest.
        ## “No buts,” Mark said.
        ## “I’m sorry, but that’s my final decision.”  Shannon turned and walked out of the office without another word.
        ## Jack followed her out, closing the door behind him.
        ## “I’m sorry,” he said.
        ## “I didn’t mean to make things worse.
        ## I just thought you might want me to come along.” “It’s not your fault,” Shannon said.
        ## “I’m just…I’m just upset.
        ## I worked so hard on this story…and now it’s all for nothing.” She sighed.
        ## “I guess I’ll just have to find something else to write about.” “Well,” Jack said.
        ## “Maybe it’s for the best.
        ## I mean, this story is about your sister…and I know how hard it is for you to talk about her.” “Yeah,” Shannon said.
        ## “I guess you’re right.
        ## I just wish things could be different.” “Me too,” Jack said.
        ## “Me too.”

