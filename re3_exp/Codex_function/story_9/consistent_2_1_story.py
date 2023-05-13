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
        self.Julie_Christensen = character('Julie Christensen')
        self.Tommy_Foster = character('Tommy Foster')
        self.Beth_Christensen = character('Beth Christensen')

    def story(self):
        self.beth_christensen_sat_down_in_a_chair_across_from_julie_and_took_her_hand()
        self.you_have_to_listen_to_me_she_said()
        self.you_re_having_the_baby()
        self.beth_no_no_no()
        self.you_don_not_understand_julie_protested()
        self.it_s_impossible()
        self.why()
        self.beth_replied()
        self.is_it_because_you_re_still_a_virgin()
        self.julie_looked_at_her_friend_with_tears_in_her_eyes_and_nodded()
        self.how_can_i_be_pregnant()
        self.how_can_that_happen()
        self.because_you_had_sex_beth_replied()
        self.you_know_how_it_happens_right()
        self.the_same_way_every_time()
        self.she_paused_for_a_moment_and_then_asked_softly_does_he_know()
        self.has_he_spoken_to_you_yet()
        self.she_then_held_up_a_hand_to_stop_julie_from_responding_before_continuing()
        self.listen_my_advice_is_that_you_talk_to_him_about_this()
        self.tell_him_what_s_going_on_and_see_what_he_says_about_it()
    def beth_christensen_sat_down_in_a_chair_across_from_julie_and_took_her_hand(self):
        self.Beth_Christensen.relations['friend'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['friend'] = 'Beth_Christensen'
        self.Beth_Christensen.gender.append('female')
        self.Julie_Christensen.gender.append('female')
    def you_have_to_listen_to_me_she_said(self):
        pass
    def you_re_having_the_baby(self):
        pass
    def beth_no_no_no(self):
        pass
    def you_don_not_understand_julie_protested(self):
        pass
    def it_s_impossible(self):
        pass
    def why(self):
        pass
    def beth_replied(self):
        pass
    def is_it_because_you_re_still_a_virgin(self):
        pass
    def julie_looked_at_her_friend_with_tears_in_her_eyes_and_nodded(self):
        pass
    def how_can_i_be_pregnant(self):
        pass
    def how_can_that_happen(self):
        pass
    def because_you_had_sex_beth_replied(self):
        pass
    def you_know_how_it_happens_right(self):
        pass
    def the_same_way_every_time(self):
        pass
    def she_paused_for_a_moment_and_then_asked_softly_does_he_know(self):
        pass
    def has_he_spoken_to_you_yet(self):
        pass
    def she_then_held_up_a_hand_to_stop_julie_from_responding_before_continuing(self):
        pass
    def listen_my_advice_is_that_you_talk_to_him_about_this(self):
        pass
    def tell_him_what_s_going_on_and_see_what_he_says_about_it(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

