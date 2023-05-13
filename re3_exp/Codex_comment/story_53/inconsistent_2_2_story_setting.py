## A young woman wakes up one day to find that she has been transformed into a bird.
## She must figure out how to reverse the spell with the help of a magical creature she meets.
## The story is set in a modern-day city, in an apartment complex.
## Jane Doe is a young woman in her early twenties.
## She has long, dark hair and brown eyes.
## She is of average height and build.
## Mister Snuggles is a small, furry creature with big ears and a long tail.
## He is Jane's friend and helper.
## Jessica Brown is Jane's sister, who is also transformed into a bird.
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
        ## A young woman wakes up one day to find that she has been transformed into a bird.
        ## She must figure out how to reverse the spell with the help of a magical creature she meets.
        ## The story is set in a modern-day city, in an apartment complex.
        ## Jane Doe is a young woman in her early twenties.
        self.Jane_Doe.age.append('young')
        self.Jane_Doe.gender.append('female')
        ## She has long, dark hair and brown eyes.
        self.Jane_Doe.appearance.append('long, dark hair')
        self.Jane_Doe.appearance.append('brown eyes')
        ## She is of average height and build.
        self.Jane_Doe.appearance.append('average height')
        self.Jane_Doe.appearance.append('average build')
        ## Mister Snuggles is a small, furry creature with big ears and a long tail.
        self.Mister_Snuggles.appearance.append('small')
        self.Mister_Snuggles.appearance.append('furry')
        self.Mister_Snuggles.appearance.append('big ears')
        self.Mister_Snuggles.appearance.append('long tail')
        ## He is Jane's friend and helper.
        self.Jane_Doe.relations['friend'] = 'Mister_Snuggles'
        self.Mister_Snuggles.relations['helper'] = 'Jane_Doe'
        ## Jessica Brown is Jane's sister, who is also transformed into a bird.
        self.Jane_Doe.relations['sister'] = 'Jessica_Brown'
        self.Jessica_Brown.relations['sister'] = 'Jane_Doe'
        self.Jessica_Brown.gender.append('female')

