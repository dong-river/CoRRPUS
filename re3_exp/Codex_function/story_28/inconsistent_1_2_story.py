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
        self.Payton_Dupree = character('Payton Dupree')
        self.Amanda_Dupree = character('Amanda Dupree')
        self.Olivia_Dupree = character('Olivia Dupree')

    def story(self):
        self.olivia_dupree_s_cheeks_were_stained_with_tears_as_she_approached_the_boarding_area_for_the_plane_to_new_york()
        self.her_arms_were_wrapped_around_her_guardian_s_waist_and_she_was_clutching_her_new_backpack_to_her_chest()
        self.she_was_only_four_years_old_but_she_had_never_been_away_from_home_before_and_didn_not_know_why_she_had_to_go_on_this_trip()
        self.i_don_not_want_to_go_olivia_whimpered_looking_up_at_her_mother_s_face()
        self.amanda_knelt_down_on_one_knee_and_embraced_her_daughter_in_a_tight_hug()
        self.olivia_you_have_to_go()
        self.your_aunt_payton_is_very_busy_and_can_not_take_care_of_you_right_now_amanda_said_softly()
        self.i_know_you_re_going_to_like_new_york()
        self.olivia_released_a_loud_sob_and_buried_her_face_in_amanda_s_shoulder()
        self.it_ll_be_okay_amanda_promised_her_daughter_again()
        self.you_ll_stay_with_your_aunt_for_a_few_days_get_some_rest_eat_good_food_the_works()
        self.i_bet_it_ll_be_really_fun()
        self.olivia_looked_at_amanda_and_wiped_a_tear_away_from_the_corner_of_her_eye_with_the_back_of_her_hand()
        self.are_you_coming_back()
    def olivia_dupree_s_cheeks_were_stained_with_tears_as_she_approached_the_boarding_area_for_the_plane_to_new_york(self):
        pass
        
    def her_arms_were_wrapped_around_her_guardian_s_waist_and_she_was_clutching_her_new_backpack_to_her_chest(self):
        self.Olivia_Dupree.relations['guardian'] = 'Amanda_Dupree'
        self.Olivia_Dupree.appearance.append('clutched backpack')
        
    def she_was_only_four_years_old_but_she_had_never_been_away_from_home_before_and_didn_not_know_why_she_had_to_go_on_this_trip(self):
        self.Olivia_Dupree.age.append('4')
        
    def i_don_not_want_to_go_olivia_whimpered_looking_up_at_her_mother_s_face(self):
        self.Olivia_Dupree.relations['mother'] = 'Amanda_Dupree'
        
    def amanda_knelt_down_on_one_knee_and_embraced_her_daughter_in_a_tight_hug(self):
        self.Amanda_Dupree.relations['daughter'] = 'Olivia_Dupree'
        
    def olivia_you_have_to_go(self):
        pass
        
    def your_aunt_payton_is_very_busy_and_can_not_take_care_of_you_right_now_amanda_said_softly(self):
        self.Olivia_Dupree.relations['aunt'] = 'Payton_Dupree'
        self.Payton_Dupree.relations['niece'] = 'Olivia_Dupree'
        
    def i_know_you_re_going_to_like_new_york(self):
        pass
        
    def olivia_released_a_loud_sob_and_buried_her_face_in_amanda_s_shoulder(self):
        pass
        
    def it_ll_be_okay_amanda_promised_her_daughter_again(self):
        pass
        
    def you_ll_stay_with_your_aunt_for_a_few_days_get_some_rest_eat_good_food_the_works(self):
        pass
        
    def i_bet_it_ll_be_really_fun(self):
        pass
        
    def olivia_looked_at_amanda_and_wiped_a_tear_away_from_the_corner_of_her_eye_with_the_back_of_her_hand(self):
        pass
        
    def are_you_coming_back(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

