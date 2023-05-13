## Olivia Dupree's cheeks were stained with tears as she approached the boarding area for the plane to New York.
## Her arms were wrapped around her guardian's waist, and she was clutching her new backpack to her chest.
## She was only four years old, but she had never been away from home before and didn't know why she had to go on this trip.
## "I don't want to go," Olivia whimpered, looking up at her mother's face.
## Amanda knelt down on one knee and embraced her daughter in a tight hug.
## "Olivia, you have to go.
## Your Aunt Payton is very busy and can't take care of you right now," Amanda said softly.
## "I know you're going to like New York."
## Olivia released a loud sob and buried her face in Amanda's shoulder.
## "It'll be okay," Amanda promised her daughter again.
## "You'll stay with your aunt for a few days, get some rest, eat good food-the works!
## I bet it'll be really fun."
## Olivia looked at Amanda and wiped a tear away from the corner of her eye with the back of her hand.
## "Are you coming back?"

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
        self.Payton_Dupree = character('Payton Dupree')
        self.Amanda_Dupree = character('Amanda Dupree')
        self.Olivia_Dupree = character('Olivia Dupree')

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
        ## Olivia Dupree's cheeks were stained with tears as she approached the boarding area for the plane to New York.
        self.set_appearance(self.Olivia_Dupree, "cheeks were stained with tears")
        ## Her arms were wrapped around her guardian's waist, and she was clutching her new backpack to her chest.
        self.set_relation(self.Olivia_Dupree, 'guardian', self.Amanda_Dupree)
        self.set_relation(self.Amanda_Dupree, 'guardian', self.Olivia_Dupree)
        ## She was only four years old, but she had never been away from home before and didn't know why she had to go on this trip.
        self.set_age(self.Olivia_Dupree, "four years old")
        ## "I don't want to go," Olivia whimpered, looking up at her mother's face.
        self.set_relation(self.Olivia_Dupree, 'mother', self.Amanda_Dupree)
        self.set_relation(self.Amanda_Dupree, 'daughter', self.Olivia_Dupree)
        ## Amanda knelt down on one knee and embraced her daughter in a tight hug.
        ## "Olivia, you have to go.
        ## Your Aunt Payton is very busy and can't take care of you right now," Amanda said softly.
        self.set_relation(self.Olivia_Dupree, 'aunt', self.Payton_Dupree)
        self.set_relation(self.Payton_Dupree, 'niece', self.Olivia_Dupree)
        ## "I know you're going to like New York."
        ## Olivia released a loud sob and buried her face in Amanda's shoulder.
        ## "It'll be okay," Amanda promised her daughter again.
        ## "You'll stay with your aunt for a few days, get some rest, eat good food-the works!
        ## I bet it'll be really fun."
        ## Olivia looked at Amanda and wiped a tear away from the corner of her eye with the back of her hand.
        ## "Are you coming back?"
        ## "Of course I'm coming back!" Amanda said.
        ## "I'll be back in a few days, and then we'll go on a vacation together.
        ## Would you like that?"
        ## Olivia nodded her head and hugged Amanda tightly.
        ## "I love you, Mommy," she whispered.
        ## "I love you too, sweetie," Amanda replied.
        ## She kissed her daughter's forehead and stood up.
        ## "I have to go now, but I'll see you soon."
        ## Amanda waved goodbye to her daughter as she walked away.
        ## Olivia watched her mother disappear into the crowd of people.
        ## Then she turned and walked toward the boarding area.
        ## The next few days passed by in a blur.
        ## Olivia stayed with her aunt in New York and did her best to get along with Payton's two daughters, who were only a few years older than her.
        ## She missed her mother, but she tried not to think about it too much.
        ## Olivia was sitting on the couch in Payton's apartment, watching a movie with her cousins, when the phone rang.
        ## Payton answered it and spoke for a few minutes before hanging up.
        ## "That was your mother," Payton said to Olivia.
        ## "She's on her way home now."
        ## "Really?" Olivia asked, her eyes lighting up.
        ## "Yes," Payton replied.
        ## "She should be here in a few hours."
        ## Olivia smiled and stood up.
        ## "I'm going to go pack my things," she said.
        ## "Okay," Payton said.
        ## "I'll call you when she gets here."
        ## Olivia ran to her room and began throwing her clothes into her backpack.
        ## She couldn't wait to see her mother again.
        ## It had only been a few days, but it felt like forever.
        ## "Olivia!" Payton called from the living room.
        ## "Your mother is here!"
        ## Olivia dropped the shirt she was holding and ran to the front door.
        ## She threw her arms around Amanda and hugged her tightly.
        ## "I missed you so much," Olivia said.
        ## "I missed you too, sweetie," Amanda replied.
        ## "Are you ready to go home?"
        ## "Yes," Olivia said.
        ## She picked up her backpack and followed Amanda out the door.
        ## "Bye, Aunt Payton!" she called over her shoulder.
        ## "Bye, Olivia," Payton said.
        ## She smiled and waved as the two of them walked down the hall.
        ## Amanda and Olivia spent the next few days relaxing at home.
        ## Amanda took her daughter to the park and they went shopping together.
        ## Olivia was happy to be back with her mother, and she didn't want to leave her side.
        ## A few days later, Amanda had to go to work.
        ## She kissed Olivia on the forehead and told her to have a good day.
        ## Then she left for the office.
        ## Olivia spent the day playing with her toys and watching TV.
        ## She was just starting to get bored when there was a knock at the door.
        ## Olivia ran to answer it and found a man standing on the other side.
        ## He was tall and thin, with short brown hair and a pair of glasses perched on the bridge of his nose.
        ## He was wearing a suit and tie, and he was holding a briefcase in one hand.
        ## "Hello," the man said.
        ## "My name is Mr.
        ## Jones.
        ## I'm a lawyer, and I'm here to see Amanda Dupree."
        ## "She's not here right now," Olivia replied.
        ## "She had to go to work."
        ## "I see," Mr.
        ## Jones said.
        ## "Do you know when she'll be back?"
        ## "She said she'd be home in time for dinner," Olivia replied.
        ## "Would you like to come inside and wait for her?"
        ## "Yes, thank you," Mr.
        ## Jones said.
        ## He stepped into the house and closed the door behind him.
        ## Olivia led him into the living room and sat down on the couch.
        ## Mr.
        ## Jones took a seat in the armchair across from her.
        ## "So, what's your name?" he asked.
        ## "Olivia," she replied.
        ## "It's very nice to meet you, Olivia," Mr.
        ## Jones said.
        ## He smiled at her, and she smiled back.
        ## "Would you like something to drink?" she asked.
        ## "No, thank you," Mr.
        ## Jones replied.
        ## "I'm fine."
        ## Olivia nodded and sat back on the couch.
        ## She picked up the remote control and started flipping through the channels.
        ## "So, what do you like to do for fun?" Mr.
        ## Jones asked.
        ## "I like to play with my toys," Olivia replied.
        ## "I have a lot of them."
        ## "That's nice," Mr.
        ## Jones said.
        ## "Do you have any brothers or sisters?"
        ## "No," Olivia replied.
        ## "It's just me and my mom."
        ## "I see," Mr.
        ## Jones said.
        ## "Do you have any friends?"
        ## "Not really," Olivia replied.
        ## "My mom says I'm too young to have friends."
        ## "I see," Mr.
        ## Jones said.
        ## "Well, that's too bad.
        ## Friends can be a lot of fun."
        ## "I know," Olivia said.
        ## "My mom says I can have friends when I'm older."
        ## "That's good," Mr.
        ## Jones said.
        ## "So, what does your mom do for a living?"
        ## "She's a lawyer," Olivia replied.
        ## "Like you."
        ## "I see," Mr.
        ## Jones said.
        ## "That's very interesting."
        ## "I know," Olivia said.
        ## "She works really hard.
        ## Sometimes she has to work late at night, and she doesn't get home until after I've gone to bed."
        ## "I see," Mr.
        ## Jones said.
        ## "Well, I'm sure she's a very good lawyer."
        ## "She is," Olivia said.
        ## "She always wins her cases."
        ## "That's good," Mr.
        ## Jones said.
        ## "So, what do you want to be when you grow up?"
        ## "I don't know," Olivia replied.
        ## "I haven't really thought about it."
        ## "Well, you have plenty of time to decide," Mr.
        ## Jones said.
        ## "You're still very young."
        ## "I know," Olivia said.
        ## "My mom says I can be anything I want when I grow up."
        ## "That's good," Mr.
        ## Jones said.
        ## "So, do you have any pets?"
        ## "No," Olivia replied.
        ## "My mom says we can't have any pets because we travel a lot."
        ## "I see," Mr.
        ## Jones said.
        ## "Well, that's too bad.
        ## Pets can be a lot of fun."
        ## "I know," Olivia said.
        ## "My mom says I can have a pet when I'm older."
        ## "That's good," Mr.
        ## Jones said.
        ## "So, what do you like to do for fun?"
        ## "I like to play with my toys," Olivia replied.
        ## "I have a lot of them."
        ## "That's nice," Mr.
        ## Jones said.
        ## "Do you have any brothers or sisters?"
        ## "No," Olivia replied.
        ## "It's just me and my mom."
        ## "I see," Mr.
        ## Jones said.
        ## "Do you have any friends?"
        ## "Not really," Olivia replied.
        ## "My mom says I'm too young to have friends."
        ## "I see," Mr.
        ## Jones said.
        ## "Well, that's too bad.
        ## Friends can be a lot of fun."
        ## "I know," Olivia said.
        ## "My mom says I can have friends when I'm older."
        ## "That's good," Mr.
        ## Jones said.
        ## "So, what does your mom do for a living?"
        ## "She's a lawyer," Olivia replied.
        ## "Like you