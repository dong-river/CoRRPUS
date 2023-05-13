## Alex Preston is now a ghost and he watches as Jennie gets out of her wrecked car.
## She has long dark hair and brown eyes.
## Her body is athletic.
## It's obvious she takes care of herself.
## She is stunned and in pain.
## She can't remember the accident but she feels like something's wrong with her shoulder.
## She saw her tire blow out and then she crashed into a tree.
## She was lucky that no one else was on the road or she could have caused a head-on collision.
## Alex kneels down next to her and holds his hand out to comfort her as best he can.
## He wonders if he can help ease her pain somehow, but he's not sure how to do it yet.
## He may need some time to get used to his new form before he can figure out what to do with it all the time when it comes to things like this.
## Jennie tries to make sense of what happened when the car veered off into the trees, heading right for them but then suddenly slowing down until it barely hit them at all instead of going right through them with disastrous results.

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
        ## Alex Preston is now a ghost and he watches as Jennie gets out of her wrecked car.
        ## She has long dark hair and brown eyes.
        self.set_appearance(self.Jennie_Mayfield, "long dark hair")
        self.set_appearance(self.Jennie_Mayfield, "brown eyes")
        ## Her body is athletic.
        self.set_appearance(self.Jennie_Mayfield, "athletic")
        ## It's obvious she takes care of herself.
        ## She is stunned and in pain.
        ## She can't remember the accident but she feels like something's wrong with her shoulder.
        ## She saw her tire blow out and then she crashed into a tree.
        ## She was lucky that no one else was on the road or she could have caused a head-on collision.
        ## Alex kneels down next to her and holds his hand out to comfort her as best he can.
        ## He wonders if he can help ease her pain somehow, but he's not sure how to do it yet.
        ## He may need some time to get used to his new form before he can figure out what to do with it all the time when it comes to things like this.
        ## Jennie tries to make sense of what happened when the car veered off into the trees, heading right for them but then suddenly slowing down until it barely hit them at all instead of going right through them with disastrous results.
        ## The next day, Jennie goes to see Aaron Mayfield, the man she loves.
        self.set_relation(self.Jennie_Mayfield, 'lover', self.Aaron_Mayfield)
        self.set_relation(self.Aaron_Mayfield, 'lover', self.Jennie_Mayfield)
        ## Aaron Mayfield is a tall man with short brown hair and brown eyes.
        self.set_appearance(self.Aaron_Mayfield, "short brown hair")
        self.set_appearance(self.Aaron_Mayfield, "brown eyes")
        ## He is a lawyer who works at his father's firm.
        self.set_occupation(self.Aaron_Mayfield, "lawyer")
        self.set_relation(self.Aaron_Mayfield, 'father', self.Aaron_Mayfield)
        ## He is wearing a suit and tie.
        ## He is sitting at his desk, reading a newspaper.
        ## Jennie Mayfield walks into the office.
        ## She has long dark hair and brown eyes.
        ## Her body is athletic.
        ## It's obvious she takes care of herself.
        ## She is wearing a blue dress with white flowers on it.
        ## She is carrying a purse in one hand and a briefcase in the other.
        ## She looks tired but happy to see him.
        ## Aaron Mayfield looks up from his newspaper and smiles when he sees her.
        ## "Jennie! I'm glad you could make it."
        ## Jennie Mayfield smiles back at him.
        ## "I'm glad I could too."
        ## Jennie Mayfield sits down across from Aaron Mayfield.
        ## "How are you doing?"
        ## "I'm doing well."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "How was your day?"
        ## "It was good."
        ## "I'm glad to hear that."
        ## "