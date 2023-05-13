## Tina Sanchez sat behind the mirror in her large dressing room, dabbing makeup on a young model’s face.
## “Turn your head slightly,” she instructed.
## “That’s it, yes!
## Perfect!
## You are so beautiful!
## The designer will be ecstatic.
## I just know it.
## You know how strict he is about his designs being showcased by only the best-looking models he can find.
## This is going to be a big show!”  Tina glanced around the room at all the other stylists working on other models.
## They were everywhere, creating intricate hairstyles and painting beautiful designs on faces and bodies to match the clothing they were dressing.
## She smiled at her own reflection in the mirror—her thick black hair was swept back from her face and she had on perfectly applied makeup that perfectly matched her short black dress that perfectly matched her shoes that perfectly matched everything else about her appearance today.
## There was nothing about her that wasn’t perfect in every detail, no matter what others might say about it all—perfectly understated and incredibly chic, perfect for working in the New York fashion industry where only the best of everything counted for anything at all…
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
        self.Jessica_Campbell = character('Jessica Campbell')
        self.John_Smith = character('John Smith')
        self.Tina_Sanchez = character('Tina Sanchez')

    def story(self):
        ## Tina Sanchez sat behind the mirror in her large dressing room, dabbing makeup on a young model’s face.
        self.Tina_Sanchez.gender.append('female')
        self.Tina_Sanchez.occupation.append('makeup artist')
        ## “Turn your head slightly,” she instructed.
        ## “That’s it, yes!
        ## Perfect!
        ## You are so beautiful!
        ## The designer will be ecstatic.
        ## I just know it.
        ## You know how strict he is about his designs being showcased by only the best-looking models he can find.
        ## This is going to be a big show!”  Tina glanced around the room at all the other stylists working on other models.
        ## They were everywhere, creating intricate hairstyles and painting beautiful designs on faces and bodies to match the clothing they were dressing.
        ## She smiled at her own reflection in the mirror—her thick black hair was swept back from her face and she had on perfectly applied makeup that perfectly matched her short black dress that perfectly matched her shoes that perfectly matched everything else about her appearance today.
        ## There was nothing about her that wasn’t perfect in every detail, no matter what others might say about it all—perfectly understated and incredibly chic, perfect for working in the New York fashion industry where only the best of everything counted for anything at all…

