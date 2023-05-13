## Landon Shaw stood over the metal table, his stethoscope on and his head bent down to listen to the heart of the dead girl lying before him.
## He was 30 years old and wore a black coat over a crisp white shirt and tie.
## His hair was short and spiky on top, like he had just walked out of a movie with Leonardo DiCaprio in it.
## He turned to the nurse next to him, a pretty brunette with a tight ponytail.
## "Could you write that down for me?"
## Landon asked her, referring to her notepad where she had written down what he said about the body on the table in front of them.
## "Could you tell me again what she said?"
## The nurse shrugged, pointing back at Landon with her pen.
## "You were there."
## Landon rolled his eyes and returned his attention to the body lying before him.
## The only body he'd been able to work on since Payton's accident almost one year ago; something he felt immensely guilty about but couldn't seem to control.
## Payton was his fiancé, not even wife yet and now she's gone for good just as he got that promise ring on her finger.
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
        ## Landon Shaw stood over the metal table, his stethoscope on and his head bent down to listen to the heart of the dead girl lying before him.
        self.Landon_Shaw.appearance.append("black coat")
        self.Landon_Shaw.appearance.append("white shirt")
        self.Landon_Shaw.appearance.append("tie")
        self.Landon_Shaw.appearance.append("spiky hair")
        self.Landon_Shaw.occupation.append("doctor")
        ## He was 30 years old and wore a black coat over a crisp white shirt and tie.
        self.Landon_Shaw.age.append("30")
        ## His hair was short and spiky on top, like he had just walked out of a movie with Leonardo DiCaprio in it.
        self.Landon_Shaw.appearance.append("short hair")
        ## He turned to the nurse next to him, a pretty brunette with a tight ponytail.
        self.Maggie_Shaw.appearance.append("brunette")
        self.Maggie_Shaw.appearance.append("ponytail")
        ## "Could you write that down for me?"
        ## Landon asked her, referring to her notepad where she had written down what he said about the body on the table in front of them.
        ## "Could you tell me again what she said?"
        ## The nurse shrugged, pointing back at Landon with her pen.
        ## "You were there."
        ## Landon rolled his eyes and returned his attention to the body lying before him.
        ## The only body he'd been able to work on since Payton's accident almost one year ago; something he felt immensely guilty about but couldn't seem to control.
        self.Payton_Parskin.relations['fiance'] = 'Landon_Shaw'
        self.Landon_Shaw.relations['fiance'] = 'Payton_Parskin'
        ## Payton was his fiancé, not even wife yet and now she's gone for good just as he got that promise ring on her finger.

