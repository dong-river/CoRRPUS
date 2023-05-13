## Olivia Dupree's cheeks were stained with tears as she approached the boarding area for the plane to New York.
## Her arms were wrapped around her guardian's waist, and she was clutching her new backpack to her chest.
## She was only four years old, but she had never been away from home before and didn't know why she had to go on this trip.
## "I don't want to go," Olivia whimpered, looking up at her mother's face.
## Amanda knelt down on one knee and embraced her daughter in a tight hug.
## "Olivia, you have to go.
## Your Aunt Payton is very busy and can't take care of you right now," Amanda said softly.
## "I know you're going to like New York."
## Olivia released a loud sob and buried her face in Amanda's shoulder.
## "It'll be okay," Amanda promised her daughter again.
## "You'll stay with your aunt for a few days, get some rest, eat good food-the works!
## I bet it'll be really fun."
## Olivia looked at Amanda and wiped a tear away from the corner of her eye with the back of her hand.
## "Are you coming back?"
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
        self.Payton_Dupree = character('Payton Dupree')
        self.Amanda_Dupree = character('Amanda Dupree')
        self.Olivia_Dupree = character('Olivia Dupree')

    def story(self):
        ## Olivia Dupree's cheeks were stained with tears as she approached the boarding area for the plane to New York.
        self.Olivia_Dupree.appearance.append('tears')
        self.Olivia_Dupree.age.append('four')
        ## Her arms were wrapped around her guardian's waist, and she was clutching her new backpack to her chest.
        self.Olivia_Dupree.relations['guardian'] = 'Amanda_Dupree'
        self.Amanda_Dupree.relations['daughter'] = 'Olivia_Dupree'
        ## She was only four years old, but she had never been away from home before and didn't know why she had to go on this trip.
        self.Olivia_Dupree.age.append('four')
        ## "I don't want to go," Olivia whimpered, looking up at her mother's face.
        self.Olivia_Dupree.relations['mother'] = 'Amanda_Dupree'
        self.Amanda_Dupree.relations['daughter'] = 'Olivia_Dupree'
        ## Amanda knelt down on one knee and embraced her daughter in a tight hug.
        self.Amanda_Dupree.relations['daughter'] = 'Olivia_Dupree'
        self.Olivia_Dupree.relations['mother'] = 'Amanda_Dupree'
        ## "Olivia, you have to go.
        ## Your Aunt Payton is very busy and can't take care of you right now," Amanda said softly.
        self.Olivia_Dupree.relations['aunt'] = 'Payton_Dupree'
        self.Payton_Dupree.relations['niece'] = 'Olivia_Dupree'
        ## "I know you're going to like New York."
        ## Olivia released a loud sob and buried her face in Amanda's shoulder.
        ## "It'll be okay," Amanda promised her daughter again.
        ## "You'll stay with your aunt for a few days, get some rest, eat good food-the works!
        ## I bet it'll be really fun."
        ## Olivia looked at Amanda and wiped a tear away from the corner of her eye with the back of her hand.
        ## "Are you coming back?"

