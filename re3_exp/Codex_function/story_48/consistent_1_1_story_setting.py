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
        self.Shannon_Fitzgerald = character('Shannon Fitzgerald')
        self.Olivia_Kane = character('Olivia Kane')
        self.Richard_Kane = character('Richard Kane')

    def story(self):
        self.after_the_loss_of_her_mother_shannon_is_determined_to_keep_her_promise_and_finish_her_degree()
        self.but_with_mounting_bills_and_a_full_time_job_shannon_is_struggling_to_make_ends_meet()
        self.when_she_s_offered_a_position_as_a_live_in_nanny_for_a_wealthy_family_shannon_jumps_at_the_chance()
        self.but_she_soon_discovers_that_the_family_s_secrets_are_far_more_dangerous_than_she_could_have_imagined()
        self.the_story_is_set_in_a_small_town_in_the_united_states()
        self.shannon_fitzgerald_is_a_young_woman_in_her_early_twenties()
        self.she_is_of_average_height_and_build_with_shoulder_length_brown_hair_and_brown_eyes()
        self.shannon_is_a_diligent_student_working_hard_to_earn_her_degree_despite_the_challenges_she_faces()
        self.olivia_kane_is_a_woman_in_her_thirties()
        self.she_is_the_wife_of_a_wealthy_man_and_the_mother_of_two_children()
        self.olivia_is_a_beautiful_woman_with_long_blonde_hair_and_blue_eyes()
        self.richard_kane_is_a_man_in_his_forties()
        self.he_is_the_husband_of_olivia_kane_and_the_father_of_two_children()
        self.richard_is_a_successful_businessman_with_a_commanding_presence_and_an_air_of_authority_about_him()
    def after_the_loss_of_her_mother_shannon_is_determined_to_keep_her_promise_and_finish_her_degree(self):
        pass

    def but_with_mounting_bills_and_a_full_time_job_shannon_is_struggling_to_make_ends_meet(self):
        pass

    def when_she_s_offered_a_position_as_a_live_in_nanny_for_a_wealthy_family_shannon_jumps_at_the_chance(self):
        pass

    def but_she_soon_discovers_that_the_family_s_secrets_are_far_more_dangerous_than_she_could_have_imagined(self):
        pass

    def the_story_is_set_in_a_small_town_in_the_united_states(self):
        pass

    def shannon_fitzgerald_is_a_young_woman_in_her_early_twenties(self):
        self.Shannon_Fitzgerald.age.append('young')
        self.Shannon_Fitzgerald.gender.append('female')

    def she_is_of_average_height_and_build_with_shoulder_length_brown_hair_and_brown_eyes(self):
        self.Shannon_Fitzgerald.appearance.append('average height')
        self.Shannon_Fitzgerald.appearance.append('average build')
        self.Shannon_Fitzgerald.appearance.append('shoulder length brown hair')
        self.Shannon_Fitzgerald.appearance.append('brown eyes')

    def shannon_is_a_diligent_student_working_hard_to_earn_her_degree_despite_the_challenges_she_faces(self):
        self.Shannon_Fitzgerald.occupation.append('diligent student')
        self.Shannon_Fitzgerald.occupation.append('hard worker')

    def olivia_kane_is_a_woman_in_her_thirties(self):
        self.Olivia_Kane.age.append('thirties')
        self.Olivia_Kane.gender.append('female')

    def she_is_the_wife_of_a_wealthy_man_and_the_mother_of_two_children(self):
        self.Olivia_Kane.relations['husband'] = 'Richard_Kane'
        self.Olivia_Kane.relations['children'] = 'two'
        self.Richard_Kane.relations['wife'] = 'Olivia_Kane'
        self.Richard_Kane.relations['children'] = 'two'

    def olivia_is_a_beautiful_woman_with_long_blonde_hair_and_blue_eyes(self):
        self.Olivia_Kane.appearance.append('beautiful')
        self.Olivia_Kane.appearance.append('long blonde hair')
        self.Olivia_Kane.appearance.append('blue eyes')

    def richard_kane_is_a_man_in_his_forties(self):
        self.Richard_Kane.age.append('forties')
        self.Richard_Kane.gender.append('male')

    def he_is_the_husband_of_olivia_kane_and_the_father_of_two_children(self):
        self.Richard_Kane.relations['husband'] = 'Olivia_Kane'
        self.Richard_Kane.relations['children'] = 'two'
        self.Olivia_Kane.relations['husband'] = 'Richard_Kane'
        self.Olivia_Kane.relations['children'] = 'two'

    def richard_is_a_successful_businessman_with_a_commanding_presence_and_an_air_of_authority_about_him(self):
        self.Richard_Kane.occupation.append('successful businessman')
        self.Richard_Kane.appearance.append('commanding presence')
        self.Richard_Kane.appearance.append('air of authority')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

