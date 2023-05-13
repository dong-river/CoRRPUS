## After a year of being together, John andabegan to notice the cracks in their relationship.
## With jobs and school pulling them in different directions, they began to grow apart.
## However, when John loses his job and Abby is diagnosed with cancer, they are forced to lean on each other for support.
## Through their difficult journey, they realize that they still have feelings for each other and their relationship is stronger than ever.
## The story is set in a small town in the US.
## John Doe is a tall, handsome man in his early 30s.
## He has dark hair and eyes and is usually clean-shaven.
## He works as a salesperson for a local company.
## Abby Mills is a beautiful woman in her early 30s.
## She has blonde hair and blue eyes.
## She is a teacher at a local elementary school.
## Mike Benson is Abby's ex-boyfriend.
## He is in his early 30s and is also a teacher at the same elementary school as Abby.
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
        self.John_Doe = character('John Doe')
        self.Abby_Mills = character('Abby Mills')
        self.Mike_Benson = character('Mike Benson')

    def story(self):
        ## The story is set in a small town in the US.
        ## John Doe is a tall, handsome man in his early 30s.
        self.John_Doe.age.append('early 30s')
        self.John_Doe.appearance.append('tall')
        self.John_Doe.appearance.append('handsome')
        self.John_Doe.gender.append('male')
        ## He has dark hair and eyes and is usually clean-shaven.
        self.John_Doe.appearance.append('dark hair')
        self.John_Doe.appearance.append('dark eyes')
        self.John_Doe.appearance.append('clean-shaven')
        ## He works as a salesperson for a local company.
        self.John_Doe.occupation.append('salesperson')
        ## Abby Mills is a beautiful woman in her early 30s.
        self.Abby_Mills.age.append('early 30s')
        self.Abby_Mills.appearance.append('beautiful')
        self.Abby_Mills.gender.append('female')
        ## She has blonde hair and blue eyes.
        self.Abby_Mills.appearance.append('blonde hair')
        self.Abby_Mills.appearance.append('blue eyes')
        ## She is a teacher at a local elementary school.
        self.Abby_Mills.occupation.append('teacher')
        ## Mike Benson is Abby's ex-boyfriend.
        self.Mike_Benson.relations['ex-boyfriend'] = 'Abby_Mills'
        self.Abby_Mills.relations['ex-boyfriend'] = 'Mike_Benson'
        ## He is in his early 30s and is also a teacher at the same elementary school as Abby.
        self.Mike_Benson.age.append('early 30s')
        self.Mike_Benson.occupation.append('teacher')

