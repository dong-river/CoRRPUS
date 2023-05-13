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
        self.charles_wilson_is_a_police_detective_who_is_assigned_to_investigate_nina_s_case()
        self.he_s_in_his_forties_and_has_a_wife_and_two_kids_at_home()
        self.he_s_a_good_cop_but_he_s_also_a_bit_of_a_ladies_man_and_has_a_tendency_to_flirt_with_the_women_he_meets_on_the_job()
        self.nina_peterson_is_a_young_woman_in_her_early_twenties()
        self.she_s_about_5_4_with_long_blonde_hair_and_blue_eyes()
        self.she_s_a_bit_shy_and_introverted_but_generally_a_good_person()
        self.jeff_foster_is_the_man_who_nina_meets_at_the_bar_and_brings_home_with_her()
        self.he_s_in_his_early_thirties_and_is_of_average_height_with_dark_hair_and_eyes()
    def nina_a_college_student_is_studying_for_her_final_exams_and_is_struggling_to_stay_focused(self):
        self.Nina_Peterson.relations['college_student'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['final_exams'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['struggling_to_stay_focused'] = 'Nina_Peterson'
    def she_takes_a_break_from_studying_to_go_for_a_walk_and_ends_up_at_a_bar(self):
        self.Nina_Peterson.relations['break_from_studying'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['go_for_a_walk'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['ends_up_at_a_bar'] = 'Nina_Peterson'
    def she_has_a_few_drinks_and_starts_chatting_with_the_guy_next_to_her(self):
        self.Nina_Peterson.relations['few_drinks'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['starts_chatting_with_the_guy_next_to_her'] = 'Nina_Peterson'
    def they_hit_it_off_and_end_up_back_at_his_place(self):
        self.Nina_Peterson.relations['hit_it_off'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['end_up_back_at_his_place'] = 'Nina_Peterson'
    def nina_wakes_up_the_next_morning_naked_in_his_bed_with_no_recollection_of_what_happened(self):
        self.Nina_Peterson.relations['wakes_up_the_next_morning'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['naked_in_his_bed'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['no_recollection_of_what_happened'] = 'Nina_Peterson'
    def she_panics_and_quickly_leaves(self):
        self.Nina_Peterson.relations['panics'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['quickly_leaves'] = 'Nina_Peterson'
    def the_guy_tries_to_stop_her_but_she_s_out_the_door_before_he_can_say_anything(self):
        self.Nina_Peterson.relations['guy_tries_to_stop_her'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['she_s_out_the_door_before_he_can_say_anything'] = 'Nina_Peterson'
    def nina_doesn_not_want_to_believe_she_was_raped_but_she_can_not_remember_what_happened(self):
        self.Nina_Peterson.relations['doesn_not_want_to_believe_she_was_raped'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['she_can_not_remember_what_happened'] = 'Nina_Peterson'
    def the_story_is_set_in_a_college_town(self):
        self.Nina_Peterson.relations['story_is_set_in_a_college_town'] = 'Nina_Peterson'
    def charles_wilson_is_a_police_detective_who_is_assigned_to_investigate_nina_s_case(self):
        self.Charles_Wilson.relations['police_detective'] = 'Charles_Wilson'
        self.Charles_Wilson.relations['investigate_nina_s_case'] = 'Charles_Wilson'
    def he_s_in_his_forties_and_has_a_wife_and_two_kids_at_home(self):
        self.Charles_Wilson.relations['in_his_forties'] = 'Charles_Wilson'
        self.Charles_Wilson.relations['has_a_wife_and_two_kids_at_home'] = 'Charles_Wilson'
    def he_s_a_good_cop_but_he_s_also_a_bit_of_a_ladies_man_and_has_a_tendency_to_flirt_with_the_women_he_meets_on_the_job(self):
        self.Charles_Wilson.relations['good_cop'] = 'Charles_Wilson'
        self.Charles_Wilson.relations['bit_of_a_ladies_man'] = 'Charles_Wilson'
        self.Charles_Wilson.relations['has_a_tendency_to_flirt_with_the_women_he_meets_on_the_job'] = 'Charles_Wilson'
    def nina_peterson_is_a_young_woman_in_her_early_twenties(self):
        self.Nina_Peterson.relations['young_woman'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['early_twenties'] = 'Nina_Peterson'
    def she_s_about_5_4_with_long_blonde_hair_and_blue_eyes(self):
        self.Nina_Peterson.relations['about_5_4'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['long_blonde_hair'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['blue_eyes'] = 'Nina_Peterson'
    def she_s_a_bit_shy_and_introverted_but_generally_a_good_person(self):
        self.Nina_Peterson.relations['bit_shy'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['introverted'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['generally_a_good_person'] = 'Nina_Peterson'
    def jeff_foster_is_the_man_who_nina_meets_at_the_bar_and_brings_home_with_her(self):
        self.Jeff_Foster.relations['man_who_nina_meets_at_the_bar_and_brings_home_with_her'] = 'Jeff_Foster'
    def he_s_in_his_early_thirties_and_is_of_average_height_with_dark_hair_and_eyes(self):
        self.Jeff_Foster.relations['in_his_early_thirties'] = 'Jeff_Foster'
        self.Jeff_Foster.relations['is_of_average_height'] = 'Jeff_Foster'
        self.Jeff_Foster.relations['dark_hair_and_eyes'] = 'Jeff_Foster'

# Create a world model state to track each character's appearance, personality, and relations with other characters.

