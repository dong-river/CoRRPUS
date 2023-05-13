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
        self.Jennifer_Ann_Smith = character('Jennifer Ann Smith')
        self.Clara_Smith = character('Clara Smith')
        self.Robert_Smith = character('Robert Smith')

    def story(self):
        self.jennifer_ann_smith_is_a_27_year_old_woman_who_has_just_moved_into_a_new_apartment_and_started_a_new_job_as_a_receptionist_at_an_office_building_downtown_chicago_illinois_united_states_of_america()
        self.jennifer_was_excited_about_her_new_apartment()
        self.she_didn_not_know_anybody_there_and_had_no_friends_in_the_city_but_she_decided_it_was_time_to_leave_her_family_behind_and_become_independent()
        self.she_spent_her_days_calling_friends_from_college_and_sending_emails_to_her_family_in_other_states()
        self.she_found_herself_to_be_very_busy_with_work_and_keeping_in_touch_with_people_so_she_never_even_had_time_to_meet_anybody_outside_of_work()
        self.it_seemed_as_if_everybody_else_were_settling_down_while_she_was_working_herself_to_death_in_the_big_city()
        self.it_had_been_almost_two_months_since_jennifer_moved_into_her_new_apartment_when_one_day_she_found_that_she_wasn_not_really_satisfied_with_it_anymore_which_caught_her_by_surprise_as_she_had_never_even_thought_of_moving_out_yet()
    def jennifer_ann_smith_is_a_27_year_old_woman_who_has_just_moved_into_a_new_apartment_and_started_a_new_job_as_a_receptionist_at_an_office_building_downtown_chicago_illinois_united_states_of_america(self):
        self.Jennifer_Ann_Smith.age.append('27')
        self.Jennifer_Ann_Smith.gender.append('female')
        self.Jennifer_Ann_Smith.occupation.append('receptionist')
    def jennifer_was_excited_about_her_new_apartment(self):
        pass
    def she_didn_not_know_anybody_there_and_had_no_friends_in_the_city_but_she_decided_it_was_time_to_leave_her_family_behind_and_become_independent(self):
        self.Jennifer_Ann_Smith.relations['family'] = 'Clara_Smith, Robert_Smith'
        self.Clara_Smith.relations['daughter'] = 'Jennifer_Ann_Smith'
        self.Robert_Smith.relations['daughter'] = 'Jennifer_Ann_Smith'
    def she_spent_her_days_calling_friends_from_college_and_sending_emails_to_her_family_in_other_states(self):
        pass
    def she_found_herself_to_be_very_busy_with_work_and_keeping_in_touch_with_people_so_she_never_even_had_time_to_meet_anybody_outside_of_work(self):
        pass
    def it_seemed_as_if_everybody_else_were_settling_down_while_she_was_working_herself_to_death_in_the_big_city(self):
        pass
    def it_had_been_almost_two_months_since_jennifer_moved_into_her_new_apartment_when_one_day_she_found_that_she_wasn_not_really_satisfied_with_it_anymore_which_caught_her_by_surprise_as_she_had_never_even_thought_of_moving_out_yet(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

