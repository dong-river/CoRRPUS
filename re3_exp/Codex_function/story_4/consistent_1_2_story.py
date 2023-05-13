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
        self.Shannon_Kincaid = character('Shannon Kincaid')
        self.Jack_Kincaid = character('Jack Kincaid')
        self.Mark_Woodbury = character('Mark Woodbury')

    def story(self):
        self.mark_woodbury_a_middle_aged_man_with_graying_hair_and_a_mustache_smiled_at_shannon_as_she_walked_into_his_office()
        self.well_if_it_isn_t_my_little_investigative_reporter_he_said()
        self.shannon_smiled_back()
        self.hello_mark_she_said_cheerfully()
        self.you_have_to_admit_that_i_do_have_a_knack_for_getting_good_stories_mark_laughed()
        self.that_you_do_young_lady()
        self.that_you_do()
        self.and_there_s_no_one_better_at_getting_to_the_bottom_of_a_story_than_you_are()
        self.unfortunately_he_took_off_his_glasses_and_began_cleaning_them_with_his_handkerchief_as_he_spoke()
        self.unfortunately_i_m_going_to_have_to_turn_down_your_latest_assignment_request_and_it_is_an_unusual_request_at_that_shannon_put_her_hands_on_her_hips_and_frowned_angrily_at_him_in_reply()
        self.what()
        self.you_can_t_turn_me_down()
        self.you_know_how_long_i_worked_on_this_story_how_many_interviews_i_did_how_many_people_i_asked_questions_of()
        self.this_is_my_ticket_out_of_the_boring_little_old_city_pages_a_big_exclusive_front_page_story_for_real_this_time()
    def mark_woodbury_a_middle_aged_man_with_graying_hair_and_a_mustache_smiled_at_shannon_as_she_walked_into_his_office(self):
        self.Mark_Woodbury.appearance.append('middle aged')
        self.Mark_Woodbury.appearance.append('graying hair')
        self.Mark_Woodbury.appearance.append('mustache')
        self.Mark_Woodbury.relations['smiled at'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['smiled at'] = 'Mark_Woodbury'
        self.Shannon_Kincaid.relations['walked into'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['walked into'] = 'Shannon_Kincaid'

    def well_if_it_isn_t_my_little_investigative_reporter_he_said(self):
        self.Mark_Woodbury.relations['little investigative reporter'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['little investigative reporter'] = 'Mark_Woodbury'

    def shannon_smiled_back(self):
        self.Shannon_Kincaid.relations['smiled back'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['smiled back'] = 'Shannon_Kincaid'

    def hello_mark_she_said_cheerfully(self):
        self.Shannon_Kincaid.relations['said cheerfully'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['said cheerfully'] = 'Shannon_Kincaid'

    def you_have_to_admit_that_i_do_have_a_knack_for_getting_good_stories_mark_laughed(self):
        self.Mark_Woodbury.relations['admit that'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['admit that'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['knack for getting good stories'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['knack for getting good stories'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['laughed'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['laughed'] = 'Mark_Woodbury'

    def that_you_do_young_lady(self):
        self.Mark_Woodbury.relations['young lady'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['young lady'] = 'Mark_Woodbury'

    def that_you_do(self):
        pass

    def and_there_s_no_one_better_at_getting_to_the_bottom_of_a_story_than_you_are(self):
        pass

    def unfortunately_he_took_off_his_glasses_and_began_cleaning_them_with_his_handkerchief_as_he_spoke(self):
        self.Mark_Woodbury.appearance.append('glasses')
        self.Mark_Woodbury.appearance.append('handkerchief')

    def unfortunately_i_m_going_to_have_to_turn_down_your_latest_assignment_request_and_it_is_an_unusual_request_at_that_shannon_put_her_hands_on_her_hips_and_frowned_angrily_at_him_in_reply(self):
        self.Mark_Woodbury.relations['turn down'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['turn down'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['unusual request'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['unusual request'] = 'Mark_Woodbury'
        self.Shannon_Kincaid.relations['put her hands on her hips'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['put her hands on her hips'] = 'Shannon_Kincaid'
        self.Shannon_Kincaid.relations['frowned angrily'] = 'Mark_Woodbury'
        self.Mark_Woodbury.relations['frowned angrily'] = 'Shannon_Kincaid'

    def what(self):
        pass

    def you_can_t_turn_me_down(self):
        pass

    def you_know_how_long_i_worked_on_this_story_how_many_interviews_i_did_how_many_people_i_asked_questions_of(self):
        pass

    def this_is_my_ticket_out_of_the_boring_little_old_city_pages_a_big_exclusive_front_page_story_for_real_this_time(self):
        pass
## Create a world model state to track each character's appearance, personality, and relations with other characters.

