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
        self.Shannon_Mulaney = character('Shannon Mulaney')
        self.Jess_Abernathy = character('Jess Abernathy')
        self.Olivia_Kendall = character('Olivia Kendall')

    def story(self):
        self.shannon_mulaney_looked_out_her_bedroom_window_at_the_dark_sky()
        self.a_storm_was_coming_and_shannon_knew_that_there_would_be_a_tornado_warning_in_her_town_tomorrow()
        self.she_also_knew_that_her_mom_wasn_not_going_to_listen_to_the_warning_and_stay_home()
        self.shannon_turned_away_from_the_window_and_sighed_as_she_looked_around_her_room()
        self.she_was_about_to_turn_20_years_old_and_here_she_was_still_living_with_her_mom_in_a_small_town_in_upstate_new_york()
        self.her_mom_hadn_not_let_go_of_life_after_losing_shannon_s_dad_when_shannon_was_9_so_she_kept_busy_going_here_and_there_until_late_at_night_rarely_taking_care_of_shannon()
        self.there_were_days_that_shannon_felt_like_nobody_wanted_her_around_except_for_jess_abernathy_who_had_been_appointed_as_an_official_university_staff_member_at_xyz_university_to_be_assigned_as_an_ra_resident_assistant_in_a_dormitory_suite_named_sky_house()
        self.while_jess_had_barely_known_this_girl_she_seemed_so_lonely_but_just_not_willing_to_talk_about_it_or_anything_else_really_as_a_friend_it_was_tough_to_watch_your_best_friend_face_the_loss_of_their_parent_over_many_years_go_by_without_doing_anything_about_it_or_trying_to_change_things()
    def shannon_mulaney_looked_out_her_bedroom_window_at_the_dark_sky(self):
        pass
    def a_storm_was_coming_and_shannon_knew_that_there_would_be_a_tornado_warning_in_her_town_tomorrow(self):
        pass
    def she_also_knew_that_her_mom_wasn_not_going_to_listen_to_the_warning_and_stay_home(self):
        pass
    def shannon_turned_away_from_the_window_and_sighed_as_she_looked_around_her_room(self):
        pass
    def she_was_about_to_turn_20_years_old_and_here_she_was_still_living_with_her_mom_in_a_small_town_in_upstate_new_york(self):
        self.Shannon_Mulaney.age.append('20')
        self.Shannon_Mulaney.relations['mom'] = 'Shannon_Mulaney'
    def her_mom_hadn_not_let_go_of_life_after_losing_shannon_s_dad_when_shannon_was_9_so_she_kept_busy_going_here_and_there_until_late_at_night_rarely_taking_care_of_shannon(self):
        self.Shannon_Mulaney.relations['dad'] = 'Shannon_Mulaney'
    def there_were_days_that_shannon_felt_like_nobody_wanted_her_around_except_for_jess_abernathy_who_had_been_appointed_as_an_official_university_staff_member_at_xyz_university_to_be_assigned_as_an_ra_resident_assistant_in_a_dormitory_suite_named_sky_house(self):
        self.Shannon_Mulaney.relations['jess_abernathy'] = 'Jess_Abernathy'
        self.Jess_Abernathy.relations['shannon_mulaney'] = 'Shannon_Mulaney'
    def while_jess_had_barely_known_this_girl_she_seemed_so_lonely_but_just_not_willing_to_talk_about_it_or_anything_else_really_as_a_friend_it_was_tough_to_watch_your_best_friend_face_the_loss_of_their_parent_over_many_years_go_by_without_doing_anything_about_it_or_trying_to_change_things(self):
        self.Shannon_Mulaney.relations['best_friend'] = 'Jess_Abernathy'
        self.Jess_Abernathy.relations['best_friend'] = 'Shannon_Mulaney'
        
# Create a world model state to track each character's appearance, personality, and relations with other characters.
