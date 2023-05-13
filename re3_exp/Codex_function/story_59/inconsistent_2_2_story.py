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
        self.Payton_Parskin = character('Payton Parskin')
        self.Landon_Shaw = character('Landon Shaw')
        self.Maggie_Shaw = character('Maggie Shaw')

    def story(self):
        self.landon_shaw_the_handsome_mechanic_was_just_climbing_into_bed_when_his_sister_maggie_barged_in_without_knocking()
        self.what_is_it()
        self.he_asked_irritably()
        self.he_was_exhausted_and_was_hoping_to_get_a_full_eight_hours_of_sleep_tonight_but_that_seemed_unlikely_now()
        self.i_need_to_talk_to_you_she_said_insistently()
        self.landon_didn_not_want_to_talk_he_wanted_to_sleep_but_maggie_looked_so_desperate_that_he_couldn_not_say_no()
        self.fine_he_said_in_an_irritated_tone_what_do_you_want()
        self.maggie_sat_down_on_the_edge_of_her_brother_s_bed_and_took_a_deep_breath()
        self.i_need_your_help()
        self.her_words_sounded_thick_with_tears()
        self.you_are_my_only_hope()
        self.she_had_waited_until_she_knew_her_brother_would_be_home_before_she_came_over_and_now_it_was_already_after_midnight_there_wasn_not_much_time_left_to_make_him_change_his_mind_about_her_plan()
        self.what_are_you_talking_about()
        self.landon_replied_harshly()
        self.just_spit_it_out_already()
        self.he_rolled_over_and_turned_off_the_light_by_his_side_of_the_bed_before_settling_down_to_go_back_to_sleep_for_just_another_few_minutes_before_his_alarm_clock_would_go_off_in_a_couple_of_hours_anyway()
    def landon_shaw_the_handsome_mechanic_was_just_climbing_into_bed_when_his_sister_maggie_barged_in_without_knocking(self):
        self.Landon_Shaw.appearance.append('handsome')
        self.Landon_Shaw.occupation.append('mechanic')
        self.Landon_Shaw.relations['sister'] = 'Maggie_Shaw'
        self.Maggie_Shaw.relations['brother'] = 'Landon_Shaw'
        self.Landon_Shaw.gender.append('male')
        self.Maggie_Shaw.gender.append('female')
        
    def what_is_it(self):
        pass
        
    def he_asked_irritably(self):
        pass
        
    def he_was_exhausted_and_was_hoping_to_get_a_full_eight_hours_of_sleep_tonight_but_that_seemed_unlikely_now(self):
        pass
        
    def i_need_to_talk_to_you_she_said_insistently(self):
        pass
        
    def landon_didn_not_want_to_talk_he_wanted_to_sleep_but_maggie_looked_so_desperate_that_he_couldn_not_say_no(self):
        pass
        
    def fine_he_said_in_an_irritated_tone_what_do_you_want(self):
        pass
        
    def maggie_sat_down_on_the_edge_of_her_brother_s_bed_and_took_a_deep_breath(self):
        pass
        
    def i_need_your_help(self):
        pass
        
    def her_words_sounded_thick_with_tears(self):
        pass
        
    def you_are_my_only_hope(self):
        pass
        
    def she_had_waited_until_she_knew_her_brother_would_be_home_before_she_came_over_and_now_it_was_already_after_midnight_there_wasn_not_much_time_left_to_make_him_change_his_mind_about_her_plan(self):
        pass
        
    def what_are_you_talking_about(self):
        pass
        
    def landon_replied_harshly(self):
        pass
        
    def just_spit_it_out_already(self):
        pass
        
    def he_rolled_over_and_turned_off_the_light_by_his_side_of_the_bed_before_settling_down_to_go_back_to_sleep_for_just_another_few_minutes_before_his_alarm_clock_would_go_off_in_a_couple_of_hours_anyway(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

