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
        self.when_the_last_of_the_world_s_trees_are_gone_the_humans_are_forced_to_find_alternative_sources_of_oxygen()
        self.they_build_giant_machines_to_simulate_the_trees_but_the_air_is_still_not_clean_enough()
        self.the_government_decides_to_send_a_team_of_scientists_to_mars_to_see_if_there_is_any_possibility_of_life_there()
        self.if_they_can_find_a_way_to_terraform_mars_maybe_the_humans_can_have_a_chance_at_survival()
        self.the_story_is_set_in_a_future_world_where_the_last_of_the_trees_have_been_wiped_out_and_the_humans_are_struggling_to_find_a_way_to_survive()
        self.nadia_kaminski_is_a_scientist_who_specializes_in_astrobiology()
        self.she_is_chosen_to_be_part_of_the_team_that_is_sent_to_mars_to_investigate_the_possibility_of_life_there()
        self.connor_riley_is_an_astronaut_who_is_chosen_to_be_the_pilot_of_the_spaceship_that_will_take_the_team_to_mars()
        self.abigail_harper_is_a_doctor_who_is_chosen_to_be_part_of_the_medical_team_that_will_be_responsible_for_the_health_of_the_astronauts_during_their_stay_on_mars()
    def when_the_last_of_the_world_s_trees_are_gone_the_humans_are_forced_to_find_alternative_sources_of_oxygen(self):
        pass
    def they_build_giant_machines_to_simulate_the_trees_but_the_air_is_still_not_clean_enough(self):
        pass
    def the_government_decides_to_send_a_team_of_scientists_to_mars_to_see_if_there_is_any_possibility_of_life_there(self):
        pass
    def if_they_can_find_a_way_to_terraform_mars_maybe_the_humans_can_have_a_chance_at_survival(self):
        pass
    def the_story_is_set_in_a_future_world_where_the_last_of_the_trees_have_been_wiped_out_and_the_humans_are_struggling_to_find_a_way_to_survive(self):
        pass
    def nadia_kaminski_is_a_scientist_who_specializes_in_astrobiology(self):
        self.Nadia_Kaminski.occupation.append('scientist')
        self.Nadia_Kaminski.occupation.append('astrobiology')
    def she_is_chosen_to_be_part_of_the_team_that_is_sent_to_mars_to_investigate_the_possibility_of_life_there(self):
        pass
    def connor_riley_is_an_astronaut_who_is_chosen_to_be_the_pilot_of_the_spaceship_that_will_take_the_team_to_mars(self):
        self.Connor_Riley.occupation.append('astronaut')
        self.Connor_Riley.occupation.append('pilot')
    def abigail_harper_is_a_doctor_who_is_chosen_to_be_part_of_the_medical_team_that_will_be_responsible_for_the_health_of_the_astronauts_during_their_stay_on_mars(self):
        self.Abigail_Harper.occupation.append('doctor')
        self.Abigail_Harper.occupation.append('medical team')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

