## John Doe sat at his desk staring out the window.
## He stared at the parked cars, their roofs covered in snow.
## Everything was so quiet and still; a perfect scene to frame the past few months.
## John shook his head and glanced back at his computer screen.
## He needed to stay focused if he wanted to get this done by five o'clock.
## The thing is, he didn't really want to get it done by five o'clock; he wanted a real job where he didn't have to deal with all of this extra responsibility.
## John's boss, Mr. Benson, had been pressuring him to sell more merchandise because of the slow economy over the past few months.
## This forced John to work longer hours and spend less time with Abby on their date nights.
## "John!"
## John spun around in his chair just as Mr. Benson walked into his office.
## "How's everything going?"
## John hesitated for a moment before responding and Mr. Benson jumped on this small sign of weakness.
## "Everything okay?
## If you have any problems just let me know," he said in a deep voice as he nodded toward John's computer screen.
## "Well," John started, "I think I'm going to need some extra time with my work today."
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
        ## John Doe sat at his desk staring out the window.
        ## He stared at the parked cars, their roofs covered in snow.
        ## Everything was so quiet and still; a perfect scene to frame the past few months.
        ## John shook his head and glanced back at his computer screen.
        ## He needed to stay focused if he wanted to get this done by five o'clock.
        ## The thing is, he didn't really want to get it done by five o'clock; he wanted a real job where he didn't have to deal with all of this extra responsibility.
        ## John's boss, Mr. Benson, had been pressuring him to sell more merchandise because of the slow economy over the past few months.
        ## This forced John to work longer hours and spend less time with Abby on their date nights.
        self.John_Doe.relations['boss'] = 'Mike_Benson'
        self.Mike_Benson.relations['employee'] = 'John_Doe'
        self.John_Doe.relations['girlfriend'] = 'Abby_Mills'
        self.Abby_Mills.relations['boyfriend'] = 'John_Doe'
        ## "John!"
        ## John spun around in his chair just as Mr. Benson walked into his office.
        ## "How's everything going?"
        ## John hesitated for a moment before responding and Mr. Benson jumped on this small sign of weakness.
        ## "Everything okay?
        ## If you have any problems just let me know," he said in a deep voice as he nodded toward John's computer screen.
        ## "Well," John started, "I think I'm going to need some extra time with my work today."

