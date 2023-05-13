## Olivia Fria Spierings was marching down the hallway when Colonel Damien Riggs's aide called her into his office.
## She knew what was coming.
## She was short and skinny with long dark hair, blue eyes, and a pretty face.
## She wanted to join the army because it looked like an exciting career to her and she wanted a new challenge in life.
## But the army wasn't very interested in people who looked like Olivia Fria Spierings.
## So they made her a supply clerk, which was basically a glorified file clerk.
## It wasn't exactly challenging work and she spent most of her time indoors at a desk behind piles of paperwork instead of out on the battlefield as she had hoped when she joined up seven years ago at age 18.
## Colonel Damien Riggs watched Olivia through half-closed eyes as she entered his office.
## This girl made him uncomfortable for some reason, and he wasn't quite sure why.
## He didn't like pretty young girls with long dark hair and blue eyes whose slender arms were covered in tattoos from their fingertips all the way up to their shoulders including one with bird wings wrapped around them from shoulder to shoulder that he found particularly interesting (though he couldn't explain why).

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
        ## Olivia Fria Spierings was marching down the hallway when Colonel Damien Riggs's aide called her into his office.
        self.set_gender(self.Olivia_Fria_Spierings, "female")
        self.set_relation(self.Olivia_Fria_Spierings, 'colonel', self.Colonel_Damien_Riggs)
        self.set_relation(self.Colonel_Damien_Riggs, 'aide', self.Olivia_Fria_Spierings)
        ## She knew what was coming.
        ## She was short and skinny with long dark hair, blue eyes, and a pretty face.
        self.set_appearance(self.Olivia_Fria_Spierings, "short")
        self.set_appearance(self.Olivia_Fria_Spierings, "skinny")
        self.set_appearance(self.Olivia_Fria_Spierings, "long dark hair")
        self.set_appearance(self.Olivia_Fria_Spierings, "blue eyes")
        self.set_appearance(self.Olivia_Fria_Spierings, "pretty face")
        ## She wanted to join the army because it looked like an exciting career to her and she wanted a new challenge in life.
        self.set_occupation(self.Olivia_Fria_Spierings, "army")
        ## But the army wasn't very interested in people who looked like Olivia Fria Spierings.
        ## So they made her a supply clerk, which was basically a glorified file clerk.
        self.set_occupation(self.Olivia_Fria_Spierings, "supply clerk")
        ## It wasn't exactly challenging work and she spent most of her time indoors at a desk behind piles of paperwork instead of out on the battlefield as she had hoped when she joined up seven years ago at age 18.
        self.set_age(self.Olivia_Fria_Spierings, "18")
        ## Colonel Damien Riggs watched Olivia through half-closed eyes as she entered his office.
        self.set_gender(self.Colonel_Damien_Riggs, "male")
        ## This girl made him uncomfortable for some reason, and he wasn't quite sure why.
        ## He didn't like pretty young girls with long dark hair and blue eyes whose slender arms were covered in tattoos from their fingertips all the way up to their shoulders including one with bird wings wrapped around them from shoulder to shoulder that he found particularly interesting (though he couldn't explain why).
        self.set_appearance(self.Olivia_Fria_Spierings, "pretty young")
        self.set_appearance(self.Olivia_Fria_Spierings, "long dark hair")
        self.set_appearance(self.Olivia_Fria_Spierings, "blue eyes")
        self.set_appearance(self.Olivia_Fria_Spierings, "slender arms")
        self.set_appearance(self.Olivia_Fria_Spierings, "tattoos")
        self.set_appearance(self.Olivia_Fria_Spierings, "bird wings")
 

