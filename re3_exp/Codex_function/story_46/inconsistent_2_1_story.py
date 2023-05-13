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
        self.Jessica_Campbell = character('Jessica Campbell')
        self.John_Smith = character('John Smith')
        self.Tina_Sanchez = character('Tina Sanchez')

    def story(self):
        self.tina_sanchez_sat_behind_the_mirror_in_her_large_dressing_room_dabbing_makeup_on_a_young_model_s_face()
        self.turn_your_head_slightly_she_instructed()
        self.that_s_it_yes()
        self.perfect()
        self.you_are_so_beautiful()
        self.the_designer_will_be_ecstatic()
        self.i_just_know_it()
        self.you_know_how_strict_he_is_about_his_designs_being_showcased_by_only_the_best_looking_models_he_can_find()
        self.this_is_going_to_be_a_big_show_tina_glanced_around_the_room_at_all_the_other_stylists_working_on_other_models()
        self.they_were_everywhere_creating_intricate_hairstyles_and_painting_beautiful_designs_on_faces_and_bodies_to_match_the_clothing_they_were_dressing()
        self.she_smiled_at_her_own_reflection_in_the_mirror_her_thick_black_hair_was_swept_back_from_her_face_and_she_had_on_perfectly_applied_makeup_that_perfectly_matched_her_short_black_dress_that_perfectly_matched_her_shoes_that_perfectly_matched_everything_else_about_her_appearance_today()
        self.there_was_nothing_about_her_that_wasn_t_perfect_in_every_detail_no_matter_what_others_might_say_about_it_all_perfectly_understated_and_incredibly_chic_perfect_for_working_in_the_new_york_fashion_industry_where_only_the_best_of_everything_counted_for_anything_at_all()
    def tina_sanchez_sat_behind_the_mirror_in_her_large_dressing_room_dabbing_makeup_on_a_young_model_s_face(self):
        self.Tina_Sanchez.relations['employer'] = 'Jessica_Campbell'
    def turn_your_head_slightly_she_instructed(self):
        pass
    def that_s_it_yes(self):
        pass
    def perfect(self):
        pass
    def you_are_so_beautiful(self):
        pass
    def the_designer_will_be_ecstatic(self):
        pass
    def i_just_know_it(self):
        pass
    def you_know_how_strict_he_is_about_his_designs_being_showcased_by_only_the_best_looking_models_he_can_find(self):
        pass
    def this_is_going_to_be_a_big_show_tina_glanced_around_the_room_at_all_the_other_stylists_working_on_other_models(self):
        pass
    def they_were_everywhere_creating_intricate_hairstyles_and_painting_beautiful_designs_on_faces_and_bodies_to_match_the_clothing_they_were_dressing(self):
        pass
    def she_smiled_at_her_own_reflection_in_the_mirror_her_thick_black_hair_was_swept_back_from_her_face_and_she_had_on_perfectly_applied_makeup_that_perfectly_matched_her_short_black_dress_that_perfectly_matched_her_shoes_that_perfectly_matched_everything_else_about_her_appearance_today(self):
        pass
    def there_was_nothing_about_her_that_wasn_t_perfect_in_every_detail_no_matter_what_others_might_say_about_it_all_perfectly_understated_and_incredibly_chic_perfect_for_working_in_the_new_york_fashion_industry_where_only_the_best_of_everything_counted_for_anything_at_all(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

