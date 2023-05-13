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
        self.Riley_Harper = character('Riley Harper')
        self.Chase_Elliott = character('Chase Elliott')
        self.Jonas_Harper = character('Jonas Harper')

    def story(self):
        self.after_the_death_of_her_father_a_young_woman_moves_to_a_small_town_to_start_a_new_life()
        self.she_quickly_learns_that_the_town_is_full_of_secrets_and_that_her_father_s_death_may_not_have_been_an_accident()
        self.the_story_is_set_in_a_small_town_in_the_middle_of_nowhere()
        self.riley_harper_is_a_young_woman_in_her_early_twenties()
        self.she_has_long_dark_hair_and_hazel_eyes()
        self.she_is_of_average_height_and_build()
        self.chase_elliott_is_a_young_man_in_his_early_twenties_who_works_at_the_local_gas_station()
        self.he_has_dark_hair_and_brown_eyes_and_is_of_average_height_and_build()
        self.jonas_harper_is_riley_s_late_father()
        self.he_was_a_successful_businessman_who_died_suddenly_in_a_car_accident()
    def after_the_death_of_her_father_a_young_woman_moves_to_a_small_town_to_start_a_new_life(self):
        pass
    def she_quickly_learns_that_the_town_is_full_of_secrets_and_that_her_father_s_death_may_not_have_been_an_accident(self):
        pass
    def the_story_is_set_in_a_small_town_in_the_middle_of_nowhere(self):
        pass
    def riley_harper_is_a_young_woman_in_her_early_twenties(self):
        self.Riley_Harper.gender.append('female')
        self.Riley_Harper.age.append('young')
    def she_has_long_dark_hair_and_hazel_eyes(self):
        self.Riley_Harper.appearance.append('long dark hair')
        self.Riley_Harper.appearance.append('hazel eyes')
    def she_is_of_average_height_and_build(self):
        self.Riley_Harper.appearance.append('average height')
        self.Riley_Harper.appearance.append('average build')
    def chase_elliott_is_a_young_man_in_his_early_twenties_who_works_at_the_local_gas_station(self):
        self.Chase_Elliott.gender.append('male')
        self.Chase_Elliott.age.append('young')
        self.Chase_Elliott.occupation.append('gas station')
    def he_has_dark_hair_and_brown_eyes_and_is_of_average_height_and_build(self):
        self.Chase_Elliott.appearance.append('dark hair')
        self.Chase_Elliott.appearance.append('brown eyes')
        self.Chase_Elliott.appearance.append('average height')
        self.Chase_Elliott.appearance.append('average build')
    def jonas_harper_is_riley_s_late_father(self):
        self.Riley_Harper.relations['father'] = 'Jonas_Harper'
        self.Jonas_Harper.relations['daughter'] = 'Riley_Harper'
    def he_was_a_successful_businessman_who_died_suddenly_in_a_car_accident(self):
        self.Jonas_Harper.occupation.append('businessman')
        self.Jonas_Harper.occupation.append('dead')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

