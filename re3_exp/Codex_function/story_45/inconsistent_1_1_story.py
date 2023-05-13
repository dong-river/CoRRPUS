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
        self.Nina_Harman = character('Nina Harman')
        self.Jake_Ryan = character('Jake Ryan')
        self.Karen_Hartman = character('Karen Hartman')

    def story(self):
        self.karen_hartman_sat_on_her_bed_absentmindedly_picking_at_a_loose_thread_in_the_bedspread()
        self.she_watched_nina_work_away_on_a_school_project_scowling_at_the_pieces_of_paper_nina_was_spread_out_on_her_bed()
        self.it_was_late_afternoon_and_karen_wanted_to_just_lay_back_and_relax_for_a_few_minutes_before_she_went_home()
        self.instead_she_was_stuck_in_her_room_helping_her_friend_who_wasn_not_exactly_an_expert_when_it_came_to_organization()
        self.nina_paused_in_her_work_and_looked_up_at_karen()
        self.is_something_wrong()
        self.no()
        self.i_m_fine()
        self.karen_lied()
        self.nina_didn_not_fall_for_it()
        self.don_not_lie_to_me()
        self.she_said_flatly_before_getting_up_and_turning_away_from_karen_so_that_she_couldn_not_see_the_hurt_in_her_eyes()
        self.it_s_about_the_fifth_time_you_ve_gotten_off_my_bed_today()
        self.there_was_a_long_silence_before_nina_continued_to_speak_again_without_turning_around()
        self.if_you_want_me_to_leave_you_alone_just_say_so()
        self.her_voice_was_barely_above_a_whisper_as_tears_stung_her_eyes()
    def karen_hartman_sat_on_her_bed_absentmindedly_picking_at_a_loose_thread_in_the_bedspread(self):
        pass
    def she_watched_nina_work_away_on_a_school_project_scowling_at_the_pieces_of_paper_nina_was_spread_out_on_her_bed(self):
        self.Nina_Harman.relations['friend'] = 'Karen_Hartman'
        self.Karen_Hartman.relations['friend'] = 'Nina_Harman'
    def it_was_late_afternoon_and_karen_wanted_to_just_lay_back_and_relax_for_a_few_minutes_before_she_went_home(self):
        pass
    def instead_she_was_stuck_in_her_room_helping_her_friend_who_wasn_not_exactly_an_expert_when_it_came_to_organization(self):
        pass
    def nina_paused_in_her_work_and_looked_up_at_karen(self):
        pass
    def is_something_wrong(self):
        pass
    def no(self):
        pass
    def i_m_fine(self):
        pass
    def karen_lied(self):
        pass
    def nina_didn_not_fall_for_it(self):
        pass
    def don_not_lie_to_me(self):
        pass
    def she_said_flatly_before_getting_up_and_turning_away_from_karen_so_that_she_couldn_not_see_the_hurt_in_her_eyes(self):
        pass
    def it_s_about_the_fifth_time_you_ve_gotten_off_my_bed_today(self):
        pass
    def there_was_a_long_silence_before_nina_continued_to_speak_again_without_turning_around(self):
        pass
    def if_you_want_me_to_leave_you_alone_just_say_so(self):
        pass
    def her_voice_was_barely_above_a_whisper_as_tears_stung_her_eyes(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

