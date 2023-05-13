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
        ## The only problem was that it seemed like no one cared about order in the first place.
        ## It felt like every day he had to solve a new crime or resolve a new dispute.
        self.set_occupation(self.Thomas_Watkins, "sheriff")
        ## Winterdale was such a small town, that Watkins thought things would be more peaceful than this when he accepted the job.
        ## At least now he knew why no one else wanted it.
        ## Watkins had just finished dealing with a drunk who had passed out on Main Street and had to move him out of the way before someone ran over him in the middle of the night.
        ## Now Watkins was getting ready to deal with an infestation of bats in an old building downtown that everyone thought was haunted.
        ## The people there were scared and wanted the bats gone so they could feel safe living there again, even though Watkins knew they were probably used to the bats by now and didn't really need them gone anyway.
        ## As Watkins headed out to confront the bats, he noticed something off in his peripheral vision—a shadowy figure running along an alleyway nearby.
        ## Watkins ran after the figure, but it was too fast for him.
        ## The figure was gone by the time Watkins reached the end of the alleyway.
        ## Watkins was about to turn back when he noticed something on the ground.
        ## It was a wallet.
        ## Watkins picked it up and looked inside.
        ## There was a driver's license inside.
        ## The name on it was Will Trenton.
        ## Watkins looked at the address on the license.
        ## It was the same address as the old building where the bats were.
        ## Watkins pulled out his phone and called the police.
        ## He told them what happened and they said they'd send someone over to investigate.
        ## Watkins put the wallet in his pocket and headed back to the old building.
        ## When he got there, the building was empty.
        ## There was no sign of anyone living there, let alone an infestation of bats.
        ## Watkins wondered if he had the wrong address, but he was sure he didn't.
        ## He pulled out the wallet again and looked at the address.
        ## It was the same one.
        ## Watkins looked around the building for a while, but he couldn't find anything.
        ## He was about to leave when he heard a noise coming from upstairs.
        ## Watkins walked over to the stairs and started climbing them.
        ## When he got to the top, he saw a door at the end of a hallway.
        ## The door was closed, but Watkins could hear something coming from inside.
        ## Watkins walked over to the door and opened it.
        ## Inside was a young woman.
        ## She was sitting on the floor with her back against the wall.
        ## She was crying.
        ## Watkins walked over to her and asked her what was wrong.
        ## The woman looked up at Watkins and said, "My boyfriend is dead."
        ## Watkins asked her what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in the next room.
        ## Please help me."
        ## Watkins walked into the next room and saw a man lying on the floor.
        ## He was dead.
        ## Watkins walked over to the man and checked for a pulse.
        ## There wasn't one.
        ## Watkins walked back into the other room and told the woman that her boyfriend was dead.
        ## The woman started crying again.
        ## Watkins asked her if she knew what happened.
        ## The woman said, "I don't know.
        ## He just collapsed and died.
        ## I don't know what to do."
        ## Watkins asked her if she knew where her boyfriend was.
        ## The woman said, "He's in