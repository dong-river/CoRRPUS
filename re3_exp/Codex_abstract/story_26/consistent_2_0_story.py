## Karen Hanson was having a hard time finding her aunt Lettie.
## She tried calling several times, but she wasn't answering her phone.
## She didn't want to bother Bob and Mary, so she decided to drive over to the Hanson residence.
## When Karen arrived at the house, no one answered the door.
## "How can this be?"
## she thought to herself.
## "It's way too early for them to go out for the day."
## Suddenly she got an idea.
## She went around back and climbed in through a window in Bob's workshop where they would often play tricks on each other and say they wouldn't lock it when they left.
## (The door had been jammed ever since Bob's last attempt.)
## Karen was sure that was where Lettie would be right now.
## She burst into the room and found Lettie curled up on the bed sobbing.
## When she looked up, Karen saw that her eyes were blackened and red from crying so much.
## "What happened?"
## asked Karen frantically as she came running over to sit down next to her aunt on the bed.
## "I've been trying to call you all morning!"

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
        self.Lettie_Hanson = character('Lettie Hanson')
        self.Bob_Hanson = character('Bob Hanson')
        self.Karen_Hanson = character('Karen Hanson')

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
        ## Karen Hanson was having a hard time finding her aunt Lettie.
        self.set_relation(self.Lettie_Hanson, 'aunt', self.Karen_Hanson)
        self.set_relation(self.Karen_Hanson, 'niece', self.Lettie_Hanson)
        self.set_gender(self.Karen_Hanson, 'female')
        ## She tried calling several times, but she wasn't answering her phone.
        ## She didn't want to bother Bob and Mary, so she decided to drive over to the Hanson residence.
        self.set_relation(self.Bob_Hanson, 'wife', self.Lettie_Hanson)
        self.set_relation(self.Lettie_Hanson, 'husband', self.Bob_Hanson)
        self.set_gender(self.Bob_Hanson, 'male')
        ## When Karen arrived at the house, no one answered the door.
        ## "How can this be?"
        ## she thought to herself.
        ## "It's way too early for them to go out for the day."
        ## Suddenly she got an idea.
        ## She went around back and climbed in through a window in Bob's workshop where they would often play tricks on each other and say they wouldn't lock it when they left.
        ## (The door had been jammed ever since Bob's last attempt.)
        self.set_occupation(self.Bob_Hanson, 'workshop')
        ## Karen was sure that was where Lettie would be right now.
        ## She burst into the room and found Lettie curled up on the bed sobbing.
        ## When she looked up, Karen saw that her eyes were blackened and red from crying so much.
        self.set_appearance(self.Lettie_Hanson, 'blackened and red eyes')
        ## "What happened?"
        ## asked Karen frantically as she came running over to sit down next to her aunt on the bed.
        ## "I've been trying to call you all morning!"
