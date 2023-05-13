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
        ## She was not unhappy.
        ## But she wasn't exactly happy either.
        ## She lived in a beautiful house in a nice neighborhood with her husband Richard Stevenson.
        self.Rachel_Stephenson.relations['husband'] = 'Richard_Stevenson'
        self.Richard_Stevenson.relations['wife'] = 'Rachel_Stephenson'
        self.Richard_Stevenson.appearance.append('handsome')
        ## She had two wonderful children, Jonathan and Cynthia.
        self.Rachel_Stephenson.relations['children'] = ['John_Mason', 'Cynthia_Mason']
        self.John_Mason.relations['mother'] = 'Rachel_Stephenson'
        self.John_Mason.relations['father'] = 'Richard_Stevenson'
        self.Cynthia_Mason.relations['mother'] = 'Rachel_Stephenson'
        self.Cynthia_Mason.relations['father'] = 'Richard_Stevenson'
        ## In many ways, Rachel was content with her life as it was.
        ## The trouble was that Richard didn't bring her much excitement in bed anymore.
        ## The truth be told, he hadn't for a long time now, even when they were first married ten years ago, which was how they met in the first place.
        ## Richard had been paying more attention to his work lately than he did to her.
        ## More and more often she would find him sitting at his desk late into the night working on something rather than coming to bed where he belonged by their bedside clock it would sometimes be one or two in the morning before he'd come to bed where his wife would be patiently waiting for him even though she knew what kind of a night he'd have for sexual gratification!

##
## The story is set in the present day and takes place in the United States.
## Joan Westfall is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind.
## Brent Westfall is Joan's husband. He is a kind and loving man who is struggling to cope with his wife's death.
## Jason Westfall is Joan's son. He is a young boy who is struggling to understand his mother's death.
## Jason Westfall sits on the floor, looking at the empty box that used to hold his sister-in-law's belongings. 
## His gaze is unfocused, his dark blue eyes brimming with tears.
## He cries for hours, eventually falling asleep from exhaustion.
## When he wakes up, he feels dazed and ill.
## Joan died in a car accident on a rainy day several weeks ago.
## Jason has been carrying on with life ever since as best he can manage, but he still doesn't really know how to cope with Joan's death.
## Create a world model state to track each character's appearance, personality, and relations with other characters.

