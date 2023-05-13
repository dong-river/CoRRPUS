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
        ## Harold Martinez works at the gas station as a clerk.
        ## He works every night, from 10pm to 7am.
        self.set_occupation(self.Harold_Martinez, "clerk")
        ## He is a middle-aged Hispanic man with dark brown hair, dark eyes, and a medium build.
        self.set_appearance(self.Harold_Martinez, "dark brown hair")
        self.set_appearance(self.Harold_Martinez, "dark eyes")
        self.set_appearance(self.Harold_Martinez, "medium build")
        self.set_age(self.Harold_Martinez, "middle-aged")
        self.set_gender(self.Harold_Martinez, "male")
        ## Tonight was supposed to be a quiet night shift, with few customers visiting the gas station.
        ## The shift started on time at 10pm and there were no customers during the first hour.
        ## Then at around 11:45pm, there was a customer who walked into the gas station with bags under his eyes.
        self.David_Garcia = character('David Garcia')
        ## He seemed to be disheveled and his hair was messy.
        self.set_appearance(self.David_Garcia, "disheveled")
        self.set_appearance(self.David_Garcia, "messy hair")
        ## His clothes were dirty and he looked like he hadn’t shaved in days.
        self.set_appearance(self.David_Garcia, "dirty clothes")
        self.set_appearance(self.David_Garcia, "unshaven")
        ## As he looked at Harold, his eyes seem ed like they haven’t seen the light of day for weeks; they look dead somehow.
        ## When he walked up to Harold and said "give me all your money," it took a moment for Harold to process what the man said because the voice that came out was not the one he expected to hear.
        ## Instead of hearing an angry or aggressive voice, what came out of this man's mouth is monotone and flat like there's no emotion behind it.
        ## "I'm sorry," Harold said immediately after processing what happened.
        ## "I'm not joking around!
## The story is set in the present day and takes place in the United States.
## Joan Westfall is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind.
## Brent Westfall is Joan's husband. He is a kind and loving man who is struggling to cope with his wife's death.
## Jason Westfall is Joan's son. He is a young boy who is struggling to understand his mother's death.
## Jason Westfall sits on the floor, looking at the empty box that used to hold his sister-in-law's belongings. 
## His gaze is unfocused. his dark blue eyes brimming with tears.
## He cries for hours, eventually falling asleep from exhaustion.
## When he wakes up, he feels dazed and ill.
## Joan died in a car accident on a rainy day several weeks ago.
## Jason has been carrying on with life ever since as best he can manage, but he still doesn't really know how to cope with Joan's death.
## Create a world model state to track each character's appearance, personality, and relations with other characters.

