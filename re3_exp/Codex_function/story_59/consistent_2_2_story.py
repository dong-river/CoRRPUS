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
        self.landon_shaw_stood_over_the_metal_table_his_stethoscope_on_and_his_head_bent_down_to_listen_to_the_heart_of_the_dead_girl_lying_before_him()
        self.he_was_30_years_old_and_wore_a_black_coat_over_a_crisp_white_shirt_and_tie()
        self.his_hair_was_short_and_spiky_on_top_like_he_had_just_walked_out_of_a_movie_with_leonardo_dicaprio_in_it()
        self.he_turned_to_the_nurse_next_to_him_a_pretty_brunette_with_a_tight_ponytail()
        self.could_you_write_that_down_for_me()
        self.landon_asked_her_referring_to_her_notepad_where_she_had_written_down_what_he_said_about_the_body_on_the_table_in_front_of_them()
        self.could_you_tell_me_again_what_she_said()
        self.the_nurse_shrugged_pointing_back_at_landon_with_her_pen()
        self.you_were_there()
        self.landon_rolled_his_eyes_and_returned_his_attention_to_the_body_lying_before_him()
        self.the_only_body_he_d_been_able_to_work_on_since_payton_s_accident_almost_one_year_ago_something_he_felt_immensely_guilty_about_but_couldn_not_seem_to_control()
        self.payton_was_his_fiancé_not_even_wife_yet_and_now_she_s_gone_for_good_just_as_he_got_that_promise_ring_on_her_finger()
    def landon_shaw_stood_over_the_metal_table_his_stethoscope_on_and_his_head_bent_down_to_listen_to_the_heart_of_the_dead_girl_lying_before_him(self):
        self.Landon_Shaw.occupation.append('doctor')
        
    def he_was_30_years_old_and_wore_a_black_coat_over_a_crisp_white_shirt_and_tie(self):
        self.Landon_Shaw.age.append('30')
        
    def his_hair_was_short_and_spiky_on_top_like_he_had_just_walked_out_of_a_movie_with_leonardo_dicaprio_in_it(self):
        self.Landon_Shaw.appearance.append('short hair')
        
    def he_turned_to_the_nurse_next_to_him_a_pretty_brunette_with_a_tight_ponytail(self):
        self.Maggie_Shaw.appearance.append('pretty')
        self.Maggie_Shaw.gender.append('female')
        self.Landon_Shaw.relations['nurse'] = 'Maggie_Shaw'
        self.Maggie_Shaw.relations['doctor'] = 'Landon_Shaw'
        
    def could_you_write_that_down_for_me(self):
        pass
        
    def landon_asked_her_referring_to_her_notepad_where_she_had_written_down_what_he_said_about_the_body_on_the_table_in_front_of_them(self):
        pass
        
    def could_you_tell_me_again_what_she_said(self):
        pass
        
    def the_nurse_shrugged_pointing_back_at_landon_with_her_pen(self):
        pass
        
    def you_were_there(self):
        pass
        
    def landon_rolled_his_eyes_and_returned_his_attention_to_the_body_lying_before_him(self):
        pass
        
    def the_only_body_he_d_been_able_to_work_on_since_payton_s_accident_almost_one_year_ago_something_he_felt_immensely_guilty_about_but_couldn_not_seem_to_control(self):
        self.Landon_Shaw.relations['fiancé'] = 'Payton_Parskin'
        self.Payton_Parskin.relations['fiancé'] = 'Landon_Shaw'
        
    def payton_was_his_fiancé_not_even_wife_yet_and_now_she_s_gone_for_good_just_as_he_got_that_promise_ring_on_her_finger(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

