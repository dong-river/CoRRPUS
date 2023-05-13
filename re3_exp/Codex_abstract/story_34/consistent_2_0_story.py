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
        ## Thomas Watkins paced around his office.
        ## As the new sheriff of Winterdale, he was responsible for maintaining order in the town.
        self.set_occupation(self.Thomas_Watkins, "new sheriff")
        ## The only problem was that it seemed like no one cared about order in the first place.
        ## It felt like every day he had to solve a new crime or resolve a new dispute.
        ## Winterdale was such a small town, that Watkins thought things would be more peaceful than this when he accepted the job.
        ## At least now he knew why no one else wanted it.
        ## Watkins had just finished dealing with a drunk who had passed out on Main Street and had to move him out of the way before someone ran over him in the middle of the night.
        ## Now Watkins was getting ready to deal with an infestation of bats in an old building downtown that everyone thought was haunted.
        ## The people there were scared and wanted the bats gone so they could feel safe living there again, even though Watkins knew they were probably used to the bats by now and didn't really need them gone anyway.
        ## As Watkins headed out to confront the bats, he noticed something off in his peripheral vision—a shadowy figure running along an alleyway nearby.
        ## Watkins turned to see what it was and saw that it was just a dog.
        ## It was a pitbull, with a black coat and white markings on its face.
        ## It was running along the alleyway, and Watkins followed it, curious to see where it was going.
        ## The dog ran into an abandoned warehouse and Watkins followed it inside.
        ## He saw that the dog was standing over a dead body.
        ## The body was a young woman.
        ## She had been stabbed multiple times in the chest, and her throat had been slit.
        ## Watkins called the police and they took the body away.
        ## Watkins was given the case and he set out to find the killer.
        ## Watkins went to the morgue to examine the body.
        ## He saw that the woman had been stabbed with a knife, and her throat had been cut with a razor.
        ## Watkins also saw that she had been wearing a necklace with a pendant on it.
        ## It was a silver heart with the word "Amanda" engraved on it.
        ## Watkins took the necklace as evidence.
        ## Watkins went to the crime scene to investigate.
        ## He saw that there was a trail of blood leading from the body to the door of the warehouse.
        ## Watkins followed the trail and saw that it led to a car parked outside.
        ## The car was a black sedan with a broken taillight.
        ## Watkins took a picture of the car and sent it to his partner, Detective James Wilson.
        ## Wilson told Watkins that the car belonged to Amanda Wilkinson, a woman who had been reported missing two days ago.
        ## Watkins went to Amanda's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.
        ## There was a broken vase on the floor, and the sofa was overturned.
        ## Watkins also saw that there was a bloody handprint on the wall.
        ## Watkins took a picture of the handprint and sent it to Wilson.
        ## Wilson told Watkins that the handprint belonged to Will Trenton, Amanda's boyfriend.
        ## Watkins went to Will's house to investigate.
        ## He saw that there were signs of a struggle in the living room.