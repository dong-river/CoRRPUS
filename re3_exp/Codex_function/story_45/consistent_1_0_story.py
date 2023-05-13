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
        self.Nina_Harman = character('Nina Harman')
        self.Jake_Ryan = character('Jake Ryan')
        self.Karen_Hartman = character('Karen Hartman')

    def story(self):
        self.karen_hartman_was_worried_about_her_daughter_nina()
        self.she_was_worried_because_the_child_was_becoming_increasingly_withdrawn_and_moody()
        self.it_all_started_a_few_months_ago_when_she_would_wake_up_in_the_middle_of_the_night_sobbing_and_thrashing_wildly_around_in_her_bed()
        self.every_time_she_was_questioned_about_it_she_would_give_the_same_answer_i_don_not_know()
        self.karen_decided_to_put_it_out_of_her_mind_as_her_daughter_began_school_this_year()
        self.but_she_started_having_problems_there_too_showing_unusual_interest_in_anything_that_resembled_ghost_stories_or_movies_with_lots_of_special_effects()
        self.she_even_began_asking_questions_about_ghosts_in_everyday_life_to_both_her_teachers_and_the_students_around_her_at_school()
        self.some_of_the_other_students_had_heard_rumors_about_a_house_on_charlotte_street_that_supposedly_haunted_and_laughed_at_nina_s_questions_and_rumors_went_through_the_school_about_nina_having_a_crush_on_a_cute_boy_that_lived_there_named_jake_ryan()
        self.do_you_know_who_i_am_talking_about()
        self.asked_nina_anxiously_as_she_continued_pacing_back_and_forth_from_one_end_of_karen_s_living_room_to_another_stopping_every_so_often_to_look_at_something_intently_out_one_of_the_windows_or_shake_her_head_slowly_side_to_side_like_someone_in_deep_thought()
        self.karen_shook_her_head_no_in_response()
    def karen_hartman_was_worried_about_her_daughter_nina(self):
        self.Nina_Harman.gender.append('female')
        self.Karen_Hartman.gender.append('female')
        self.Nina_Harman.relations['mother'] = 'Karen_Hartman'
        self.Karen_Hartman.relations['daughter'] = 'Nina_Harman'

    def she_was_worried_because_the_child_was_becoming_increasingly_withdrawn_and_moody(self):
        pass
    
    def it_all_started_a_few_months_ago_when_she_would_wake_up_in_the_middle_of_the_night_sobbing_and_thrashing_wildly_around_in_her_bed(self):
        pass
    
    def every_time_she_was_questioned_about_it_she_would_give_the_same_answer_i_don_not_know(self):
        pass
    
    def karen_decided_to_put_it_out_of_her_mind_as_her_daughter_began_school_this_year(self):
        pass
    
    def but_she_started_having_problems_there_too_showing_unusual_interest_in_anything_that_resembled_ghost_stories_or_movies_with_lots_of_special_effects(self):
        pass
    
    def she_even_began_asking_questions_about_ghosts_in_everyday_life_to_both_her_teachers_and_the_students_around_her_at_school(self):
        pass
    
    def some_of_the_other_students_had_heard_rumors_about_a_house_on_charlotte_street_that_supposedly_haunted_and_laughed_at_nina_s_questions_and_rumors_went_through_the_school_about_nina_having_a_crush_on_a_cute_boy_that_lived_there_named_jake_ryan(self):
        pass
    
    def do_you_know_who_i_am_talking_about(self):
        pass
    
    def asked_nina_anxiously_as_she_continued_pacing_back_and_forth_from_one_end_of_karen_s_living_room_to_another_stopping_every_so_often_to_look_at_something_intently_out_one_of_the_windows_or_shake_her_head_slowly_side_to_side_like_someone_in_deep_thought(self):
        pass
    
    def karen_shook_her_head_no_in_response(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

