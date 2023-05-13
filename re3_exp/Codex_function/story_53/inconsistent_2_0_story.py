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
        self.Jane_Doe = character('Jane Doe')
        self.Mister_Snuggles = character('Mister Snuggles')
        self.Jessica_Brown = character('Jessica Brown')

    def story(self):
        self.jessica_brown_was_jane_s_best_friend_since_childhood()
        self.she_was_visiting_her_in_her_apartment_that_evening()
        self.they_were_both_sitting_on_the_couch_watching_tv()
        self.jane_had_a_frown_on_her_face_she_was_confused_and_upset_about_something()
        self.jessica_she_said_what_s_wrong()
        self.nothing_is_wrong_jessica_replied_though_she_knew_it_wasn_not_true()
        self.why_do_you_ask()
        self.because_you_don_not_look_like_yourself()
        self.oh_sorry()
        self.i_ve_been_thinking_about_something()
        self.what_have_you_been_thinking_about()
        self.jane_asked_slightly_curious_as_to_what_her_friend_had_been_up_to_all_day_while_she_was_out_of_the_apartment()
        self.in_all_honesty_jane_had_hardly_any_close_friends_other_than_jessica_she_didn_not_seem_to_make_many_friends_during_the_years_of_high_school_and_university_and_was_always_too_shy_to_start_a_conversation_with_anyone_else_whenever_the_opportunity_presented_itself_for_fear_of_being_rejected()
        self.her_only_other_significant_friendship_in_life_came_from_childhood_when_she_spent_almost_every_day_with_jessica_who_lived_next_door_with_her_family()
    def jessica_brown_was_jane_s_best_friend_since_childhood(self):
        self.Jane_Doe.relations['best friend'] = 'Jessica_Brown'
        self.Jessica_Brown.relations['best friend'] = 'Jane_Doe'
        self.Jane_Doe.age.append('childhood')
        self.Jessica_Brown.age.append('childhood')
        
    def she_was_visiting_her_in_her_apartment_that_evening(self):
        self.Jane_Doe.relations['apartment'] = 'Jessica_Brown'
        self.Jessica_Brown.relations['apartment'] = 'Jane_Doe'
        
    def they_were_both_sitting_on_the_couch_watching_tv(self):
        self.Jane_Doe.relations['couch'] = 'Jessica_Brown'
        self.Jessica_Brown.relations['couch'] = 'Jane_Doe'
        
    def jane_had_a_frown_on_her_face_she_was_confused_and_upset_about_something(self):
        self.Jane_Doe.appearance.append('frown')
        
    def jessica_she_said_what_s_wrong(self):
        pass
        
    def nothing_is_wrong_jessica_replied_though_she_knew_it_wasn_not_true(self):
        pass
        
    def why_do_you_ask(self):
        pass
        
    def because_you_don_not_look_like_yourself(self):
        pass
        
    def oh_sorry(self):
        pass
        
    def i_ve_been_thinking_about_something(self):
        pass
        
    def what_have_you_been_thinking_about(self):
        pass
        
    def jane_asked_slightly_curious_as_to_what_her_friend_had_been_up_to_all_day_while_she_was_out_of_the_apartment(self):
        pass
        
    def in_all_honesty_jane_had_hardly_any_close_friends_other_than_jessica_she_didn_not_seem_to_make_many_friends_during_the_years_of_high_school_and_university_and_was_always_too_shy_to_start_a_conversation_with_anyone_else_whenever_the_opportunity_presented_itself_for_fear_of_being_rejected(self):
        pass
        
    def her_only_other_significant_friendship_in_life_came_from_childhood_when_she_spent_almost_every_day_with_jessica_who_lived_next_door_with_her_family(self):
        pass

