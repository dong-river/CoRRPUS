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
        self.Charles_Wilson = character('Charles Wilson')
        self.Nina_Peterson = character('Nina Peterson')
        self.Jeff_Foster = character('Jeff Foster')

    def story(self):
        self.charles_wilson_sits_in_his_office_filling_out_reports()
        self.he_s_in_his_forties_in_good_shape_and_has_short_black_hair()
        self.his_wife_is_out_shopping()
        self.she_thinks_he_s_at_work_but_instead_he_s_sitting_at_his_desk_daydreaming_about_the_girl_he_s_been_dating_for_the_past_few_weeks()
        self.she_s_a_college_student_and_is_twenty_years_younger_than_him_but_charles_doesn_not_care()
        self.as_long_as_she_has_a_pulse_she_can_have_him()
        self.he_fantasizes_about_taking_her_to_dinner_tomorrow_night_and_ending_up_back_at_her_place_to_have_sex()
        self.he_thinks_about_bending_her_over_putting_it_in_doggy_style_pounding_away_until_she_moans()
        self.he_thinks_about_pounding_her_until_she_screams_for_mercy_begging_him_to_stop_with_tears_streaming_down_her_face_good_afternoon_charles()
        self.his_sergeant_calls_from_the_doorway_of_his_office_waking_him_from_his_fantasy()
        self.just_wanted_to_let_you_know_we_just_got_a_rape_case_down_on_the_south_side()
        self.great()
        self.charles_said_sarcastically_with_a_sigh()
        self.when_do_i_get_my_vacation()
        self.his_sergeant_laughs_as_he_walks_away_leaving_charles_alone_with_his_fantasies_again()
    def charles_wilson_sits_in_his_office_filling_out_reports(self):
        pass
    def he_s_in_his_forties_in_good_shape_and_has_short_black_hair(self):
        self.Charles_Wilson.age.append('forties')
        self.Charles_Wilson.appearance.append('short black hair')
    def his_wife_is_out_shopping(self):
        self.Charles_Wilson.relations['wife'] = 'Nina_Peterson'
        self.Nina_Peterson.relations['husband'] = 'Charles_Wilson'
    def she_thinks_he_s_at_work_but_instead_he_s_sitting_at_his_desk_daydreaming_about_the_girl_he_s_been_dating_for_the_past_few_weeks(self):
        self.Charles_Wilson.relations['girl'] = 'Jeff_Foster'
        self.Jeff_Foster.relations['boy'] = 'Charles_Wilson'
    def she_s_a_college_student_and_is_twenty_years_younger_than_him_but_charles_doesn_not_care(self):
        self.Jeff_Foster.age.append('twenty years younger')
        self.Jeff_Foster.occupation.append('college student')
    def as_long_as_she_has_a_pulse_she_can_have_him(self):
        pass
    def he_fantasizes_about_taking_her_to_dinner_tomorrow_night_and_ending_up_back_at_her_place_to_have_sex(self):
        pass
    def he_thinks_about_bending_her_over_putting_it_in_doggy_style_pounding_away_until_she_moans(self):
        pass
    def he_thinks_about_pounding_her_until_she_screams_for_mercy_begging_him_to_stop_with_tears_streaming_down_her_face_good_afternoon_charles(self):
        pass
    def his_sergeant_calls_from_the_doorway_of_his_office_waking_him_from_his_fantasy(self):
        self.Charles_Wilson.relations['sergeant'] = 'Jeff_Foster'
        self.Jeff_Foster.relations['officer'] = 'Charles_Wilson'
    def just_wanted_to_let_you_know_we_just_got_a_rape_case_down_on_the_south_side(self):
        pass
    def great(self):
        pass
    def charles_said_sarcastically_with_a_sigh(self):
        pass
    def when_do_i_get_my_vacation(self):
        pass
    def his_sergeant_laughs_as_he_walks_away_leaving_charles_alone_with_his_fantasies_again(self):
        pass
        
w = World()
w.story()

