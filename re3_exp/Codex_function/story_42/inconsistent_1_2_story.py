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
        self.Valerie_Russo = character('Valerie Russo')
        self.Carl_Russo = character('Carl Russo')
        self.Antoinette_Russo = character('Antoinette Russo')

    def story(self):
        self.carl_russo_parked_his_car_in_front_of_the_police_station_excited_to_tell_his_coworker_and_friend_john_davis_about_a_television_show_he_was_watching()
        self.the_show_was_called_police_intervention_and_its_goal_was_to_catch_police_officers_on_camera_during_a_routine_traffic_stop_who_were_unfairly_profiling()
        self.hey_davis()
        self.carl_shouted_as_he_burst_through_the_front_door_of_the_police_station()
        self.john_waved_at_carl_from_across_the_room()
        self.he_stopped_talking_to_the_other_cops_and_turned_around_to_face_carl_as_he_approached_him()
        self.hey_russo_john_said_with_a_big_smile_on_his_face()
        self.you_re_in_a_good_mood_today()
        self.carl_dropped_his_things_on_his_desk_and_looked_at_john_curiously()
        self.i_have_good_news()
        self.and_i_know_you_ll_appreciate_it()
        self.he_nodded_at_one_of_the_other_cops_nearby_and_laughed_when_that_cop_made_fun_of_him_for_going_to_ucla_instead_of_california_state_university_at_northridge()
        self.they_all_shared_some_good_natured_laughs_together_before_they_turned_back_towards_carl_and_john_when_they_heard_carl_s_next_sentence_i_watched_this_great_tv_show_last_night_called_police_intervention()
        self.what_s_that()
        self.one_of_the_young_rookie_cops_asked()
        self.like_cops()
    def carl_russo_parked_his_car_in_front_of_the_police_station_excited_to_tell_his_coworker_and_friend_john_davis_about_a_television_show_he_was_watching(self):
        self.Carl_Russo.relations['coworker'] = 'John_Davis'
        self.Carl_Russo.relations['friend'] = 'John_Davis'
        self.Carl_Russo.gender.append('male')
        self.Carl_Russo.occupation.append('police officer')
        self.Carl_Russo.appearance.append('brown hair')
        self.Carl_Russo.appearance.append('brown eyes')
        self.Carl_Russo.appearance.append('tan skin')
        self.Carl_Russo.appearance.append('muscular')
        self.Carl_Russo.age.append('thirty-two')

        self.John_Davis = character('John Davis')
        self.John_Davis.relations['coworker'] = 'Carl_Russo'
        self.John_Davis.relations['friend'] = 'Carl_Russo'
        self.John_Davis.gender.append('male')
        self.John_Davis.occupation.append('police officer')
        self.John_Davis.appearance.append('blonde hair')
        self.John_Davis.appearance.append('blue eyes')
        self.John_Davis.appearance.append('tan skin')
        self.John_Davis.appearance.append('muscular')
        self.John_Davis.age.append('thirty-five')

    def the_show_was_called_police_intervention_and_its_goal_was_to_catch_police_officers_on_camera_during_a_routine_traffic_stop_who_were_unfairly_profiling(self):
        self.Police_Intervention = character('Police Intervention')
        self.Police_Intervention.appearance.append('television show')
        self.Police_Intervention.appearance.append('police officers')
        self.Police_Intervention.appearance.append('camera')
        self.Police_Intervention.appearance.append('routine traffic stop')
        self.Police_Intervention.appearance.append('unfairly profiling')

    def hey_davis(self):
        self.Carl_Russo.relations['coworker'] = 'John_Davis'
        self.Carl_Russo.relations['friend'] = 'John_Davis'
        self.John_Davis.relations['coworker'] = 'Carl_Russo'
        self.John_Davis.relations['friend'] = 'Carl_Russo'

    def carl_shouted_as_he_burst_through_the_front_door_of_the_police_station(self):
        self.Carl_Russo.appearance.append('shouted')

    def john_waved_at_carl_from_across_the_room(self):
        self.John_Davis.appearance.append('waved')

    def he_stopped_talking_to_the_other_cops_and_turned_around_to_face_carl_as_he_approached_him(self):
        self.John_Davis.appearance.append('stopped talking')

    def hey_russo_john_said_with_a_big_smile_on_his_face(self):
        self.John_Davis.appearance.append('smile')

    def you_re_in_a_good_mood_today(self):
        self.John_Davis.appearance.append('good mood')

    def carl_dropped_his_things_on_his_desk_and_looked_at_john_curiously(self):
        self.Carl_Russo.appearance.append('curious')

    def i_have_good_news(self):
        self.Carl_Russo.appearance.append('good news')

    def and_i_know_you_ll_appreciate_it(self):
        self.Carl_Russo.appearance.append('appreciate')

    def he_nodded_at_one_of_the_other_cops_nearby_and_laughed_when_that_cop_made_fun_of_him_for_going_to_ucla_instead_of_california_state_university_at_northridge(self):
        self.Carl_Russo.appearance.append('nodded')
        self.Carl_Russo.appearance.append('laughed')

    def they_all_shared_some_good_natured_laughs_together_before_they_turned_back_towards_carl_and_john_when_they_heard_carl_s_next_sentence_i_watched_this_great_tv_show_last_night_called_police_intervention(self):
        self.Carl_Russo.appearance.append('shared some good natured laughs')

    def what_s_that(self):
        self.Carl_Russo.appearance.append('good natured laughs')

    def one_of_the_young_rookie_cops_asked(self):
        self.Rookie_Cop = character('Rookie Cop')
        self.Rookie_Cop.relations['coworker'] = 'Carl_Russo'
        self.Rookie_Cop.relations['friend'] = 'Carl_Russo'
        self.Rookie_Cop.relations['coworker'] = 'John_Davis'
        self.Rookie_Cop.relations['friend'] = 'John_Davis'
        self.Rookie_Cop.gender.append('male')
        self.Rookie_Cop.occupation.append('police officer')
        self.Rookie_Cop.appearance.append('young')
        self.Rookie_Cop.appearance.append('brown hair')
        self.Rookie_Cop.appearance.append('brown eyes')
        self.Rookie_Cop.appearance.append('tan skin')
        self.Rookie_Cop.appearance.append('muscular')
        self.Rookie_Cop.age.append('twenty-five')

    def like_cops(self):
        self.Police_Intervention.appearance.append('cops')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

