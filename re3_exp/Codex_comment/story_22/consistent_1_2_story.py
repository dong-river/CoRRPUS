## Harold Martinez works at the gas station as a clerk.
## He works every night, from 10pm to 7am.
## He is a middle-aged Hispanic man with dark brown hair, dark eyes, and a medium build.
## Tonight was supposed to be a quiet night shift, with few customers visiting the gas station.
## The shift started on time at 10pm and there were no customers during the first hour.
## Then at around 11:45pm, there was a customer who walked into the gas station with bags under his eyes.
## He seemed to be disheveled and his hair was messy.
## His clothes were dirty and he looked like he hadn’t shaved in days.
## As he looked at Harold, his eyes seem ed like they haven’t seen the light of day for weeks; they look dead somehow.
## When he walked up to Harold and said "give me all your money," it took a moment for Harold to process what the man said because the voice that came out was not the one he expected to hear.
## Instead of hearing an angry or aggressive voice, what came out of this man's mouth is monotone and flat like there's no emotion behind it.
## "I'm sorry," Harold said immediately after processing what happened.
## "I'm not joking around!
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
        self.Harold_Martinez = character('Harold Martinez')
        self.David_Garcia = character('David Garcia')

    def story(self):
        ## Harold Martinez works at the gas station as a clerk.
        self.Harold_Martinez.occupation.append('clerk')
        ## He works every night, from 10pm to 7am.
        self.Harold_Martinez.occupation.append('10pm to 7am')
        ## He is a middle-aged Hispanic man with dark brown hair, dark eyes, and a medium build.
        self.Harold_Martinez.appearance.append('dark brown hair')
        self.Harold_Martinez.appearance.append('dark eyes')
        self.Harold_Martinez.appearance.append('medium build')
        self.Harold_Martinez.age.append('middle-aged')
        ## Tonight was supposed to be a quiet night shift, with few customers visiting the gas station.
        ## The shift started on time at 10pm and there were no customers during the first hour.
        ## Then at around 11:45pm, there was a customer who walked into the gas station with bags under his eyes.
        ## He seemed to be disheveled and his hair was messy.
        ## His clothes were dirty and he looked like he hadn’t shaved in days.
        ## As he looked at Harold, his eyes seem ed like they haven’t seen the light of day for weeks; they look dead somehow.
        ## When he walked up to Harold and said "give me all your money," it took a moment for Harold to process what the man said because the voice that came out was not the one he expected to hear.
        ## Instead of hearing an angry or aggressive voice, what came out of this man's mouth is monotone and flat like there's no emotion behind it.
        self.David_Garcia.appearance.append('bags under his eyes')
        self.David_Garcia.appearance.append('disheveled')
        self.David_Garcia.appearance.append('messy hair')
        self.David_Garcia.appearance.append('dirty clothes')
        self.David_Garcia.appearance.append('unshaved')
        self.David_Garcia.appearance.append('dead eyes')
        ## "I'm sorry," Harold said immediately after processing what happened.
        ## "I'm not joking around!
        self.David_Garcia.appearance.append('monotone and flat voice')

