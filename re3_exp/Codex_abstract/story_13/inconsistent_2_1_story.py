## Emily Hellinger awoke to her alarm clock on a warm morning in late summer.
## She lay in bed and stretched, noting that the clock was 5:30.
## Emily turned off the alarm and stood, rubbing her eyes.
## The tall blonde woman looked over at the sleeping form of her wife Sherry, who was lying on her side.
## Emily knelt down beside the bed and gazed upon Sherry's sleeping face.
## She smiled lightly and then placed a soft kiss on Sherry's forehead.
## Emily rose from the bed and went into the bathroom.
## She closed the door behind her and stood in front of the mirror above the sink, turning on a light switch.
## She looked at herself in the mirror and could hardly believe how young she looked for 44 years old.
## Her once long blonde hair had been cut short for years now, but it still framed her oval face well without giving off an aged appearance like some older women with shorter hair tend to have.
## Her blue eyes were as vivid as ever, though they were frequently hidden by dark sunglasses that hid bags under them from lack of sleep or stress related issues with work or family matters--it all depended on who you asked about it.

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
        self.Sherry_Hellinger = character('Sherry Hellinger')
        self.Emily_Hellinger = character('Emily Hellinger')
        self.John_Hellinger = character('John Hellinger')

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
        ## Emily Hellinger awoke to her alarm clock on a warm morning in late summer.
        self.set_gender(self.Emily_Hellinger, "female")
        ## She lay in bed and stretched, noting that the clock was 5:30.
        ## Emily turned off the alarm and stood, rubbing her eyes.
        ## The tall blonde woman looked over at the sleeping form of her wife Sherry, who was lying on her side.
        self.set_relation(self.Emily_Hellinger, 'wife', self.Sherry_Hellinger)
        self.set_relation(self.Sherry_Hellinger, 'wife', self.Emily_Hellinger)
        self.set_gender(self.Sherry_Hellinger, "female")
        ## Emily knelt down beside the bed and gazed upon Sherry's sleeping face.
        ## She smiled lightly and then placed a soft kiss on Sherry's forehead.
        ## Emily rose from the bed and went into the bathroom.
        ## She closed the door behind her and stood in front of the mirror above the sink, turning on a light switch.
        ## She looked at herself in the mirror and could hardly believe how young she looked for 44 years old.
        self.set_age(self.Emily_Hellinger, "44 years old")
        ## Her once long blonde hair had been cut short for years now, but it still framed her oval face well without giving off an aged appearance like some older women with shorter hair tend to have.
        self.set_appearance(self.Emily_Hellinger, "once long blonde hair")
        ## Her blue eyes were as vivid as ever, though they were frequently hidden by dark sunglasses that hid bags under them from lack of sleep or stress related issues with work or family matters--it all depended on who you asked about it.
        self.set_appearance(self.Emily_Hellinger, "blue eyes")
