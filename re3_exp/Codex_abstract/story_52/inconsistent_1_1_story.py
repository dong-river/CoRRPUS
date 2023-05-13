## Rachel Stephenson stood at the sink, drinking a glass of wine and reflecting on her life.
## She was not unhappy.
## But she wasn't exactly happy either.
## She lived in a beautiful house in a nice neighborhood with her husband Richard Stevenson.
## She had two wonderful children, Jonathan and Cynthia.
## In many ways, Rachel was content with her life as it was.
## The trouble was that Richard didn't bring her much excitement in bed anymore.
## The truth be told, he hadn't for a long time now, even when they were first married ten years ago, which was how they met in the first place.
## Richard had been paying more attention to his work lately than he did to her.
## More and more often she would find him sitting at his desk late into the night working on something rather than coming to bed where he belonged by their bedside clock it would sometimes be one or two in the morning before he'd come to bed where his wife would be patiently waiting for him even though she knew what kind of a night he'd have for sexual gratification!
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
        self.Sarah_Mason = character('Sarah Mason')
        self.Rachel_Stephenson = character('Rachel Stephenson')
        self.John_Mason = character('John Mason')

    def story(self):
        ## Rachel Stephenson stood at the sink, drinking a glass of wine and reflecting on her life.
        self.Rachel_Stephenson.appearance.append('stand')
        self.Rachel_Stephenson.appearance.append('sink')
        self.Rachel_Stephenson.appearance.append('drink')
        self.Rachel_Stephenson.appearance.append('wine')
        self.Rachel_Stephenson.appearance.append('reflect')
        ## She was not unhappy.
        self.Rachel_Stephenson.appearance.append('unhappy')
        ## But she wasn't exactly happy either.
        self.Rachel_Stephenson.appearance.append('happy')
        ## She lived in a beautiful house in a nice neighborhood with her husband Richard Stevenson.
        self.Rachel_Stephenson.relations['husband'] = 'Richard_Stevenson'
        self.Richard_Stevenson.relations['wife'] = 'Rachel_Stephenson'
        ## She had two wonderful children, Jonathan and Cynthia.
        self.Rachel_Stephenson.relations['children'] = 'John_Mason'
        self.Rachel_Stephenson.relations['children'] = 'Sarah_Mason'
        self.John_Mason.relations['mother'] = 'Rachel_Stephenson'
        self.Sarah_Mason.relations['mother'] = 'Rachel_Stephenson'
        ## In many ways, Rachel was content with her life as it was.
        ## The trouble was that Richard didn't bring her much excitement in bed anymore.
        self.Richard_Stevenson.appearance.append('excitement')
        ## The truth be told, he hadn't for a long time now, even when they were first married ten years ago, which was how they met in the first place.
        self.Richard_Stevenson.appearance.append('married')
        ## Richard had been paying more attention to his work lately than he did to her.
        self.Richard_Stevenson.appearance.append('attention')
        ## More and more often she would find him sitting at his desk late into the night working on something rather than coming to bed where he belonged by their bedside clock it would sometimes be one or two in the morning before he'd come to bed where his wife would be patiently waiting for him even though she knew what kind of a night he'd have for sexual gratification!
        self.Richard_Stevenson.appearance.append('desk')
        self.Richard_Stevenson.appearance.append('working')
        self.Richard_Stevenson.appearance.append('bed')
        self.Richard_Stevenson.appearance.append('clock')
        self.Richard_Stevenson.appearance.append('gratification')
        
