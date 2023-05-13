## John Doe was packing up his truck and preparing to leave the small town he'd been living in.
## He would be forced to leave the town, if he wanted to get back on his feet after losing his job.
## The job had given him a place to live and with the large paychecks he was making each week, he was able to save up some money.
## His truck was filled with boxes of clothes and essentials such as clothing and personal belongings for when he had needed to travel for work or when he was between jobs.
## He had originally planned on staying in the town for at least a few months before moving on to another one, but now he didn't have that option.
## He'd have to move on sooner than expected, if he wanted something more than this small town.
## It wasn't just a small town; it was an out-of-the-way place that lacked any real opportunities besides being a construction worker in order to make ends meet.
## No matter how hard John worked, it didn't seem like there were enough jobs available that paid as well as what John had been getting at his last job in Atlanta; therefore, John would have struggled even harder than before once he found another construction gig again elsewhere outside of the small town.

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
        self.John_Doe = character('John Doe')
        self.Abby_Mills = character('Abby Mills')
        self.Mike_Benson = character('Mike Benson')

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
        ## John Doe was packing up his truck and preparing to leave the small town he'd been living in.
        self.set_gender(self.John_Doe, "male")
        self.set_age(self.John_Doe, "adult")
        self.set_occupation(self.John_Doe, "construction worker")
        ## He would be forced to leave the town, if he wanted to get back on his feet after losing his job.
        ## The job had given him a place to live and with the large paychecks he was making each week, he was able to save up some money.
        ## His truck was filled with boxes of clothes and essentials such as clothing and personal belongings for when he had needed to travel for work or when he was between jobs.
        ## He had originally planned on staying in the town for at least a few months before moving on to another one, but now he didn't have that option.
        ## He'd have to move on sooner than expected, if he wanted something more than this small town.
        ## It wasn't just a small town; it was an out-of-the-way place that lacked any real opportunities besides being a construction worker in order to make ends meet.
        ## No matter how hard John worked, it didn't seem like there were enough jobs available that paid as well as what John had been getting at his last job in Atlanta; therefore, John would have struggled even harder than before once he found another construction gig again elsewhere outside of the small town.
