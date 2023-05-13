## Jimmy Jackson was worried.
## His best friend, Jenny Anderson, had just disappeared.
## It had all started when he had been working at his father's garage, right across the street from a large and lonely house.
## The man who lived there, Mr. Jones, was not very popular in town.
## He was mean and cruel to anyone who crossed him.
## Jimmy suspected that he might have killed someone once or twice.
## Jimmy heard a noise outside his garage door and saw a black cat run across the street to the lonely house next door.
## Curious, Jimmy followed it and found it sitting on the windowsill of Mr. Jones' bedroom on the second floor of his home.
## As Jimmy stared up at him in shock, Mr. Jones came out of his room with two jars full of mice and tossed them both out his window where they fell onto their sides upon impact with the grass below them--the mice inside were running around like crazy before the broken glass killed them both instantly!
## Mr. Jones went back into his room whistling innocently to himself as if nothing had happened!
## This was too much for Jimmy to handle--he fainted on the spot!
## Jimmy awoke with a start as Jenny shook him awake "What happened?"
## asked Jenny "I don't know!"

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
        self.Jenny_Anderson = character('Jenny Anderson')
        self.Jimmy_Jackson = character('Jimmy Jackson')
        self.Principal_Stevens = character('Principal Stevens')

    def set_appearance(self, character, appearance):
        character.appearance.append(appearance)
    
    def set_occupation(self, character, occupation):
        character.occupation.append(occupation)
    
    def set_gender(self, character, gender):
        character.gender.append(gender)
    
    def set_age(self, character, age):
        character.age.append(age)
    
    def set_relation(self, character, relation, other_character):
        character.relations[relation] = other_character.name
        
    def story(self):
        ## Jimmy Jackson was worried.
        self.set_gender(self.Jimmy_Jackson, "male")
        ## His best friend, Jenny Anderson, had just disappeared.
        self.set_relation(self.Jimmy_Jackson, 'best friend', self.Jenny_Anderson)
        self.set_relation(self.Jenny_Anderson, 'best friend', self.Jimmy_Jackson)
        self.set_gender(self.Jenny_Anderson, "female")
        ## It had all started when he had been working at his father's garage, right across the street from a large and lonely house.
        self.set_relation(self.Jimmy_Jackson, 'father', self.Jimmy_Jackson)
        self.set_occupation(self.Jimmy_Jackson, 'garage')
        ## The man who lived there, Mr. Jones, was not very popular in town.
        ## He was mean and cruel to anyone who crossed him.
        ## Jimmy suspected that he might have killed someone once or twice.
        ## Jimmy heard a noise outside his garage door and saw a black cat run across the street to the lonely house next door.
        ## Curious, Jimmy followed it and found it sitting on the windowsill of Mr. Jones' bedroom on the second floor of his home.
        ## As Jimmy stared up at him in shock, Mr. Jones came out of his room with two jars full of mice and tossed them both out his window where they fell onto their sides upon impact with the grass below them--the mice inside were running around like crazy before the broken glass killed them both instantly!
        ## Mr. Jones went back into his room whistling innocently to himself as if nothing had happened!
        ## This was too much for Jimmy to handle--he fainted on the spot!
        ## Jimmy awoke with a start as Jenny shook him awake "What happened?"
        ## asked Jenny "I don't know!"
