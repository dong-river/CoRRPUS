## Emily Hellinger walked into the kitchen in her pajamas, her hazel eyes squinting against the dim light.
## She brushed her long brown hair out of her face as she yawned.
## Looking at the wall clock, she knew it was still early for John to be home.
## Glancing around the house, she noticed that he was nowhere to be found.
## Seeing his keys on the counter, she shrugged and went back to bed.
## She fell asleep quickly after having a late dinner and woke up early in the morning.
## Slipping into some jeans and a sweatshirt, Emily set off to find John.
## The spring air was brisk but warming up nicely as she headed down their street towards downtown Hillside Hills.
## Feeling a tingle of excitement pass through her at seeing so many people up and about in this small town during this quiet time of year, Emily smiled with delight as she scanned the nearly empty street for John's big blue truck.
## It wasn't parked near work or at home; it wasn't even parked near any of their family friends' houses where he might be visiting them on this gray morning while they were eating breakfast or watering their plants or other mundane tasks that people did on a Saturday morning before 9 am.

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
        ## Emily Hellinger walked into the kitchen in her pajamas, her hazel eyes squinting against the dim light.
        self.set_gender(self.Emily_Hellinger, "female")
        self.set_age(self.Emily_Hellinger, "young")
        self.set_appearance(self.Emily_Hellinger, "hazel eyes")
        ## She brushed her long brown hair out of her face as she yawned.
        self.set_appearance(self.Emily_Hellinger, "long brown hair")
        ## Looking at the wall clock, she knew it was still early for John to be home.
        self.set_relation(self.Emily_Hellinger, 'husband', self.John_Hellinger)
        self.set_relation(self.John_Hellinger, 'wife', self.Emily_Hellinger)
        ## Glancing around the house, she noticed that he was nowhere to be found.
        ## Seeing his keys on the counter, she shrugged and went back to bed.
        ## She fell asleep quickly after having a late dinner and woke up early in the morning.
        ## Slipping into some jeans and a sweatshirt, Emily set off to find John.
        ## The spring air was brisk but warming up nicely as she headed down their street towards downtown Hillside Hills.
        ## Feeling a tingle of excitement pass through her at seeing so many people up and about in this small town during this quiet time of year, Emily smiled with delight as she scanned the nearly empty street for John's big blue truck.
        ## It wasn't parked near work or at home; it wasn't even parked near any of their family friends' houses where he might be visiting them on this gray morning while they were eating breakfast or watering their plants or other mundane tasks that people did on a Saturday morning before 9 am.
world = World()
world.story()
world.Emily_Hellinger.appearance

## Create a world model state to track each character's appearance, personality, and relations with other characters.

