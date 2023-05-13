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
        self.Karen_Smith = character('Karen Smith')
        self.Janice_Smith = character('Janice Smith')
        self.Leah_White = character('Leah White')

    def story(self):
        self.a_girl_is_juggling_her_job_her_schoolwork_and_her_ailing_mother()
        self.when_her_mother_finally_passes_away_the_girl_is_left_with_an_immense_sense_of_guilt()
        self.the_story_is_set_in_a_small_town_in_the_midwest()
        self.karen_smith_is_a_young_woman_in_her_early_twenties()
        self.she_has_shoulder_length_brown_hair_and_brown_eyes()
        self.she_is_of_average_height_and_build()
        self.janice_smith_is_karen_s_mother()
        self.she_is_in_her_early_fifties_and_is_quite_ill_she_has_short_graying_hair_and_blue_eyes()
        self.leah_white_is_karen_s_best_friend()
        self.she_is_also_in_her_early_twenties_and_has_shoulder_length_blond_hair_and_blue_eyes()
    def a_girl_is_juggling_her_job_her_schoolwork_and_her_ailing_mother(self):
        self.Karen_Smith.gender.append('female')
    def when_her_mother_finally_passes_away_the_girl_is_left_with_an_immense_sense_of_guilt(self):
        self.Janice_Smith.relations['daughter'] = 'Karen_Smith'
        self.Karen_Smith.relations['mother'] = 'Janice_Smith'
    def the_story_is_set_in_a_small_town_in_the_midwest(self):
        pass
    def karen_smith_is_a_young_woman_in_her_early_twenties(self):
        self.Karen_Smith.age.append('early twenties')
    def she_has_shoulder_length_brown_hair_and_brown_eyes(self):
        self.Karen_Smith.appearance.append("brown hair")
        self.Karen_Smith.appearance.append("brown eyes")
    def she_is_of_average_height_and_build(self):
        pass
    def janice_smith_is_karen_s_mother(self):
        self.Karen_Smith.relations['mother'] = 'Janice_Smith'
        self.Janice_Smith.relations['daughter'] = 'Karen_Smith'
    def she_is_in_her_early_fifties_and_is_quite_ill_she_has_short_graying_hair_and_blue_eyes(self):
        self.Janice_Smith.age.append('early fifties')
        self.Janice_Smith.appearance.append("short gray hair")
        self.Janice_Smith.appearance.append("blue eyes")
    def leah_white_is_karen_s_best_friend(self):
        self.Karen_Smith.relations['best friend'] = 'Leah_White'
        self.Leah_White.relations['best friend'] = 'Karen_Smith'
    def she_is_also_in_her_early_twenties_and_has_shoulder_length_blond_hair_and_blue_eyes(self):
        self.Leah_White.age.append('early twenties')
        self.Leah_White.appearance.append("blond hair")
        self.Leah_White.appearance.append("blue eyes")

## Create a world model state to track each character's appearance, personality, and relations with other characters.

