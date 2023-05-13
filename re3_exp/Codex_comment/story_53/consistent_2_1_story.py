## Jessica Brown woke up at her usual time.
## Today was Saturday, which meant she could sleep in.
## But something was not right.
## She sat up in bed and glanced around the room.
## "What is going on?"
## she thought to herself.
## The room was identical to how it had been last night.
## It seemed to be unchanged except for her sister Jane's side of the room, which looked like a bomb had hit it.
## Clothes and books were scattered all over the floor, as if there had been a windstorm, while Jane slept on peacefully as though nothing was wrong, unaware of the havoc that had occurred just hours earlier.
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
        self.Jane_Doe = character('Jane Doe')
        self.Mister_Snuggles = character('Mister Snuggles')
        self.Jessica_Brown = character('Jessica Brown')

    def story(self):
        ## Jessica Brown woke up at her usual time.
        self.Jessica_Brown.occupation.append('student')
        ## Today was Saturday, which meant she could sleep in.
        ## But something was not right.
        ## She sat up in bed and glanced around the room.
        ## "What is going on?"
        ## she thought to herself.
        ## The room was identical to how it had been last night.
        ## It seemed to be unchanged except for her sister Jane's side of the room, which looked like a bomb had hit it.
        self.Jane_Doe.relations['sister'] = 'Jessica_Brown'
        self.Jessica_Brown.relations['sister'] = 'Jane_Doe'
        ## Clothes and books were scattered all over the floor, as if there had been a windstorm, while Jane slept on peacefully as though nothing was wrong, unaware of the havoc that had occurred just hours earlier.
        ## Mister Snuggles was a small, fluffy white dog.
        self.Mister_Snuggles.appearance.append('small')
        self.Mister_Snuggles.appearance.append('fluffy')
        self.Mister_Snuggles.appearance.append('white')
        self.Mister_Snuggles.appearance.append('dog')
        ## He was the best dog in the world.
        ## He was also very smart.
        ## He could do tricks like sit and stay, but he was also capable of more complex tasks such as fetching a ball or opening doors.
        ## Mister Snuggles was the perfect pet.

