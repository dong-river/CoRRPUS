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
        self.Lettie_Hanson = character('Lettie Hanson')
        self.Bob_Hanson = character('Bob Hanson')
        self.Karen_Hanson = character('Karen Hanson')

    def story(self):
        self.karen_hanson_was_having_a_hard_time_finding_her_aunt_lettie()
        self.she_tried_calling_several_times_but_she_wasn_not_answering_her_phone()
        self.she_didn_not_want_to_bother_bob_and_mary_so_she_decided_to_drive_over_to_the_hanson_residence()
        self.when_karen_arrived_at_the_house_no_one_answered_the_door()
        self.how_can_this_be()
        self.she_thought_to_herself()
        self.it_s_way_too_early_for_them_to_go_out_for_the_day()
        self.suddenly_she_got_an_idea()
        self.she_went_around_back_and_climbed_in_through_a_window_in_bob_s_workshop_where_they_would_often_play_tricks_on_each_other_and_say_they_wouldn_not_lock_it_when_they_left()
        self.the_door_had_been_jammed_ever_since_bob_s_last_attempt()
        self.karen_was_sure_that_was_where_lettie_would_be_right_now()
        self.she_burst_into_the_room_and_found_lettie_curled_up_on_the_bed_sobbing()
        self.when_she_looked_up_karen_saw_that_her_eyes_were_blackened_and_red_from_crying_so_much()
        self.what_happened()
        self.asked_karen_frantically_as_she_came_running_over_to_sit_down_next_to_her_aunt_on_the_bed()
        self.i_ve_been_trying_to_call_you_all_morning()
    def karen_hanson_was_having_a_hard_time_finding_her_aunt_lettie(self):
        self.Lettie_Hanson.relations['niece'] = 'Karen_Hanson'
        self.Karen_Hanson.relations['aunt'] = 'Lettie_Hanson'
    def she_tried_calling_several_times_but_she_wasn_not_answering_her_phone(self):
        pass
    def she_didn_not_want_to_bother_bob_and_mary_so_she_decided_to_drive_over_to_the_hanson_residence(self):
        self.Lettie_Hanson.relations['husband'] = 'Bob_Hanson'
        self.Lettie_Hanson.relations['daughter'] = 'Karen_Hanson'
        self.Bob_Hanson.relations['wife'] = 'Lettie_Hanson'
        self.Karen_Hanson.relations['parents'] = 'Bob_Hanson'
        self.Bob_Hanson.relations['daughter'] = 'Karen_Hanson'
    def when_karen_arrived_at_the_house_no_one_answered_the_door(self):
        pass
    def how_can_this_be(self):
        pass
    def she_thought_to_herself(self):
        pass
    def it_s_way_too_early_for_them_to_go_out_for_the_day(self):
        pass
    def suddenly_she_got_an_idea(self):
        pass
    def she_went_around_back_and_climbed_in_through_a_window_in_bob_s_workshop_where_they_would_often_play_tricks_on_each_other_and_say_they_wouldn_not_lock_it_when_they_left(self):
        self.Bob_Hanson.occupation.append('workshop')
    def the_door_had_been_jammed_ever_since_bob_s_last_attempt(self):
        self.Bob_Hanson.appearance.append('jammed door')
    def karen_was_sure_that_was_where_lettie_would_be_right_now(self):
        self.Lettie_Hanson.occupation.append('bed')
    def she_burst_into_the_room_and_found_lettie_curled_up_on_the_bed_sobbing(self):
        pass
    def when_she_looked_up_karen_saw_that_her_eyes_were_blackened_and_red_from_crying_so_much(self):
        self.Lettie_Hanson.appearance.append('blackened eyes')
    def what_happened(self):
        pass
    def asked_karen_frantically_as_she_came_running_over_to_sit_down_next_to_her_aunt_on_the_bed(self):
        pass
    def i_ve_been_trying_to_call_you_all_morning(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

