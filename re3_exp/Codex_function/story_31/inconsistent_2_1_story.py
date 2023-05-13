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
        self.Riley_Harper = character('Riley Harper')
        self.Chase_Elliott = character('Chase Elliott')
        self.Jonas_Harper = character('Jonas Harper')

    def story(self):
        self.chase_elliott_glanced_at_his_watch_as_he_pulled_into_his_driveway()
        self.it_was_late_but_at_least_he_d_gotten_the_first_day_of_summer_vacation_off_to_a_good_start()
        self.riley_harper_had_arrived_from_chicago_that_morning_and_had_immediately_begun_unpacking()
        self.from_what_chase_could_tell_she_hadn_not_unpacked_much_more_than_a_few_pieces_of_clothing_and_her_camera_equipment_when_she_decided_to_take_a_walk_around_town()
        self.her_new_town_where_he_would_soon_be_training_her_as_his_replacement_until_a_permanent_sheriff_could_be_found()
        self.it_had_been_an_interesting_few_days_since_the_first_visit_riley_made_to_his_office_at_the_police_station_after_learning_about_her_father_s_death()
        self.they_d_gone_to_dinner_together_that_night_and_since_then_they_d_seen_each_other_nearly_every_day_while_they_settled_riley_into_their_town()
        self.chase_grabbed_his_briefcase_from_the_passenger_seat_of_his_truck_and_slammed_the_door_shut_with_his_hip_before_making_his_way_toward_the_house()
        self.he_glanced_up_at_the_windows_wondering_if_riley_was_in_her_room()
        self.the_second_story_bedroom_faced_out_over_the_driveway_and_while_he_could_hear_a_television_blaring_through_an_open_window_there_was_no_sign_of_riley_herself()
    def chase_elliott_glanced_at_his_watch_as_he_pulled_into_his_driveway(self):
        pass
        
    def it_was_late_but_at_least_he_d_gotten_the_first_day_of_summer_vacation_off_to_a_good_start(self):
        pass
        
    def riley_harper_had_arrived_from_chicago_that_morning_and_had_immediately_begun_unpacking(self):
        self.Riley_Harper.relations['city'] = 'Chicago'
        self.Riley_Harper.relations['town'] = 'Hemlock_Grove'
        self.Riley_Harper.occupation.append('photographer')
        self.Riley_Harper.gender.append('female')
        
    def from_what_chase_could_tell_she_hadn_not_unpacked_much_more_than_a_few_pieces_of_clothing_and_her_camera_equipment_when_she_decided_to_take_a_walk_around_town(self):
        self.Riley_Harper.occupation.append('photographer')
        
    def her_new_town_where_he_would_soon_be_training_her_as_his_replacement_until_a_permanent_sheriff_could_be_found(self):
        self.Riley_Harper.relations['town'] = 'Hemlock_Grove'
        self.Chase_Elliott.relations['town'] = 'Hemlock_Grove'
        self.Riley_Harper.relations['replacement'] = 'Chase_Elliott'
        self.Chase_Elliott.relations['trainer'] = 'Riley_Harper'
        
    def it_had_been_an_interesting_few_days_since_the_first_visit_riley_made_to_his_office_at_the_police_station_after_learning_about_her_father_s_death(self):
        self.Riley_Harper.relations['father'] = 'Jonas_Harper'
        self.Jonas_Harper.relations['daughter'] = 'Riley_Harper'
        self.Jonas_Harper.occupation.append('sheriff')
        self.Jonas_Harper.gender.append('male')
        self.Chase_Elliott.relations['office'] = 'police_station'
        self.Riley_Harper.relations['office'] = 'police_station'
        self.Riley_Harper.relations['death'] = 'Jonas_Harper'
        
    def they_d_gone_to_dinner_together_that_night_and_since_then_they_d_seen_each_other_nearly_every_day_while_they_settled_riley_into_their_town(self):
        self.Riley_Harper.relations['town'] = 'Hemlock_Grove'
        self.Chase_Elliott.relations['town'] = 'Hemlock_Grove'
        
    def chase_grabbed_his_briefcase_from_the_passenger_seat_of_his_truck_and_slammed_the_door_shut_with_his_hip_before_making_his_way_toward_the_house(self):
        pass
        
    def he_glanced_up_at_the_windows_wondering_if_riley_was_in_her_room(self):
        self.Riley_Harper.relations['room'] = 'bedroom'
        self.Chase_Elliott.relations['house'] = 'bedroom'
        
    def the_second_story_bedroom_faced_out_over_the_driveway_and_while_he_could_hear_a_television_blaring_through_an_open_window_there_was_no_sign_of_riley_herself(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

