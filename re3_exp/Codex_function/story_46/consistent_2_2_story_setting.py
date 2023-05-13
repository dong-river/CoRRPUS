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
        self.a_young_woman_fresh_out_of_college_moves_to_new_york_city_to_start_her_dream_job_but_discovers_that_the_reality_of_working_in_the_fashion_industry_is_far_different_from_what_she_expected()
        self.the_story_is_set_in_new_york_city()
        self.jessica_campbell_is_a_22_year_old_woman_who_has_just_graduated_from_college()
        self.she_is_tall_and_thin_with_long_blond_hair_and_blue_eyes()
        self.john_smith_is_a_26_year_old_man_who_works_as_a_model()
        self.he_is_tall_and_handsome_with_short_brown_hair_and_blue_eyes()
        self.tina_sanchez_is_a_22_year_old_woman_who_works_as_a_model()
        self.she_is_short_and_thin_with_long_black_hair_and_brown_eyes()
    def a_young_woman_fresh_out_of_college_moves_to_new_york_city_to_start_her_dream_job_but_discovers_that_the_reality_of_working_in_the_fashion_industry_is_far_different_from_what_she_expected(self):
        pass
    def the_story_is_set_in_new_york_city(self):
        pass
    def jessica_campbell_is_a_22_year_old_woman_who_has_just_graduated_from_college(self):
        self.Jessica_Campbell.age.append('22')
        self.Jessica_Campbell.gender.append('female')
    def she_is_tall_and_thin_with_long_blond_hair_and_blue_eyes(self):
        self.Jessica_Campbell.appearance.append('tall')
        self.Jessica_Campbell.appearance.append('thin')
        self.Jessica_Campbell.appearance.append('long blond hair')
        self.Jessica_Campbell.appearance.append('blue eyes')
    def john_smith_is_a_26_year_old_man_who_works_as_a_model(self):
        self.John_Smith.age.append('26')
        self.John_Smith.gender.append('male')
        self.John_Smith.occupation.append('model')
    def he_is_tall_and_handsome_with_short_brown_hair_and_blue_eyes(self):
        self.John_Smith.appearance.append('tall')
        self.John_Smith.appearance.append('handsome')
        self.John_Smith.appearance.append('short brown hair')
        self.John_Smith.appearance.append('blue eyes')
    def tina_sanchez_is_a_22_year_old_woman_who_works_as_a_model(self):
        self.Tina_Sanchez.age.append('22')
        self.Tina_Sanchez.gender.append('female')
        self.Tina_Sanchez.occupation.append('model')
    def she_is_short_and_thin_with_long_black_hair_and_brown_eyes(self):
        self.Tina_Sanchez.appearance.append('short')
        self.Tina_Sanchez.appearance.append('thin')
        self.Tina_Sanchez.appearance.append('long black hair')
        self.Tina_Sanchez.appearance.append('brown eyes')
        
# Create a world model state to track each character's appearance, personality, and relations with other characters.

