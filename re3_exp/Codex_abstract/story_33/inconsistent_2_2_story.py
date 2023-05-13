## Charles Wilson finished up his last final exam and heaved a huge sigh of relief.
## It was finally over.
## He felt a sense of accomplishment knowing that he had made it through college.
## Even though he was twenty-three years old, he knew it wasn't too late to finish his education.
## He never thought he would get that far, but there he was with a degree in hand.
## Now the real work would begin.
## He'd have to find an internship and hopefully an eventual job that could allow him to pay back his student loans and still support himself along the way.
## He gathered up his belongings, checking to make sure that everything was in place before making his way out of the classroom.
## The teacher stopped him just as he was about to leave and asked if he could talk with Charles for a minute in private.
## Reluctantly, Charles agreed and went into her office after the rest of the students had left for lunch or otherwise gone on their way.
## He took a seat at her desk while she took hers and sat across from him, gesturing for him to continue taking one as well while she leaned forward with her elbows on her desk and her hands clasped together looking down at them in thought.

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
        self.Charles_Wilson = character('Charles Wilson')
        self.Nina_Peterson = character('Nina Peterson')
        self.Jeff_Foster = character('Jeff Foster')

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
        ## Charles Wilson finished up his last final exam and heaved a huge sigh of relief.
        ## It was finally over.
        self.set_relation(self.Charles_Wilson, 'final_exam', self.Charles_Wilson)
        ## He felt a sense of accomplishment knowing that he had made it through college.
        self.set_occupation(self.Charles_Wilson, 'college')
        ## Even though he was twenty-three years old, he knew it wasn't too late to finish his education.
        self.set_age(self.Charles_Wilson, 'twenty-three')
        ## He never thought he would get that far, but there he was with a degree in hand.
        self.set_occupation(self.Charles_Wilson, 'degree')
        ## Now the real work would begin.
        ## He'd have to find an internship and hopefully an eventual job that could allow him to pay back his student loans and still support himself along the way.
        self.set_occupation(self.Charles_Wilson, 'internship')
        self.set_occupation(self.Charles_Wilson, 'job')
        ## He gathered up his belongings, checking to make sure that everything was in place before making his way out of the classroom.
        ## The teacher stopped him just as he was about to leave and asked if he could talk with Charles for a minute in private.
        self.set_relation(self.Charles_Wilson, 'teacher', self.Nina_Peterson)
        ## Reluctantly, Charles agreed and went into her office after the rest of the students had left for lunch or otherwise gone on their way.
        self.set_relation(self.Charles_Wilson, 'student', self.Jeff_Foster)
        ## He took a seat at her desk while she took hers and sat across from him, gesturing for him to continue taking one as well while she leaned forward with her elbows on her desk and her hands clasped together looking down at them in thought.
        self.set_relation(self.Charles_Wilson, 'teacher', self.Nina_Peterson)
        self.set_relation(self.Nina_Peterson, 'student', self.Charles_Wilson)
 
