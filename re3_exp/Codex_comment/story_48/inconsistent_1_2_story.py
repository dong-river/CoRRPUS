## Richard Kane glanced at his watch, frowning.
## His daughter's bedtime was rapidly approaching, and he had yet to settle the kid down.
## When she wasn't having trouble falling asleep, she was up before dawn and running through the house.
## She and her brother had little interest in television.
## He suspected that their mother was mostly responsible for that.
## Olivia rarely watched any shows with them in front of the screen, and their father didn't bother trying to convince her otherwise.
## He rose from his seat at the table with a sigh and glanced around the room.
## He spotted his wife by one of the large picture windows, staring out at the backyard with a pensive expression on her face.
## She hadn't moved since he had last spoken to her, an hour ago at least.
## He moved towards her and touched her shoulder, then turned towards their youngest child.
## "Bring Jack into your room," he said quietly before returning his attention to Olivia.
## She turned to him slowly, nodding without a word before heading towards their son's bedroom with Jack trotting behind her cheerfully.
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
        self.Shannon_Fitzgerald = character('Shannon Fitzgerald')
        self.Olivia_Kane = character('Olivia Kane')
        self.Richard_Kane = character('Richard Kane')

    def story(self):
        ## Richard Kane glanced at his watch, frowning.
        ## His daughter's bedtime was rapidly approaching, and he had yet to settle the kid down.
        self.Olivia_Kane.relations['daughter'] = 'Shannon_Fitzgerald'
        self.Shannon_Fitzgerald.relations['father'] = 'Richard_Kane'
        self.Richard_Kane.relations['daughter'] = 'Shannon_Fitzgerald'
        ## When she wasn't having trouble falling asleep, she was up before dawn and running through the house.
        ## She and her brother had little interest in television.
        ## He suspected that their mother was mostly responsible for that.
        self.Shannon_Fitzgerald.relations['mother'] = 'Olivia_Kane'
        ## Olivia rarely watched any shows with them in front of the screen, and their father didn't bother trying to convince her otherwise.
        ## He rose from his seat at the table with a sigh and glanced around the room.
        ## He spotted his wife by one of the large picture windows, staring out at the backyard with a pensive expression on her face.
        ## She hadn't moved since he had last spoken to her, an hour ago at least.
        ## He moved towards her and touched her shoulder, then turned towards their youngest child.
        ## "Bring Jack into your room," he said quietly before returning his attention to Olivia.
        ## She turned to him slowly, nodding without a word before heading towards their son's bedroom with Jack trotting behind her cheerfully.

