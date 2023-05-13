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
        self.Jenny_Anderson = character('Jenny Anderson')
        self.Jimmy_Jackson = character('Jimmy Jackson')
        self.Principal_Stevens = character('Principal Stevens')

    def story(self):
        self.jimmy_jackson_leaned_back_against_the_couch_in_jenny_s_living_room()
        self.hey_do_you_think_the_state_will_have_a_good_football_team_this_year()
        self.he_asked()
        self.don_not_be_silly_jenny_replied_from_her_seat_on_the_opposite_end_of_the_couch()
        self.west_virginia_is_always_a_powerhouse()
        self.maybe_next_year_jimmy_said_with_a_chuckle()
        self.but_that_s_not_what_i_meant()
        self.i_mean_this_year()
        self.jenny_turned_to_face_jimmy_and_reached_out_to_put_her_arm_around_his_shoulders()
        self.i_m_sorry_about_last_night_she_said_apologetically()
        self.i_had_a_lot_on_my_mind_and_didn_not_feel_like_talking()
        self.she_paused_before_adding_but_we_should_probably_break_up()
        self.jimmy_looked_at_her_incredulously()
        self.what_are_you_talking_about()
        self.he_demanded_angrily_pushing_her_arm_away_from_him()
        self.after_all_these_years_you_re_just_going_to_dump_me()
        self.for_what()
        self.what_could_be_so_important_that_you_d_throw_away_something_like_this()
        self.he_gestured_back_and_forth_between_them_as_if_they_were_nothing_more_than_an_old_sweater_jenny_didn_not_want_anymore()
        self.as_if_they_had_never_meant_anything_to_each_other_at_all()
    def jimmy_jackson_leaned_back_against_the_couch_in_jenny_s_living_room(self):
        self.Jimmy_Jackson.relations['Jenny_Anderson'] = 'boyfriend'
        self.Jenny_Anderson.relations['Jimmy_Jackson'] = 'girlfriend'
        self.Jimmy_Jackson.age.append('young')
        self.Jimmy_Jackson.gender.append('male')
        self.Jenny_Anderson.age.append('young')
        self.Jenny_Anderson.gender.append('female')
        
    def hey_do_you_think_the_state_will_have_a_good_football_team_this_year(self):
        pass
        
    def he_asked(self):
        pass
        
    def don_not_be_silly_jenny_replied_from_her_seat_on_the_opposite_end_of_the_couch(self):
        pass
        
    def west_virginia_is_always_a_powerhouse(self):
        pass
        
    def maybe_next_year_jimmy_said_with_a_chuckle(self):
        pass
        
    def but_that_s_not_what_i_meant(self):
        pass
        
    def i_mean_this_year(self):
        pass
        
    def jenny_turned_to_face_jimmy_and_reached_out_to_put_her_arm_around_his_shoulders(self):
        pass
        
    def i_m_sorry_about_last_night_she_said_apologetically(self):
        pass
        
    def i_had_a_lot_on_my_mind_and_didn_not_feel_like_talking(self):
        pass
        
    def she_paused_before_adding_but_we_should_probably_break_up(self):
        pass
        
    def jimmy_looked_at_her_incredulously(self):
        pass
        
    def what_are_you_talking_about(self):
        pass
        
    def he_demanded_angrily_pushing_her_arm_away_from_him(self):
        pass
        
    def after_all_these_years_you_re_just_going_to_dump_me(self):
        pass
        
    def for_what(self):
        pass
        
    def what_could_be_so_important_that_you_d_throw_away_something_like_this(self):
        pass
        
    def he_gestured_back_and_forth_between_them_as_if_they_were_nothing_more_than_an_old_sweater_jenny_didn_not_want_anymore(self):
        pass
        
    def as_if_they_had_never_meant_anything_to_each_other_at_all(self):
        pass

## Generate a story from the model.

