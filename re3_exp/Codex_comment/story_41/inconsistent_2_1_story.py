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

    def story(self):
        ## Alex Preston is now a ghost and he watches as Jennie gets out of her wrecked car.
        ## She has long dark hair and brown eyes.
        self.Jennie_Mayfield.appearance.append('long dark hair')
        self.Jennie_Mayfield.appearance.append('brown eyes')
        ## Her body is athletic.
        ## It's obvious she takes care of herself.
        self.Jennie_Mayfield.appearance.append('athletic')
        ## She is stunned and in pain.
        ## She can't remember the accident but she feels like something's wrong with her shoulder.
        ## She saw her tire blow out and then she crashed into a tree.
        ## She was lucky that no one else was on the road or she could have caused a head-on collision.
        ## Alex kneels down next to her and holds his hand out to comfort her as best he can.
        ## He wonders if he can help ease her pain somehow, but he's not sure how to do it yet.
        ## He may need some time to get used to his new form before he can figure out what to do with it all the time when it comes to things like this.
        ## Jennie tries to make sense of what happened when the car veered off into the trees, heading right for them but then suddenly slowing down until it barely hit them at all instead of going right through them with disastrous results.

