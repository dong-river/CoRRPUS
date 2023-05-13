## Shannon Mulaney walked into her dorm room and flopped down on her bed.
## She had just gotten off the phone with her mom and they'd argued again.
## The bad grades she'd been getting all semester were affecting her softball scholarship, so Shannon knew that her mom was upset.
## They hadn't spoken in two weeks, though, and Shannon still felt hurt by the fight they'd had before she left Michigan.
## Her whole life she had felt like the odd one out in the family, with both of her sisters being more popular than she was, and now it seemed that her mom was starting to see it too.
## As she lay there waiting for Olivia to come back from class, Shannon closed her eyes and fell asleep.
## "So when did your mom get cancer?"
## Jess asked as she set down a few books on top of some envelopes that were stacked on the small desk across from Shannon's bed.
## "She didn't," Shannon answered without looking up from the book open in front of her.
## "What do you mean?
## She's been sick for a year."
## Jess sounded confused.
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
        self.Shannon_Mulaney = character('Shannon Mulaney')
        self.Jess_Abernathy = character('Jess Abernathy')
        self.Olivia_Kendall = character('Olivia Kendall')

    def story(self):
        ## Shannon Mulaney walked into her dorm room and flopped down on her bed.
        self.Shannon_Mulaney.relations['dorm'] = 'dorm room'
        ## She had just gotten off the phone with her mom and they'd argued again.
        self.Shannon_Mulaney.relations['mom'] = 'mom'
        self.Shannon_Mulaney.relations['dad'] = 'dad'
        self.Shannon_Mulaney.relations['sisters'] = 'sisters'
        ## The bad grades she'd been getting all semester were affecting her softball scholarship, so Shannon knew that her mom was upset.
        ## They hadn't spoken in two weeks, though, and Shannon still felt hurt by the fight they'd had before she left Michigan.
        ## Her whole life she had felt like the odd one out in the family, with both of her sisters being more popular than she was, and now it seemed that her mom was starting to see it too.
        ## As she lay there waiting for Olivia to come back from class, Shannon closed her eyes and fell asleep.
        ## "So when did your mom get cancer?"
        ## Jess asked as she set down a few books on top of some envelopes that were stacked on the small desk across from Shannon's bed.
        ## "She didn't," Shannon answered without looking up from the book open in front of her.
        ## "What do you mean?
        ## She's been sick for a year."
        ## Jess sounded confused.

## The story is set in the near future and takes place in an unspecified location in the United States.
## Anna is a woman who has recently lost her job. She is a kind and sympathetic person who is eager to help the people she left behind.
## John is Anna's husband. He is a kind and loving man who is struggling to cope with his wife's death.
## Create a world model state to track each character's appearance, personality, and relations with other characters.

