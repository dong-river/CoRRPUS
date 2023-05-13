## Leah White waited impatiently for her granddaughter, Karen, to arrive.
## As she peered through the curtains of her small living room window, she spotted a familiar car making its way down the driveway.
## She smiled; her Karen was home.
## “Hi, Grandma!” Karen said as she came in through the door.
## Leah came out from behind the sofa and hugged her beloved granddaughter warmly.
## “Karen…you are so pretty!
## What happened to that little thing who used to play Barbies with me?
## And what are you doing with all those bags?
## You’re going on a trip?”  Karen sat down and began pulling items out of the bags while answering her grandmother’s questions.
## “Yeah, it’s too much trouble to take all my textbooks to school; I get there too early anyhow.
## So I decided to buy them online this semester.
## And I was just about to walk into Wal-Mart for a few things for Mom—she asked me last night—when Dad called me and told me he wanted me to pick up some things at Sam’s club today instead of going there today.
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
        ## Leah White waited impatiently for her granddaughter, Karen, to arrive.
        self.Leah_White.relations['granddaughter'] = 'Karen_Smith'
        self.Karen_Smith.relations['grandmother'] = 'Leah_White'
        ## As she peered through the curtains of her small living room window, she spotted a familiar car making its way down the driveway.
        ## She smiled; her Karen was home.
        ## “Hi, Grandma!” Karen said as she came in through the door.
        ## Leah came out from behind the sofa and hugged her beloved granddaughter warmly.
        ## “Karen…you are so pretty!
        ## What happened to that little thing who used to play Barbies with me?
        ## And what are you doing with all those bags?
        ## You’re going on a trip?”  Karen sat down and began pulling items out of the bags while answering her grandmother’s questions.
        ## “Yeah, it’s too much trouble to take all my textbooks to school; I get there too early anyhow.
        ## So I decided to buy them online this semester.
        ## And I was just about to walk into Wal-Mart for a few things for Mom—she asked me last night—when Dad called me and told me he wanted me to pick up some things at Sam’s club today instead of going there today.

