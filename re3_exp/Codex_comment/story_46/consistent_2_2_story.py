## Tina Sanchez sat in her dressing room at Model City.
## She had just changed into her new dress and looked at herself in the mirror.
## It was a bright, sunny morning and her stylist, Rachel Cunningham, stood next to her, brushing out Tina’s long black hair.
## “You’re such a beautiful girl, Tina!
## I can’t believe you haven’t been chosen to be in any magazines yet!
## I saw some of the girls who were selected for our next runway show.
## Your co-workers are going to be so jealous!
## You’re definitely one of the most beautiful women here.
## Do you want me to put your hair up or leave it down?”  Tina thought for a moment before responding.
## “Well, since we are doing a fashion show on the beach, I think my hair should be down so that it looks like I just came out of the ocean.
## What do you think?”  Rachel smiled as she finished brushing out Tina’s hair and started putting bobby pins in it.
## “I think that sounds perfect!
## Here you go!
## Wow...you look amazing!
## The cameramen are going to love you today!
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
        self.Jessica_Campbell = character('Jessica Campbell')
        self.John_Smith = character('John Smith')
        self.Tina_Sanchez = character('Tina Sanchez')

    def story(self):
        ## Tina Sanchez sat in her dressing room at Model City.
        self.Tina_Sanchez.occupation.append('model')
        ## She had just changed into her new dress and looked at herself in the mirror.
        ## It was a bright, sunny morning and her stylist, Rachel Cunningham, stood next to her, brushing out Tina’s long black hair.
        ## “You’re such a beautiful girl, Tina!
        ## I can’t believe you haven’t been chosen to be in any magazines yet!
        ## I saw some of the girls who were selected for our next runway show.
        ## Your co-workers are going to be so jealous!
        ## You’re definitely one of the most beautiful women here.
        ## Do you want me to put your hair up or leave it down?”  Tina thought for a moment before responding.
        ## “Well, since we are doing a fashion show on the beach, I think my hair should be down so that it looks like I just came out of the ocean.
        ## What do you think?”  Rachel smiled as she finished brushing out Tina’s hair and started putting bobby pins in it.
        ## “I think that sounds perfect!
        ## Here you go!
        ## Wow...you look amazing!
        ## The cameramen are going to love you today!

