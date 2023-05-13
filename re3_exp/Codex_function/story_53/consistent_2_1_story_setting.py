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
        self.a_young_woman_wakes_up_one_day_to_find_that_she_has_been_transformed_into_a_bird()
        self.she_must_figure_out_how_to_reverse_the_spell_with_the_help_of_a_magical_creature_she_meets()
        self.the_story_is_set_in_a_modern_day_city_in_an_apartment_complex()
        self.jane_doe_is_a_young_woman_in_her_early_twenties()
        self.she_has_long_dark_hair_and_brown_eyes()
        self.she_is_of_average_height_and_build()
        self.mister_snuggles_is_a_small_furry_creature_with_big_ears_and_a_long_tail()
        self.he_is_jane_s_friend_and_helper()
        self.jessica_brown_is_jane_s_sister_who_is_also_transformed_into_a_bird()
    def a_young_woman_wakes_up_one_day_to_find_that_she_has_been_transformed_into_a_bird(self):
        self.Jane_Doe.gender.append('female')
        self.Jane_Doe.age.append('young')
        self.Jane_Doe.appearance.append('bird')
    def she_must_figure_out_how_to_reverse_the_spell_with_the_help_of_a_magical_creature_she_meets(self):
        self.Mister_Snuggles.appearance.append('magical')
    def the_story_is_set_in_a_modern_day_city_in_an_apartment_complex(self):
        pass
    def jane_doe_is_a_young_woman_in_her_early_twenties(self):
        self.Jane_Doe.age.append('early twenties')
    def she_has_long_dark_hair_and_brown_eyes(self):
        self.Jane_Doe.appearance.append('long dark hair')
        self.Jane_Doe.appearance.append('brown eyes')
    def she_is_of_average_height_and_build(self):
        self.Jane_Doe.appearance.append('average height')
        self.Jane_Doe.appearance.append('average build')
    def mister_snuggles_is_a_small_furry_creature_with_big_ears_and_a_long_tail(self):
        self.Mister_Snuggles.appearance.append('small')
        self.Mister_Snuggles.appearance.append('furry')
        self.Mister_Snuggles.appearance.append('big ears')
        self.Mister_Snuggles.appearance.append('long tail')
    def he_is_jane_s_friend_and_helper(self):
        self.Jane_Doe.relations['friend'] = 'Mister_Snuggles'
        self.Mister_Snuggles.relations['helper'] = 'Jane_Doe'
    def jessica_brown_is_jane_s_sister_who_is_also_transformed_into_a_bird(self):
        self.Jane_Doe.relations['sister'] = 'Jessica_Brown'
        self.Jessica_Brown.relations['sister'] = 'Jane_Doe'
        self.Jessica_Brown.appearance.append('bird')

