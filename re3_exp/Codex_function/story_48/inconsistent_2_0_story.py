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
        self.Shannon_Fitzgerald = character('Shannon Fitzgerald')
        self.Olivia_Kane = character('Olivia Kane')
        self.Richard_Kane = character('Richard Kane')

    def story(self):
        self.richard_kane_is_a_very_successful_businessman()
        self.he_owns_many_restaurants_and_businesses_all_over_the_city_bringing_in_millions_of_dollars_in_revenue_every_year()
        self.but_business_alone_cannot_satisfy_richard()
        self.he_has_a_strong_thirst_for_the_thrill_of_the_game_and_enjoys_gambling_always_striving_to_push_his_luck_with_each_new_venture()
        self.richard_is_married_to_olivia_kane_a_beautiful_woman_who_never_failed_to_meet_his_high_expectations()
        self.olivia_was_always_stylish_and_popular_but_she_married_into_money_which_made_her_even_more_popular_among_the_upper_class_of_society()
        self.despite_their_wealth_and_popularity_richard_and_olivia_wanted_children_which_would_ensure_that_they_passed_on_their_status_into_the_next_generation()
        self.they_spent_several_years_trying_to_conceive_but_were_unable_to_do_so_until_one_day_olivia_became_pregnant()
        self.a_son_was_born_first_but_died_shortly_after_birth()
        self.it_was_only_then_that_a_daughter_came_along_two_years_later_but_this_child_also_did_not_survive_past_infancy_despite_their_desperate_efforts_to_save_her_life()
        self.despite_these_crushing_losses_and_failing_health_for_both_of_them_olivia_loved_her_husband_dearly_despite_his_weaknesses_for_gambling_and_foolish_risks_in_business_dealings()
    def richard_kane_is_a_very_successful_businessman(self):
        self.Richard_Kane.occupation.append('businessman')
    def he_owns_many_restaurants_and_businesses_all_over_the_city_bringing_in_millions_of_dollars_in_revenue_every_year(self):
        pass
    def but_business_alone_cannot_satisfy_richard(self):
        pass
    def he_has_a_strong_thirst_for_the_thrill_of_the_game_and_enjoys_gambling_always_striving_to_push_his_luck_with_each_new_venture(self):
        pass
    def richard_is_married_to_olivia_kane_a_beautiful_woman_who_never_failed_to_meet_his_high_expectations(self):
        self.Richard_Kane.relations['wife'] = 'Olivia_Kane'
        self.Olivia_Kane.relations['husband'] = 'Richard_Kane'
    def olivia_was_always_stylish_and_popular_but_she_married_into_money_which_made_her_even_more_popular_among_the_upper_class_of_society(self):
        pass
    def despite_their_wealth_and_popularity_richard_and_olivia_wanted_children_which_would_ensure_that_they_passed_on_their_status_into_the_next_generation(self):
        pass
    def they_spent_several_years_trying_to_conceive_but_were_unable_to_do_so_until_one_day_olivia_became_pregnant(self):
        pass
    def a_son_was_born_first_but_died_shortly_after_birth(self):
        pass
    def it_was_only_then_that_a_daughter_came_along_two_years_later_but_this_child_also_did_not_survive_past_infancy_despite_their_desperate_efforts_to_save_her_life(self):
        pass
    def despite_these_crushing_losses_and_failing_health_for_both_of_them_olivia_loved_her_husband_dearly_despite_his_weaknesses_for_gambling_and_foolish_risks_in_business_dealings(self):
        pass

# Create a world model state to track each character's appearance, personality, and relations with other characters.

