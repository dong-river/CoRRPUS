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
        self.Karen_Smith.age.append('young')
        self.Karen_Smith.gender.append('female')
        self.Karen_Smith.relations['mother'] = 'Janice_Smith'
        self.Janice_Smith.relations['daughter'] = 'Karen_Smith'
        ## When her mother finally passes away, the girl is left with an immense sense of guilt.
        ## The story is set in a small town in the Midwest.
        ## Karen Smith is a young woman in her early twenties.
        self.Karen_Smith.age.append('early twenties')
        ## She has shoulder-length brown hair and brown eyes.
        self.Karen_Smith.appearance.append('shoulder-length brown hair')
        self.Karen_Smith.appearance.append('brown eyes')
        ## She is of average height and build.
        self.Karen_Smith.appearance.append('average height')
        self.Karen_Smith.appearance.append('average build')
        ## Janice Smith is Karen’s mother.
        self.Janice_Smith.relations['daughter'] = 'Karen_Smith'
        ## She is in her early fifties and is quite ill. She has short, graying hair and blue eyes.
        self.Janice_Smith.age.append('early fifties')
        self.Janice_Smith.appearance.append('short graying hair')
        self.Janice_Smith.appearance.append('blue eyes')
        ## Leah White is Karen’s best friend.
        self.Karen_Smith.relations['best friend'] = 'Leah_White'
        self.Leah_White.relations['best friend'] = 'Karen_Smith'
        ## She is also in her early twenties and has shoulder-length blond hair and blue eyes.
        self.Leah_White.age.append('early twenties')
        self.Leah_White.appearance.append('shoulder-length blond hair')
        self.Leah_White.appearance.append('blue eyes')

## A man is running for his life.
## He is being chased by a monster.
## The monster is a giant spider, with four eyes and eight legs.
## The man is running through the woods.
## He is carrying a bag.
## The bag contains a map, a flashlight, and a gun.
## The man is wearing a red jacket and black pants.
## The monster is running after the man.
## The monster is chasing the man.
## The man is running away from the monster.
## The man is trying to escape from the monster.
## Create a world model state to track each character's appearance, personality, and relations with other characters.

