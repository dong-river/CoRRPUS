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
        self.thomas_watkins_paced_around_his_office()
        self.as_the_new_sheriff_of_winterdale_he_was_responsible_for_maintaining_order_in_the_town()
        self.the_only_problem_was_that_it_seemed_like_no_one_cared_about_order_in_the_first_place()
        self.it_felt_like_every_day_he_had_to_solve_a_new_crime_or_resolve_a_new_dispute()
        self.winterdale_was_such_a_small_town_that_watkins_thought_things_would_be_more_peaceful_than_this_when_he_accepted_the_job()
        self.at_least_now_he_knew_why_no_one_else_wanted_it()
        self.watkins_had_just_finished_dealing_with_a_drunk_who_had_passed_out_on_main_street_and_had_to_move_him_out_of_the_way_before_someone_ran_over_him_in_the_middle_of_the_night()
        self.now_watkins_was_getting_ready_to_deal_with_an_infestation_of_bats_in_an_old_building_downtown_that_everyone_thought_was_haunted()
        self.the_people_there_were_scared_and_wanted_the_bats_gone_so_they_could_feel_safe_living_there_again_even_though_watkins_knew_they_were_probably_used_to_the_bats_by_now_and_didn_not_really_need_them_gone_anyway()
        self.as_watkins_headed_out_to_confront_the_bats_he_noticed_something_off_in_his_peripheral_vision_a_shadowy_figure_running_along_an_alleyway_nearby()
    def thomas_watkins_paced_around_his_office(self):
        self.Thomas_Watkins.occupation.append('sheriff')
        
    def as_the_new_sheriff_of_winterdale_he_was_responsible_for_maintaining_order_in_the_town(self):
        self.Thomas_Watkins.occupation.append('sheriff')
        
    def the_only_problem_was_that_it_seemed_like_no_one_cared_about_order_in_the_first_place(self):
        pass
        
    def it_felt_like_every_day_he_had_to_solve_a_new_crime_or_resolve_a_new_dispute(self):
        pass
        
    def winterdale_was_such_a_small_town_that_watkins_thought_things_would_be_more_peaceful_than_this_when_he_accepted_the_job(self):
        pass
        
    def at_least_now_he_knew_why_no_one_else_wanted_it(self):
        pass
        
    def watkins_had_just_finished_dealing_with_a_drunk_who_had_passed_out_on_main_street_and_had_to_move_him_out_of_the_way_before_someone_ran_over_him_in_the_middle_of_the_night(self):
        pass
        
    def now_watkins_was_getting_ready_to_deal_with_an_infestation_of_bats_in_an_old_building_downtown_that_everyone_thought_was_haunted(self):
        pass
        
    def the_people_there_were_scared_and_wanted_the_bats_gone_so_they_could_feel_safe_living_there_again_even_though_watkins_knew_they_were_probably_used_to_the_bats_by_now_and_didn_not_really_need_them_gone_anyway(self):
        pass
        
    def as_watkins_headed_out_to_confront_the_bats_he_noticed_something_off_in_his_peripheral_vision_a_shadowy_figure_running_along_an_alleyway_nearby(self):
        pass
        
## Create a world model state to track each character's appearance, personality, and relations with other characters.

