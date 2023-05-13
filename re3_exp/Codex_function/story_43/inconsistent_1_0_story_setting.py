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
        self.Shannon_Mulaney = character('Shannon Mulaney')
        self.Jess_Abernathy = character('Jess Abernathy')
        self.Olivia_Kendall = character('Olivia Kendall')

    def story(self):
        self.after_losing_her_mom_to_cancer_shannon_is_really_struggling_in_her_first_year_of_college()
        self.she_s_failing_all_her_classes_and_is_ready_to_give_up_when_she_meets_her_ra_jess()
        self.jess_is_really_easy_to_talk_to_and_has_been_through_a_lot_in_her_life()
        self.through_their_talks_and_late_night_study_sessions_shannon_starts_to_turn_her_life_around()
        self.the_story_is_set_in_shannon_s_college_dorm_room_and_the_common_areas_of_the_dorm_building()
        self.shannon_mulaney_is_a_20_year_old_student_at_xyz_university()
        self.she_is_petite_and_has_long_curly_red_hair()
        self.shannon_is_from_a_small_town_in_upstate_new_york_and_is_the_only_child_of_her_parents()
        self.jess_abernathy_is_a_21_year_old_student_at_xyz_university_and_shannon_s_ra()
        self.jess_is_tall_and_has_straight_blond_hair_that_she_often_wears_in_a_ponytail()
        self.she_is_originally_from_california_and_is_the_oldest_of_three_sisters()
        self.olivia_kendall_is_shannon_s_best_friend_from_high_school_who_is_also_attending_xyz_university_with_her()
        self.olivia_is_of_average_height_with_wavy_brown_hair_and_hazel_eyes()
    def after_losing_her_mom_to_cancer_shannon_is_really_struggling_in_her_first_year_of_college(self):
        self.Shannon_Mulaney.relations['mom'] = 'dead'
    def she_s_failing_all_her_classes_and_is_ready_to_give_up_when_she_meets_her_ra_jess(self):
        self.Shannon_Mulaney.occupation.append('student')
        self.Jess_Abernathy.occupation.append('RA')
    def jess_is_really_easy_to_talk_to_and_has_been_through_a_lot_in_her_life(self):
        pass
    def through_their_talks_and_late_night_study_sessions_shannon_starts_to_turn_her_life_around(self):
        pass
    def the_story_is_set_in_shannon_s_college_dorm_room_and_the_common_areas_of_the_dorm_building(self):
        self.Shannon_Mulaney.occupation.append('student')
    def shannon_mulaney_is_a_20_year_old_student_at_xyz_university(self):
        self.Shannon_Mulaney.age.append('20')
        self.Shannon_Mulaney.occupation.append('student')
    def she_is_petite_and_has_long_curly_red_hair(self):
        self.Shannon_Mulaney.appearance.append('petite')
        self.Shannon_Mulaney.appearance.append('long curly red hair')
    def shannon_is_from_a_small_town_in_upstate_new_york_and_is_the_only_child_of_her_parents(self):
        self.Shannon_Mulaney.relations['parents'] = 'dead'
    def jess_abernathy_is_a_21_year_old_student_at_xyz_university_and_shannon_s_ra(self):
        self.Jess_Abernathy.age.append('21')
        self.Jess_Abernathy.occupation.append('student')
    def jess_is_tall_and_has_straight_blond_hair_that_she_often_wears_in_a_ponytail(self):
        self.Jess_Abernathy.appearance.append('tall')
        self.Jess_Abernathy.appearance.append('straight blond hair')
    def she_is_originally_from_california_and_is_the_oldest_of_three_sisters(self):
        self.Jess_Abernathy.relations['sisters'] = '3'
    def olivia_kendall_is_shannon_s_best_friend_from_high_school_who_is_also_attending_xyz_university_with_her(self):
        self.Shannon_Mulaney.relations['best friend'] = 'Olivia_Kendall'
        self.Olivia_Kendall.relations['best friend'] = 'Shannon_Mulaney'
    def olivia_is_of_average_height_with_wavy_brown_hair_and_hazel_eyes(self):
        self.Olivia_Kendall.appearance.append('average height')
        self.Olivia_Kendall.appearance.append('wavy brown hair')
        self.Olivia_Kendall.appearance.append('hazel eyes')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

