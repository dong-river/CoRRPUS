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
        self.Sherry_Hellinger = character('Sherry Hellinger')
        self.Emily_Hellinger = character('Emily Hellinger')
        self.John_Hellinger = character('John Hellinger')

    def story(self):
        self.sherry_had_the_perfect_life_three_healthy_children_a_loving_wife_and_a_job_to_support_them_until_she_discovers_what_was_happening_right_in_front_of_her()
        self.sherry_s_wife_has_been_cheating_on_her_with_her_brother_ever_since_they_ve_been_married()
        self.a_panic_attack_at_work_forces_sherry_to_deal_with_her_personal_life_head_on()
        self.after_gaining_some_closure_she_moves_out_of_state_with_her_children_to_start_afresh()
        self.the_story_is_set_in_the_present_day_in_a_small_town_in_the_midwest()
        self.sherry_hellinger_is_a_middle_aged_woman_with_short_brown_hair_and_green_eyes()
        self.she_is_of_average_height_and_build()
        self.emily_hellinger_is_sherry_s_wife_of_ten_years()
        self.she_is_a_tall_woman_with_long_blond_hair_and_blue_eyes()
        self.she_is_in_her_early_40s()
        self.john_hellinger_is_sherry_s_older_brother()
        self.he_is_a_tall_man_with_short_brown_hair_and_blue_eyes()
        self.he_is_in_his_early_40s()
    def sherry_had_the_perfect_life_three_healthy_children_a_loving_wife_and_a_job_to_support_them_until_she_discovers_what_was_happening_right_in_front_of_her(self):
        self.Sherry_Hellinger.occupation.append('support')
        self.Sherry_Hellinger.relations['children'] = 'three_healthy_children'
        self.Sherry_Hellinger.relations['wife'] = 'Emily_Hellinger'
    def sherry_s_wife_has_been_cheating_on_her_with_her_brother_ever_since_they_ve_been_married(self):
        self.Sherry_Hellinger.relations['brother'] = 'John_Hellinger'
    def a_panic_attack_at_work_forces_sherry_to_deal_with_her_personal_life_head_on(self):
        self.Sherry_Hellinger.occupation.append('work')
    def after_gaining_some_closure_she_moves_out_of_state_with_her_children_to_start_afresh(self):
        self.Sherry_Hellinger.relations['children'] = 'three_healthy_children'
    def the_story_is_set_in_the_present_day_in_a_small_town_in_the_midwest(self):
        pass
    def sherry_hellinger_is_a_middle_aged_woman_with_short_brown_hair_and_green_eyes(self):
        self.Sherry_Hellinger.appearance.append('short brown hair')
        self.Sherry_Hellinger.appearance.append('green eyes')
        self.Sherry_Hellinger.age.append('middle-aged')
    def she_is_of_average_height_and_build(self):
        pass
    def emily_hellinger_is_sherry_s_wife_of_ten_years(self):
        self.Sherry_Hellinger.relations['wife'] = 'Emily_Hellinger'
        self.Emily_Hellinger.relations['wife'] = 'Sherry_Hellinger'
    def she_is_a_tall_woman_with_long_blond_hair_and_blue_eyes(self):
        self.Emily_Hellinger.appearance.append('tall')
        self.Emily_Hellinger.appearance.append('long blond hair')
        self.Emily_Hellinger.appearance.append('blue eyes')
    def she_is_in_her_early_40s(self):
        self.Emily_Hellinger.age.append('early 40s')
    def john_hellinger_is_sherry_s_older_brother(self):
        self.Sherry_Hellinger.relations['brother'] = 'John_Hellinger'
        self.John_Hellinger.relations['brother'] = 'Sherry_Hellinger'
    def he_is_a_tall_man_with_short_brown_hair_and_blue_eyes(self):
        self.John_Hellinger.appearance.append('tall')
        self.John_Hellinger.appearance.append('short brown hair')
        self.John_Hellinger.appearance.append('blue eyes')
    def he_is_in_his_early_40s(self):
        self.John_Hellinger.age.append('early 40s')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

