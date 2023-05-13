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
        self.Sarah_Mason = character('Sarah Mason')
        self.Rachel_Stephenson = character('Rachel Stephenson')
        self.John_Mason = character('John Mason')

    def story(self):
        self.rachel_stephenson_stood_at_the_sink_drinking_a_glass_of_wine_and_reflecting_on_her_life()
        self.she_was_not_unhappy()
        self.but_she_wasn_not_exactly_happy_either()
        self.she_lived_in_a_beautiful_house_in_a_nice_neighborhood_with_her_husband_richard_stevenson()
        self.she_had_two_wonderful_children_jonathan_and_cynthia()
        self.in_many_ways_rachel_was_content_with_her_life_as_it_was()
        self.the_trouble_was_that_richard_didn_not_bring_her_much_excitement_in_bed_anymore()
        self.the_truth_be_told_he_hadn_not_for_a_long_time_now_even_when_they_were_first_married_ten_years_ago_which_was_how_they_met_in_the_first_place()
        self.richard_had_been_paying_more_attention_to_his_work_lately_than_he_did_to_her()
        self.more_and_more_often_she_would_find_him_sitting_at_his_desk_late_into_the_night_working_on_something_rather_than_coming_to_bed_where_he_belonged_by_their_bedside_clock_it_would_sometimes_be_one_or_two_in_the_morning_before_he_d_come_to_bed_where_his_wife_would_be_patiently_waiting_for_him_even_though_she_knew_what_kind_of_a_night_he_d_have_for_sexual_gratification()
    def rachel_stephenson_stood_at_the_sink_drinking_a_glass_of_wine_and_reflecting_on_her_life(self):
        self.Rachel_Stephenson.appearance.append("drinking a glass of wine")
        
    def she_was_not_unhappy(self):
        pass
        
    def but_she_wasn_not_exactly_happy_either(self):
        pass
        
    def she_lived_in_a_beautiful_house_in_a_nice_neighborhood_with_her_husband_richard_stevenson(self):
        self.Rachel_Stephenson.relations['husband'] = 'Richard_Stephenson'
        
    def she_had_two_wonderful_children_jonathan_and_cynthia(self):
        self.Rachel_Stephenson.relations['children'] = 'Jonathan_Stephenson'
        self.Rachel_Stephenson.relations['children'] = 'Cynthia_Stephenson'
        
    def in_many_ways_rachel_was_content_with_her_life_as_it_was(self):
        pass
        
    def the_trouble_was_that_richard_didn_not_bring_her_much_excitement_in_bed_anymore(self):
        pass
        
    def the_truth_be_told_he_hadn_not_for_a_long_time_now_even_when_they_were_first_married_ten_years_ago_which_was_how_they_met_in_the_first_place(self):
        pass
        
    def richard_had_been_paying_more_attention_to_his_work_lately_than_he_did_to_her(self):
        pass
        
    def more_and_more_often_she_would_find_him_sitting_at_his_desk_late_into_the_night_working_on_something_rather_than_coming_to_bed_where_he_belonged_by_their_bedside_clock_it_would_sometimes_be_one_or_two_in_the_morning_before_he_d_come_to_bed_where_his_wife_would_be_patiently_waiting_for_him_even_though_she_knew_what_kind_of_a_night_he_d_have_for_sexual_gratification(self):
        pass
        
## Create a world model state to track each character's appearance, personality, and relations with other characters.

