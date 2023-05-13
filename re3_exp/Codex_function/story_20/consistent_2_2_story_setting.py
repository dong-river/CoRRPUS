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
        self.the_novel_is_set_in_a_future_in_which_the_world_is_at_war()
        self.the_main_character_a_young_girl_is_drafted_into_the_army()
        self.the_story_is_set_in_a_future_world_that_is_at_war()
        self.olivia_fria_spierings_is_a_young_girl_who_is_drafted_into_the_army()
        self.she_is_a_small_skinny_girl_with_long_dark_hair_and_blue_eyes()
        self.colonel_damien_riggs_is_the_commanding_officer_of_olivia_s_unit()
        self.he_is_a_tall_muscular_man_in_his_early_40s_with_short_graying_hair_and_blue_eyes()
    def the_novel_is_set_in_a_future_in_which_the_world_is_at_war(self):
        pass
    def the_main_character_a_young_girl_is_drafted_into_the_army(self):
        pass
    def the_story_is_set_in_a_future_world_that_is_at_war(self):
        pass
    def olivia_fria_spierings_is_a_young_girl_who_is_drafted_into_the_army(self):
        self.Olivia_Fria_Spierings.gender.append('female')
        self.Olivia_Fria_Spierings.age.append('young')
    def she_is_a_small_skinny_girl_with_long_dark_hair_and_blue_eyes(self):
        self.Olivia_Fria_Spierings.appearance.append('small')
        self.Olivia_Fria_Spierings.appearance.append('skinny')
        self.Olivia_Fria_Spierings.appearance.append('long dark hair')
        self.Olivia_Fria_Spierings.appearance.append('blue eyes')
    def colonel_damien_riggs_is_the_commanding_officer_of_olivia_s_unit(self):
        self.Colonel_Damien_Riggs.occupation.append('commanding officer')
        self.Olivia_Fria_Spierings.relations['commanding officer'] = 'Colonel_Damien_Riggs'
    def he_is_a_tall_muscular_man_in_his_early_40s_with_short_graying_hair_and_blue_eyes(self):
        self.Colonel_Damien_Riggs.appearance.append('tall')
        self.Colonel_Damien_Riggs.appearance.append('muscular')
        self.Colonel_Damien_Riggs.appearance.append('short graying hair')
        self.Colonel_Damien_Riggs.appearance.append('blue eyes')
        self.Colonel_Damien_Riggs.age.append('40s')

