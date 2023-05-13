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
        self.Shannon_Riley = character('Shannon Riley')
        self.Robert_Riley = character('Robert Riley')
        self.Jillian_Riley = character('Jillian Riley')

    def story(self):
        self.after_the_loss_of_her_father_shannon_is_determined_to_follow_in_his_footsteps_and_become_a_successful_journalist()
        self.however_when_she_lands_her_first_major_assignment_she_quickly_discovers_that_the_ugly_reality_of_life_in_the_city_is_far_different_from_the_dream_she_imagined()
        self.the_story_is_set_in_a_large_city()
        self.shannon_riley_is_a_young_woman_in_her_early_twenties()
        self.she_has_long_brown_hair_and_blue_eyes()
        self.she_is_of_average_height_and_build()
        self.robert_riley_is_shannon_s_father()
        self.he_was_a_successful_journalist_who_died_suddenly_of_a_heart_attack()
        self.jillian_riley_is_shannon_s_mother()
        self.she_is_a_stay_at_home_mom_who_is_struggling_to_cope_with_her_husband_s_death()
    def after_the_loss_of_her_father_shannon_is_determined_to_follow_in_his_footsteps_and_become_a_successful_journalist(self):
        self.Shannon_Riley.relations['father'] = 'Robert_Riley'
        self.Robert_Riley.relations['daughter'] = 'Shannon_Riley'
        self.Shannon_Riley.occupation.append('journalist')
    def however_when_she_lands_her_first_major_assignment_she_quickly_discovers_that_the_ugly_reality_of_life_in_the_city_is_far_different_from_the_dream_she_imagined(self):
        pass
    def the_story_is_set_in_a_large_city(self):
        pass
    def shannon_riley_is_a_young_woman_in_her_early_twenties(self):
        self.Shannon_Riley.age.append('young')
        self.Shannon_Riley.gender.append('female')
    def she_has_long_brown_hair_and_blue_eyes(self):
        self.Shannon_Riley.appearance.append('long brown hair')
        self.Shannon_Riley.appearance.append('blue eyes')
    def she_is_of_average_height_and_build(self):
        pass
    def robert_riley_is_shannon_s_father(self):
        pass
    def he_was_a_successful_journalist_who_died_suddenly_of_a_heart_attack(self):
        self.Robert_Riley.occupation.append('journalist')
    def jillian_riley_is_shannon_s_mother(self):
        self.Shannon_Riley.relations['mother'] = 'Jillian_Riley'
        self.Jillian_Riley.relations['daughter'] = 'Shannon_Riley'
    def she_is_a_stay_at_home_mom_who_is_struggling_to_cope_with_her_husband_s_death(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

