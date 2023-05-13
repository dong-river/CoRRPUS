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
        self.John_Doe = character('John Doe')
        self.Abby_Mills = character('Abby Mills')
        self.Mike_Benson = character('Mike Benson')

    def story(self):
        self.john_doe_was_packing_up_his_truck_and_preparing_to_leave_the_small_town_he_d_been_living_in()
        self.he_would_be_forced_to_leave_the_town_if_he_wanted_to_get_back_on_his_feet_after_losing_his_job()
        self.the_job_had_given_him_a_place_to_live_and_with_the_large_paychecks_he_was_making_each_week_he_was_able_to_save_up_some_money()
        self.his_truck_was_filled_with_boxes_of_clothes_and_essentials_such_as_clothing_and_personal_belongings_for_when_he_had_needed_to_travel_for_work_or_when_he_was_between_jobs()
        self.he_had_originally_planned_on_staying_in_the_town_for_at_least_a_few_months_before_moving_on_to_another_one_but_now_he_didn_not_have_that_option()
        self.he_d_have_to_move_on_sooner_than_expected_if_he_wanted_something_more_than_this_small_town()
        self.it_wasn_not_just_a_small_town_it_was_an_out_of_the_way_place_that_lacked_any_real_opportunities_besides_being_a_construction_worker_in_order_to_make_ends_meet()
        self.no_matter_how_hard_john_worked_it_didn_not_seem_like_there_were_enough_jobs_available_that_paid_as_well_as_what_john_had_been_getting_at_his_last_job_in_atlanta_therefore_john_would_have_struggled_even_harder_than_before_once_he_found_another_construction_gig_again_elsewhere_outside_of_the_small_town()
    def john_doe_was_packing_up_his_truck_and_preparing_to_leave_the_small_town_he_d_been_living_in(self):
        self.John_Doe.occupation.append('construction worker')
    def he_would_be_forced_to_leave_the_town_if_he_wanted_to_get_back_on_his_feet_after_losing_his_job(self):
        self.John_Doe.relations['sister'] = 'Abby_Mills'
        self.Abby_Mills.relations['brother'] = 'John_Doe'
    def the_job_had_given_him_a_place_to_live_and_with_the_large_paychecks_he_was_making_each_week_he_was_able_to_save_up_some_money(self):
        pass
    def his_truck_was_filled_with_boxes_of_clothes_and_essentials_such_as_clothing_and_personal_belongings_for_when_he_had_needed_to_travel_for_work_or_when_he_was_between_jobs(self):
        pass
    def he_had_originally_planned_on_staying_in_the_town_for_at_least_a_few_months_before_moving_on_to_another_one_but_now_he_didn_not_have_that_option(self):
        pass
    def he_d_have_to_move_on_sooner_than_expected_if_he_wanted_something_more_than_this_small_town(self):
        pass
    def it_wasn_not_just_a_small_town_it_was_an_out_of_the_way_place_that_lacked_any_real_opportunities_besides_being_a_construction_worker_in_order_to_make_ends_meet(self):
        pass
    def no_matter_how_hard_john_worked_it_didn_not_seem_like_there_were_enough_jobs_available_that_paid_as_well_as_what_john_had_been_getting_at_his_last_job_in_atlanta_therefore_john_would_have_struggled_even_harder_than_before_once_he_found_another_construction_gig_again_elsewhere_outside_of_the_small_town(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

