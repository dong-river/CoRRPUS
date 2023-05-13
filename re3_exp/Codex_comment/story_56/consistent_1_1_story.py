## Leah White stood in front of the mirror, slipping on her long black leather jacket.
## “Karen, are you ready?” she asked to her best friend.
## “Almost,” Karen replied from inside the bathroom.
## “I just have to run down and feed the cat, then I’ll be done.”  Leah glanced at her watch, then turned around.
## She was ready to leave in fifteen minutes.
## She began to fidget as she waited for Karen.
## Leah was impatiently waiting for Karen because they were running late for their job as waitresses at a local diner called Coco Bells that had been a regular haunt of theirs for many years.
## They usually only worked part-time at the diner during college because they already worked full-time at an advertising firm where they sold bumper stickers, flags, and other small items that promised “I support our troops!” and other mantras of political propaganda and BS like that.
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
        ## Leah White stood in front of the mirror, slipping on her long black leather jacket.
        self.Leah_White.appearance.append('long black leather jacket')
        ## “Karen, are you ready?” she asked to her best friend.
        self.Karen_Smith.relations['best friend'] = 'Leah_White'
        ## “Almost,” Karen replied from inside the bathroom.
        ## “I just have to run down and feed the cat, then I’ll be done.”  Leah glanced at her watch, then turned around.
        ## She was ready to leave in fifteen minutes.
        ## She began to fidget as she waited for Karen.
        ## Leah was impatiently waiting for Karen because they were running late for their job as waitresses at a local diner called Coco Bells that had been a regular haunt of theirs for many years.
        ## They usually only worked part-time at the diner during college because they already worked full-time at an advertising firm where they sold bumper stickers, flags, and other small items that promised “I support our troops!” and other mantras of political propaganda and BS like that.

