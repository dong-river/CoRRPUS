## Chase Elliott glanced at his watch as he pulled into his driveway.
## It was late, but at least he'd gotten the first day of summer vacation off to a good start.
## Riley Harper had arrived from Chicago that morning and had immediately begun unpacking.
## From what Chase could tell, she hadn't unpacked much more than a few pieces of clothing and her camera equipment when she decided to take a walk around town.
## Her new town, where he would soon be training her as his replacement until a permanent sheriff could be found.
## It had been an interesting few days since the first visit Riley made to his office at the police station after learning about her father's death.
## They'd gone to dinner together that night and since then they'd seen each other nearly every day while they settled Riley into their town.
## Chase grabbed his briefcase from the passenger seat of his truck and slammed the door shut with his hip before making his way toward the house.
## He glanced up at the windows, wondering if Riley was in her room.
## The second story bedroom faced out over the driveway and while he could hear a television blaring through an open window, there was no sign of Riley herself.

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
        self.Riley_Harper = character('Riley Harper')
        self.Chase_Elliott = character('Chase Elliott')
        self.Jonas_Harper = character('Jonas Harper')

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
        ## Chase Elliott glanced at his watch as he pulled into his driveway.
        ## It was late, but at least he'd gotten the first day of summer vacation off to a good start.
        self.set_appearance(self.Chase_Elliott, "glanced at his watch")
        self.set_appearance(self.Chase_Elliott, "pulled into his driveway")
        self.set_appearance(self.Chase_Elliott, "It was late")
        self.set_appearance(self.Chase_Elliott, "at least he'd gotten the first day of summer vacation off to a good start")
        ## Riley Harper had arrived from Chicago that morning and had immediately begun unpacking.
        self.set_appearance(self.Riley_Harper, "arrived from Chicago that morning")
        self.set_appearance(self.Riley_Harper, "had immediately begun unpacking")
        ## From what Chase could tell, she hadn't unpacked much more than a few pieces of clothing and her camera equipment when she decided to take a walk around town.
        self.set_appearance(self.Chase_Elliott, "From what Chase could tell")
        self.set_appearance(self.Chase_Elliott, "she hadn't unpacked much more than a few pieces of clothing and her camera equipment when she decided to take a walk around town")
        ## Her new town, where he would soon be training her as his replacement until a permanent sheriff could be found.
        self.set_appearance(self.Riley_Harper, "Her new town")
        self.set_appearance(self.Riley_Harper, "where he would soon be training her as his replacement until a permanent sheriff could be found")
        ## It had been an interesting few days since the first visit Riley made to his office at the police station after learning about her father's death.
        self.set_appearance(self.Chase_Elliott, "It had been an interesting few days")
        self.set_appearance(self.Chase_Elliott, "since the first visit Riley made to his office at the police station after learning about her father's death")
        ## They'd gone to dinner together that night and since then they'd seen each other nearly every day while they settled Riley into their town.
        self.set_appearance(self.Chase_Elliott, "They'd gone to dinner together that night")
        self.set_appearance(self.Chase_Elliott, "since then they'd seen each other nearly every day while they settled Riley into their town")
        ## Chase grabbed his briefcase from the passenger seat of his truck and slammed the door shut with his hip before making his way toward the house.
        self.set_appearance(self.Chase_Elliott, "Chase grabbed his briefcase from the passenger seat of his truck")
        self.set_appearance(self.Chase_Elliott, "slammed the door shut with his hip before making his way toward the house")
        ## He glanced up at the windows, wondering if Riley was in her room.
        self.set_appearance(self.Chase_Elliott, "He glanced up at the windows")
        self.set_appearance(self.Chase_Elliott, "wondering if Riley was in her room")
        ## The second story bedroom faced out over the driveway and while he could hear a television blaring through an open window, there was no sign of Riley herself.
        self.set_appearance(self.Chase_Elliott, "The second story bedroom faced out over the driveway")
        self.set_appearance(self.Chase_Elliott, "he could hear a television blaring through an open window")
        self.set_appearance(self.Chase_Elliott, "there was no sign of Riley herself")
