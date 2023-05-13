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
        self.Shannon_Burke = character('Shannon Burke')
        self.Charles_Burke = character('Charles Burke')
        self.Maxine_Carter = character('Maxine Carter')

    def story(self):
        self.maxine_carter_looked_over_at_her_latest_hire_shannon_burke_with_a_puzzled_expression()
        self.shannon_had_a_wild_look_in_her_eyes_as_she_paced_back_and_forth_across_the_floor_of_maxine_s_office()
        self.she_kept_checking_her_watch_while_jumping_up_every_so_often_to_peek_through_the_blinds_at_the_news_station_beyond()
        self.maxine_found_it_difficult_to_understand_why_this_woman_was_so_edgy_when_they_were_due_to_start_filming_in_a_few_minutes()
        self.it_wasn_not_like_she_was_an_inexperienced_intern()
        self.for_that_matter_it_wasn_not_like_she_hadn_not_been_out_on_assignments_before()
        self.okay_shan_said_maxine_breaking_into_the_young_woman_s_monologue_of_nervous_babble()
        self.what_s_the_big_deal()
        self.the_camera_is_in_position_and_everything_is_ready_to_go()
        self.shannon_whipped_around_with_a_surprised_look_on_her_face_and_smiled_broadly_at_maxine_as_if_suddenly_realizing_where_she_was()
        self.oh()
        self.right()
        self.she_laughed_nervously()
        self.sorry_max()
        self.maxine_smiled_but_did_not_respond_to_shannon_s_apology_or_explanation_for_her_strange_behavior()
        self.the_woman_needed_no_prompting_to_continue_where_she_had_left_off_moments_before()
        self.i_have_been_thinking_about_what_you_said_about_your_reporting_strategy_for_this_case()
    def maxine_carter_looked_over_at_her_latest_hire_shannon_burke_with_a_puzzled_expression(self):
        self.Shannon_Burke.relations['latest_hire'] = 'Maxine_Carter'
        self.Maxine_Carter.relations['latest_hire'] = 'Shannon_Burke'
        
    def shannon_had_a_wild_look_in_her_eyes_as_she_paced_back_and_forth_across_the_floor_of_maxine_s_office(self):
        self.Shannon_Burke.appearance.append('wild look')
        
    def she_kept_checking_her_watch_while_jumping_up_every_so_often_to_peek_through_the_blinds_at_the_news_station_beyond(self):
        pass
    
    def maxine_found_it_difficult_to_understand_why_this_woman_was_so_edgy_when_they_were_due_to_start_filming_in_a_few_minutes(self):
        pass
    
    def it_wasn_not_like_she_was_an_inexperienced_intern(self):
        pass
    
    def for_that_matter_it_wasn_not_like_she_hadn_not_been_out_on_assignments_before(self):
        pass
    
    def okay_shan_said_maxine_breaking_into_the_young_woman_s_monologue_of_nervous_babble(self):
        self.Maxine_Carter.relations['young_woman'] = 'Shannon_Burke'
        self.Shannon_Burke.relations['young_woman'] = 'Maxine_Carter'
        
    def what_s_the_big_deal(self):
        pass
    
    def the_camera_is_in_position_and_everything_is_ready_to_go(self):
        pass
    
    def shannon_whipped_around_with_a_surprised_look_on_her_face_and_smiled_broadly_at_maxine_as_if_suddenly_realizing_where_she_was(self):
        self.Shannon_Burke.appearance.append('surprised look')
        self.Shannon_Burke.appearance.append('smiled broadly')
        
    def oh(self):
        pass
    
    def right(self):
        pass
    
    def she_laughed_nervously(self):
        self.Shannon_Burke.appearance.append('laughed nervously')
        
    def sorry_max(self):
        pass
    
    def maxine_smiled_but_did_not_respond_to_shannon_s_apology_or_explanation_for_her_strange_behavior(self):
        self.Maxine_Carter.appearance.append('smiled')
        
    def the_woman_needed_no_prompting_to_continue_where_she_had_left_off_moments_before(self):
        pass
    
    def i_have_been_thinking_about_what_you_said_about_your_reporting_strategy_for_this_case(self):
        pass

