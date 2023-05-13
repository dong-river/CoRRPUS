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

    def story(self):
        ## Emily Hellinger walked into the kitchen in her pajamas, her hazel eyes squinting against the dim light.
        self.Emily_Hellinger.appearance.append('hazel eyes')
        ## She brushed her long brown hair out of her face as she yawned.
        self.Emily_Hellinger.appearance.append('long brown hair')
        ## Looking at the wall clock, she knew it was still early for John to be home.
        self.Emily_Hellinger.relations['husband'] = 'John_Hellinger'
        self.John_Hellinger.relations['wife'] = 'Emily_Hellinger'
        ## Glancing around the house, she noticed that he was nowhere to be found.
        ## Seeing his keys on the counter, she shrugged and went back to bed.
        ## She fell asleep quickly after having a late dinner and woke up early in the morning.
        ## Slipping into some jeans and a sweatshirt, Emily set off to find John.
        ## The spring air was brisk but warming up nicely as she headed down their street towards downtown Hillside Hills.
        ## Feeling a tingle of excitement pass through her at seeing so many people up and about in this small town during this quiet time of year, Emily smiled with delight as she scanned the nearly empty street for John's big blue truck.
        self.John_Hellinger.appearance.append('big blue truck')
        ## It wasn't parked near work or at home; it wasn't even parked near any of their family friends' houses where he might be visiting them on this gray morning while they were eating breakfast or watering their plants or other mundane tasks that people did on a Saturday morning before 9 am.

