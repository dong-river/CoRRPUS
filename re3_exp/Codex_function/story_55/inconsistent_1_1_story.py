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
        self.Emma_Saunders = character('Emma Saunders')
        self.Jackson_Cooper = character('Jackson Cooper')
        self.Olivia_Saunders = character('Olivia Saunders')

    def story(self):
        self.olivia_saunders_woke_up_in_the_middle_of_the_night()
        self.she_could_hear_footsteps_outside_her_room_and_so_she_slowly_got_out_of_bed()
        self.liv()
        self.what_are_you_doing()
        self.asked_her_sister_emma()
        self.it_s_the_middle_of_the_night()
        self.i_heard_something_said_olivia_in_a_hushed_voice()
        self.emma_grabbed_her_sister_s_hand_and_opened_her_bedroom_door_if_you_heard_something_i_want_to_hear_it_too_she_said()
        self.olivia_was_about_to_say_that_there_was_nothing_out_there_but_when_she_stepped_into_the_hallway_she_froze()
        self.she_felt_as_if_something_wasn_not_right_and_so_they_slowly_walked_down_the_stairs_towards_their_parents_room()
        self.the_footsteps_that_they_heard_were_coming_from_there()
        self.their_dad_s_light_was_on_and_olivia_saw_a_strange_shadow_moving_behind_their_parents_open_door()
        self.dad()
        self.emma_whispered_through_the_door_after_knocking_on_it_lightly()
        self.they_waited_for_an_answer_but_none_came_they_pushed_open_the_door_and_rushed_into_their_parent_s_room_to_see_that_their_dad_was_gone()
        self.he_had_disappeared_in_his_sleep_while_it_happened_to_be_the_middle_of_the_night()
    def olivia_saunders_woke_up_in_the_middle_of_the_night(self):
        pass
        
    def she_could_hear_footsteps_outside_her_room_and_so_she_slowly_got_out_of_bed(self):
        pass
        
    def liv(self):
        pass
        
    def what_are_you_doing(self):
        pass
        
    def asked_her_sister_emma(self):
        self.Emma_Saunders.relations['sister'] = 'Olivia_Saunders'
        self.Olivia_Saunders.relations['sister'] = 'Emma_Saunders'
        
    def it_s_the_middle_of_the_night(self):
        pass
        
    def i_heard_something_said_olivia_in_a_hushed_voice(self):
        pass
        
    def emma_grabbed_her_sister_s_hand_and_opened_her_bedroom_door_if_you_heard_something_i_want_to_hear_it_too_she_said(self):
        pass
        
    def olivia_was_about_to_say_that_there_was_nothing_out_there_but_when_she_stepped_into_the_hallway_she_froze(self):
        pass
        
    def she_felt_as_if_something_wasn_not_right_and_so_they_slowly_walked_down_the_stairs_towards_their_parents_room(self):
        pass
        
    def the_footsteps_that_they_heard_were_coming_from_there(self):
        pass
        
    def their_dad_s_light_was_on_and_olivia_saw_a_strange_shadow_moving_behind_their_parents_open_door(self):
        self.Olivia_Saunders.relations['parents'] = 'Jackson_Cooper'
        self.Jackson_Cooper.relations['daughter'] = 'Olivia_Saunders'
        
    def dad(self):
        pass
        
    def emma_whispered_through_the_door_after_knocking_on_it_lightly(self):
        pass
        
    def they_waited_for_an_answer_but_none_came_they_pushed_open_the_door_and_rushed_into_their_parent_s_room_to_see_that_their_dad_was_gone(self):
        pass
        
    def he_had_disappeared_in_his_sleep_while_it_happened_to_be_the_middle_of_the_night(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

