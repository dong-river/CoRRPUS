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
        self.emily_hellinger_is_sherry_s_wife_of_15_years()
        self.she_is_a_tall_woman_with_short_brown_hair_and_hazel_eyes()
        self.she_is_in_her_early_40s()
        self.john_hellinger_is_sherry_s_older_brother()
        self.he_is_a_tall_man_with_short_brown_hair_and_blue_eyes()
        self.he_is_in_his_early_40s()
    def the_story_is_set_in_the_present_day_in_a_small_town_in_the_midwest(self):
        pass
    def sherry_hellinger_is_a_middle_aged_woman_with_short_brown_hair_and_green_eyes(self):
        self.Sherry_Hellinger.age.append('middle-aged')
        self.Sherry_Hellinger.appearance.append('short brown hair')
        self.Sherry_Hellinger.appearance.append('green eyes')
        self.Sherry_Hellinger.gender.append('female')
    def she_is_of_average_height_and_build(self):
        pass
    def emily_hellinger_is_sherry_s_wife_of_15_years(self):
        self.Sherry_Hellinger.relations['wife'] = 'Emily_Hellinger'
        self.Emily_Hellinger.relations['spouse'] = 'Sherry_Hellinger'
        self.Emily_Hellinger.age.append('early-40s')
        self.Emily_Hellinger.appearance.append('short brown hair')
        self.Emily_Hellinger.appearance.append('hazel eyes')
        self.Emily_Hellinger.gender.append('female')
    def she_is_a_tall_woman_with_short_brown_hair_and_hazel_eyes(self):
        pass
    def she_is_in_her_early_40s(self):
        pass
    def john_hellinger_is_sherry_s_older_brother(self):
        self.Sherry_Hellinger.relations['brother'] = 'John_Hellinger'
        self.John_Hellinger.relations['sister'] = 'Sherry_Hellinger'
        self.John_Hellinger.age.append('early-40s')
        self.John_Hellinger.appearance.append('short brown hair')
        self.John_Hellinger.appearance.append('blue eyes')
        self.John_Hellinger.gender.append('male')
    def he_is_a_tall_man_with_short_brown_hair_and_blue_eyes(self):
        pass
    def he_is_in_his_early_40s(self):
        pass
    def sherry_had_the_perfect_life_three_healthy_children_a_loving_wife_and_a_job_to_support_them_until_she_discovers_what_was_happening_right_in_front_of_her(self):
        pass
    def sherry_s_wife_has_been_cheating_on_her_with_her_brother_ever_since_they_ve_been_married(self):
        pass
    def a_panic_attack_at_work_forces_sherry_to_deal_with_her_personal_life_head_on(self):
        pass
    def after_gaining_some_closure_she_moves_out_of_state_with_her_children_to_start_afresh(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

