## Connor Riley is an engineer who has recently been chosen to design and build the machines that will be used to simulate the trees on Mars.
## He had been working for three years to earn this assignment, and he wasn't about to let anything go wrong.
## While working on his most recent assignment, Connor decided to call in sick.
## He was very worried about having the equipment he designed fail while testing and he wasn't willing to take any chances.
## Later that day, Connor regretted his decision to call in sick because a key part of his invention began malfunctioning during the test.
## Several people were injured before it could be stopped.
## After much debate between Connor's boss and another division of the company, they decided that Connor was too valuable an employee to lose so they transferred him immediately out of his department and into another division where no one would remember how badly he had messed up at his last job.

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
        self.Nadia_Kaminski = character('Nadia Kaminski')
        self.Connor_Riley = character('Connor Riley')
        self.Abigail_Harper = character('Abigail Harper')

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
        ## Connor Riley is an engineer who has recently been chosen to design and build the machines that will be used to simulate the trees on Mars.
        self.set_occupation(self.Connor_Riley, "engineer")
        ## He had been working for three years to earn this assignment, and he wasn't about to let anything go wrong.
        ## While working on his most recent assignment, Connor decided to call in sick.
        ## He was very worried about having the equipment he designed fail while testing and he wasn't willing to take any chances.
        ## Later that day, Connor regretted his decision to call in sick because a key part of his invention began malfunctioning during the test.
        ## Several people were injured before it could be stopped.
        ## After much debate between Connor's boss and another division of the company, they decided that Connor was too valuable an employee to lose so they transferred him immediately out of his department and into another division where no one would remember how badly he had messed up at his last job.
        ## Nadia Kaminski is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        self.set_age(self.Nadia_Kaminski, "young")
        self.set_gender(self.Nadia_Kaminski, "female")
        ## She is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        self.set_occupation(self.Nadia_Kaminski, "college student")
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        self.set_occupation(self.Abigail_Harper, "graduate student")
        self.set_relation(self.Nadia_Kaminski, 'coworker', self.Abigail_Harper)
        self.set_relation(self.Abigail_Harper, 'coworker', self.Nadia_Kaminski)
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Abigail is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Abigail is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Abigail has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when she was young so she has always had to work for everything she has.
        ## Nadia has been working on the Mars simulation project for several months now and she feels like she is finally getting somewhere.
        ## She has been working with Abigail Harper who is a graduate student at MIT.
        ## Abigail has been working on the project for over a year now and she feels like she is finally getting somewhere.
        ## She has been working with Nadia Kaminski who is a young woman who has been hired by Connor's boss to work on the Mars simulation project.
        ## Nadia is very excited about this opportunity because she believes that it will help her get a job at NASA when she graduates from college.
        ## Nadia is a hard worker and she is determined to succeed.
        ## Her father died when