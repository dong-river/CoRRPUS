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
        self.set_age(self.Emily_Hellinger, "middle aged")
        ## She lay in bed and stretched, noting that the clock was 5:30.
        ## Emily turned off the alarm and stood, rubbing her eyes.
        ## The tall blonde woman looked over at the sleeping form of her wife Sherry, who was lying on her side.
        self.set_gender(self.Sherry_Hellinger, "female")
        self.set_relation(self.Emily_Hellinger, 'wife', self.Sherry_Hellinger)
        self.set_relation(self.Sherry_Hellinger, 'wife', self.Emily_Hellinger)
        ## Emily knelt down beside the bed and gazed upon Sherry's sleeping face.
        ## She smiled lightly and then placed a soft kiss on Sherry's forehead.
        ## Emily rose from the bed and went into the bathroom.
        ## She closed the door behind her and stood in front of the mirror above the sink, turning on a light switch.
        ## She looked at herself in the mirror and could hardly believe how young she looked for 44 years old.
        self.set_age(self.Emily_Hellinger, "44 years old")
        ## Her once long blonde hair had been cut short for years now, but it still framed her oval face well without giving off an aged appearance like some older women with shorter hair tend to have.
        self.set_appearance(self.Emily_Hellinger, "blonde hair")
        ## Her blue eyes were as vivid as ever, though they were frequently hidden by dark sunglasses that hid bags under them from lack of sleep or stress related issues with work or family matters--it all depended on who you asked about it.
        self.set_appearance(self.Emily_Hellinger, "blue eyes")
        self.set_appearance(self.Emily_Hellinger, "dark sunglasses")
        ## Emily turned on the shower and stepped in.
        ## She washed her hair and body, and then rinsed off.
        ## Emily turned off the water and stepped out of the shower, wrapping a towel around her body.
        ## She dried off and then went back into the bedroom, where she dressed in her work clothes.
        ## Emily put on a white button down shirt, a black tie, and a black blazer.
        ## She looked at herself in the mirror, noting how professional she appeared.
        ## Emily went downstairs to the kitchen and saw her wife Sherry making breakfast.
        self.set_occupation(self.Sherry_Hellinger, "cook")
        ## Sherry smiled at her and said, "Good morning, Emily. I made you some eggs and bacon."
        ## Emily smiled back at her and said, "Thank you, Sherry."
        ## Emily sat down at the table and ate her breakfast.
        ## When she finished, she kissed Sherry on the cheek and said, "I'll see you later, dear."
        ## Emily left for work, driving to the office building where she worked as an accountant.
        self.set_occupation(self.Emily_Hellinger, "accountant")
        ## She parked her car and went inside, riding the elevator up to her floor.
        ## Emily walked down the hallway and went into her office, sitting down at her desk.
        ## She turned on her computer and began working on the day's tasks.
        ## Emily worked for several hours, stopping only to eat lunch.
        ## She finished her work and then went home, where she found her wife Sherry cooking dinner.
        self.set_occupation(self.Sherry_Hellinger, "cook")
        ## Emily smiled and said, "It smells delicious, Sherry."
        ## Sherry smiled back at her and said, "Thank you, Emily. I hope you like it."
        ## Emily and Sherry ate dinner together, and then went to bed.
        ## The next morning, Emily awoke to her alarm clock.
        ## She turned it off and stood, stretching.
        ## Emily looked over at the sleeping form of her wife Sherry, who was lying on her side.
        ## Emily knelt down beside the bed and gazed upon Sherry's sleeping face.
        ## She smiled lightly and then placed a soft kiss on Sherry's forehead.
        ## Emily rose from the bed and went into the bathroom.
        ## She closed the door behind her and stood in front of the mirror above the sink, turning on a light switch.
        ## She looked at herself in the mirror and could hardly believe how young she looked for 44 years old.
        ## Her once long blonde hair had been cut short for years now, but it still framed her oval face well without giving off an aged appearance like some older women with shorter hair tend to have.
        ## Her blue eyes were as vivid as ever, though they were frequently hidden by dark sunglasses that hid bags under them from lack of sleep or stress related issues with work or family matters--it all depended on who you asked about it.
        ## Emily turned on the shower and stepped in.
        ## She washed her hair and body, and then rinsed off.
        ## Emily turned off the water and stepped out of the shower, wrapping a towel around her body.
        ## She dried off and then went back into the bedroom, where she dressed in her work clothes.
        ## Emily put on a white button down shirt, a black tie, and a black blazer.
        ## She looked at herself in the mirror, noting how professional she appeared.
        ## Emily went downstairs to the kitchen and saw her wife Sherry making breakfast.
        ## Sherry smiled at her and said, "Good morning, Emily. I made you some eggs and bacon."
        ## Emily smiled back at her and said, "Thank you, Sherry."
        ## Emily sat down at the table and ate her breakfast.
        ## When she finished, she kissed Sherry on the cheek and said, "I'll see you later, dear."
        ## Emily left for work, driving to the office building where she worked as an accountant.
        ## She parked her car and went inside, riding the elevator up to her floor.
        ## Emily walked down the hallway and went into her office, sitting down at her desk.
        ## She turned on her computer and began working on the day's tasks.
        ## Emily worked for several hours, stopping only to eat lunch.
        ## She finished her work and then went home, where she found her wife Sherry cooking dinner.
        ## Emily smiled and said, "It smells delicious, Sherry."
        ## Sherry smiled back at her and said, "Thank you, Emily. I hope you like it."
        ## Emily and Sherry ate dinner together, and then went to bed.
        ## The next morning, Emily awoke to her alarm clock.
        ## She turned it off and stood, stretching.
        ## Emily looked over at the sleeping form of her wife Sherry, who was lying on her side.
        ## Emily knelt down beside the bed and gazed upon Sherry's sleeping face.
        ## She smiled lightly and then placed a soft kiss on Sherry's forehead.
        ## Emily rose from the bed and went into the bathroom.
        ## She closed the door behind her and stood in front of the mirror above the sink, turning on a light switch.
        ## She looked at herself in the mirror and could hardly believe how young she looked for 44 years old.
        ## Her once long blonde hair had been cut short for years now, but it still framed her oval face well without giving off an aged appearance like some older women with shorter hair tend to have.
        ## Her blue eyes were as vivid as ever, though they were frequently hidden by dark sunglasses that hid bags under them from lack of sleep or stress related issues with work or family matters--it all depended on who you asked about it.
        ## Emily turned on the shower and stepped in.
        ## She washed her hair and body, and then rinsed off.
        ## Emily turned off the water and stepped out of the shower, wrapping a towel around her body.
        ## She dried off and then went back into the bedroom, where she dressed in her work clothes.
        ## Emily put on a white button down shirt, a black tie, and a black blazer.
        ## She looked at herself in the mirror, noting how professional she appeared.
        ## Emily went downstairs to the kitchen and saw her wife Sherry making breakfast.
        ## Sherry smiled at her and said, "Good morning, Emily. I made you some eggs and bacon."
        ## Emily smiled back at her and said, "Thank you, Sherry."
        ## Emily sat down at the table and ate her breakfast.
        ## When she finished, she kissed Sherry on the cheek and said, "I'll see you later, dear."
        ## Emily left for work, driving to the office building where she worked as an accountant.
        ## She parked her car and went inside, riding the elevator up to her floor.
        ## Emily walked down the hallway and went into her office, sitting down at her desk.
        ## She turned on her computer and began working on the day's tasks.
        ## Emily worked for several hours, stopping only to eat lunch.
        ## She finished her work and then went home, where she found her wife Sherry cooking dinner.
        ## Emily smiled and said, "It smells delicious, Sherry."
        ## Sherry smiled back at her and said, "Thank you, Emily. I hope you like it."
        ## Emily and Sherry ate dinner together, and then went to bed.
        ## The next morning, Emily awoke to her alarm clock.
        ## She turned it off and stood, stretching.
        ## Emily looked over at the sleeping form of her wife Sherry, who was lying on her side.
        ## Emily knelt down beside the bed and gazed upon Sherry's sleeping face.
        ## She smiled lightly and then placed a soft kiss on Sherry's forehead.
        ## Emily rose from the bed and went into the bathroom.
        ## She closed the door behind her and stood in front of the mirror above the sink, turning on a light switch.
        ## She looked at herself in the mirror and could hardly believe how young she looked for 44 years old.
        ## Her once long blonde hair had been cut short for years now, but it still framed her oval face well without giving off an aged appearance like some older women with shorter hair tend to have.
        ## Her blue eyes were as vivid as ever, though they were frequently hidden by dark sunglasses that hid bags under them from lack of sleep or stress related issues with work or family matters--it all depended on who you asked about it.
        ## Emily turned on the shower and stepped in.
        ## She washed her hair and body, and then rinsed off.
        ## Emily turned off the water and stepped out of the shower, wrapping a towel around her body.
        ## She dried off and then went back into the bedroom, where she dressed in her work clothes.
        ## Emily put on a white button down shirt, a black tie, and a black blazer.
        ## She looked at herself in the mirror, noting how professional she appeared.
        ##