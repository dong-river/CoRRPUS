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
        self.shannon_mulaney_walked_into_her_dorm_room_and_flopped_down_on_her_bed()
        self.she_had_just_gotten_off_the_phone_with_her_mom_and_they_d_argued_again()
        self.the_bad_grades_she_d_been_getting_all_semester_were_affecting_her_softball_scholarship_so_shannon_knew_that_her_mom_was_upset()
        self.they_hadn_not_spoken_in_two_weeks_though_and_shannon_still_felt_hurt_by_the_fight_they_d_had_before_she_left_michigan()
        self.her_whole_life_she_had_felt_like_the_odd_one_out_in_the_family_with_both_of_her_sisters_being_more_popular_than_she_was_and_now_it_seemed_that_her_mom_was_starting_to_see_it_too()
        self.as_she_lay_there_waiting_for_olivia_to_come_back_from_class_shannon_closed_her_eyes_and_fell_asleep()
        self.so_when_did_your_mom_get_cancer()
        self.jess_asked_as_she_set_down_a_few_books_on_top_of_some_envelopes_that_were_stacked_on_the_small_desk_across_from_shannon_s_bed()
        self.she_didn_not_shannon_answered_without_looking_up_from_the_book_open_in_front_of_her()
        self.what_do_you_mean()
        self.she_s_been_sick_for_a_year()
        self.jess_sounded_confused()
    def shannon_mulaney_walked_into_her_dorm_room_and_flopped_down_on_her_bed(self):
        self.Shannon_Mulaney.appearance.append('dorm room')
    def she_had_just_gotten_off_the_phone_with_her_mom_and_they_d_argued_again(self):
        self.Shannon_Mulaney.relations['mom'] = 'Shannon_Mulaney'
    def the_bad_grades_she_d_been_getting_all_semester_were_affecting_her_softball_scholarship_so_shannon_knew_that_her_mom_was_upset(self):
        self.Shannon_Mulaney.occupation.append('softball scholarship')
    def they_hadn_not_spoken_in_two_weeks_though_and_shannon_still_felt_hurt_by_the_fight_they_d_had_before_she_left_michigan(self):
        self.Shannon_Mulaney.relations['michigan'] = 'Shannon_Mulaney'
    def her_whole_life_she_had_felt_like_the_odd_one_out_in_the_family_with_both_of_her_sisters_being_more_popular_than_she_was_and_now_it_seemed_that_her_mom_was_starting_to_see_it_too(self):
        self.Shannon_Mulaney.relations['sisters'] = 'Shannon_Mulaney'
    def as_she_lay_there_waiting_for_olivia_to_come_back_from_class_shannon_closed_her_eyes_and_fell_asleep(self):
        self.Shannon_Mulaney.relations['olivia'] = 'Olivia_Kendall'
    def so_when_did_your_mom_get_cancer(self):
        self.Jess_Abernathy.relations['Shannon_Mulaney'] = 'Shannon_Mulaney'
    def jess_asked_as_she_set_down_a_few_books_on_top_of_some_envelopes_that_were_stacked_on_the_small_desk_across_from_shannon_s_bed(self):
        self.Jess_Abernathy.appearance.append('Shannon_Mulaney')
    def she_didn_not_shannon_answered_without_looking_up_from_the_book_open_in_front_of_her(self):
        self.Shannon_Mulaney.appearance.append('book')
    def what_do_you_mean(self):
        pass
    def she_s_been_sick_for_a_year(self):
        self.Shannon_Mulaney.appearance.append('sick')
    def jess_sounded_confused(self):
        self.Jess_Abernathy.appearance.append('confused')

## Create a world model state to track each character's appearance, personality, and relations with other characters.

