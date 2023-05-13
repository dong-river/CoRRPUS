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
        self.Karen_Smith = character('Karen Smith')
        self.Janice_Smith = character('Janice Smith')
        self.Leah_White = character('Leah White')

    def story(self):
        self.leah_white_waited_impatiently_for_her_granddaughter_karen_to_arrive()
        self.as_she_peered_through_the_curtains_of_her_small_living_room_window_she_spotted_a_familiar_car_making_its_way_down_the_driveway()
        self.she_smiled_her_karen_was_home()
        self.hi_grandma_karen_said_as_she_came_in_through_the_door()
        self.leah_came_out_from_behind_the_sofa_and_hugged_her_beloved_granddaughter_warmly()
        self.karen_you_are_so_pretty()
        self.what_happened_to_that_little_thing_who_used_to_play_barbies_with_me()
        self.and_what_are_you_doing_with_all_those_bags()
        self.you_re_going_on_a_trip_karen_sat_down_and_began_pulling_items_out_of_the_bags_while_answering_her_grandmother_s_questions()
        self.yeah_it_s_too_much_trouble_to_take_all_my_textbooks_to_school_i_get_there_too_early_anyhow()
        self.so_i_decided_to_buy_them_online_this_semester()
        self.and_i_was_just_about_to_walk_into_wal_mart_for_a_few_things_for_mom_she_asked_me_last_night_when_dad_called_me_and_told_me_he_wanted_me_to_pick_up_some_things_at_sam_s_club_today_instead_of_going_there_today()
    def leah_white_waited_impatiently_for_her_granddaughter_karen_to_arrive(self):
        self.Leah_White.relations['granddaughter'] = 'Karen_Smith'
        self.Karen_Smith.relations['grandmother'] = 'Leah_White'

    def as_she_peered_through_the_curtains_of_her_small_living_room_window_she_spotted_a_familiar_car_making_its_way_down_the_driveway(self):
        pass

    def she_smiled_her_karen_was_home(self):
        pass

    def hi_grandma_karen_said_as_she_came_in_through_the_door(self):
        pass

    def leah_came_out_from_behind_the_sofa_and_hugged_her_beloved_granddaughter_warmly(self):
        pass

    def karen_you_are_so_pretty(self):
        pass

    def what_happened_to_that_little_thing_who_used_to_play_barbies_with_me(self):
        self.Karen_Smith.relations['barbie'] = 'Leah_White'
        self.Leah_White.relations['barbie'] = 'Karen_Smith'

    def and_what_are_you_doing_with_all_those_bags(self):
        pass

    def you_re_going_on_a_trip_karen_sat_down_and_began_pulling_items_out_of_the_bags_while_answering_her_grandmother_s_questions(self):
        pass

    def yeah_it_s_too_much_trouble_to_take_all_my_textbooks_to_school_i_get_there_too_early_anyhow(self):
        pass

    def so_i_decided_to_buy_them_online_this_semester(self):
        pass

    def and_i_was_just_about_to_walk_into_wal_mart_for_a_few_things_for_mom_she_asked_me_last_night_when_dad_called_me_and_told_me_he_wanted_me_to_pick_up_some_things_at_sam_s_club_today_instead_of_going_there_today(self):
        self.Karen_Smith.relations['mom'] = 'Janice_Smith'
        self.Janice_Smith.relations['daughter'] = 'Karen_Smith'

## Create a world model state to track each character's appearance, personality, and relations with other characters.

