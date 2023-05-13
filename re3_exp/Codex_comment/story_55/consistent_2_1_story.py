## Olivia Saunders woke up in the middle of the night.
## She could hear footsteps outside her room, and so she slowly got out of bed.
## "Liv?
## What are you doing?"
## asked her sister, Emma.
## "It's the middle of the night."
## "I heard something," said Olivia in a hushed voice.
## Emma grabbed her sister's hand and opened her bedroom door, "If you heard something, I want to hear it too," she said.
## Olivia was about to say that there was nothing out there, but when she stepped into the hallway, she froze.
## She felt as if something wasn't right and so they slowly walked down the stairs, towards their parents' room.
## The footsteps that they heard were coming from there.
## Their dad's light was on and Olivia saw a strange shadow moving behind their parents' open door.
## "Dad?"
## Emma whispered through the door after knocking on it lightly.
## They waited for an answer, but none came; they pushed open the door and rushed into their parent's room to see that their dad was gone!
## He had disappeared in his sleep while it happened to be the middle of the night!
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
        self.Emma_Saunders = character('Emma Saunders')
        self.Jackson_Cooper = character('Jackson Cooper')
        self.Olivia_Saunders = character('Olivia Saunders')

    def story(self):
        ## Olivia Saunders woke up in the middle of the night.
        ## She could hear footsteps outside her room, and so she slowly got out of bed.
        ## "Liv?
        ## What are you doing?"
        ## asked her sister, Emma.
        ## "It's the middle of the night."
        self.Emma_Saunders.relations['sister'] = 'Olivia_Saunders'
        self.Olivia_Saunders.relations['sister'] = 'Emma_Saunders'
        ## "I heard something," said Olivia in a hushed voice.
        ## Emma grabbed her sister's hand and opened her bedroom door, "If you heard something, I want to hear it too," she said.
        ## Olivia was about to say that there was nothing out there, but when she stepped into the hallway, she froze.
        ## She felt as if something wasn't right and so they slowly walked down the stairs, towards their parents' room.
        ## The footsteps that they heard were coming from there.
        ## Their dad's light was on and Olivia saw a strange shadow moving behind their parents' open door.
        ## "Dad?"
        ## Emma whispered through the door after knocking on it lightly.
        ## They waited for an answer, but none came; they pushed open the door and rushed into their parent's room to see that their dad was gone!
        ## He had disappeared in his sleep while it happened to be the middle of the night!

