## Thomas Watkins paced around his office.
## As the new sheriff of Winterdale, he was responsible for maintaining order in the town.
## The only problem was that it seemed like no one cared about order in the first place.
## It felt like every day he had to solve a new crime or resolve a new dispute.
## Winterdale was such a small town, that Watkins thought things would be more peaceful than this when he accepted the job.
## At least now he knew why no one else wanted it.
## Watkins had just finished dealing with a drunk who had passed out on Main Street and had to move him out of the way before someone ran over him in the middle of the night.
## Now Watkins was getting ready to deal with an infestation of bats in an old building downtown that everyone thought was haunted.
## The people there were scared and wanted the bats gone so they could feel safe living there again, even though Watkins knew they were probably used to the bats by now and didn't really need them gone anyway.
## As Watkins headed out to confront the bats, he noticed something off in his peripheral vision—a shadowy figure running along an alleyway nearby.
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
        self.Will_Trenton = character('Will Trenton')
        self.Amanda_Wilkinson = character('Amanda Wilkinson')
        self.Thomas_Watkins = character('Thomas Watkins')

    def story(self):
        ## Thomas Watkins paced around his office.
        ## As the new sheriff of Winterdale, he was responsible for maintaining order in the town.
        self.Thomas_Watkins.occupation.append("sheriff")
        ## The only problem was that it seemed like no one cared about order in the first place.
        ## It felt like every day he had to solve a new crime or resolve a new dispute.
        ## Winterdale was such a small town, that Watkins thought things would be more peaceful than this when he accepted the job.
        ## At least now he knew why no one else wanted it.
        ## Watkins had just finished dealing with a drunk who had passed out on Main Street and had to move him out of the way before someone ran over him in the middle of the night.
        ## Now Watkins was getting ready to deal with an infestation of bats in an old building downtown that everyone thought was haunted.
        ## The people there were scared and wanted the bats gone so they could feel safe living there again, even though Watkins knew they were probably used to the bats by now and didn't really need them gone anyway.
        ## As Watkins headed out to confront the bats, he noticed something off in his peripheral vision—a shadowy figure running along an alleyway nearby.
        ## Create a world model state to track each character's appearance, personality, and relations with other characters.

