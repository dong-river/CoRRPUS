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
        self.set_occupation(self.Harold_Martinez, "gas station clerk")
        ## He works every night, from 10pm to 7am.
        ## He is a middle-aged Hispanic man with dark brown hair, dark eyes, and a medium build.
        self.set_appearance(self.Harold_Martinez, "middle-aged Hispanic man")
        self.set_appearance(self.Harold_Martinez, "dark brown hair")
        self.set_appearance(self.Harold_Martinez, "dark eyes")
        self.set_appearance(self.Harold_Martinez, "medium build")
        ## Tonight was supposed to be a quiet night shift, with few customers visiting the gas station.
        ## The shift started on time at 10pm and there were no customers during the first hour.
        ## Then at around 11:45pm, there was a customer who walked into the gas station with bags under his eyes.
        ## He seemed to be disheveled and his hair was messy.
        ## His clothes were dirty and he looked like he hadn’t shaved in days.
        self.set_appearance(self.David_Garcia, "bags under his eyes")
        self.set_appearance(self.David_Garcia, "disheveled")
        self.set_appearance(self.David_Garcia, "messy hair")
        self.set_appearance(self.David_Garcia, "dirty clothes")
        self.set_appearance(self.David_Garcia, "unshaven")
        ## As he looked at Harold, his eyes seem ed like they haven’t seen the light of day for weeks; they look dead somehow.
        ## When he walked up to Harold and said "give me all your money," it took a moment for Harold to process what the man said because the voice that came out was not the one he expected to hear.
        ## Instead of hearing an angry or aggressive voice, what came out of this man's mouth is monotone and flat like there's no emotion behind it.
        self.set_appearance(self.David_Garcia, "dead eyes")
        ## "I'm sorry," Harold said immediately after processing what happened.
        ## "I'm not joking around!
        
## The story is set in the present day and takes place in the United States.
## The story is about a young girl named Emily who lives with her parents.
## Emily is a happy and outgoing girl.
## She has many friends and enjoys spending time with them.
## Emily's parents are kind and loving people who care deeply for their daughter.
## They try to do whatever they can to make Emily happy.
## Emily's parents are always busy working, so they don't have much time to spend with their daughter.
## Emily's parents are worried about their daughter because she has been acting strangely lately.
## They are worried that something might be wrong with her.
## Emily's parents have noticed that she has been spending less time with her friends and more time alone in her room.
## They are concerned about this change in behavior.
## Emily's parents decide to talk to her about what is going on.
## Emily's parents ask her if everything is alright, but she doesn't answer.
## Emily's parents ask her if she is feeling sick or if there is something bothering her.
## Emily's parents ask her if there is anything they can do to help her.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents ask her if there is anything they can do to help her.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents ask her if there is anything they can do to help her.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily's parents tell her that they will always be there for her no matter what happens.
## Emily's parents tell her that they are worried about her and want to make sure she is ok.
## Emily's parents tell her that they love her very much and want to help her if she needs it.
## Emily