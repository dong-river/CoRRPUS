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
        self.at_thirty_six_years_old_payton_s_biological_clock_is_ticking_but_she_s_never_found_the_right_person_to_have_children_with()
        self.she_s_always_been_a_career_woman_and_she_s_not_sure_she_s_ready_to_give_up_her_freedom()
        self.when_her_best_friend_from_college_dies_unexpectedly_leaving_behind_a_four_year_old_daughter_payton_is_faced_with_the_decision_of_whether_or_not_to_take_on_the_responsibility_of_raising_her()
        self.the_story_is_set_in_new_york_city()
        self.payton_dupree_is_a_36_year_old_successful_businesswoman()
        self.she_has_never_been_married_and_does_not_have_any_children()
        self.she_is_fiercely_independent_and_has_always_put_her_career_first()
        self.amanda_dupree_is_payton_s_deceased_best_friend_from_college()
        self.she_was_a_stay_at_home_mom_and_died_suddenly_leaving_behind_her_4_year_old_daughter_olivia()
        self.olivia_dupree_is_amanda_s_4_year_old_daughter_and_payton_s_goddaughter()
        self.she_is_a_precocious_and_energetic_child_who_has_been_through_a_lot_in_her_young_life()
    def at_thirty_six_years_old_payton_s_biological_clock_is_ticking_but_she_s_never_found_the_right_person_to_have_children_with(self):
        pass
    def she_s_always_been_a_career_woman_and_she_s_not_sure_she_s_ready_to_give_up_her_freedom(self):
        pass
    def when_her_best_friend_from_college_dies_unexpectedly_leaving_behind_a_four_year_old_daughter_payton_is_faced_with_the_decision_of_whether_or_not_to_take_on_the_responsibility_of_raising_her(self):
        pass
    def the_story_is_set_in_new_york_city(self):
        pass
    def payton_dupree_is_a_36_year_old_successful_businesswoman(self):
        self.Payton_Dupree.age.append('36')
        self.Payton_Dupree.occupation.append('successful businesswoman')
    def she_has_never_been_married_and_does_not_have_any_children(self):
        self.Payton_Dupree.relations['has_never_been_married'] = True
        self.Payton_Dupree.relations['does_not_have_any_children'] = True
    def she_is_fiercely_independent_and_has_always_put_her_career_first(self):
        self.Payton_Dupree.relations['fiercely_independent'] = True
        self.Payton_Dupree.relations['has_always_put_her_career_first'] = True
    def amanda_dupree_is_payton_s_deceased_best_friend_from_college(self):
        self.Payton_Dupree.relations['best_friend_from_college'] = 'Amanda_Dupree'
        self.Amanda_Dupree.relations['deceased'] = True
    def she_was_a_stay_at_home_mom_and_died_suddenly_leaving_behind_her_4_year_old_daughter_olivia(self):
        self.Amanda_Dupree.relations['stay_at_home_mom'] = True
        self.Amanda_Dupree.relations['suddenly_left_behind_her_4_year_old_daughter_olivia'] = True
    def olivia_dupree_is_amanda_s_4_year_old_daughter_and_payton_s_goddaughter(self):
        self.Amanda_Dupree.relations['daughter'] = 'Olivia_Dupree'
        self.Payton_Dupree.relations['goddaughter'] = 'Olivia_Dupree'
    def she_is_a_precocious_and_energetic_child_who_has_been_through_a_lot_in_her_young_life(self):
        self.Olivia_Dupree.relations['precocious'] = True
        self.Olivia_Dupree.relations['energetic'] = True
        self.Olivia_Dupree.relations['has_been_through_a_lot_in_her_young_life'] = True

## Create a world model state to track each character's appearance, personality, and relations with other characters.