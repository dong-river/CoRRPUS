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
        self.shannon_mulaney_is_an_18_year_old_from_michigan_and_is_attending_xyz_university_in_boston_massachusetts_on_a_full_softball_scholarship_xyz_being_a_large_division_1_universities_in_boston_with_over_30_000_students()
        self.shannon_is_5_10_with_wavy_brown_blonde_ombre_roots_which_she_dyes_herself_blue_eyes_pale_skin_and_an_athletic_build_somewhat_muscular_especially_in_legs_thighs()
        self.jess_abernathy_is_a_21_year_old_student_at_xyz_university_and_shannon_s_ra()
        self.jess_is_tall_and_has_straight_blond_hair_that_she_often_wears_in_a_ponytail()
        self.she_is_originally_from_california_and_is_the_oldest_of_three_sisters()
        self.olivia_kendall_is_shannon_s_best_friend_from_high_school_who_is_also_attending_xyz_university_with_her()
        self.olivia_is_of_average_height_with_wavy_brown_hair_and_hazel_eyes()
    def after_losing_her_mom_to_cancer_shannon_is_really_struggling_in_her_first_year_of_college(self):
        self.Shannon_Mulaney.relations['mom'] = 'Cancer'
        
    def she_s_failing_all_her_classes_and_is_ready_to_give_up_when_she_meets_her_ra_jess(self):
        self.Shannon_Mulaney.occupation.append('student')
        self.Shannon_Mulaney.relations['ra'] = 'Jess_Abernathy'
        self.Jess_Abernathy.relations['student'] = 'Shannon_Mulaney'
        
    def jess_is_really_easy_to_talk_to_and_has_been_through_a_lot_in_her_life(self):
        self.Jess_Abernathy.appearance.append('easy to talk to')
        
    def through_their_talks_and_late_night_study_sessions_shannon_starts_to_turn_her_life_around(self):
        pass
    
    def the_story_is_set_in_shannon_s_college_dorm_room_and_the_common_areas_of_the_dorm_building(self):
        self.Shannon_Mulaney.occupation.append('student')
        
    def shannon_mulaney_is_an_18_year_old_from_michigan_and_is_attending_xyz_university_in_boston_massachusetts_on_a_full_softball_scholarship_xyz_being_a_large_division_1_universities_in_boston_with_over_30_000_students(self):
        self.Shannon_Mulaney.age.append('18')
        self.Shannon_Mulaney.occupation.append('student')
        
    def shannon_is_5_10_with_wavy_brown_blonde_ombre_roots_which_she_dyes_herself_blue_eyes_pale_skin_and_an_athletic_build_somewhat_muscular_especially_in_legs_thighs(self):
        self.Shannon_Mulaney.appearance.append('5_10')
        self.Shannon_Mulaney.appearance.append('wavy_brown_blonde_ombre_roots')
        self.Shannon_Mulaney.appearance.append('blue_eyes')
        self.Shannon_Mulaney.appearance.append('pale_skin')
        self.Shannon_Mulaney.appearance.append('somewhat_muscular')
        self.Shannon_Mulaney.appearance.append('especially_in_legs_thighs')
        
    def jess_abernathy_is_a_21_year_old_student_at_xyz_university_and_shannon_s_ra(self):
        self.Jess_Abernathy.age.append('21')
        self.Jess_Abernathy.occupation.append('student')
        self.Jess_Abernathy.relations['student'] = 'Shannon_Mulaney'
        
    def jess_is_tall_and_has_straight_blond_hair_that_she_often_wears_in_a_ponytail(self):
        self.Jess_Abernathy.appearance.append('tall')
        self.Jess_Abernathy.appearance.append('straight_blond_hair')
        
    def she_is_originally_from_california_and_is_the_oldest_of_three_sisters(self):
        self.Jess_Abernathy.appearance.append('from_california')
        self.Jess_Abernathy.appearance.append('oldest_of_three_sisters')
        
    def olivia_kendall_is_shannon_s_best_friend_from_high_school_who_is_also_attending_xyz_university_with_her(self):
        self.Olivia_Kendall.relations['best_friend'] = 'Shannon_Mulaney'
        self.Shannon_Mulaney.relations['best_friend'] = 'Olivia_Kendall'
        self.Olivia_Kendall.occupation.append('student')
        
    def olivia_is_of_average_height_with_wavy_brown_hair_and_hazel_eyes(self):
        self.Olivia_Kendall.appearance.append('average_height')
        self.Olivia_Kendall.appearance.append('wavy_brown_hair')
        self.Olivia_Kendall.appearance.append('hazel_eyes')
        
## Create a world model state to track each character's appearance, personality, and relations with other characters.

