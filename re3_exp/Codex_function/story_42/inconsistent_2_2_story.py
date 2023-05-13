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
        self.carl_russo_was_tired_of_work()
        self.he_was_tired_of_being_a_rich_businessman_and_owning_his_own_company()
        self.it_was_exciting_in_the_beginning_but_now_it_felt_like_just_another_day_at_the_office_except_he_had_to_put_on_pants_every_morning()
        self.when_valerie_started_applying_to_medical_schools_he_hoped_that_becoming_a_doctor_would_make_her_happy()
        self.at_first_it_seemed_like_it_would_but_then_she_started_taking_too_many_hours_off_work_and_not_putting_in_enough_effort_in_school_which_led_to_his_decision_to_take_a_year_off_to_travel_the_world_before_going_back_to_school()
        self.carl_needed_this_time_away_from_everything()
        self.he_didn_not_even_want_to_look_at_his_email_or_phone_for_four_months()
        self.yes_he_was_old_fashioned_like_that_and_preferred_face_to_face_communication_with_people_instead_of_texting_or_writing_an_email_or_a_letter_via_snail_mail()
        self.there_was_something_nice_about_a_hand_written_letter_that_you_couldn_not_get_with_technology_these_days_then_again_he_did_understand_people_s_attraction_to_the_feel_of_having_their_words_in_written_form_instead_of_staring_at_a_screen_all_day_long()
    def carl_russo_was_tired_of_work(self):
        self.Carl_Russo.occupation.append('rich businessman')
    
    def he_was_tired_of_being_a_rich_businessman_and_owning_his_own_company(self):
        self.Carl_Russo.occupation.append('owner')
    
    def it_was_exciting_in_the_beginning_but_now_it_felt_like_just_another_day_at_the_office_except_he_had_to_put_on_pants_every_morning(self):
        pass
    
    def when_valerie_started_applying_to_medical_schools_he_hoped_that_becoming_a_doctor_would_make_her_happy(self):
        self.Carl_Russo.relations['wife'] = 'Valerie_Russo'
        self.Valerie_Russo.relations['husband'] = 'Carl_Russo'
        self.Valerie_Russo.occupation.append('medical school')
    
    def at_first_it_seemed_like_it_would_but_then_she_started_taking_too_many_hours_off_work_and_not_putting_in_enough_effort_in_school_which_led_to_his_decision_to_take_a_year_off_to_travel_the_world_before_going_back_to_school(self):
        self.Carl_Russo.occupation.append('travelling')
    
    def carl_needed_this_time_away_from_everything(self):
        pass
    
    def he_didn_not_even_want_to_look_at_his_email_or_phone_for_four_months(self):
        pass
    
    def yes_he_was_old_fashioned_like_that_and_preferred_face_to_face_communication_with_people_instead_of_texting_or_writing_an_email_or_a_letter_via_snail_mail(self):
        pass
    
    def there_was_something_nice_about_a_hand_written_letter_that_you_couldn_not_get_with_technology_these_days_then_again_he_did_understand_people_s_attraction_to_the_feel_of_having_their_words_in_written_form_instead_of_staring_at_a_screen_all_day_long(self):
        pass
    
    
## Create a world model state to track each character's appearance, personality, and relations with other characters.

