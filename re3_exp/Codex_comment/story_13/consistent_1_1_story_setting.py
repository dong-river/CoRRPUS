## Sherry had the perfect life--three healthy children, a loving wife, and a job to support them; until she discovers what was happening right in front of her.
## Sherry's wife has been cheating on her with her brother ever since they've been married.
## A panic attack at work forces Sherry to deal with her personal life head on.
## After gaining some closure, she moves out of state with her children to start afresh.
## The story is set in the present day in a small town in the midwest.
## Sherry Hellinger is a middle-aged woman with short brown hair and green eyes.
## She is of average height and build.
## Emily Hellinger is Sherry's wife of ten years.
## She is a tall woman with long blond hair and blue eyes.
## She is in her early 40s.
## John Hellinger is Sherry's older brother.
## He is a tall man with short brown hair and blue eyes.
## He is in his early 40s.
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
        self.Sherry_Hellinger = character('Sherry Hellinger')
        self.Emily_Hellinger = character('Emily Hellinger')
        self.John_Hellinger = character('John Hellinger')

    def story(self):
        ## Sherry had the perfect life--three healthy children, a loving wife, and a job to support them; until she discovers what was happening right in front of her.
        self.Sherry_Hellinger.relations['wife'] = 'Emily_Hellinger'
        self.Sherry_Hellinger.relations['brother'] = 'John_Hellinger'
        self.Sherry_Hellinger.gender.append('female')
        self.Sherry_Hellinger.age.append('middle-aged')
        ## Sherry's wife has been cheating on her with her brother ever since they've been married.
        self.Emily_Hellinger.relations['wife'] = 'Sherry_Hellinger'
        self.Emily_Hellinger.relations['lover'] = 'John_Hellinger'
        self.Emily_Hellinger.gender.append('female')
        self.Emily_Hellinger.age.append('early 40s')
        self.John_Hellinger.relations['sister'] = 'Sherry_Hellinger'
        self.John_Hellinger.relations['lover'] = 'Emily_Hellinger'
        self.John_Hellinger.gender.append('male')
        self.John_Hellinger.age.append('early 40s')
        ## A panic attack at work forces Sherry to deal with her personal life head on.
        ## After gaining some closure, she moves out of state with her children to start afresh.
        ## The story is set in the present day in a small town in the midwest.
        ## Sherry Hellinger is a middle-aged woman with short brown hair and green eyes.
        self.Sherry_Hellinger.appearance.append("short brown hair")
        self.Sherry_Hellinger.appearance.append("green eyes")
        ## She is of average height and build.
        ## Emily Hellinger is Sherry's wife of ten years.
        ## She is a tall woman with long blond hair and blue eyes.
        self.Emily_Hellinger.appearance.append("long blond hair")
        self.Emily_Hellinger.appearance.append("blue eyes")
        ## She is in her early 40s.
        ## John Hellinger is Sherry's older brother.
        ## He is a tall man with short brown hair and blue eyes.
        self.John_Hellinger.appearance.append("short brown hair")
        self.John_Hellinger.appearance.append("blue eyes")
        ## He is in his early 40s.

