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
        self.Jennie_Mayfield = character('Jennie Mayfield')
        self.Aaron_Mayfield = character('Aaron Mayfield')
        self.Alex_Preston = character('Alex Preston')

    def story(self):
        self.alex_preston_is_now_a_ghost_and_he_watches_as_jennie_gets_out_of_her_wrecked_car()
        self.she_has_long_dark_hair_and_brown_eyes()
        self.her_body_is_athletic()
        self.it_s_obvious_she_takes_care_of_herself()
        self.she_is_stunned_and_in_pain()
        self.she_can_not_remember_the_accident_but_she_feels_like_something_s_wrong_with_her_shoulder()
        self.she_saw_her_tire_blow_out_and_then_she_crashed_into_a_tree()
        self.she_was_lucky_that_no_one_else_was_on_the_road_or_she_could_have_caused_a_head_on_collision()
        self.alex_kneels_down_next_to_her_and_holds_his_hand_out_to_comfort_her_as_best_he_can()
        self.he_wonders_if_he_can_help_ease_her_pain_somehow_but_he_s_not_sure_how_to_do_it_yet()
        self.he_may_need_some_time_to_get_used_to_his_new_form_before_he_can_figure_out_what_to_do_with_it_all_the_time_when_it_comes_to_things_like_this()
        self.jennie_tries_to_make_sense_of_what_happened_when_the_car_veered_off_into_the_trees_heading_right_for_them_but_then_suddenly_slowing_down_until_it_barely_hit_them_at_all_instead_of_going_right_through_them_with_disastrous_results()
    def alex_preston_is_now_a_ghost_and_he_watches_as_jennie_gets_out_of_her_wrecked_car(self):
        pass
    def she_has_long_dark_hair_and_brown_eyes(self):
        self.Jennie_Mayfield.appearance.append("long dark hair")
        self.Jennie_Mayfield.appearance.append("brown eyes")
    def her_body_is_athletic(self):
        self.Jennie_Mayfield.appearance.append("athletic")
    def it_s_obvious_she_takes_care_of_herself(self):
        pass
    def she_is_stunned_and_in_pain(self):
        pass
    def she_can_not_remember_the_accident_but_she_feels_like_something_s_wrong_with_her_shoulder(self):
        pass
    def she_saw_her_tire_blow_out_and_then_she_crashed_into_a_tree(self):
        pass
    def she_was_lucky_that_no_one_else_was_on_the_road_or_she_could_have_caused_a_head_on_collision(self):
        pass
    def alex_kneels_down_next_to_her_and_holds_his_hand_out_to_comfort_her_as_best_he_can(self):
        pass
    def he_wonders_if_he_can_help_ease_her_pain_somehow_but_he_s_not_sure_how_to_do_it_yet(self):
        pass
    def he_may_need_some_time_to_get_used_to_his_new_form_before_he_can_figure_out_what_to_do_with_it_all_the_time_when_it_comes_to_things_like_this(self):
        pass
    def jennie_tries_to_make_sense_of_what_happened_when_the_car_veered_off_into_the_trees_heading_right_for_them_but_then_suddenly_slowing_down_until_it_barely_hit_them_at_all_instead_of_going_right_through_them_with_disastrous_results(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

