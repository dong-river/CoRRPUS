## Approximately a year ago, 29 year old Payton Parskin was in a fatal car accident.
## She died instantly and went to Heaven.
## But, Payton made a deal with God that if he let her back on Earth for just one day, she would spend that day doing good deeds.
## The day comes and Payton wakes up alive and well.
## She isn't quite sure what to do with her day but she is determined to make the most of it.
## The story is set in the present day in a small town.
## Payton Parskin is a beautiful young woman with long blonde hair and blue eyes.
## She is 29 years old and was killed in a car accident approximately a year ago.
## Landon Shaw is a handsome young man who was Payton's boyfriend at the time of her death.
## He is 27 years old and works as a mechanic.
## Maggie Shaw is Landon's sister and Payton's best friend.
## She is 25 years old and works as a teacher.
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
        self.Payton_Parskin = character('Payton Parskin')
        self.Landon_Shaw = character('Landon Shaw')
        self.Maggie_Shaw = character('Maggie Shaw')

    def story(self):
        ## Approximately a year ago, 29 year old Payton Parskin was in a fatal car accident.
        self.Payton_Parskin.age.append('29')
        ## She died instantly and went to Heaven.
        ## But, Payton made a deal with God that if he let her back on Earth for just one day, she would spend that day doing good deeds.
        ## The day comes and Payton wakes up alive and well.
        ## She isn't quite sure what to do with her day but she is determined to make the most of it.
        ## The story is set in the present day in a small town.
        ## Payton Parskin is a beautiful young woman with long blonde hair and blue eyes.
        self.Payton_Parskin.appearance.append('long blonde hair')
        self.Payton_Parskin.appearance.append('blue eyes')
        self.Payton_Parskin.gender.append('female')
        ## She is 29 years old and was killed in a car accident approximately a year ago.
        self.Payton_Parskin.age.append('29')
        ## Landon Shaw is a handsome young man who was Payton's boyfriend at the time of her death.
        self.Payton_Parskin.relations['boyfriend'] = 'Landon_Shaw'
        self.Landon_Shaw.relations['girlfriend'] = 'Payton_Parskin'
        self.Landon_Shaw.appearance.append('handsome')
        self.Landon_Shaw.age.append('27')
        self.Landon_Shaw.gender.append('male')
        ## He is 27 years old and works as a mechanic.
        self.Landon_Shaw.occupation.append('mechanic')
        ## Maggie Shaw is Landon's sister and Payton's best friend.
        self.Landon_Shaw.relations['sister'] = 'Maggie_Shaw'
        self.Maggie_Shaw.relations['brother'] = 'Landon_Shaw'
        self.Payton_Parskin.relations['best_friend'] = 'Maggie_Shaw'
        self.Maggie_Shaw.relations['best_friend'] = 'Payton_Parskin'
        ## She is 25 years old and works as a teacher.
        self.Maggie_Shaw.age.append('25')
        self.Maggie_Shaw.occupation.append('teacher')
        self.Maggie_Shaw.gender.append('female')

