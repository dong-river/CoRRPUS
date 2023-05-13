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
        self.Jennifer_Ann_Smith = character('Jennifer Ann Smith')
        self.Clara_Smith = character('Clara Smith')
        self.Robert_Smith = character('Robert Smith')

    def story(self):
        self.after_a_long_day_at_work_the_last_thing_jennifer_wanted_was_to_deal_with_her_phone_ringing_off_the_hook()
        self.she_thought_about_ignoring_it_but_she_knew_her_mother_would_just_keep_calling_back_until_she_answered()
        self.jennifer_sure_wasn_not_in_the_mood_to_listen_to_her_mother_complain_about_her_life_but_she_didn_not_have_a_choice()
        self.the_story_is_set_in_jennifer_s_home_after_she_has_gotten_off_from_work()
        self.jennifer_ann_smith_is_a_27_year_old_woman_who_has_just_moved_into_a_new_apartment_and_started_a_new_job_as_a_receptionist_at_an_office_building_downtown_chicago_illinois_united_states_of_america_clara_smith_is_jennifer_s_mother()
        self.she_is_a_heavyset_woman_in_her_late_50s_with_graying_hair_that_she_often_dyes_blonde()
        self.robert_smith_is_jennifer_s_father()
        self.he_is_a_tall_man_in_his_early_60s_with_thinning_gray_hair_and_a_mustache()
    def after_a_long_day_at_work_the_last_thing_jennifer_wanted_was_to_deal_with_her_phone_ringing_off_the_hook(self):
        pass
    def she_thought_about_ignoring_it_but_she_knew_her_mother_would_just_keep_calling_back_until_she_answered(self):
        pass
    def jennifer_sure_wasn_not_in_the_mood_to_listen_to_her_mother_complain_about_her_life_but_she_didn_not_have_a_choice(self):
        pass
    def the_story_is_set_in_jennifer_s_home_after_she_has_gotten_off_from_work(self):
        pass
    def jennifer_ann_smith_is_a_27_year_old_woman_who_has_just_moved_into_a_new_apartment_and_started_a_new_job_as_a_receptionist_at_an_office_building_downtown_chicago_illinois_united_states_of_america_clara_smith_is_jennifer_s_mother(self):
        self.Jennifer_Ann_Smith.age.append('27')
        self.Jennifer_Ann_Smith.gender.append('female')
        self.Clara_Smith.relations['daughter'] = 'Jennifer_Ann_Smith'
        self.Jennifer_Ann_Smith.relations['mother'] = 'Clara_Smith'
    def she_is_a_heavyset_woman_in_her_late_50s_with_graying_hair_that_she_often_dyes_blonde(self):
        self.Clara_Smith.age.append('late 50s')
        self.Clara_Smith.gender.append('female')
        self.Clara_Smith.appearance.append('heavyset')
    def robert_smith_is_jennifer_s_father(self):
        self.Jennifer_Ann_Smith.relations['father'] = 'Robert_Smith'
        self.Robert_Smith.relations['daughter'] = 'Jennifer_Ann_Smith'
    def he_is_a_tall_man_in_his_early_60s_with_thinning_gray_hair_and_a_mustache(self):
        self.Robert_Smith.age.append('early 60s')
        self.Robert_Smith.gender.append('male')
        self.Robert_Smith.appearance.append('tall')
        self.Robert_Smith.appearance.append('thinning gray hair')
        self.Robert_Smith.appearance.append('mustache')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

