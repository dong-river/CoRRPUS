## Carl Russo parked his car in front of the police station, excited to tell his coworker and friend, John Davis, about a television show he was watching.
## The show was called 'Police Intervention', and its goal was to catch police officers on camera during a routine traffic stop who were unfairly profiling.
## "Hey, Davis!"
## Carl shouted as he burst through the front door of the police station.
## John waved at Carl from across the room.
## He stopped talking to the other cops and turned around to face Carl as he approached him.
## "Hey Russo," John said with a big smile on his face.
## "You're in a good mood today!"
## Carl dropped his things on his desk and looked at John curiously.
## "I have good news!
## And I know you'll appreciate it."
## He nodded at one of the other cops nearby and laughed when that cop made fun of him for going to UCLA instead of California State University at Northridge.
## They all shared some good-natured laughs together before they turned back towards Carl and John when they heard Carl's next sentence; "I watched this great TV show last night called 'Police Intervention'."
## "What's that?"
## one of the young rookie cops asked.
## "Like COPS?"
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
        self.Valerie_Russo = character('Valerie Russo')
        self.Carl_Russo = character('Carl Russo')
        self.Antoinette_Russo = character('Antoinette Russo')

    def story(self):
        ## Carl Russo parked his car in front of the police station, excited to tell his coworker and friend, John Davis, about a television show he was watching.
        self.Carl_Russo.occupation.append('police officer')
        self.Carl_Russo.relations['friend'] = 'John_Davis'
        self.Carl_Russo.relations['wife'] = 'Valerie_Russo'
        self.Carl_Russo.relations['daughter'] = 'Antoinette_Russo'
        self.Carl_Russo.appearance.append('dark brown hair')
        self.Carl_Russo.appearance.append('brown eyes')
        self.Carl_Russo.appearance.append('light skin')
        self.Carl_Russo.appearance.append('6 feet tall')
        self.Carl_Russo.appearance.append('180 pounds')
        self.Carl_Russo.gender.append('male')
        self.Carl_Russo.age.append('40')
        ## The show was called 'Police Intervention', and its goal was to catch police officers on camera during a routine traffic stop who were unfairly profiling.
        ## "Hey, Davis!"
        ## Carl shouted as he burst through the front door of the police station.
        ## John waved at Carl from across the room.
        ## He stopped talking to the other cops and turned around to face Carl as he approached him.
        ## "Hey Russo," John said with a big smile on his face.
        ## "You're in a good mood today!"
        self.John_Davis.relations['friend'] = 'Carl_Russo'
        self.John_Davis.appearance.append('dark brown hair')
        self.John_Davis.appearance.append('brown eyes')
        self.John_Davis.appearance.append('light skin')
        self.John_Davis.appearance.append('6 feet tall')
        self.John_Davis.appearance.append('180 pounds')
        self.John_Davis.gender.append('male')
        self.John_Davis.age.append('40')
        self.John_Davis.occupation.append('police officer')
        ## Carl dropped his things on his desk and looked at John curiously.
        ## "I have good news!
        ## And I know you'll appreciate it."
        ## He nodded at one of the other cops nearby and laughed when that cop made fun of him for going to UCLA instead of California State University at Northridge.
        ## They all shared some good-natured laughs together before they turned back towards Carl and John when they heard Carl's next sentence; "I watched this great TV show last night called 'Police Intervention'."
        ## "What's that?"
        ## one of the young rookie cops asked.
        ## "Like COPS?"
        self.Valerie_Russo.occupation.append('police officer')
        self.Valerie_Russo.relations['husband'] = 'Carl_Russo'
        self.Valerie_Russo.relations['daughter'] = 'Antoinette_Russo'
        self.Valerie_Russo.appearance.append('dark brown hair')
        self.Valerie_Russo.appearance.append('brown eyes')
        self.Valerie_Russo.appearance.append('light skin')
        self.Valerie_Russo.appearance.append('6 feet tall')
        self.Valerie_Russo.appearance.append('180 pounds')
        self.Valerie_Russo.gender.append('female')
        self.Valerie_Russo.age.append('40')
        self.Antoinette_Russo.relations['mother'] = 'Valerie_Russo'
        self.Antoinette_Russo.relations['father'] = 'Carl_Russo'
        self.Antoinette_Russo.appearance.append('dark brown hair')
        self.Antoinette_Russo.appearance.append('brown eyes')
        self.Antoinette_Russo.appearance.append('light skin')
        self.Antoinette_Russo.appearance.append('6 feet tall')
        self.Antoinette_Russo.appearance.append('180 pounds')
        self.Antoinette_Russo.gender.append('female')
        self.Antoinette_Russo.age.append('20')

