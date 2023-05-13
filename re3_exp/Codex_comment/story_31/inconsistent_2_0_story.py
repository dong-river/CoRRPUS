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

    def story(self):
        ## Chase Elliott glanced at his watch as he pulled into his driveway.
        ## It was late, but at least he'd gotten the first day of summer vacation off to a good start.
        self.Chase_Elliott.occupation.append('police officer')
        ## Riley Harper had arrived from Chicago that morning and had immediately begun unpacking.
        self.Riley_Harper.relations['father'] = 'Jonas_Harper'
        self.Jonas_Harper.relations['daughter'] = 'Riley_Harper'
        ## From what Chase could tell, she hadn't unpacked much more than a few pieces of clothing and her camera equipment when she decided to take a walk around town.
        self.Riley_Harper.occupation.append('photographer')
        ## Her new town, where he would soon be training her as his replacement until a permanent sheriff could be found.
        ## It had been an interesting few days since the first visit Riley made to his office at the police station after learning about her father's death.
        ## They'd gone to dinner together that night and since then they'd seen each other nearly every day while they settled Riley into their town.
        ## Chase grabbed his briefcase from the passenger seat of his truck and slammed the door shut with his hip before making his way toward the house.
        ## He glanced up at the windows, wondering if Riley was in her room.
        ## The second story bedroom faced out over the driveway and while he could hear a television blaring through an open window, there was no sign of Riley herself.

