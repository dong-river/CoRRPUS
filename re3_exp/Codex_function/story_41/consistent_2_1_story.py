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
        self.alex_preston_is_worried_about_his_girlfriend_jennie_mayfield()
        self.he_s_never_seen_her_so_upset()
        self.when_he_asked_her_what_was_wrong_she_broke_down_and_told_him_about_a_car_accident_she_had_just_witnessed()
        self.they_were_in_his_new_car_alex_driving_and_jennie_in_the_passenger_seat()
        self.they_were_on_their_way_to_the_mountains_for_a_hike_and_picnic_at_the_park_nearby_when_a_car_jumped_the_center_line_and_slammed_into_them_head_on()
        self.luckily_they_both_walked_away_without_any_major_injuries()
        self.however_they_had_to_stay_behind_as_the_police_dealt_with_the_other_driver_who_was_arrested_for_reckless_driving()
        self.they_watched_from_a_distance_as_paramedics_took_care_of_people_from_both_cars_involved_in_the_accident()
        self.at_least_everyone_walked_away_from_it_unharmed_physically_alex_thought_although_the_people_involved_might_still_be_emotionally_scarred()
        self.the_police_wouldn_not_let_anyone_get_close_to_either_car_involved_in_case_there_was_some_way_of_preserving_evidence_which_could_be_used_against_them_later_on_in_court_if_it_came_to_that_point()
        self.the_police_took_statements_from_everyone_who_had_been_present_at_the_scene()
    def alex_preston_is_worried_about_his_girlfriend_jennie_mayfield(self):
        self.Jennie_Mayfield.relations['boyfriend'] = 'Alex_Preston'
        self.Alex_Preston.relations['girlfriend'] = 'Jennie_Mayfield'
        self.Alex_Preston.gender.append('male')

    def he_s_never_seen_her_so_upset(self):
        pass

    def when_he_asked_her_what_was_wrong_she_broke_down_and_told_him_about_a_car_accident_she_had_just_witnessed(self):
        pass

    def they_were_in_his_new_car_alex_driving_and_jennie_in_the_passenger_seat(self):
        self.Alex_Preston.occupation.append('driver')

    def they_were_on_their_way_to_the_mountains_for_a_hike_and_picnic_at_the_park_nearby_when_a_car_jumped_the_center_line_and_slammed_into_them_head_on(self):
        pass

    def luckily_they_both_walked_away_without_any_major_injuries(self):
        pass

    def however_they_had_to_stay_behind_as_the_police_dealt_with_the_other_driver_who_was_arrested_for_reckless_driving(self):
        pass

    def they_watched_from_a_distance_as_paramedics_took_care_of_people_from_both_cars_involved_in_the_accident(self):
        pass

    def at_least_everyone_walked_away_from_it_unharmed_physically_alex_thought_although_the_people_involved_might_still_be_emotionally_scarred(self):
        pass

    def the_police_wouldn_not_let_anyone_get_close_to_either_car_involved_in_case_there_was_some_way_of_preserving_evidence_which_could_be_used_against_them_later_on_in_court_if_it_came_to_that_point(self):
        pass

    def the_police_took_statements_from_everyone_who_had_been_present_at_the_scene(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

