## After a car crash, a woman starts seeing ghosts.
## The ghosts tell her she has to right the wrongs they did in life in order to move on.
## She's not sure if she's going crazy or if this is really happening.
## The story is set in a small town in the United States.
## Jennie Mayfield is a young woman in her early twenties.
## She has long dark hair and brown eyes.
## She is of average height and build.
## Aaron Mayfield is Jennie's older brother.
## He is in his late twenties and has short blond hair and blue eyes.
## He is taller than Jennie and has a muscular build.
## Alex Preston is a young man in his early twenties, who is Jennie's boyfriend and Aaron's best friend.
## He has short dark hair and brown eyes, and is of average height and build.
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
        self.Jennie_Mayfield = character('Jennie Mayfield')
        self.Aaron_Mayfield = character('Aaron Mayfield')
        self.Alex_Preston = character('Alex Preston')

    def story(self):
        ## After a car crash, a woman starts seeing ghosts.
        ## The ghosts tell her she has to right the wrongs they did in life in order to move on.
        ## She's not sure if she's going crazy or if this is really happening.
        ## The story is set in a small town in the United States.
        ## Jennie Mayfield is a young woman in her early twenties.
        self.Jennie_Mayfield.age.append('young')
        self.Jennie_Mayfield.age.append('early twenties')
        ## She has long dark hair and brown eyes.
        self.Jennie_Mayfield.appearance.append('long dark hair')
        self.Jennie_Mayfield.appearance.append('brown eyes')
        ## She is of average height and build.
        self.Jennie_Mayfield.appearance.append('average height')
        self.Jennie_Mayfield.appearance.append('average build')
        ## Aaron Mayfield is Jennie's older brother.
        self.Jennie_Mayfield.relations['older brother'] = 'Aaron_Mayfield'
        self.Aaron_Mayfield.relations['younger sister'] = 'Jennie_Mayfield'
        ## He is in his late twenties and has short blond hair and blue eyes.
        self.Aaron_Mayfield.age.append('late twenties')
        self.Aaron_Mayfield.appearance.append('short blond hair')
        self.Aaron_Mayfield.appearance.append('blue eyes')
        ## He is taller than Jennie and has a muscular build.
        self.Aaron_Mayfield.appearance.append('taller than Jennie')
        self.Aaron_Mayfield.appearance.append('muscular build')
        ## Alex Preston is a young man in his early twenties, who is Jennie's boyfriend and Aaron's best friend.
        self.Alex_Preston.age.append('young')
        self.Alex_Preston.age.append('early twenties')
        self.Jennie_Mayfield.relations['boyfriend'] = 'Alex_Preston'
        self.Aaron_Mayfield.relations['best friend'] = 'Alex_Preston'
        self.Alex_Preston.relations['girlfriend'] = 'Jennie_Mayfield'
        self.Alex_Preston.relations['best friend'] = 'Aaron_Mayfield'
        ## He has short dark hair and brown eyes, and is of average height and build.
        self.Alex_Preston.appearance.append('short dark hair')
        self.Alex_Preston.appearance.append('brown eyes')
        self.Alex_Preston.appearance.append('average height')
        self.Alex_Preston.appearance.append('average build')

