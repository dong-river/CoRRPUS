## The grass is always greener on the other side.
## This is a lesson that John learns the hard way when he cheated on his wife with her best friend.
## When he tries to reconcile with his wife, he realizes that she has been cheating on him with her best friend's husband.
## The story is set in a small town in the midwest.
## Sarah Mason is a beautiful woman with long blond hair and blue eyes.
## She is the wife of John Mason and the mother of two children.
## Rachel Stephenson is Sarah's best friend and the wife of Richard Stevenson.
## John Mason is Sarah's husband and the father of two children.
## He is a successful businessman who has a wandering eye.
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
        ## The grass is always greener on the other side.
        ## This is a lesson that John learns the hard way when he cheated on his wife with her best friend.
        self.John_Mason.relations['wife'] = 'Sarah_Mason'
        self.John_Mason.relations['best_friend'] = 'Rachel_Stephenson'
        ## When he tries to reconcile with his wife, he realizes that she has been cheating on him with her best friend's husband.
        self.Sarah_Mason.relations['husband'] = 'John_Mason'
        self.Sarah_Mason.relations['best_friend'] = 'Rachel_Stephenson'
        ## The story is set in a small town in the midwest.
        ## Sarah Mason is a beautiful woman with long blond hair and blue eyes.
        self.Sarah_Mason.appearance.append('long blond hair')
        self.Sarah_Mason.appearance.append('blue eyes')
        ## She is the wife of John Mason and the mother of two children.
        self.Sarah_Mason.relations['husband'] = 'John_Mason'
        self.Sarah_Mason.relations['children'] = '2'
        ## Rachel Stephenson is Sarah's best friend and the wife of Richard Stevenson.
        self.Rachel_Stephenson.relations['best_friend'] = 'Sarah_Mason'
        self.Rachel_Stephenson.relations['husband'] = 'Richard_Stevenson'
        ## John Mason is Sarah's husband and the father of two children.
        self.John_Mason.relations['wife'] = 'Sarah_Mason'
        self.John_Mason.relations['children'] = '2'
        ## He is a successful businessman who has a wandering eye.
        self.John_Mason.occupation.append('successful businessman')

