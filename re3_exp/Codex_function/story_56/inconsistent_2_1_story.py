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
        self.Karen_Smith = character('Karen Smith')
        self.Janice_Smith = character('Janice Smith')
        self.Leah_White = character('Leah White')

    def story(self):
        self.leah_white_stood_in_front_of_the_mirror_slipping_on_her_long_black_leather_jacket()
        self.karen_are_you_ready_she_asked_to_her_best_friend()
        self.almost_karen_replied_from_inside_the_bathroom()
        self.i_just_have_to_run_down_and_feed_the_cat_then_i_ll_be_done_leah_glanced_at_her_watch_then_turned_around()
        self.she_was_ready_to_leave_in_fifteen_minutes()
        self.she_began_to_fidget_as_she_waited_for_karen()
        self.leah_was_impatiently_waiting_for_karen_because_they_were_running_late_for_their_job_as_waitresses_at_a_local_diner_called_coco_bells_that_had_been_a_regular_haunt_of_theirs_for_many_years()
        self.they_usually_only_worked_part_time_at_the_diner_during_college_because_they_already_worked_full_time_at_an_advertising_firm_where_they_sold_bumper_stickers_flags_and_other_small_items_that_promised_i_support_our_troops_and_other_mantras_of_political_propaganda_and_bs_like_that()
    def leah_white_stood_in_front_of_the_mirror_slipping_on_her_long_black_leather_jacket(self):
        self.Leah_White.appearance.append('long black leather jacket')
        self.Leah_White.age.append('young')
        self.Leah_White.gender.append('female')
    def karen_are_you_ready_she_asked_to_her_best_friend(self):
        self.Leah_White.relations['best friend'] = 'Karen_Smith'
        self.Karen_Smith.relations['best friend'] = 'Leah_White'
    def almost_karen_replied_from_inside_the_bathroom(self):
        pass
    def i_just_have_to_run_down_and_feed_the_cat_then_i_ll_be_done_leah_glanced_at_her_watch_then_turned_around(self):
        self.Karen_Smith.relations['cat'] = 'cat'
    def she_was_ready_to_leave_in_fifteen_minutes(self):
        pass
    def she_began_to_fidget_as_she_waited_for_karen(self):
        pass
    def leah_was_impatiently_waiting_for_karen_because_they_were_running_late_for_their_job_as_waitresses_at_a_local_diner_called_coco_bells_that_had_been_a_regular_haunt_of_theirs_for_many_years(self):
        self.Leah_White.relations['waitress'] = 'Coco_Bells'
        self.Karen_Smith.relations['waitress'] = 'Coco_Bells'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
    def they_usually_only_worked_part_time_at_the_diner_during_college_because_they_already_worked_full_time_at_an_advertising_firm_where_they_sold_bumper_stickers_flags_and_other_small_items_that_promised_i_support_our_troops_and_other_mantras_of_political_propaganda_and_bs_like_that(self):
        self.Leah_White.relations['waitress'] = 'Coco_Bells'
        self.Karen_Smith.relations['waitress'] = 'Coco_Bells'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
        self.Karen_Smith.relations['waitress'] = 'Leah_White'
        self.Leah_White.relations['waitress'] = 'Karen_Smith'
