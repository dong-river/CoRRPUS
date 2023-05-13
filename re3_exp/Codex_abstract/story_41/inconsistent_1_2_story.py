## Alex Preston is worried about his girlfriend, Jennie Mayfield.
## He's never seen her so upset.
## When he asked her what was wrong, she broke down and told him about a car accident she had just witnessed.
## They were in his new car, Alex driving and Jennie in the passenger seat.
## They were on their way to the mountains for a hike and picnic at the park nearby when a car jumped the center line and slammed into them head on.
## Luckily they both walked away without any major injuries.
## However, they had to stay behind as the police dealt with the other driver who was arrested for reckless driving.
## They watched from a distance as paramedics took care of people from both cars involved in the accident.
## At least everyone walked away from it unharmed physically, Alex thought, although the people involved might still be emotionally scarred.
## The police wouldn't let anyone get close to either car involved in case there was some way of preserving evidence which could be used against them later on in court if it came to that point.
## The police took statements from everyone who had been present at the scene.

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
        self.Jennie_Mayfield = character('Jennie Mayfield')
        self.Aaron_Mayfield = character('Aaron Mayfield')
        self.Alex_Preston = character('Alex Preston')

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
        ## Alex Preston is worried about his girlfriend, Jennie Mayfield.
        self.set_relation(self.Alex_Preston, 'girlfriend', self.Jennie_Mayfield)
        self.set_relation(self.Jennie_Mayfield, 'boyfriend', self.Alex_Preston)
        ## He's never seen her so upset.
        ## When he asked her what was wrong, she broke down and told him about a car accident she had just witnessed.
        ## They were in his new car, Alex driving and Jennie in the passenger seat.
        ## They were on their way to the mountains for a hike and picnic at the park nearby when a car jumped the center line and slammed into them head on.
        ## Luckily they both walked away without any major injuries.
        ## However, they had to stay behind as the police dealt with the other driver who was arrested for reckless driving.
        ## They watched from a distance as paramedics took care of people from both cars involved in the accident.
        ## At least everyone walked away from it unharmed physically, Alex thought, although the people involved might still be emotionally scarred.
        ## The police wouldn't let anyone get close to either car involved in case there was some way of preserving evidence which could be used against them later on in court if it came to that point.
        ## The police took statements from everyone who had been present at the scene.

 
