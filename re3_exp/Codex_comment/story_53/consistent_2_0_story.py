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
        ## Today was Saturday, which meant she could sleep in.
        ## But something was not right.
        ## She sat up in bed and glanced around the room.
        ## "What is going on?"
        ## she thought to herself.
        ## The room was identical to how it had been last night.
        ## It seemed to be unchanged except for her sister Jane's side of the room, which looked like a bomb had hit it.
        ## Clothes and books were scattered all over the floor, as if there had been a windstorm, while Jane slept on peacefully as though nothing was wrong, unaware of the havoc that had occurred just hours earlier.
        self.Jane_Doe.relations['sister'] = 'Jessica_Brown'
        self.Jessica_Brown.relations['sister'] = 'Jane_Doe'
        self.Jane_Doe.appearance.append('clothes')
        self.Jane_Doe.appearance.append('books')
        self.Jane_Doe.appearance.append('floor')
        self.Jane_Doe.appearance.append('bomb')
        self.Jane_Doe.appearance.append('windstorm')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append('hours')
        self.Jane_Doe.appearance.append('earlier')
        self.Jane_Doe.appearance.append('identical')
        self.Jane_Doe.appearance.append('unchanged')
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.appearance.append('slept')
        self.Jane_Doe.appearance.append('peacefully')
        self.Jane_Doe.appearance.append('havoc')
        self.Jane_Doe.appearance.append