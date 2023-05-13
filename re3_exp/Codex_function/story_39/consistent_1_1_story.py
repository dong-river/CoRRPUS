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
        self.connor_riley_is_an_engineer_who_has_recently_been_chosen_to_design_and_build_the_machines_that_will_be_used_to_simulate_the_trees_on_mars()
        self.he_had_been_working_for_three_years_to_earn_this_assignment_and_he_wasn_not_about_to_let_anything_go_wrong()
        self.while_working_on_his_most_recent_assignment_connor_decided_to_call_in_sick()
        self.he_was_very_worried_about_having_the_equipment_he_designed_fail_while_testing_and_he_wasn_not_willing_to_take_any_chances()
        self.later_that_day_connor_regretted_his_decision_to_call_in_sick_because_a_key_part_of_his_invention_began_malfunctioning_during_the_test()
        self.several_people_were_injured_before_it_could_be_stopped()
        self.after_much_debate_between_connor_s_boss_and_another_division_of_the_company_they_decided_that_connor_was_too_valuable_an_employee_to_lose_so_they_transferred_him_immediately_out_of_his_department_and_into_another_division_where_no_one_would_remember_how_badly_he_had_messed_up_at_his_last_job()
    def connor_riley_is_an_engineer_who_has_recently_been_chosen_to_design_and_build_the_machines_that_will_be_used_to_simulate_the_trees_on_mars(self):
        self.Connor_Riley.occupation.append('engineer')
        self.Connor_Riley.gender.append('male')
    def he_had_been_working_for_three_years_to_earn_this_assignment_and_he_wasn_not_about_to_let_anything_go_wrong(self):
        pass
    def while_working_on_his_most_recent_assignment_connor_decided_to_call_in_sick(self):
        pass
    def he_was_very_worried_about_having_the_equipment_he_designed_fail_while_testing_and_he_wasn_not_willing_to_take_any_chances(self):
        pass
    def later_that_day_connor_regretted_his_decision_to_call_in_sick_because_a_key_part_of_his_invention_began_malfunctioning_during_the_test(self):
        pass
    def several_people_were_injured_before_it_could_be_stopped(self):
        pass
    def after_much_debate_between_connor_s_boss_and_another_division_of_the_company_they_decided_that_connor_was_too_valuable_an_employee_to_lose_so_they_transferred_him_immediately_out_of_his_department_and_into_another_division_where_no_one_would_remember_how_badly_he_had_messed_up_at_his_last_job(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

