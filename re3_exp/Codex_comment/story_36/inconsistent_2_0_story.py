## Julia Fletcher knocks on the door to her sister's hospital room.
## Karen answers the door, having just come out of the bathroom.
## "Oh good, you're up.
## The doctor said you could go home today," Julia says, hugging her sister.
## "That's great news.
## I was beginning to feel like a prisoner in here," Karen says.
## "Although I'm glad they took care of my daughter."
## "They took care of your daughter?"
## Julia asks.
## "The one who's dead?"
## Karen gasps and holds her stomach, grimacing with pain as she collapses on the bed, tears streaming down her face.
## "She's dead?
## She died?"
## she cries.
## "What happened?
## Was it a car accident?"
## "I'm so sorry, Karen," Julia says as she sits on the bed next to her sister and pulls her into a hug.
## "No one told you yet?
## You must have been asleep when they came and told me."
## Her voice catches in her throat as she realizes what happened while Karen was asleep.
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
        ## Julia Fletcher knocks on the door to her sister's hospital room.
        ## Karen answers the door, having just come out of the bathroom.
        ## "Oh good, you're up.
        ## The doctor said you could go home today," Julia says, hugging her sister.
        self.Julia_Fletcher.relations['sister'] = 'Karen_Fletcher'
        self.Karen_Fletcher.relations['sister'] = 'Julia_Fletcher'
        ## "That's great news.
        ## I was beginning to feel like a prisoner in here," Karen says.
        ## "Although I'm glad they took care of my daughter."
        ## "They took care of your daughter?"
        ## Julia asks.
        ## "The one who's dead?"
        ## Karen gasps and holds her stomach, grimacing with pain as she collapses on the bed, tears streaming down her face.
        ## "She's dead?
        ## She died?"
        ## she cries.
        ## "What happened?
        ## Was it a car accident?"
        ## "I'm so sorry, Karen," Julia says as she sits on the bed next to her sister and pulls her into a hug.
        ## "No one told you yet?
        ## You must have been asleep when they came and told me."
        ## Her voice catches in her throat as she realizes what happened while Karen was asleep.


