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

    def story(self):
        ## Olivia Fria Spierings was marching down the hallway when Colonel Damien Riggs's aide called her into his office.
        self.Olivia_Fria_Spierings.gender.append('female')
        self.Colonel_Damien_Riggs.relations['aide'] = 'Olivia_Fria_Spierings'
        ## She knew what was coming.
        ## She was short and skinny with long dark hair, blue eyes, and a pretty face.
        self.Olivia_Fria_Spierings.appearance.append("short")
        self.Olivia_Fria_Spierings.appearance.append("skinny")
        self.Olivia_Fria_Spierings.appearance.append("long dark hair")
        self.Olivia_Fria_Spierings.appearance.append("blue eyes")
        self.Olivia_Fria_Spierings.appearance.append("pretty face")
        ## She wanted to join the army because it looked like an exciting career to her and she wanted a new challenge in life.
        self.Olivia_Fria_Spierings.occupation.append("army")
        ## But the army wasn't very interested in people who looked like Olivia Fria Spierings.
        ## So they made her a supply clerk, which was basically a glorified file clerk.
        self.Olivia_Fria_Spierings.occupation.append("supply clerk")
        ## It wasn't exactly challenging work and she spent most of her time indoors at a desk behind piles of paperwork instead of out on the battlefield as she had hoped when she joined up seven years ago at age 18.
        self.Olivia_Fria_Spierings.age.append("18")
        ## Colonel Damien Riggs watched Olivia through half-closed eyes as she entered his office.
        ## This girl made him uncomfortable for some reason, and he wasn't quite sure why.
        self.Colonel_Damien_Riggs.relations['Olivia'] = 'Olivia_Fria_Spierings'
        ## He didn't like pretty young girls with long dark hair and blue eyes whose slender arms were covered in tattoos from their fingertips all the way up to their shoulders including one with bird wings wrapped around them from shoulder to shoulder that he found particularly interesting (though he couldn't explain why).
        self.Olivia_Fria_Spierings.appearance.append("long dark hair")
        self.Olivia_Fria_Spierings.appearance.append("blue eyes")
        self.Olivia_Fria_Spierings.appearance.append("covered in tattoos")
        self.Olivia_Fria_Spierings.appearance.append("bird wings wrapped around them from shoulder to shoulder")

