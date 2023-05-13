## Carl Russo was tired of work.
## He was tired of being a rich businessman and owning his own company.
## It was exciting in the beginning, but now it felt like just another day at the office, except he had to put on pants every morning.
## When Valerie started applying to medical schools, he hoped that becoming a doctor would make her happy.
## At first, it seemed like it would, but then she started taking too many hours off work and not putting in enough effort in school, which led to his decision to take a year off to travel the world before going back to school.
## Carl needed this time away from everything.
## He didn't even want to look at his email or phone for four months!
## Yes, he was old-fashioned like that and preferred face-to-face communication with people instead of texting or writing an email or a letter via snail mail.
## There was something nice about a hand-written letter that you couldn't get with technology these days; then again he did understand people's attraction to the feel of having their words in written form instead of staring at a screen all day long.

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
        self.Valerie_Russo = character('Valerie Russo')
        self.Carl_Russo = character('Carl Russo')
        self.Antoinette_Russo = character('Antoinette Russo')

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
        ## Carl Russo was tired of work.
        self.set_occupation(self.Carl_Russo, "rich businessman")
        ## He was tired of being a rich businessman and owning his own company.
        self.set_occupation(self.Carl_Russo, "rich businessman")
        ## It was exciting in the beginning, but now it felt like just another day at the office, except he had to put on pants every morning.
        ## When Valerie started applying to medical schools, he hoped that becoming a doctor would make her happy.
        self.set_relation(self.Carl_Russo, 'wife', self.Valerie_Russo)
        self.set_relation(self.Valerie_Russo, 'husband', self.Carl_Russo)
        self.set_occupation(self.Valerie_Russo, "doctor")
        ## At first, it seemed like it would, but then she started taking too many hours off work and not putting in enough effort in school, which led to his decision to take a year off to travel the world before going back to school.
        ## Carl needed this time away from everything.
        ## He didn't even want to look at his email or phone for four months!
        ## Yes, he was old-fashioned like that and preferred face-to-face communication with people instead of texting or writing an email or a letter via snail mail.
        ## There was something nice about a hand-written letter that you couldn't get with technology these days; then again he did understand people's attraction to the feel of having their words in written form instead of staring at a screen all day long.
