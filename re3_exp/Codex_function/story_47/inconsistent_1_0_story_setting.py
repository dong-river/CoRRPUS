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
        self.Shannon_Burke = character('Shannon Burke')
        self.Charles_Burke = character('Charles Burke')
        self.Maxine_Carter = character('Maxine Carter')

    def story(self):
        self.after_the_loss_of_her_father_shannon_is_determined_to_follow_in_his_footsteps_and_become_a_successful_journalist()
        self.however_when_she_lands_her_first_major_assignment_she_quickly_discovers_that_the_ugly_reality_of_life_in_the_city_is_far_different_from_the_dream_she_imagined()
        self.the_story_is_set_in_a_large_city()
        self.shannon_burke_is_a_young_woman_in_her_early_twenties()
        self.she_is_of_average_height_and_build_with_shoulder_length_brown_hair_and_hazel_eyes()
        self.charles_burke_is_shannon_s_father()
        self.he_was_a_successful_journalist_who_died_unexpectedly_a_few_years_ago()
        self.maxine_carter_is_a_veteran_reporter_who_takes_shannon_under_her_wing_at_the_news_station()
        self.she_is_in_her_late_forties_and_is_known_for_her_no_nonsense_attitude_and_sharp_wit()
    def after_the_loss_of_her_father_shannon_is_determined_to_follow_in_his_footsteps_and_become_a_successful_journalist(self):
        pass
    
    def however_when_she_lands_her_first_major_assignment_she_quickly_discovers_that_the_ugly_reality_of_life_in_the_city_is_far_different_from_the_dream_she_imagined(self):
        pass
        
    def the_story_is_set_in_a_large_city(self):
        pass
    
    def shannon_burke_is_a_young_woman_in_her_early_twenties(self):
        self.Shannon_Burke.age.append('young')
        self.Shannon_Burke.gender.append('female')
        
    def she_is_of_average_height_and_build_with_shoulder_length_brown_hair_and_hazel_eyes(self):
        self.Shannon_Burke.appearance.append('average height')
        self.Shannon_Burke.appearance.append('average build')
        self.Shannon_Burke.appearance.append('shoulder length brown hair')
        self.Shannon_Burke.appearance.append('hazel eyes')
        
    def charles_burke_is_shannon_s_father(self):
        self.Shannon_Burke.relations['father'] = 'Charles_Burke'
        self.Charles_Burke.relations['daughter'] = 'Shannon_Burke'
        
    def he_was_a_successful_journalist_who_died_unexpectedly_a_few_years_ago(self):
        self.Charles_Burke.occupation.append('journalist')
        
    def maxine_carter_is_a_veteran_reporter_who_takes_shannon_under_her_wing_at_the_news_station(self):
        self.Maxine_Carter.occupation.append('reporter')
        self.Shannon_Burke.relations['mentor'] = 'Maxine_Carter'
        self.Maxine_Carter.relations['mentee'] = 'Shannon_Burke'
        
    def she_is_in_her_late_forties_and_is_known_for_her_no_nonsense_attitude_and_sharp_wit(self):
        self.Maxine_Carter.age.append('older')
        self.Maxine_Carter.gender.append('female')

world = World()
world.story()
 
world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world.Shannon_Burke.gender

world.Shannon_Burke.age

world.Maxine_Carter.age

world.Maxine_Carter.gender

world.Charles_Burke.occupation

world.Charles_Burke.relations

world.Maxine_Carter.relations

world.Shannon_Burke.relations

world.Shannon_Burke.appearance

world.Maxine_Carter.occupation

world