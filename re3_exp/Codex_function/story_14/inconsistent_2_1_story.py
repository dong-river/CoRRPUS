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
        self.jimmy_jackson_was_worried()
        self.his_best_friend_jenny_anderson_had_just_disappeared()
        self.it_had_all_started_when_he_had_been_working_at_his_father_s_garage_right_across_the_street_from_a_large_and_lonely_house()
        self.the_man_who_lived_there_mr_jones_was_not_very_popular_in_town()
        self.he_was_mean_and_cruel_to_anyone_who_crossed_him()
        self.jimmy_suspected_that_he_might_have_killed_someone_once_or_twice()
        self.jimmy_heard_a_noise_outside_his_garage_door_and_saw_a_black_cat_run_across_the_street_to_the_lonely_house_next_door()
        self.curious_jimmy_followed_it_and_found_it_sitting_on_the_windowsill_of_mr_jones_bedroom_on_the_second_floor_of_his_home()
        self.as_jimmy_stared_up_at_him_in_shock_mr_jones_came_out_of_his_room_with_two_jars_full_of_mice_and_tossed_them_both_out_his_window_where_they_fell_onto_their_sides_upon_impact_with_the_grass_below_them_the_mice_inside_were_running_around_like_crazy_before_the_broken_glass_killed_them_both_instantly()
        self.mr_jones_went_back_into_his_room_whistling_innocently_to_himself_as_if_nothing_had_happened()
        self.this_was_too_much_for_jimmy_to_handle_he_fainted_on_the_spot()
        self.jimmy_awoke_with_a_start_as_jenny_shook_him_awake_what_happened()
        self.asked_jenny_i_don_not_know()
    def jimmy_jackson_was_worried(self):
        pass
    def his_best_friend_jenny_anderson_had_just_disappeared(self):
        self.Jenny_Anderson.relations['best_friend'] = 'Jimmy_Jackson'
        self.Jimmy_Jackson.relations['best_friend'] = 'Jenny_Anderson'
    def it_had_all_started_when_he_had_been_working_at_his_father_s_garage_right_across_the_street_from_a_large_and_lonely_house(self):
        self.Jimmy_Jackson.relations['father'] = 'Jimmy_Jackson'
    def the_man_who_lived_there_mr_jones_was_not_very_popular_in_town(self):
        self.Jimmy_Jackson.relations['mr_jones'] = 'Jimmy_Jackson'
    def he_was_mean_and_cruel_to_anyone_who_crossed_him(self):
        self.Jimmy_Jackson.relations['mr_jones'] = 'Jimmy_Jackson'
    def jimmy_suspected_that_he_might_have_killed_someone_once_or_twice(self):
        self.Jimmy_Jackson.relations['mr_jones'] = 'Jimmy_Jackson'
    def jimmy_heard_a_noise_outside_his_garage_door_and_saw_a_black_cat_run_across_the_street_to_the_lonely_house_next_door(self):
        self.Jimmy_Jackson.relations['mr_jones'] = 'Jimmy_Jackson'
    def curious_jimmy_followed_it_and_found_it_sitting_on_the_windowsill_of_mr_jones_bedroom_on_the_second_floor_of_his_home(self):
        self.Jimmy_Jackson.relations['mr_jones'] = 'Jimmy_Jackson'
    def as_jimmy_stared_up_at_him_in_shock_mr_jones_came_out_of_his_room_with_two_jars_full_of_mice_and_tossed_them_both_out_his_window_where_they_fell_onto_their_sides_upon_impact_with_the_grass_below_them_the_mice_inside_were_running_around_like_crazy_before_the_broken_glass_killed_them_both_instantly(self):
        self.Jimmy_Jackson.relations['mr_jones'] = 'Jimmy_Jackson'
    def mr_jones_went_back_into_his_room_whistling_innocently_to_himself_as_if_nothing_had_happened(self):
        self.Jimmy_Jackson.relations['mr_jones'] = 'Jimmy_Jackson'
    def this_was_too_much_for_jimmy_to_handle_he_fainted_on_the_spot(self):
        self.Jimmy_Jackson.relations['mr_jones'] = 'Jimmy_Jackson'
    def jimmy_awoke_with_a_start_as_jenny_shook_him_awake_what_happened(self):
        self.Jimmy_Jackson.relations['mr_jones'] = 'Jimmy_Jackson'
        self.Jenny_Anderson.relations['best_friend'] = 'Jimmy_Jackson'
        self.Jimmy_Jackson.relations['best_friend'] = 'Jenny_Anderson'
    def asked_jenny_i_don_not_know(self):
        self.Jimmy_Jackson.relations['mr_jones'] = 'Jimmy_Jackson'
        self.Jenny_Anderson.relations['best_friend'] = 'Jimmy_Jackson'
        self.Jimmy_Jackson.relations['best_friend'] = 'Jenny_Anderson'

## Create a world model state to track each character's appearance, personality, and relations with other characters.

