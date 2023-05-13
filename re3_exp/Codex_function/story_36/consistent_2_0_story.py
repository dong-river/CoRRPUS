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
        self.Karen_Fletcher = character('Karen Fletcher')
        self.Kate_Fletcher = character('Kate Fletcher')
        self.Julia_Fletcher = character('Julia Fletcher')

    def story(self):
        self.julia_fletcher_had_been_the_only_person_to_witness_the_murder_of_her_daughter_in_law_karen_on_that_fateful_day_in_february()
        self.ever_since_then_she_has_been_on_a_constant_watch_for_karen_s_ghost_and_sees_her_shadow_sometimes()
        self.the_doctors_say_that_she_is_suffering_from_hallucinations_due_to_her_condition()
        self.but_every_time_she_sees_it_her_health_seems_to_worsen_drastically()
        self.on_one_fine_day_when_she_started_convulsing_no_one_could_do_anything_about_it_except_for_the_nurse_who_has_been_working_with_julia_for_the_past_four_years()
        self.she_might_be_seeing_things_i_can_see_my_daughter_in_this_mirror()
        self.why_is_my_body_shaking()
        self.is_this_a_fit()
        self.it_feels_like_i_am_shaking_all_over_and_i_can_not_control_myself()
        self.why_am_i_talking_like_this()
        self.am_i_speaking_without_a_tongue_or_without_feeling_a_mouth_she_sobbed_while_clutching_her_chest_at_the_same_time()
        self.a_jolt_of_fear_ran_through_everyone_who_was_witnessing_julia_s_state_at_that_time_including_karen_s_daughter_kate_who_was_trying_to_give_comfort_to_her_mother_in_law()
    def julia_fletcher_had_been_the_only_person_to_witness_the_murder_of_her_daughter_in_law_karen_on_that_fateful_day_in_february(self):
        self.Karen_Fletcher.relations['mother_in_law'] = 'Julia_Fletcher'
        self.Julia_Fletcher.relations['daughter_in_law'] = 'Karen_Fletcher'
        
    def ever_since_then_she_has_been_on_a_constant_watch_for_karen_s_ghost_and_sees_her_shadow_sometimes(self):
        pass
        
    def the_doctors_say_that_she_is_suffering_from_hallucinations_due_to_her_condition(self):
        pass
        
    def but_every_time_she_sees_it_her_health_seems_to_worsen_drastically(self):
        pass
        
    def on_one_fine_day_when_she_started_convulsing_no_one_could_do_anything_about_it_except_for_the_nurse_who_has_been_working_with_julia_for_the_past_four_years(self):
        pass
        
    def she_might_be_seeing_things_i_can_see_my_daughter_in_this_mirror(self):
        pass
        
    def why_is_my_body_shaking(self):
        pass
        
    def is_this_a_fit(self):
        pass
        
    def it_feels_like_i_am_shaking_all_over_and_i_can_not_control_myself(self):
        pass
        
    def why_am_i_talking_like_this(self):
        pass
        
    def am_i_speaking_without_a_tongue_or_without_feeling_a_mouth_she_sobbed_while_clutching_her_chest_at_the_same_time(self):
        pass
        
    def a_jolt_of_fear_ran_through_everyone_who_was_witnessing_julia_s_state_at_that_time_including_karen_s_daughter_kate_who_was_trying_to_give_comfort_to_her_mother_in_law(self):
        self.Karen_Fletcher.relations['daughter'] = 'Kate_Fletcher'
        self.Kate_Fletcher.relations['mother'] = 'Karen_Fletcher'
        self.Kate_Fletcher.relations['mother_in_law'] = 'Julia_Fletcher'
        self.Julia_Fletcher.relations['daughter_in_law'] = 'Kate_Fletcher'
        
## Create a world model state to track each character's appearance, personality, and relations with other characters.

