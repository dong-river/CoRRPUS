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
        self.emily_hellinger_awoke_to_her_alarm_clock_on_a_warm_morning_in_late_summer()
        self.she_lay_in_bed_and_stretched_noting_that_the_clock_was_5_30()
        self.emily_turned_off_the_alarm_and_stood_rubbing_her_eyes()
        self.the_tall_blonde_woman_looked_over_at_the_sleeping_form_of_her_wife_sherry_who_was_lying_on_her_side()
        self.emily_knelt_down_beside_the_bed_and_gazed_upon_sherry_s_sleeping_face()
        self.she_smiled_lightly_and_then_placed_a_soft_kiss_on_sherry_s_forehead()
        self.emily_rose_from_the_bed_and_went_into_the_bathroom()
        self.she_closed_the_door_behind_her_and_stood_in_front_of_the_mirror_above_the_sink_turning_on_a_light_switch()
        self.she_looked_at_herself_in_the_mirror_and_could_hardly_believe_how_young_she_looked_for_44_years_old()
        self.her_once_long_blonde_hair_had_been_cut_short_for_years_now_but_it_still_framed_her_oval_face_well_without_giving_off_an_aged_appearance_like_some_older_women_with_shorter_hair_tend_to_have()
        self.her_blue_eyes_were_as_vivid_as_ever_though_they_were_frequently_hidden_by_dark_sunglasses_that_hid_bags_under_them_from_lack_of_sleep_or_stress_related_issues_with_work_or_family_matters_it_all_depended_on_who_you_asked_about_it()
    def emily_hellinger_awoke_to_her_alarm_clock_on_a_warm_morning_in_late_summer(self):
        self.Emily_Hellinger.occupation.append("police officer")
        
    def she_lay_in_bed_and_stretched_noting_that_the_clock_was_5_30(self):
        pass
        
    def emily_turned_off_the_alarm_and_stood_rubbing_her_eyes(self):
        self.Emily_Hellinger.appearance.append("blue eyes")
        self.Emily_Hellinger.age.append("44")
        
    def the_tall_blonde_woman_looked_over_at_the_sleeping_form_of_her_wife_sherry_who_was_lying_on_her_side(self):
        self.Emily_Hellinger.relations['wife'] = 'Sherry_Hellinger'
        self.Sherry_Hellinger.relations['wife'] = 'Emily_Hellinger'
        self.Emily_Hellinger.gender.append('female')
        self.Sherry_Hellinger.gender.append('female')
        
    def emily_knelt_down_beside_the_bed_and_gazed_upon_sherry_s_sleeping_face(self):
        pass
        
    def she_smiled_lightly_and_then_placed_a_soft_kiss_on_sherry_s_forehead(self):
        pass
        
    def emily_rose_from_the_bed_and_went_into_the_bathroom(self):
        pass
        
    def she_closed_the_door_behind_her_and_stood_in_front_of_the_mirror_above_the_sink_turning_on_a_light_switch(self):
        pass
        
    def she_looked_at_herself_in_the_mirror_and_could_hardly_believe_how_young_she_looked_for_44_years_old(self):
        self.Emily_Hellinger.appearance.append("blonde hair")
        
    def her_once_long_blonde_hair_had_been_cut_short_for_years_now_but_it_still_framed_her_oval_face_well_without_giving_off_an_aged_appearance_like_some_older_women_with_shorter_hair_tend_to_have(self):
        pass
        
    def her_blue_eyes_were_as_vivid_as_ever_though_they_were_frequently_hidden_by_dark_sunglasses_that_hid_bags_under_them_from_lack_of_sleep_or_stress_related_issues_with_work_or_family_matters_it_all_depended_on_who_you_asked_about_it(self):
        pass
        
    def her_blue_eyes_were_as_vivid_as_ever_though_they_were_frequently_hidden_by_dark_sunglasses_that_hid_bags_under_them_from_lack_of_sleep_or_stress_related_issues_with_work_or_family_matters_it_all_depended_on_who_you_asked_about_it(self):
        pass


## Create a world model state to track each character's appearance, personality, and relations with other characters.

