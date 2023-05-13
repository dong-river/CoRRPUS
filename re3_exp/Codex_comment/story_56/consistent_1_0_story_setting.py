## A girl is juggling her job, her schoolwork, and her ailing mother.
## When her mother finally passes away, the girl is left with an immense sense of guilt.
## The story is set in a small town in the Midwest.
## Karen Smith is a young woman in her early twenties.
## She has shoulder-length brown hair and brown eyes.
## She is of average height and build.
## Janice Smith is Karen’s mother.
## She is in her early fifties and is quite ill. She has short, graying hair and blue eyes.
## Leah White is Karen’s best friend.
## She is also in her early twenties and has shoulder-length blond hair and blue eyes.
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
        self.Karen_Smith = character('Karen Smith')
        self.Janice_Smith = character('Janice Smith')
        self.Leah_White = character('Leah White')

    def story(self):
        ## A girl is juggling her job, her schoolwork, and her ailing mother.
        self.Karen_Smith.gender.append('female')
        self.Karen_Smith.relations['mother'] = 'Janice_Smith'
        self.Karen_Smith.relations['best_friend'] = 'Leah_White'
        self.Janice_Smith.relations['daughter'] = 'Karen_Smith'
        self.Leah_White.relations['best_friend'] = 'Karen_Smith'
        ## When her mother finally passes away, the girl is left with an immense sense of guilt.
        ## The story is set in a small town in the Midwest.
        ## Karen Smith is a young woman in her early twenties.
        self.Karen_Smith.age.append('young')
        ## She has shoulder-length brown hair and brown eyes.
        self.Karen_Smith.appearance.append('shoulder-length brown hair')
        self.Karen_Smith.appearance.append('brown eyes')
        ## She is of average height and build.
        self.Karen_Smith.appearance.append('average height')
        self.Karen_Smith.appearance.append('average build')
        ## Janice Smith is Karen’s mother.
        ## She is in her early fifties and is quite ill. She has short, graying hair and blue eyes.
        self.Janice_Smith.age.append('early fifties')
        self.Janice_Smith.appearance.append('short graying hair')
        self.Janice_Smith.appearance.append('blue eyes')
        ## Leah White is Karen’s best friend.
        ## She is also in her early twenties and has shoulder-length blond hair and blue eyes.
        self.Leah_White.age.append('early twenties')
        self.Leah_White.appearance.append('shoulder-length blond hair')
        self.Leah_White.appearance.append('blue eyes')

