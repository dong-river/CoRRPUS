## Jimmy Jackson leaned back against the couch in Jenny's living room.
## "Hey, do you think the state will have a good football team this year?"
## he asked.
## "Don't be silly," Jenny replied from her seat on the opposite end of the couch.
## "West Virginia is always a powerhouse."
## "Maybe next year," Jimmy said with a chuckle.
## "But that's not what I meant.
## I mean this year."
## Jenny turned to face Jimmy and reached out to put her arm around his shoulders.
## "I'm sorry about last night," she said apologetically.
## "I had a lot on my mind, and didn't feel like talking."
## She paused before adding, "But we should probably break up."
## Jimmy looked at her incredulously.
## "What are you talking about?"
## he demanded angrily, pushing her arm away from him.
## "After all these years, you're just going to dump me?
## For what?
## What could be so important that you'd throw away something like this?"
## He gestured back and forth between them as if they were nothing more than an old sweater Jenny didn't want anymore.
## As if they had never meant anything to each other at all.
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

    def story(self):
        ## Jimmy Jackson leaned back against the couch in Jenny's living room.
        self.Jimmy_Jackson.occupation.append('student')
        self.Jimmy_Jackson.relations['girlfriend'] = 'Jenny_Anderson'
        self.Jenny_Anderson.relations['boyfriend'] = 'Jimmy_Jackson'
        ## "Hey, do you think the state will have a good football team this year?"
        ## he asked.
        ## "Don't be silly," Jenny replied from her seat on the opposite end of the couch.
        ## "West Virginia is always a powerhouse."
        ## "Maybe next year," Jimmy said with a chuckle.
        ## "But that's not what I meant.
        ## I mean this year."
        ## Jenny turned to face Jimmy and reached out to put her arm around his shoulders.
        ## "I'm sorry about last night," she said apologetically.
        ## "I had a lot on my mind, and didn't feel like talking."
        ## She paused before adding, "But we should probably break up."
        ## Jimmy looked at her incredulously.
        ## "What are you talking about?"
        ## he demanded angrily, pushing her arm away from him.
        ## "After all these years, you're just going to dump me?
        ## For what?
        ## What could be so important that you'd throw away something like this?"
        ## He gestured back and forth between them as if they were nothing more than an old sweater Jenny didn't want anymore.
        ## As if they had never meant anything to each other at all.

