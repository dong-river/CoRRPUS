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
        self.Lettie_Hanson = character('Lettie Hanson')
        self.Bob_Hanson = character('Bob Hanson')
        self.Karen_Hanson = character('Karen Hanson')

    def story(self):
        self.karen_hanson_sat_in_the_kitchen_of_her_home_and_wondered_if_there_was_anything_that_could_snap_her_out_of_her_depression()
        self.she_had_just_lost_her_husband_and_it_seemed_as_if_everything_she_had_ever_known_was_gone()
        self.lettie_her_mother_was_also_suffering_from_grief_because_she_had_lost_the_one_person_she_loved_more_than_anything_else_in_the_world()
        self.lettie_would_have_been_one_hundred_years_old_next_week()
        self.she_had_lived_a_long_life_but_bob_s_death_felt_like_the_last_thing_left_to_live_for()
        self.lettie_cried_often_especially_when_karen_took_andrew_and_robbie_to_visit_their_graves_every_sunday()
        self.that_morning_karen_woke_up_to_see_that_it_was_a_beautiful_day_outside_as_usual()
        self.it_always_seemed_as_if_the_sky_above_their_town_was_unendingly_blue_with_white_puffy_clouds_floating_around_in_it()
        self.they_rarely_got_rainy_days_or_snowy_days_there_never_seemed_to_be_any_threat_of_harsh_weather_at_all()
        self.this_perfect_weather_only_served_to_make_lettie_feel_even_worse_about_how_everything_worked_out_for_them_both_being_alive_without_bob()
        self.karen_felt_herself_sink_into_despair_every_time_she_looked_out_of_her_window_and_realized_how_awful_life_was_without_bob_there_to_share_it_with_them_all()
    def karen_hanson_sat_in_the_kitchen_of_her_home_and_wondered_if_there_was_anything_that_could_snap_her_out_of_her_depression(self):
        self.Karen_Hanson.gender.append('female')
    def she_had_just_lost_her_husband_and_it_seemed_as_if_everything_she_had_ever_known_was_gone(self):
        self.Karen_Hanson.relations['husband'] = 'Bob_Hanson'
        self.Bob_Hanson.relations['wife'] = 'Karen_Hanson'
        self.Bob_Hanson.gender.append('male')
    def lettie_her_mother_was_also_suffering_from_grief_because_she_had_lost_the_one_person_she_loved_more_than_anything_else_in_the_world(self):
        self.Karen_Hanson.relations['mother'] = 'Lettie_Hanson'
        self.Lettie_Hanson.relations['daughter'] = 'Karen_Hanson'
        self.Lettie_Hanson.gender.append('female')
    def lettie_would_have_been_one_hundred_years_old_next_week(self):
        self.Lettie_Hanson.age.append('old')
    def she_had_lived_a_long_life_but_bob_s_death_felt_like_the_last_thing_left_to_live_for(self):
        pass
    def lettie_cried_often_especially_when_karen_took_andrew_and_robbie_to_visit_their_graves_every_sunday(self):
        self.Lettie_Hanson.relations['grandchildren'] = ['Andrew','Robbie']
        self.Karen_Hanson.relations['children'] = ['Andrew','Robbie']
    def that_morning_karen_woke_up_to_see_that_it_was_a_beautiful_day_outside_as_usual(self):
        pass
    def it_always_seemed_as_if_the_sky_above_their_town_was_unendingly_blue_with_white_puffy_clouds_floating_around_in_it(self):
        pass
    def they_rarely_got_rainy_days_or_snowy_days_there_never_seemed_to_be_any_threat_of_harsh_weather_at_all(self):
        pass
    def this_perfect_weather_only_served_to_make_lettie_feel_even_worse_about_how_everything_worked_out_for_them_both_being_alive_without_bob(self):
        pass
    def karen_felt_herself_sink_into_despair_every_time_she_looked_out_of_her_window_and_realized_how_awful_life_was_without_bob_there_to_share_it_with_them_all(self):
        pass
    
## Create a world model state to track each character's appearance, personality, and relations with other characters.

