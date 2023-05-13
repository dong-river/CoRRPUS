## Olivia Fria Spierings watched out of the window as the station slid by, then she looked at her reflection in the window.
## It had been three days since she had last seen it, and it looked all right.
## She was of average height and build with brown hair and eyes, but her body was different from that of most 15-year-olds, or so she had been told.
## She didn't see any difference between herself and the other girls in her class, but many of them already developed breasts, wore bras, and started to wear makeup.
## Maybe she would be like that soon.
## Then again it might not happen for years to come.
## She could have been one of those girls who would have to endure having flat chests for a long time yet.
## What did it matter though?
## Who wanted to go around being embarrassed?
## No one.
## She wouldn't give anyone the chance anyway by wearing a bra or dressing like a girl who couldn't be bothered with boys because they were too young or immature yet!
## She liked clothes that didn't come across as feminine in any way; jackets with hoods and sweatshirts without images on them were ideal.
## Her favorite color wasn't pink either, but black.
## Her boyfriend's pants even had an image on them in black!

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
        self.Olivia_Fria_Spierings = character('Olivia Fria Spierings')
        self.Colonel_Damien_Riggs = character('Colonel Damien Riggs')

    def set_appearance(self, character, appearance):
        character.appearance.append(appearance)
    
    def set_occupation(self, character, occupation):
        character.occupation.append(occupation)
    
    def set_gender(self, character, gender):
        character.gender.append(gender)
    
    def set_age(self, character, age):
        character.age.append(age)
    
    def set_relation(self, character, relation, other_character):
        character.relations[relation] = other_character.name
        
    def story(self):
        ## Olivia Fria Spierings watched out of the window as the station slid by, then she looked at her reflection in the window.
        ## It had been three days since she had last seen it, and it looked all right.
        ## She was of average height and build with brown hair and eyes, but her body was different from that of most 15-year-olds, or so she had been told.
        self.set_gender(self.Olivia_Fria_Spierings, "female")
        self.set_age(self.Olivia_Fria_Spierings, "15")
        self.set_appearance(self.Olivia_Fria_Spierings, "average height and build")
        self.set_appearance(self.Olivia_Fria_Spierings, "brown hair and eyes")
        ## She didn't see any difference between herself and the other girls in her class, but many of them already developed breasts, wore bras, and started to wear makeup.
        self.set_appearance(self.Olivia_Fria_Spierings, "breasts")
        ## Maybe she would be like that soon.
        ## Then again it might not happen for years to come.
        ## She could have been one of those girls who would have to endure having flat chests for a long time yet.
        self.set_appearance(self.Olivia_Fria_Spierings, "flat chests")
        ## What did it matter though?
        ## Who wanted to go around being embarrassed?
        ## No one.
        ## She wouldn't give anyone the chance anyway by wearing a bra or dressing like a girl who couldn't be bothered with boys because they were too young or immature yet!
        self.set_appearance(self.Olivia_Fria_Spierings, "bra")
        ## She liked clothes that didn't come across as feminine in any way; jackets with hoods and sweatshirts without images on them were ideal.
        self.set_appearance(self.Olivia_Fria_Spierings, "jackets with hoods and sweatshirts without images")
        ## Her favorite color wasn't pink either, but black.
        self.set_appearance(self.Olivia_Fria_Spierings, "black")
        ## Her boyfriend's pants even had an image on them in black!
        self.set_relation(self.Olivia_Fria_Spierings, 'boyfriend', self.Colonel_Damien_Riggs)
        self.set_relation(self.Colonel_Damien_Riggs, 'girlfriend', self.Olivia_Fria_Spierings)
        self.set_appearance(self.Colonel_Damien_Riggs, "black pants")
