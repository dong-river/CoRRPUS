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
        self.beth_christensen_walked_into_the_living_room_where_her_daughter_julie_was_sitting_with_her_boyfriend_tommy()
        self.she_could_tell_that_the_two_were_happy_and_carefree_and_she_instantly_knew_that_something_was_up()
        self.julie_beth_said_sternly()
        self.what_s_going_on()
        self.what_do_you_mean()
        self.julie_asked_nervously()
        self.you_look_too_happy_for_something_not_to_be_going_on_beth_replied_glaring_at_tommy()
        self.is_this_about_what_i_think_it_is()
        self.julie_turned_to_tommy_for_help_but_he_remained_silent_and_looked_away_from_her()
        self.i_m_pregnant_she_said_in_a_low_voice_after_several_moments_of_silence()
        self.she_started_to_tear_up_as_she_finished_speaking()
        self.i_m_sorry()
        self.beth_was_shocked_by_what_she_had_just_heard()
        self.she_went_to_her_daughter_and_pulled_her_into_a_hug_while_scolding_tommy_at_the_same_time()
        self.tommy_foster()
        self.what_did_you_do()
        self.when_did_this_happen()
        self.why_didn_not_you_stop_this_from_happening()
        self.you_re_the_one_who_is_supposed_to_be_responsible()
        self.now_i_have_to_deal_with_you_and_your_father_s_mistakes()
    def beth_christensen_walked_into_the_living_room_where_her_daughter_julie_was_sitting_with_her_boyfriend_tommy(self):
        self.Beth_Christensen.relations['daughter'] = 'Julie_Christensen'
        self.Julie_Christensen.relations['mother'] = 'Beth_Christensen'
        self.Julie_Christensen.relations['boyfriend'] = 'Tommy_Foster'
        self.Tommy_Foster.relations['girlfriend'] = 'Julie_Christensen'

    def she_could_tell_that_the_two_were_happy_and_carefree_and_she_instantly_knew_that_something_was_up(self):
        pass

    def julie_beth_said_sternly(self):
        pass

    def what_s_going_on(self):
        pass

    def what_do_you_mean(self):
        pass

    def julie_asked_nervously(self):
        pass

    def you_look_too_happy_for_something_not_to_be_going_on_beth_replied_glaring_at_tommy(self):
        pass

    def is_this_about_what_i_think_it_is(self):
        pass

    def julie_turned_to_tommy_for_help_but_he_remained_silent_and_looked_away_from_her(self):
        pass

    def i_m_pregnant_she_said_in_a_low_voice_after_several_moments_of_silence(self):
        pass

    def she_started_to_tear_up_as_she_finished_speaking(self):
        pass

    def i_m_sorry(self):
        pass

    def beth_was_shocked_by_what_she_had_just_heard(self):
        pass

    def she_went_to_her_daughter_and_pulled_her_into_a_hug_while_scolding_tommy_at_the_same_time(self):
        pass

    def tommy_foster(self):
        pass

    def what_did_you_do(self):
        pass

    def when_did_this_happen(self):
        pass

    def why_didn_not_you_stop_this_from_happening(self):
        pass

    def you_re_the_one_who_is_supposed_to_be_responsible(self):
        pass

    def now_i_have_to_deal_with_you_and_your_father_s_mistakes(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

