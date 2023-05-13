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
        self.Jessica_Campbell = character('Jessica Campbell')
        self.John_Smith = character('John Smith')
        self.Tina_Sanchez = character('Tina Sanchez')

    def story(self):
        self.tina_sanchez_sat_in_her_dressing_room_at_model_city()
        self.she_had_just_changed_into_her_new_dress_and_looked_at_herself_in_the_mirror()
        self.it_was_a_bright_sunny_morning_and_her_stylist_rachel_cunningham_stood_next_to_her_brushing_out_tina_s_long_black_hair()
        self.you_re_such_a_beautiful_girl_tina()
        self.i_can_t_believe_you_haven_t_been_chosen_to_be_in_any_magazines_yet()
        self.i_saw_some_of_the_girls_who_were_selected_for_our_next_runway_show()
        self.your_co_workers_are_going_to_be_so_jealous()
        self.you_re_definitely_one_of_the_most_beautiful_women_here()
        self.do_you_want_me_to_put_your_hair_up_or_leave_it_down_tina_thought_for_a_moment_before_responding()
        self.well_since_we_are_doing_a_fashion_show_on_the_beach_i_think_my_hair_should_be_down_so_that_it_looks_like_i_just_came_out_of_the_ocean()
        self.what_do_you_think_rachel_smiled_as_she_finished_brushing_out_tina_s_hair_and_started_putting_bobby_pins_in_it()
        self.i_think_that_sounds_perfect()
        self.here_you_go()
        self.wow_you_look_amazing()
        self.the_cameramen_are_going_to_love_you_today()
    def tina_sanchez_sat_in_her_dressing_room_at_model_city(self):
        self.Tina_Sanchez.occupation.append('model')
    def she_had_just_changed_into_her_new_dress_and_looked_at_herself_in_the_mirror(self):
        self.Tina_Sanchez.appearance.append('new dress')
    def it_was_a_bright_sunny_morning_and_her_stylist_rachel_cunningham_stood_next_to_her_brushing_out_tina_s_long_black_hair(self):
        self.Tina_Sanchez.appearance.append('long black hair')
        self.Tina_Sanchez.relations['stylist'] = 'Rachel Cunningham'
    def you_re_such_a_beautiful_girl_tina(self):
        self.Tina_Sanchez.appearance.append('beautiful')
    def i_can_t_believe_you_haven_t_been_chosen_to_be_in_any_magazines_yet(self):
        pass
    def i_saw_some_of_the_girls_who_were_selected_for_our_next_runway_show(self):
        pass
    def your_co_workers_are_going_to_be_so_jealous(self):
        pass
    def you_re_definitely_one_of_the_most_beautiful_women_here(self):
        pass
    def do_you_want_me_to_put_your_hair_up_or_leave_it_down_tina_thought_for_a_moment_before_responding(self):
        pass
    def well_since_we_are_doing_a_fashion_show_on_the_beach_i_think_my_hair_should_be_down_so_that_it_looks_like_i_just_came_out_of_the_ocean(self):
        pass
    def what_do_you_think_rachel_smiled_as_she_finished_brushing_out_tina_s_hair_and_started_putting_bobby_pins_in_it(self):
        pass
    def i_think_that_sounds_perfect(self):
        pass
    def here_you_go(self):
        pass
    def wow_you_look_amazing(self):
        pass
    def the_cameramen_are_going_to_love_you_today(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

