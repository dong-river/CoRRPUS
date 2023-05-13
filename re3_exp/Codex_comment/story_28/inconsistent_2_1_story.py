## Olivia Dupree is now 5 years old.
## Her mother Amanda died suddenly five years ago, and she was left in the care of her godmother Payton.
## "Hiya, Livie!"
## Payton calls from the hallway of her apartment.
## "Is your homework done?"
## "I'm playing a game," Olivia yells back to her.
## "Come on in!"
## Payton smiles and enters the living room.
## Olivia is sitting cross-legged on the floor with an iPad propped up on a pillow.
## She grins up at Payton and waves.
## "Hello!"
## she says cheerfully.
## "What have you been doing today?"
## "Not much," Payton says, bending down to hug Olivia and steal a kiss on her cheek.
## She sits down beside her niece and kisses her forehead tenderly before ruffling her hair.
## "I had a lot of work to do at the office today."
## "I want to go there sometime," Olivia tells her seriously, putting down the iPad and reaching for a toy purse instead.
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
        ## Olivia Dupree is now 5 years old.
        self.Olivia_Dupree.age.append('5 years old')
        ## Her mother Amanda died suddenly five years ago, and she was left in the care of her godmother Payton.
        self.Olivia_Dupree.relations['mother'] = 'Amanda_Dupree'
        self.Amanda_Dupree.relations['daughter'] = 'Olivia_Dupree'
        self.Olivia_Dupree.relations['godmother'] = 'Payton_Dupree'
        self.Payton_Dupree.relations['godchild'] = 'Olivia_Dupree'
        ## "Hiya, Livie!"
        ## Payton calls from the hallway of her apartment.
        ## "Is your homework done?"
        ## "I'm playing a game," Olivia yells back to her.
        ## "Come on in!"
        ## Payton smiles and enters the living room.
        ## Olivia is sitting cross-legged on the floor with an iPad propped up on a pillow.
        ## She grins up at Payton and waves.
        ## "Hello!"
        ## she says cheerfully.
        ## "What have you been doing today?"
        ## "Not much," Payton says, bending down to hug Olivia and steal a kiss on her cheek.
        ## She sits down beside her niece and kisses her forehead tenderly before ruffling her hair.
        ## "I had a lot of work to do at the office today."
        ## "I want to go there sometime," Olivia tells her seriously, putting down the iPad and reaching for a toy purse instead.

