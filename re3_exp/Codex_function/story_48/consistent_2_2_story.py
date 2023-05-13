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
        self.richard_kane_glanced_at_his_watch_frowning()
        self.his_daughter_s_bedtime_was_rapidly_approaching_and_he_had_yet_to_settle_the_kid_down()
        self.when_she_wasn_not_having_trouble_falling_asleep_she_was_up_before_dawn_and_running_through_the_house()
        self.she_and_her_brother_had_little_interest_in_television()
        self.he_suspected_that_their_mother_was_mostly_responsible_for_that()
        self.olivia_rarely_watched_any_shows_with_them_in_front_of_the_screen_and_their_father_didn_not_bother_trying_to_convince_her_otherwise()
        self.he_rose_from_his_seat_at_the_table_with_a_sigh_and_glanced_around_the_room()
        self.he_spotted_his_wife_by_one_of_the_large_picture_windows_staring_out_at_the_backyard_with_a_pensive_expression_on_her_face()
        self.she_hadn_not_moved_since_he_had_last_spoken_to_her_an_hour_ago_at_least()
        self.he_moved_towards_her_and_touched_her_shoulder_then_turned_towards_their_youngest_child()
        self.bring_jack_into_your_room_he_said_quietly_before_returning_his_attention_to_olivia()
        self.she_turned_to_him_slowly_nodding_without_a_word_before_heading_towards_their_son_s_bedroom_with_jack_trotting_behind_her_cheerfully()
    def richard_kane_glanced_at_his_watch_frowning(self):
        pass
    def his_daughter_s_bedtime_was_rapidly_approaching_and_he_had_yet_to_settle_the_kid_down(self):
        self.Richard_Kane.relations['daughter'] = 'Shannon_Fitzgerald'
        self.Shannon_Fitzgerald.relations['father'] = 'Richard_Kane'
    def when_she_wasn_not_having_trouble_falling_asleep_she_was_up_before_dawn_and_running_through_the_house(self):
        self.Shannon_Fitzgerald.appearance.append('running through the house')
    def she_and_her_brother_had_little_interest_in_television(self):
        self.Shannon_Fitzgerald.relations['brother'] = 'Jack_Fitzgerald'
        self.Jack_Fitzgerald.relations['sister'] = 'Shannon_Fitzgerald'
        self.Shannon_Fitzgerald.relations['little interest in television'] = 'Jack_Fitzgerald'
    def he_suspected_that_their_mother_was_mostly_responsible_for_that(self):
        self.Richard_Kane.relations['mother'] = 'Olivia_Kane'
        self.Olivia_Kane.relations['father'] = 'Richard_Kane'
        self.Olivia_Kane.relations['little interest in television'] = 'Jack_Fitzgerald'
        self.Olivia_Kane.relations['little interest in television'] = 'Shannon_Fitzgerald'
    def olivia_rarely_watched_any_shows_with_them_in_front_of_the_screen_and_their_father_didn_not_bother_trying_to_convince_her_otherwise(self):
        pass
    def he_rose_from_his_seat_at_the_table_with_a_sigh_and_glanced_around_the_room(self):
        pass
    def he_spotted_his_wife_by_one_of_the_large_picture_windows_staring_out_at_the_backyard_with_a_pensive_expression_on_her_face(self):
        self.Richard_Kane.relations['wife'] = 'Olivia_Kane'
        self.Olivia_Kane.relations['husband'] = 'Richard_Kane'
    def she_hadn_not_moved_since_he_had_last_spoken_to_her_an_hour_ago_at_least(self):
        pass
    def he_moved_towards_her_and_touched_her_shoulder_then_turned_towards_their_youngest_child(self):
        self.Richard_Kane.relations['youngest child'] = 'Jack_Fitzgerald'
        self.Jack_Fitzgerald.relations['father'] = 'Richard_Kane'
        self.Jack_Fitzgerald.relations['youngest child'] = 'Richard_Kane'
    def bring_jack_into_your_room_he_said_quietly_before_returning_his_attention_to_olivia(self):
        self.Richard_Kane.relations['bedroom'] = 'Olivia_Kane'
        self.Olivia_Kane.relations['bedroom'] = 'Richard_Kane'
    def she_turned_to_him_slowly_nodding_without_a_word_before_heading_towards_their_son_s_bedroom_with_jack_trotting_behind_her_cheerfully(self):
        self.Olivia_Kane.relations['son'] = 'Jack_Fitzgerald'
        self.Jack_Fitzgerald.relations['mother'] = 'Olivia_Kane'

## Create a world model state to track each character's appearance, personality, and relations with other characters.

