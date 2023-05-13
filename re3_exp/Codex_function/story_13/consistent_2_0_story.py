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
        self.Sherry_Hellinger = character('Sherry Hellinger')
        self.Emily_Hellinger = character('Emily Hellinger')
        self.John_Hellinger = character('John Hellinger')

    def story(self):
        self.emily_hellinger_walked_into_the_kitchen_in_her_pajamas_her_hazel_eyes_squinting_against_the_dim_light()
        self.she_brushed_her_long_brown_hair_out_of_her_face_as_she_yawned()
        self.looking_at_the_wall_clock_she_knew_it_was_still_early_for_john_to_be_home()
        self.glancing_around_the_house_she_noticed_that_he_was_nowhere_to_be_found()
        self.seeing_his_keys_on_the_counter_she_shrugged_and_went_back_to_bed()
        self.she_fell_asleep_quickly_after_having_a_late_dinner_and_woke_up_early_in_the_morning()
        self.slipping_into_some_jeans_and_a_sweatshirt_emily_set_off_to_find_john()
        self.the_spring_air_was_brisk_but_warming_up_nicely_as_she_headed_down_their_street_towards_downtown_hillside_hills()
        self.feeling_a_tingle_of_excitement_pass_through_her_at_seeing_so_many_people_up_and_about_in_this_small_town_during_this_quiet_time_of_year_emily_smiled_with_delight_as_she_scanned_the_nearly_empty_street_for_john_s_big_blue_truck()
        self.it_wasn_not_parked_near_work_or_at_home_it_wasn_not_even_parked_near_any_of_their_family_friends_houses_where_he_might_be_visiting_them_on_this_gray_morning_while_they_were_eating_breakfast_or_watering_their_plants_or_other_mundane_tasks_that_people_did_on_a_saturday_morning_before_9_am()
    def emily_hellinger_walked_into_the_kitchen_in_her_pajamas_her_hazel_eyes_squinting_against_the_dim_light(self):
        self.Emily_Hellinger.appearance.append("hazel eyes")
        self.Emily_Hellinger.appearance.append("long brown hair")
        self.Emily_Hellinger.appearance.append("pajamas")

    def she_brushed_her_long_brown_hair_out_of_her_face_as_she_yawned(self):
        pass

    def looking_at_the_wall_clock_she_knew_it_was_still_early_for_john_to_be_home(self):
        pass

    def glancing_around_the_house_she_noticed_that_he_was_nowhere_to_be_found(self):
        pass

    def seeing_his_keys_on_the_counter_she_shrugged_and_went_back_to_bed(self):
        pass

    def she_fell_asleep_quickly_after_having_a_late_dinner_and_woke_up_early_in_the_morning(self):
        pass

    def slipping_into_some_jeans_and_a_sweatshirt_emily_set_off_to_find_john(self):
        pass

    def the_spring_air_was_brisk_but_warming_up_nicely_as_she_headed_down_their_street_towards_downtown_hillside_hills(self):
        pass

    def feeling_a_tingle_of_excitement_pass_through_her_at_seeing_so_many_people_up_and_about_in_this_small_town_during_this_quiet_time_of_year_emily_smiled_with_delight_as_she_scanned_the_nearly_empty_street_for_john_s_big_blue_truck(self):
        self.John_Hellinger.appearance.append("big blue truck")
        self.Emily_Hellinger.relations['husband'] = 'John_Hellinger'
        self.John_Hellinger.relations['wife'] = 'Emily_Hellinger'

    def it_wasn_not_parked_near_work_or_at_home_it_wasn_not_even_parked_near_any_of_their_family_friends_houses_where_he_might_be_visiting_them_on_this_gray_morning_while_they_were_eating_breakfast_or_watering_their_plants_or_other_mundane_tasks_that_people_did_on_a_saturday_morning_before_9_am(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

