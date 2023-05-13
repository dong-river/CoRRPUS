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
        self.Payton_Parskin = character('Payton Parskin')
        self.Landon_Shaw = character('Landon Shaw')
        self.Maggie_Shaw = character('Maggie Shaw')

    def story(self):
        self.approximately_a_year_ago_29_year_old_payton_parskin_was_in_a_fatal_car_accident()
        self.she_died_instantly_and_went_to_heaven()
        self.but_payton_made_a_deal_with_god_that_if_he_let_her_back_on_earth_for_just_one_day_she_would_spend_that_day_doing_good_deeds()
        self.the_day_comes_and_payton_wakes_up_alive_and_well()
        self.she_isn_not_quite_sure_what_to_do_with_her_day_but_she_is_determined_to_make_the_most_of_it()
        self.the_story_is_set_in_the_present_day_in_a_small_town()
        self.payton_parskin_is_a_beautiful_young_woman_with_long_blonde_hair_and_blue_eyes()
        self.she_is_29_years_old_and_was_killed_in_a_car_accident_approximately_a_year_ago()
        self.landon_shaw_is_a_30_year_old_man_who_was_payton_s_fiancé_at_the_time_of_her_death()
        self.he_works_as_a_doctor_and_is_still_struggling_to_deal_with_payton_s_sudden_and_tragic_passing()
        self.maggie_shaw_is_landon_s_sister_and_payton_s_best_friend()
        self.she_is_25_years_old_and_works_as_a_teacher()
    def approximately_a_year_ago_29_year_old_payton_parskin_was_in_a_fatal_car_accident(self):
        self.Payton_Parskin.gender.append('female')
        self.Payton_Parskin.age.append(29)
    def she_died_instantly_and_went_to_heaven(self):
        pass
    def but_payton_made_a_deal_with_god_that_if_he_let_her_back_on_earth_for_just_one_day_she_would_spend_that_day_doing_good_deeds(self):
        pass
    def the_day_comes_and_payton_wakes_up_alive_and_well(self):
        pass
    def she_isn_not_quite_sure_what_to_do_with_her_day_but_she_is_determined_to_make_the_most_of_it(self):
        pass
    def the_story_is_set_in_the_present_day_in_a_small_town(self):
        pass
    def payton_parskin_is_a_beautiful_young_woman_with_long_blonde_hair_and_blue_eyes(self):
        self.Payton_Parskin.appearance.append('blonde hair')
        self.Payton_Parskin.appearance.append('blue eyes')
    def she_is_29_years_old_and_was_killed_in_a_car_accident_approximately_a_year_ago(self):
        self.Payton_Parskin.age.append(29)
    def landon_shaw_is_a_30_year_old_man_who_was_payton_s_fiancé_at_the_time_of_her_death(self):
        self.Landon_Shaw.gender.append('male')
        self.Landon_Shaw.age.append(30)
        self.Payton_Parskin.relations['fiancé'] = 'Landon_Shaw'
        self.Landon_Shaw.relations['fiancé'] = 'Payton_Parskin'
    def he_works_as_a_doctor_and_is_still_struggling_to_deal_with_payton_s_sudden_and_tragic_passing(self):
        self.Landon_Shaw.occupation.append('doctor')
    def maggie_shaw_is_landon_s_sister_and_payton_s_best_friend(self):
        self.Maggie_Shaw.gender.append('female')
        self.Landon_Shaw.relations['sister'] = 'Maggie_Shaw'
        self.Maggie_Shaw.relations['brother'] = 'Landon_Shaw'
        self.Payton_Parskin.relations['best friend'] = 'Maggie_Shaw'
        self.Maggie_Shaw.relations['best friend'] = 'Payton_Parskin'
    def she_is_25_years_old_and_works_as_a_teacher(self):
        self.Maggie_Shaw.age.append(25)
        self.Maggie_Shaw.occupation.append('teacher')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

