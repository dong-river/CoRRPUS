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
        ## The story is set in the present day and takes place in the United States.
        ## Jessica Brown woke up at her usual time.
        ## Today was Saturday, which meant she could sleep in.
        ## But something was not right.
        ## She sat up in bed and glanced around the room.
        ## "What is going on?"
        ## she thought to herself.
        ## The room was identical to how it had been last night.
        ## It seemed to be unchanged except for her sister Jane's side of the room, which looked like a bomb had hit it.
        self.Jane_Doe.appearance.append('messy')
        ## Clothes and books were scattered all over the floor, as if there had been a windstorm, while Jane slept on peacefully as though nothing was wrong, unaware of the havoc that had occurred just hours earlier.
        self.Jane_Doe.appearance.append('unaware')
        self.Jane_Doe.relations['sister'] = 'Jessica_Brown'
        self.Jessica_Brown.relations['sister'] = 'Jane_Doe'

## The story is set in the present day and takes place in the United States.
## Jane Doe is a woman who has died in a car accident.
## She is a kind and sympathetic person who is eager to help the people she left behind.
## Mister Snuggles is Jane's pet cat.
## He is a kind and loving animal who is struggling to cope with his owner's death.
## Jessica Brown is Jane's sister.
## She is a young girl who is struggling to understand her sister's death.
## Jessica Brown sits on the floor, looking at the empty box that used to hold her sister's belongings. 
## Her gaze is unfocused, her dark blue eyes brimming with tears.
## She cries for hours, eventually falling asleep from exhaustion.
## When she wakes up, she feels dazed and ill.
## Jane died in a car accident on a rainy day several weeks ago.
## Jessica has been carrying on with life ever since as best she can manage, but she still doesn't really know how to cope with Jane's death.
## Create a world model state to track each character's appearance, personality, and relations with other characters.

