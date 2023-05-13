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
        self.olivia_saunders_pulled_her_car_into_the_school_parking_lot_and_turned_off_the_engine()
        self.don_not_forget_that_the_assignments_are_due_by_tomorrow_emma_she_said_looking_at_her_daughter()
        self.i_know_mom_i_won_not_forget_emma_replied()
        self.i_told_you_i_ve_been_studying_like_crazy()
        self.alright_olivia_said_opening_the_door_and_getting_out_of_the_car()
        self.good_luck_sweetie()
        self.emma_sighed()
        self.her_mother_was_being_overly_protective_of_her_but_she_knew_why()
        self.she_had_struggled_at_school_since_third_grade_when_all_of_a_sudden_her_grades_plummeted_and_teachers_began_to_complain_about_her_behavior_in_class()
        self.all_this_time_she_had_thought_that_something_was_wrong_with_her_brain_but_doctors_never_found_anything()
        self.they_simply_diagnosed_it_as_add()
        self.in_high_school_it_got_worse_none_of_her_teachers_were_interested_in_helping_her_anymore_and_she_was_struggling_more_than_ever_to_pass_even_one_class_in_english_class_that_she_could_barely_read_now_because_of_dyslexia_and_adhd()
        self.she_s_stopped_trying_to_be_a_good_girl_in_school_because_they_weren_not_helping_anyway_so_why_not_be_what_they_thought_she_already_was()
        self.it_gave_them_more_reason_to_hate_on_you_right()
    def olivia_saunders_pulled_her_car_into_the_school_parking_lot_and_turned_off_the_engine(self):
        self.Olivia_Saunders.occupation.append('mother')
        self.Olivia_Saunders.gender.append('female')
        self.Emma_Saunders.relations['mother'] = 'Olivia_Saunders'
        self.Olivia_Saunders.relations['daughter'] = 'Emma_Saunders'
    def don_not_forget_that_the_assignments_are_due_by_tomorrow_emma_she_said_looking_at_her_daughter(self):
        pass
    def i_know_mom_i_won_not_forget_emma_replied(self):
        pass
    def i_told_you_i_ve_been_studying_like_crazy(self):
        pass
    def alright_olivia_said_opening_the_door_and_getting_out_of_the_car(self):
        pass
    def good_luck_sweetie(self):
        pass
    def emma_sighed(self):
        pass
    def her_mother_was_being_overly_protective_of_her_but_she_knew_why(self):
        pass
    def she_had_struggled_at_school_since_third_grade_when_all_of_a_sudden_her_grades_plummeted_and_teachers_began_to_complain_about_her_behavior_in_class(self):
        pass
    def all_this_time_she_had_thought_that_something_was_wrong_with_her_brain_but_doctors_never_found_anything(self):
        pass
    def they_simply_diagnosed_it_as_add(self):
        pass
    def in_high_school_it_got_worse_none_of_her_teachers_were_interested_in_helping_her_anymore_and_she_was_struggling_more_than_ever_to_pass_even_one_class_in_english_class_that_she_could_barely_read_now_because_of_dyslexia_and_adhd(self):
        pass
    def she_s_stopped_trying_to_be_a_good_girl_in_school_because_they_weren_not_helping_anyway_so_why_not_be_what_they_thought_she_already_was(self):
        pass
    def it_gave_them_more_reason_to_hate_on_you_right(self):
        pass

