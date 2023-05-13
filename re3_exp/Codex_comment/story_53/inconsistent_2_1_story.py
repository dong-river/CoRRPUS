## Jessica Brown was Jane's best friend since childhood.
## She was visiting her in her apartment that evening.
## They were both sitting on the couch, watching TV.
## Jane had a frown on her face, she was confused and upset about something.
## "Jessica," she said, "what's wrong?"
## "Nothing is wrong," Jessica replied, though she knew it wasn't true.
## "Why do you ask?"
## "Because you don't look like yourself."
## "Oh, sorry.
## I've been thinking about something."
## "What have you been thinking about?"
## Jane asked, slightly curious as to what her friend had been up to all day while she was out of the apartment.
## In all honesty, Jane had hardly any close friends other than Jessica; she didn't seem to make many friends during the years of high school and university and was always too shy to start a conversation with anyone else whenever the opportunity presented itself for fear of being rejected.
## Her only other significant friendship in life came from childhood when she spent almost every day with Jessica who lived next door with her family.
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
        self.Jane_Doe = character('Jane Doe')
        self.Mister_Snuggles = character('Mister Snuggles')
        self.Jessica_Brown = character('Jessica Brown')

    def story(self):
        ## Jane Doe is a woman who has died in a car accident. She is a kind and sympathetic person who is eager to help the people she left behind.
        self.Jane_Doe.gender.append('female')
        ## Mister Snuggles is Jane's cat. He is a kind and loving man who is struggling to cope with his wife's death.
        self.Jane_Doe.relations['cat'] = 'Mister_Snuggles'
        self.Mister_Snuggles.relations['owner'] = 'Jane_Doe'
        self.Mister_Snuggles.gender.append('male')
        ## Jessica Brown was Jane's best friend since childhood.
        self.Jane_Doe.relations['best_friend'] = 'Jessica_Brown'
        self.Jessica_Brown.relations['best_friend'] = 'Jane_Doe'
        ## She was visiting her in her apartment that evening.
        ## They were both sitting on the couch, watching TV.
        ## Jane had a frown on her face, she was confused and upset about something.
        self.Jane_Doe.appearance.append("frown")
        ## "Jessica," she said, "what's wrong?"
        ## "Nothing is wrong," Jessica replied, though she knew it wasn't true.
        ## "Why do you ask?"
        ## "Because you don't look like yourself."
        ## "Oh, sorry.
        ## I've been thinking about something."
        ## "What have you been thinking about?"
        ## Jane asked, slightly curious as to what her friend had been up to all day while she was out of the apartment.
        ## In all honesty, Jane had hardly any close friends other than Jessica; she didn't seem to make many friends during the years of high school and university and was always too shy to start a conversation with anyone else whenever the opportunity presented itself for fear of being rejected.
        ## Her only other significant friendship in life came from childhood when she spent almost every day with Jessica who lived next door with her family.

