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
        self.Mark_Woodbury.appearance.append("hurry")
        self.Mark_Woodbury.appearance.append("sidewalk")
        self.Mark_Woodbury.appearance.append("street")
    def he_didn_t_have_time_to_be_late_for_his_date_with_shannon_kincaid_and_he_wanted_to_arrive_at_the_restaurant_early_so_he_could_beat_the_rush(self):
        self.Mark_Woodbury.relations['date'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['date'] = 'Mark_Woodbury'
        self.Mark_Woodbury.appearance.append("early")
        self.Mark_Woodbury.appearance.append("restaurant")
    def as_he_neared_the_entrance_he_saw_her_waving_at_him_from_a_table_inside(self):
        self.Mark_Woodbury.appearance.append("entrance")
        self.Shannon_Kincaid.appearance.append("table")
        self.Shannon_Kincaid.appearance.append("inside")
    def i_m_sorry_i_m_late_mark_she_said_when_he_sat_down(self):
        self.Mark_Woodbury.appearance.append("late")
        self.Shannon_Kincaid.appearance.append("sat")
    def i_was_held_up_in_traffic_on_the_way_here(self):
        self.Shannon_Kincaid.appearance.append("traffic")
    def how_are_you_mark_leaned_over_and_kissed_her_cheek(self):
        self.Mark_Woodbury.appearance.append("leaned")
        self.Mark_Woodbury.appearance.append("kissed")
        self.Shannon_Kincaid.appearance.append("cheek")
    def that_was_quite_a_jolt_you_gave_me_when_you_called_a_few_minutes_ago_and_said_you_were_running_late(self):
        self.Shannon_Kincaid.appearance.append("jolt")
        self.Shannon_Kincaid.appearance.append("called")
        self.Shannon_Kincaid.appearance.append("minutes")
        self.Shannon_Kincaid.appearance.append("ago")
        self.Shannon_Kincaid.appearance.append("running")
        self.Shannon_Kincaid.appearance.append("late")
    def but_i_guess_it_s_good_that_i_got_here_when_i_did(self):
        self.Shannon_Kincaid.appearance.append("good")
        self.Shannon_Kincaid.appearance.append("got")
        self.Shannon_Kincaid.appearance.append("did")
    def if_we_had_set_this_thing_for_any_later_we_would_have_missed_our_reservation_for_sure(self):
        self.Shannon_Kincaid.appearance.append("set")
        self.Shannon_Kincaid.appearance.append("later")
        self.Shannon_Kincaid.appearance.append("missed")
        self.Shannon_Kincaid.appearance.append("reservation")
        self.Shannon_Kincaid.appearance.append("sure")
    def they_were_about_to_turn_people_away_as_i_walked_up_here_shannon_laughed_lightly(self):
        self.Shannon_Kincaid.appearance.append("turn")
        self.Shannon_Kincaid.appearance.append("people")
        self.Shannon_Kincaid.appearance.append("away")
        self.Shannon_Kincaid.appearance.append("walked")
        self.Shannon_Kincaid.appearance.append("up")
        self.Shannon_Kincaid.appearance.append("here")
        self.Shannon_Kincaid.appearance.append("laughed")
        self.Shannon_Kincaid.appearance.append("lightly")

## Create a world model state to track each character's appearance, personality, and relations with other characters.

