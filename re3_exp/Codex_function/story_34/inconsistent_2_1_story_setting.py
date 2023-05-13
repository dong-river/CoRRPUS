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
        self.Will_Trenton = character('Will Trenton')
        self.Amanda_Wilkinson = character('Amanda Wilkinson')
        self.Thomas_Watkins = character('Thomas Watkins')

    def story(self):
        self.the_townspeople_of_a_small_town_in_the_middle_of_nowhere_are_constantly_being_terrorized_by_a_serial_killer_who_only_comes_out_at_night()
        self.they_re_all_too_scared_to_leave_their_homes_after_dark_so_they_ve_hired_a_group_of_mercenaries_to_help_them_protect_themselves()
        self.the_mercenaries_are_good_at_their_jobs_but_they_re_not_prepared_for_the_sheer_brutality_of_the_killer()
        self.the_story_is_set_in_a_remote_rural_town_that_is_plagued_by_a_relentless_and_brutal_serial_killer()
        self.will_trenton_is_a_former_soldier_who_now_works_as_a_mercenary()
        self.he_s_a_tough_and_experienced_fighter_who_is_not_afraid_of_the_killer()
        self.amanda_wilkinson_is_a_local_woman_who_is_terrified_of_the_serial_killer()
        self.she_s_been_living_in_fear_for_months_and_is_ready_to_do_whatever_it_takes_to_protect_herself()
        self.thomas_watkins_is_the_sheriff_of_the_small_town()
        self.he_s_a_good_man_who_wants_to_protect_his_people_but_he_s_out_of_his_depth_when_it_comes_to_the_serial_killer()
    def the_townspeople_of_a_small_town_in_the_middle_of_nowhere_are_constantly_being_terrorized_by_a_serial_killer_who_only_comes_out_at_night(self):
        pass
        
    def they_re_all_too_scared_to_leave_their_homes_after_dark_so_they_ve_hired_a_group_of_mercenaries_to_help_them_protect_themselves(self):
        pass
        
    def the_mercenaries_are_good_at_their_jobs_but_they_re_not_prepared_for_the_sheer_brutality_of_the_killer(self):
        pass
        
    def the_story_is_set_in_a_remote_rural_town_that_is_plagued_by_a_relentless_and_brutal_serial_killer(self):
        pass
        
    def will_trenton_is_a_former_soldier_who_now_works_as_a_mercenary(self):
        self.Will_Trenton.occupation.append('mercenary')
        self.Will_Trenton.gender.append('male')
        
    def he_s_a_tough_and_experienced_fighter_who_is_not_afraid_of_the_killer(self):
        self.Will_Trenton.appearance.append('tough')
        self.Will_Trenton.appearance.append('experienced')
        
    def amanda_wilkinson_is_a_local_woman_who_is_terrified_of_the_serial_killer(self):
        self.Amanda_Wilkinson.gender.append('female')
        self.Amanda_Wilkinson.appearance.append('terrified')
        
    def she_s_been_living_in_fear_for_months_and_is_ready_to_do_whatever_it_takes_to_protect_herself(self):
        pass
        
    def thomas_watkins_is_the_sheriff_of_the_small_town(self):
        self.Thomas_Watkins.occupation.append('sheriff')
        self.Thomas_Watkins.gender.append('male')
        
    def he_s_a_good_man_who_wants_to_protect_his_people_but_he_s_out_of_his_depth_when_it_comes_to_the_serial_killer(self):
        self.Thomas_Watkins.appearance.append('good')
        self.Thomas_Watkins.appearance.append('out of depth')
        
## Create a world model state to track each character's appearance, personality, and relations with other characters.

