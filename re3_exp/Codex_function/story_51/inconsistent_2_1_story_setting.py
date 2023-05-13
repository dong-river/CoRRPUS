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
        self.John_Doe = character('John Doe')
        self.Abby_Mills = character('Abby Mills')
        self.Mike_Benson = character('Mike Benson')

    def story(self):
        self.after_a_year_of_being_together_john_andabegan_to_notice_the_cracks_in_their_relationship()
        self.with_jobs_and_school_pulling_them_in_different_directions_they_began_to_grow_apart()
        self.however_when_john_loses_his_job_and_abby_is_diagnosed_with_cancer_they_are_forced_to_lean_on_each_other_for_support()
        self.through_their_difficult_journey_they_realize_that_they_still_have_feelings_for_each_other_and_their_relationship_is_stronger_than_ever()
        self.the_story_is_set_in_a_small_town_in_the_us()
        self.john_doe_is_a_man_in_his_early_30s_with_brown_hair_and_brown_eyes()
        self.he_is_a_construction_worker_who_has_recently_lost_his_job_completion_of_a_construction_project_he_was_working_on_in_the_town_he_lives_in()
        self.abby_mills_is_a_beautiful_woman_in_her_early_30s()
        self.she_has_blonde_hair_and_blue_eyes()
        self.she_is_a_teacher_at_a_local_elementary_school()
        self.mike_benson_is_abby_s_ex_boyfriend()
        self.he_is_in_his_early_30s_and_is_also_a_teacher_at_the_same_elementary_school_as_abby()
    def after_a_year_of_being_together_john_andabegan_to_notice_the_cracks_in_their_relationship(self):
        self.John_Doe.relations['girlfriend'] = 'Abby_Mills'
        self.Abby_Mills.relations['boyfriend'] = 'John_Doe'

    def with_jobs_and_school_pulling_them_in_different_directions_they_began_to_grow_apart(self):
        pass

    def however_when_john_loses_his_job_and_abby_is_diagnosed_with_cancer_they_are_forced_to_lean_on_each_other_for_support(self):
        pass

    def through_their_difficult_journey_they_realize_that_they_still_have_feelings_for_each_other_and_their_relationship_is_stronger_than_ever(self):
        pass

    def the_story_is_set_in_a_small_town_in_the_us(self):
        pass

    def john_doe_is_a_man_in_his_early_30s_with_brown_hair_and_brown_eyes(self):
        self.John_Doe.age.append('early 30s')
        self.John_Doe.gender.append('male')
        self.John_Doe.appearance.append('brown hair')
        self.John_Doe.appearance.append('brown eyes')

    def he_is_a_construction_worker_who_has_recently_lost_his_job_completion_of_a_construction_project_he_was_working_on_in_the_town_he_lives_in(self):
        self.John_Doe.occupation.append('construction worker')

    def abby_mills_is_a_beautiful_woman_in_her_early_30s(self):
        self.Abby_Mills.age.append('early 30s')
        self.Abby_Mills.gender.append('female')
        self.Abby_Mills.appearance.append('beautiful')

    def she_has_blonde_hair_and_blue_eyes(self):
        self.Abby_Mills.appearance.append('blonde hair')
        self.Abby_Mills.appearance.append('blue eyes')

    def she_is_a_teacher_at_a_local_elementary_school(self):
        self.Abby_Mills.occupation.append('elementary school teacher')

    def mike_benson_is_abby_s_ex_boyfriend(self):
        self.Abby_Mills.relations['ex-boyfriend'] = 'Mike_Benson'
        self.Mike_Benson.relations['ex-girlfriend'] = 'Abby_Mills'

    def he_is_in_his_early_30s_and_is_also_a_teacher_at_the_same_elementary_school_as_abby(self):
        self.Mike_Benson.age.append('early 30s')
        self.Mike_Benson.gender.append('male')
        self.Mike_Benson.occupation.append('elementary school teacher')
 
world = World()
world.story()
 
world.John_Doe.appearance

world.Abby_Mills.appearance

world.John_Doe.relations

world.Abby_Mills.relations

world.Mike_Benson.relations

world.John_Doe.occupation

world.Abby_Mills.occupation

world.Mike_Benson.occupation

world.John_Doe.age

world.Abby_Mills.age

world.Mike_Benson.age

world.John_Doe.gender

world.Abby_Mills.gender

world.Mike_Benson.gender

## Create a world model state to track each character's appearance, personality, and relations with other characters.

