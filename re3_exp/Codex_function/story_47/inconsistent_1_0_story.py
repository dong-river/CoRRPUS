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
        self.Shannon_Burke = character('Shannon Burke')
        self.Charles_Burke = character('Charles Burke')
        self.Maxine_Carter = character('Maxine Carter')

    def story(self):
        self.maxine_carter_knocked_on_the_apartment_door_and_waited()
        self.she_hated_doing_this_she_much_preferred_dropping_off_the_food_that_she_cooked_for_shannon_s_boyfriend_but_he_had_insisted()
        self.a_minute_later_she_heard_steps_coming_down_the_hall_and_a_moment_later_shannon_opened_the_door()
        self.maxine_smiled_at_her_daughter()
        self.is_everything_all_right()
        self.he_didn_not_hit_you_again_did_he()
        self.shannon_rolled_her_eyes()
        self.no_mom_he_didn_not_hit_me_again()
        self.then_she_grinned_mischievously()
        self.we_had_a_great_time()
        self.we_went_to_bed_early_and_i_can_tell_you_that_neither_of_us_was_asleep_when_we_got_up()
        self.maxine_tried_to_suppress_a_smile_as_she_realized_what_her_daughter_meant()
        self.the_young_man_who_had_asked_shannon_out_a_few_weeks_ago_seemed_too_good_to_be_true_smart_and_charming_with_just_enough_edge_in_his_personality_to_make_him_mysterious()
        self.but_although_maxine_had_always_been_wary_of_men_like_that_shannon_was_of_legal_age_and_had_no_intention_of_listening_to_her_mother_s_advice_about_dating_anyone_less_than_perfect_or_even_only_nearly_perfect()
    def maxine_carter_knocked_on_the_apartment_door_and_waited(self):
        pass
    def she_hated_doing_this_she_much_preferred_dropping_off_the_food_that_she_cooked_for_shannon_s_boyfriend_but_he_had_insisted(self):
        self.Maxine_Carter.relations['daughter'] = 'Shannon_Burke'
        self.Shannon_Burke.relations['mother'] = 'Maxine_Carter'
    def a_minute_later_she_heard_steps_coming_down_the_hall_and_a_moment_later_shannon_opened_the_door(self):
        pass
    def maxine_smiled_at_her_daughter(self):
        pass
    def is_everything_all_right(self):
        pass
    def he_didn_not_hit_you_again_did_he(self):
        pass
    def shannon_rolled_her_eyes(self):
        pass
    def no_mom_he_didn_not_hit_me_again(self):
        pass
    def then_she_grinned_mischievously(self):
        pass
    def we_had_a_great_time(self):
        pass
    def we_went_to_bed_early_and_i_can_tell_you_that_neither_of_us_was_asleep_when_we_got_up(self):
        pass
    def maxine_tried_to_suppress_a_smile_as_she_realized_what_her_daughter_meant(self):
        pass
    def the_young_man_who_had_asked_shannon_out_a_few_weeks_ago_seemed_too_good_to_be_true_smart_and_charming_with_just_enough_edge_in_his_personality_to_make_him_mysterious(self):
        pass
    def but_although_maxine_had_always_been_wary_of_men_like_that_shannon_was_of_legal_age_and_had_no_intention_of_listening_to_her_mother_s_advice_about_dating_anyone_less_than_perfect_or_even_only_nearly_perfect(self):
        self.Shannon_Burke.relations['boyfriend'] = 'Charles_Burke'
        self.Charles_Burke.relations['girlfriend'] = 'Shannon_Burke'

## Create a world model state to track each character's appearance, personality, and relations with other characters.

