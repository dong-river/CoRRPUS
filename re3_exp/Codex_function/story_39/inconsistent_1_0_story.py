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
        self.Nadia_Kaminski = character('Nadia Kaminski')
        self.Connor_Riley = character('Connor Riley')
        self.Abigail_Harper = character('Abigail Harper')

    def story(self):
        self.connor_riley_sat_in_the_shuttle_craft_feeling_uneasy()
        self.he_was_scheduled_to_be_the_pilot_of_the_mars_expedition_and_should_have_been_excited_about_that_but_he_wasn_not()
        self.he_had_not_been_consulted_about_the_makeup_of_the_rest_of_the_team_and_he_didn_not_know_why_he_felt_so_uneasy_about_that_either()
        self.the_mission_was_all_about_searching_for_signs_of_life_on_mars_and_dr_harper_was_a_plant_biologist()
        self.there_was_no_point_having_a_doctor_if_they_weren_not_going_to_look_for_signs_of_life_there()
        self.and_he_knew_from_his_own_research_that_any_planets_that_had_enough_water_would_also_support_life_on_them_at_some_point_in_their_history()
        self.the_earth_isn_not_an_exception_connor_told_himself_quietly_while_tapping_his_fingers_on_his_thigh_nervously()
        self.he_really_wasn_not_looking_forward_to_being_stuck_in_a_small_space_with_four_other_people_for_a_six_month_flight_to_mars_but_one_person_in_particular_worried_him_even_more_than_anyone_else_on_the_team_nadia_kaminski()
        self.nadia_s_field_of_expertise_was_astrobiology_so_why_had_she_been_chosen()
        self.unless_someone_knew_something_she_didn_not_know()
    def connor_riley_sat_in_the_shuttle_craft_feeling_uneasy(self):
        self.Connor_Riley.occupation.append('pilot')
        
    def he_was_scheduled_to_be_the_pilot_of_the_mars_expedition_and_should_have_been_excited_about_that_but_he_wasn_not(self):
        pass
        
    def he_had_not_been_consulted_about_the_makeup_of_the_rest_of_the_team_and_he_didn_not_know_why_he_felt_so_uneasy_about_that_either(self):
        pass
        
    def the_mission_was_all_about_searching_for_signs_of_life_on_mars_and_dr_harper_was_a_plant_biologist(self):
        self.Abigail_Harper.occupation.append('plant biologist')
        
    def there_was_no_point_having_a_doctor_if_they_weren_not_going_to_look_for_signs_of_life_there(self):
        pass
        
    def and_he_knew_from_his_own_research_that_any_planets_that_had_enough_water_would_also_support_life_on_them_at_some_point_in_their_history(self):
        pass
        
    def the_earth_isn_not_an_exception_connor_told_himself_quietly_while_tapping_his_fingers_on_his_thigh_nervously(self):
        pass
        
    def he_really_wasn_not_looking_forward_to_being_stuck_in_a_small_space_with_four_other_people_for_a_six_month_flight_to_mars_but_one_person_in_particular_worried_him_even_more_than_anyone_else_on_the_team_nadia_kaminski(self):
        self.Nadia_Kaminski.occupation.append('astrobiology')
        
    def nadia_s_field_of_expertise_was_astrobiology_so_why_had_she_been_chosen(self):
        pass
        
    def unless_someone_knew_something_she_didn_not_know(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

