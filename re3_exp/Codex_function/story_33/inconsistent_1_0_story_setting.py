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
        self.Charles_Wilson = character('Charles Wilson')
        self.Nina_Peterson = character('Nina Peterson')
        self.Jeff_Foster = character('Jeff Foster')

    def story(self):
        self.nina_a_college_student_is_studying_for_her_final_exams_and_is_struggling_to_stay_focused()
        self.she_takes_a_break_from_studying_to_go_for_a_walk_and_ends_up_at_a_bar()
        self.she_has_a_few_drinks_and_starts_chatting_with_the_guy_next_to_her()
        self.they_hit_it_off_and_end_up_back_at_his_place()
        self.nina_wakes_up_the_next_morning_naked_in_his_bed_with_no_recollection_of_what_happened()
        self.she_panics_and_quickly_leaves()
        self.the_guy_tries_to_stop_her_but_she_s_out_the_door_before_he_can_say_anything()
        self.nina_doesn_not_want_to_believe_she_was_raped_but_she_can_not_remember_what_happened()
        self.the_story_is_set_in_a_college_town()
        self.charles_wilson_is_a_young_man_in_his_early_twenties()
        self.he_s_of_average_height_with_brown_hair_and_eyes()
        self.he_s_generally_a_good_guy_but_he_has_a_bit_of_a_temper()
        self.nina_peterson_is_a_young_woman_in_her_early_twenties()
        self.she_s_about_5_4_with_long_blonde_hair_and_blue_eyes()
        self.she_s_a_bit_shy_and_introverted_but_generally_a_good_person()
        self.jeff_foster_is_the_man_who_nina_meets_at_the_bar_and_brings_home_with_her()
        self.he_s_in_his_early_thirties_and_is_of_average_height_with_dark_hair_and_eyes()
    def the_story_is_set_in_a_college_town(self):
        pass
    def charles_wilson_is_a_young_man_in_his_early_twenties(self):
        self.Charles_Wilson.age.append('young')
        self.Charles_Wilson.gender.append('male')
    def he_s_of_average_height_with_brown_hair_and_eyes(self):
        self.Charles_Wilson.appearance.append('average height')
        self.Charles_Wilson.appearance.append('brown hair')
        self.Charles_Wilson.appearance.append('brown eyes')
    def he_s_generally_a_good_guy_but_he_has_a_bit_of_a_temper(self):
        pass
    def nina_peterson_is_a_young_woman_in_her_early_twenties(self):
        self.Nina_Peterson.age.append('young')
        self.Nina_Peterson.gender.append('female')
    def she_s_about_5_4_with_long_blonde_hair_and_blue_eyes(self):
        self.Nina_Peterson.appearance.append('about 5\'4"')
        self.Nina_Peterson.appearance.append('long blonde hair')
        self.Nina_Peterson.appearance.append('blue eyes')
    def she_s_a_bit_shy_and_introverted_but_generally_a_good_person(self):
        pass
    def jeff_foster_is_the_man_who_nina_meets_at_the_bar_and_brings_home_with_her(self):
        self.Nina_Peterson.relations['meets'] = 'Jeff_Foster'
    def he_s_in_his_early_thirties_and_is_of_average_height_with_dark_hair_and_eyes(self):
        self.Jeff_Foster.age.append('early thirties')
        self.Jeff_Foster.appearance.append('average height')
        self.Jeff_Foster.appearance.append('dark hair')
        self.Jeff_Foster.appearance.append('dark eyes')


## Create a world model state to track each character's appearance, personality, and relations with other characters.
