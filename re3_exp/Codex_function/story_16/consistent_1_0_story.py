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
        self.Jennifer_Ann_Smith = character('Jennifer Ann Smith')
        self.Clara_Smith = character('Clara Smith')
        self.Robert_Smith = character('Robert Smith')

    def story(self):
        self.jennifer_ann_smith_is_a_tired_looking_woman_in_her_mid_30s()
        self.she_has_shoulder_length_brown_hair_that_is_starting_to_show_some_gray_at_the_temples()
        self.jennifer_s_right_hand_clutches_the_phone_while_her_left_hand_clenches_a_cigarette_between_her_thumb_and_forefinger()
        self.her_eyes_are_narrowed_with_annoyance_as_she_listens_to_her_mother_ranting_on_the_other_end_of_the_line()
        self.where_have_you_been()
        self.demands_clara_smith_once_she_realizes_that_jennifer_has_finally_picked_up_the_phone()
        self.i_ve_been_trying_to_call_you_for_hours()
        self.i_was_at_work_says_jennifer_letting_out_a_sigh()
        self.you_know_i_don_not_get_off_until_eight()
        self.are_you_going_to_invite_me_over()
        self.asks_clara()
        self.jennifer_s_stomach_does_a_flip_as_she_lets_out_another_sigh_and_glances_down_at_her_boyfriend_robert_lying_in_bed_beside_her()
        self.the_last_thing_she_wanted_was_for_her_mother_to_barge_into_their_apartment_and_intrude_on_their_sex_life_again_but_there_wasn_not_much_she_could_do_about_it_now()
        self.if_she_turned_down_clara_s_invitation_she_knew_that_clara_would_just_continue_calling_back_all_night_until_she_agreed_to_meet_with_her_mother_for_lunch_tomorrow_or_something_like_that()
    def jennifer_ann_smith_is_a_tired_looking_woman_in_her_mid_30s(self):
        self.Jennifer_Ann_Smith.age.append('30s')
        self.Jennifer_Ann_Smith.gender.append('female')

    def she_has_shoulder_length_brown_hair_that_is_starting_to_show_some_gray_at_the_temples(self):
        self.Jennifer_Ann_Smith.appearance.append('brown hair')

    def jennifer_s_right_hand_clutches_the_phone_while_her_left_hand_clenches_a_cigarette_between_her_thumb_and_forefinger(self):
        pass

    def her_eyes_are_narrowed_with_annoyance_as_she_listens_to_her_mother_ranting_on_the_other_end_of_the_line(self):
        self.Jennifer_Ann_Smith.relations['mother'] = 'Clara_Smith'
        self.Clara_Smith.relations['daughter'] = 'Jennifer_Ann_Smith'

    def where_have_you_been(self):
        pass

    def demands_clara_smith_once_she_realizes_that_jennifer_has_finally_picked_up_the_phone(self):
        self.Clara_Smith.gender.append('female')

    def i_ve_been_trying_to_call_you_for_hours(self):
        pass

    def i_was_at_work_says_jennifer_letting_out_a_sigh(self):
        self.Jennifer_Ann_Smith.occupation.append('work')

    def you_know_i_don_not_get_off_until_eight(self):
        pass

    def are_you_going_to_invite_me_over(self):
        pass

    def asks_clara(self):
        pass

    def jennifer_s_stomach_does_a_flip_as_she_lets_out_another_sigh_and_glances_down_at_her_boyfriend_robert_lying_in_bed_beside_her(self):
        self.Jennifer_Ann_Smith.relations['boyfriend'] = 'Robert_Smith'
        self.Robert_Smith.relations['girlfriend'] = 'Jennifer_Ann_Smith'

    def the_last_thing_she_wanted_was_for_her_mother_to_barge_into_their_apartment_and_intrude_on_their_sex_life_again_but_there_wasn_not_much_she_could_do_about_it_now(self):
        pass

    def if_she_turned_down_clara_s_invitation_she_knew_that_clara_would_just_continue_calling_back_all_night_until_she_agreed_to_meet_with_her_mother_for_lunch_tomorrow_or_something_like_that(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

