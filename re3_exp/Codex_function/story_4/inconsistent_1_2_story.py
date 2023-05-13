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
        self.Shannon_Kincaid = character('Shannon Kincaid')
        self.Jack_Kincaid = character('Jack Kincaid')
        self.Mark_Woodbury = character('Mark Woodbury')

    def story(self):
        self.mark_woodbury_hurried_down_the_sidewalk_and_crossed_the_street()
        self.he_didn_t_have_time_to_be_late_for_his_date_with_shannon_kincaid_and_he_wanted_to_arrive_at_the_restaurant_early_so_he_could_beat_the_rush()
        self.as_he_neared_the_entrance_he_saw_her_waving_at_him_from_a_table_inside()
        self.i_m_sorry_i_m_late_mark_she_said_when_he_sat_down()
        self.i_was_held_up_in_traffic_on_the_way_here()
        self.how_are_you_mark_leaned_over_and_kissed_her_cheek()
        self.that_was_quite_a_jolt_you_gave_me_when_you_called_a_few_minutes_ago_and_said_you_were_running_late()
        self.but_i_guess_it_s_good_that_i_got_here_when_i_did()
        self.if_we_had_set_this_thing_for_any_later_we_would_have_missed_our_reservation_for_sure()
        self.they_were_about_to_turn_people_away_as_i_walked_up_here_shannon_laughed_lightly()
    def mark_woodbury_hurried_down_the_sidewalk_and_crossed_the_street(self):
        pass
    def he_didn_t_have_time_to_be_late_for_his_date_with_shannon_kincaid_and_he_wanted_to_arrive_at_the_restaurant_early_so_he_could_beat_the_rush(self):
        self.Mark_Woodbury.relations['date'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['date'] = 'Mark_Woodbury'
    def as_he_neared_the_entrance_he_saw_her_waving_at_him_from_a_table_inside(self):
        pass
    def i_m_sorry_i_m_late_mark_she_said_when_he_sat_down(self):
        pass
    def i_was_held_up_in_traffic_on_the_way_here(self):
        pass
    def how_are_you_mark_leaned_over_and_kissed_her_cheek(self):
        pass
    def that_was_quite_a_jolt_you_gave_me_when_you_called_a_few_minutes_ago_and_said_you_were_running_late(self):
        pass
    def but_i_guess_it_s_good_that_i_got_here_when_i_did(self):
        pass
    def if_we_had_set_this_thing_for_any_later_we_would_have_missed_our_reservation_for_sure(self):
        pass
    def they_were_about_to_turn_people_away_as_i_walked_up_here_shannon_laughed_lightly(self):
        pass

w = World()
w.story()

## Create a world model state to track each character's appearance, personality, and relations with other characters.

