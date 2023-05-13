## Mark Woodbury hurried down the sidewalk and crossed the street.
## He didn’t have time to be late for his date with Shannon Kincaid, and he wanted to arrive at the restaurant early so he could beat the rush.
## As he neared the entrance, he saw her waving at him from a table inside.
## “I’m sorry I’m late, Mark,” she said when he sat down.
## “I was held up in traffic on the way here.
## How are you?”  Mark leaned over and kissed her cheek.
## “That was quite a jolt you gave me when you called a few minutes ago and said you were running late.
## But I guess it’s good that I got here when I did.
## If we had set this thing for any later, we would have missed our reservation for sure.
## They were about to turn people away as I walked up here.”  Shannon laughed lightly.

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
        self.Shannon_Kincaid = character('Shannon Kincaid')
        self.Jack_Kincaid = character('Jack Kincaid')
        self.Mark_Woodbury = character('Mark Woodbury')

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
        ## Mark Woodbury hurried down the sidewalk and crossed the street.
        self.set_gender(self.Mark_Woodbury, "male")
        ## He didn’t have time to be late for his date with Shannon Kincaid, and he wanted to arrive at the restaurant early so he could beat the rush.
        self.set_relation(self.Mark_Woodbury, 'date', self.Shannon_Kincaid)
        self.set_relation(self.Shannon_Kincaid, 'date', self.Mark_Woodbury)
        self.set_gender(self.Shannon_Kincaid, "female")
        ## As he neared the entrance, he saw her waving at him from a table inside.
        ## “I’m sorry I’m late, Mark,” she said when he sat down.
        ## “I was held up in traffic on the way here.
        ## How are you?”  Mark leaned over and kissed her cheek.
        ## “That was quite a jolt you gave me when you called a few minutes ago and said you were running late.
        ## But I guess it’s good that I got here when I did.
        ## If we had set this thing for any later, we would have missed our reservation for sure.
        ## They were about to turn people away as I walked up here.”  Shannon laughed lightly.
        ## “You’re right, Mark.
        ## I’m sorry I made you worry.”  “It’s okay.
        ## I’m glad you’re here now.”  Shannon smiled at him.
        ## “I’m glad I’m here too.”
        ## “So what do you want to do tonight?” he asked.
        ## “I’m not sure.
        ## I haven’t really thought about it.
        ## What do you want to do?”  “I was thinking we could go see a movie.
        ## There’s a new one playing at the theater downtown.”  “Sure, that sounds like fun.
        ## What time is it?”  “It’s about six-thirty.”  “Okay, we have plenty of time then.
        ## We can eat first and then go to the movie.”  “Sounds good.”
        ## Mark and Shannon ate dinner and then went to the movie.
        ## Afterward, they walked back to Shannon’s apartment and sat on the couch together.
        ## “I had a really nice time tonight, Mark.
        ## Thank you.”  “You’re welcome, Shannon.
        ## I had a nice time too.”  “I’m glad.
        ## Maybe we can do this again sometime.”  “I’d like that.”
        ## They kissed good night and Mark left.
        ## As he walked home, he thought about how much he liked Shannon.
        ## He was glad that she had agreed to go out with him.
        ## He hoped that they would be able to go out again soon.
        ## When he got home, he went straight to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
        ## After lunch, they went back to the office and continued working on their projects.
        ## At five o’clock, Mark left work and went home.
        ## He ate dinner and then went to bed.
        ## The next morning, he got up early and went for a run.
        ## Afterward, he showered and got ready for work.
        ## When he got to the office, he sat down at his desk and turned on his computer.
        ## He checked his email and then started working on the project he had been assigned.
        ## Around noon, he went to lunch with his coworkers.
        ## They went to a nearby restaurant and ate burgers and fries.
