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
        self.Shannon_Kincaid = character('Shannon Kincaid')
        self.Jack_Kincaid = character('Jack Kincaid')
        self.Mark_Woodbury = character('Mark Woodbury')

    def story(self):
        self.after_the_loss_of_her_father_shannon_is_determined_to_follow_in_his_footsteps_and_become_a_successful_journalist()
        self.however_when_she_lands_her_first_big_story_she_quickly_learns_that_the_ugly_reality_of_life_in_the_city_is_far_different_from_the_dream_she_imagined()
        self.the_story_is_set_in_a_large_city()
        self.shannon_kincaid_is_a_young_woman_in_her_early_twenties()
        self.she_has_long_brown_hair_and_blue_eyes()
        self.she_is_of_average_height_and_build()
        self.jack_kincaid_is_shannon_s_father()
        self.he_was_a_successful_journalist_before_his_untimely_death()
        self.mark_woodbury_is_shannon_s_boss_at_the_newspaper_where_she_works()
        self.he_is_a_middle_aged_man_with_graying_hair_and_a_mustache()
    def after_the_loss_of_her_father_shannon_is_determined_to_follow_in_his_footsteps_and_become_a_successful_journalist(self):
        self.Shannon_Kincaid.relations['father'] = 'Jack_Kincaid'
        self.Jack_Kincaid.relations['daughter'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.occupation.append('journalist')
        self.Jack_Kincaid.occupation.append('journalist')
        
    def however_when_she_lands_her_first_big_story_she_quickly_learns_that_the_ugly_reality_of_life_in_the_city_is_far_different_from_the_dream_she_imagined(self):
        pass
        
    def the_story_is_set_in_a_large_city(self):
        pass
        
    def shannon_kincaid_is_a_young_woman_in_her_early_twenties(self):
        self.Shannon_Kincaid.age.append('early twenties')
        self.Shannon_Kincaid.gender.append('female')
        
    def she_has_long_brown_hair_and_blue_eyes(self):
        self.Shannon_Kincaid.appearance.append('brown hair')
        self.Shannon_Kincaid.appearance.append('blue eyes')
        
    def she_is_of_average_height_and_build(self):
        self.Shannon_Kincaid.appearance.append('average height')
        self.Shannon_Kincaid.appearance.append('average build')
        
    def jack_kincaid_is_shannon_s_father(self):
        self.Jack_Kincaid.relations['father'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['daughter'] = 'Jack_Kincaid'
        
    def he_was_a_successful_journalist_before_his_untimely_death(self):
        self.Jack_Kincaid.occupation.append('journalist')
        
    def mark_woodbury_is_shannon_s_boss_at_the_newspaper_where_she_works(self):
        self.Shannon_Kincaid.relations['boss'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['employee'] = 'Shannon_Kincaid'
        
    def he_is_a_middle_aged_man_with_graying_hair_and_a_mustache(self):
        self.Mark_Woodbury.age.append('middle aged')
        self.Mark_Woodbury.appearance.append('gray hair')
        self.Mark_Woodbury.appearance.append('mustache')

## (1) Create a world model state to track each character's appearance, personality, and relations with other characters.

