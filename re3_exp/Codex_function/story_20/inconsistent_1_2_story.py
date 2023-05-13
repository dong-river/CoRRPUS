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
        self.Olivia_Fria_Spierings = character('Olivia Fria Spierings')
        self.Colonel_Damien_Riggs = character('Colonel Damien Riggs')

    def story(self):
        self.olivia_fria_spierings_was_marching_down_the_hallway_when_colonel_damien_riggs_s_aide_called_her_into_his_office()
        self.she_knew_what_was_coming()
        self.she_was_short_and_skinny_with_long_dark_hair_blue_eyes_and_a_pretty_face()
        self.she_wanted_to_join_the_army_because_it_looked_like_an_exciting_career_to_her_and_she_wanted_a_new_challenge_in_life()
        self.but_the_army_wasn_not_very_interested_in_people_who_looked_like_olivia_fria_spierings()
        self.so_they_made_her_a_supply_clerk_which_was_basically_a_glorified_file_clerk()
        self.it_wasn_not_exactly_challenging_work_and_she_spent_most_of_her_time_indoors_at_a_desk_behind_piles_of_paperwork_instead_of_out_on_the_battlefield_as_she_had_hoped_when_she_joined_up_seven_years_ago_at_age_18()
        self.colonel_damien_riggs_watched_olivia_through_half_closed_eyes_as_she_entered_his_office()
        self.this_girl_made_him_uncomfortable_for_some_reason_and_he_wasn_not_quite_sure_why()
        self.he_didn_not_like_pretty_young_girls_with_long_dark_hair_and_blue_eyes_whose_slender_arms_were_covered_in_tattoos_from_their_fingertips_all_the_way_up_to_their_shoulders_including_one_with_bird_wings_wrapped_around_them_from_shoulder_to_shoulder_that_he_found_particularly_interesting_though_he_couldn_not_explain_why()
    def olivia_fria_spierings_was_marching_down_the_hallway_when_colonel_damien_riggs_s_aide_called_her_into_his_office(self):
        pass
    def she_knew_what_was_coming(self):
        pass
    def she_was_short_and_skinny_with_long_dark_hair_blue_eyes_and_a_pretty_face(self):
        self.Olivia_Fria_Spierings.appearance.append('short')
        self.Olivia_Fria_Spierings.appearance.append('skinny')
        self.Olivia_Fria_Spierings.appearance.append('long dark hair')
        self.Olivia_Fria_Spierings.appearance.append('blue eyes')
        self.Olivia_Fria_Spierings.appearance.append('pretty face')
    def she_wanted_to_join_the_army_because_it_looked_like_an_exciting_career_to_her_and_she_wanted_a_new_challenge_in_life(self):
        self.Olivia_Fria_Spierings.occupation.append('army')
    def but_the_army_wasn_not_very_interested_in_people_who_looked_like_olivia_fria_spierings(self):
        pass
    def so_they_made_her_a_supply_clerk_which_was_basically_a_glorified_file_clerk(self):
        self.Olivia_Fria_Spierings.occupation.append('supply clerk')
    def it_wasn_not_exactly_challenging_work_and_she_spent_most_of_her_time_indoors_at_a_desk_behind_piles_of_paperwork_instead_of_out_on_the_battlefield_as_she_had_hoped_when_she_joined_up_seven_years_ago_at_age_18(self):
        self.Olivia_Fria_Spierings.age.append('18')
    def colonel_damien_riggs_watched_olivia_through_half_closed_eyes_as_she_entered_his_office(self):
        pass
    def this_girl_made_him_uncomfortable_for_some_reason_and_he_wasn_not_quite_sure_why(self):
        pass
    def he_didn_not_like_pretty_young_girls_with_long_dark_hair_and_blue_eyes_whose_slender_arms_were_covered_in_tattoos_from_their_fingertips_all_the_way_up_to_their_shoulders_including_one_with_bird_wings_wrapped_around_them_from_shoulder_to_shoulder_that_he_found_particularly_interesting_though_he_couldn_not_explain_why(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

