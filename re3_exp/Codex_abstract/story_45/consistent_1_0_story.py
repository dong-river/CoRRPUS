## Karen Hartman was worried about her daughter, Nina.
## She was worried because the child was becoming increasingly withdrawn and moody.
## It all started a few months ago when she would wake up in the middle of the night sobbing and thrashing wildly around in her bed.
## Every time she was questioned about it, she would give the same answer, "I don't know."
## Karen decided to put it out of her mind as her daughter began school this year.
## But she started having problems there too, showing unusual interest in anything that resembled ghost stories or movies with lots of special effects.
## She even began asking questions about ghosts in everyday life to both her teachers and the students around her at school.
## Some of the other students had heard rumors about a house on Charlotte Street that supposedly haunted and laughed at Nina's questions and rumors went through the school about Nina having a crush on a cute boy that lived there named Jake Ryan.
## "Do you know who I am talking about?"
## asked Nina anxiously as she continued pacing back and forth from one end of Karen's living room to another, stopping every so often to look at something intently out one of the windows or shake her head slowly side to side like someone in deep thought.
## Karen shook her head no in response.

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
        self.Nina_Harman = character('Nina Harman')
        self.Jake_Ryan = character('Jake Ryan')
        self.Karen_Hartman = character('Karen Hartman')

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
        ## Karen Hartman was worried about her daughter, Nina.
        self.set_relation(self.Karen_Hartman, 'daughter', self.Nina_Harman)
        self.set_relation(self.Nina_Harman, 'mother', self.Karen_Hartman)
        self.set_gender(self.Karen_Hartman, "female")
        ## She was worried because the child was becoming increasingly withdrawn and moody.
        ## It all started a few months ago when she would wake up in the middle of the night sobbing and thrashing wildly around in her bed.
        ## Every time she was questioned about it, she would give the same answer, "I don't know."
        ## Karen decided to put it out of her mind as her daughter began school this year.
        ## But she started having problems there too, showing unusual interest in anything that resembled ghost stories or movies with lots of special effects.
        ## She even began asking questions about ghosts in everyday life to both her teachers and the students around her at school.
        ## Some of the other students had heard rumors about a house on Charlotte Street that supposedly haunted and laughed at Nina's questions and rumors went through the school about Nina having a crush on a cute boy that lived there named Jake Ryan.
        self.set_relation(self.Nina_Harman, 'crush', self.Jake_Ryan)
        self.set_relation(self.Jake_Ryan, 'crush', self.Nina_Harman)
        ## "Do you know who I am talking about?"
        ## asked Nina anxiously as she continued pacing back and forth from one end of Karen's living room to another, stopping every so often to look at something intently out one of the windows or shake her head slowly side to side like someone in deep thought.
        ## Karen shook her head no in response.
        self.set_relation(self.Karen_Hartman, 'daughter', self.Nina_Harman)
        self.set_relation(self.Nina_Harman, 'mother', self.Karen_Hartman)
        self.set_gender(self.Karen_Hartman, "female")
