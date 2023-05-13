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
        self.john_doe_sat_at_his_desk_staring_out_the_window()
        self.he_stared_at_the_parked_cars_their_roofs_covered_in_snow()
        self.everything_was_so_quiet_and_still_a_perfect_scene_to_frame_the_past_few_months()
        self.john_shook_his_head_and_glanced_back_at_his_computer_screen()
        self.he_needed_to_stay_focused_if_he_wanted_to_get_this_done_by_five_o_clock()
        self.the_thing_is_he_didn_not_really_want_to_get_it_done_by_five_o_clock_he_wanted_a_real_job_where_he_didn_not_have_to_deal_with_all_of_this_extra_responsibility()
        self.john_s_boss_mr_benson_had_been_pressuring_him_to_sell_more_merchandise_because_of_the_slow_economy_over_the_past_few_months()
        self.this_forced_john_to_work_longer_hours_and_spend_less_time_with_abby_on_their_date_nights()
        self.john()
        self.john_spun_around_in_his_chair_just_as_mr_benson_walked_into_his_office()
        self.how_s_everything_going()
        self.john_hesitated_for_a_moment_before_responding_and_mr_benson_jumped_on_this_small_sign_of_weakness()
        self.everything_okay()
        self.if_you_have_any_problems_just_let_me_know_he_said_in_a_deep_voice_as_he_nodded_toward_john_s_computer_screen()
        self.well_john_started_i_think_i_m_going_to_need_some_extra_time_with_my_work_today()
    def john_doe_sat_at_his_desk_staring_out_the_window(self):
        self.John_Doe.occupation.append('office worker')
    def he_stared_at_the_parked_cars_their_roofs_covered_in_snow(self):
        pass
    def everything_was_so_quiet_and_still_a_perfect_scene_to_frame_the_past_few_months(self):
        pass
    def john_shook_his_head_and_glanced_back_at_his_computer_screen(self):
        pass
    def he_needed_to_stay_focused_if_he_wanted_to_get_this_done_by_five_o_clock(self):
        pass
    def the_thing_is_he_didn_not_really_want_to_get_it_done_by_five_o_clock_he_wanted_a_real_job_where_he_didn_not_have_to_deal_with_all_of_this_extra_responsibility(self):
        pass
    def john_s_boss_mr_benson_had_been_pressuring_him_to_sell_more_merchandise_because_of_the_slow_economy_over_the_past_few_months(self):
        self.John_Doe.relations['boss'] = 'Mike_Benson'
        self.Mike_Benson.relations['employee'] = 'John_Doe'
    def this_forced_john_to_work_longer_hours_and_spend_less_time_with_abby_on_their_date_nights(self):
        self.John_Doe.relations['girlfriend'] = 'Abby_Mills'
        self.Abby_Mills.relations['boyfriend'] = 'John_Doe'
    def john(self):
        pass
    def john_spun_around_in_his_chair_just_as_mr_benson_walked_into_his_office(self):
        pass
    def how_s_everything_going(self):
        pass
    def john_hesitated_for_a_moment_before_responding_and_mr_benson_jumped_on_this_small_sign_of_weakness(self):
        pass
    def everything_okay(self):
        pass
    def if_you_have_any_problems_just_let_me_know_he_said_in_a_deep_voice_as_he_nodded_toward_john_s_computer_screen(self):
        pass
    def well_john_started_i_think_i_m_going_to_need_some_extra_time_with_my_work_today(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.
