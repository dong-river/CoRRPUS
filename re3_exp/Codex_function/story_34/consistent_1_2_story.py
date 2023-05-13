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
        self.Will_Trenton = character('Will Trenton')
        self.Amanda_Wilkinson = character('Amanda Wilkinson')
        self.Thomas_Watkins = character('Thomas Watkins')

    def story(self):
        self.thomas_watkins_squinted_as_he_surveyed_the_darkness_surrounding_the_small_town()
        self.he_and_his_team_had_been_in_place_for_almost_twenty_four_hours_so_they_were_all_getting_tired()
        self.they_d_searched_the_town_thoroughly_but_they_hadn_not_been_able_to_find_any_sign_of_the_killer()
        self.it_was_driving_them_crazy_but_there_wasn_not_much_they_could_do_except_watch_and_wait()
        self.thomas_was_a_big_man_with_brown_hair_and_brown_eyes()
        self.he_stood_at_6_2_and_had_a_muscular_build()
        self.he_normally_worked_as_a_construction_worker_but_he_also_moonlighted_as_a_mercenary_on_nights_like_this_one()
        self.his_skills_were_in_high_demand_among_local_towns_that_needed_help_protecting_themselves_from_violent_criminals_or_people_that_wanted_to_invade_their_territory_or_business_interests()
        self.thomas_was_armed_with_a_357_magnum_revolver_an_m_16_machine_gun_grenades_and_an_uzi_machine_pistol()
        self.he_looked_over_at_his_young_partner_will_trenton_and_nodded_toward_the_main_street_of_town_in_front_of_them()
        self.we_should_probably_start_taking_shifts()
        self.he_let_out_a_frustrated_sigh()
        self.there_s_no_way_we_re_going_to_get_any_sleep_tonight()
        self.will_nodded_his_agreement()
        self.okay()
    def thomas_watkins_squinted_as_he_surveyed_the_darkness_surrounding_the_small_town(self):
        pass
    def he_and_his_team_had_been_in_place_for_almost_twenty_four_hours_so_they_were_all_getting_tired(self):
        pass
    def they_d_searched_the_town_thoroughly_but_they_hadn_not_been_able_to_find_any_sign_of_the_killer(self):
        pass
    def it_was_driving_them_crazy_but_there_wasn_not_much_they_could_do_except_watch_and_wait(self):
        pass
    def thomas_was_a_big_man_with_brown_hair_and_brown_eyes(self):
        self.Thomas_Watkins.appearance.append('big')
        self.Thomas_Watkins.appearance.append('brown hair')
        self.Thomas_Watkins.appearance.append('brown eyes')
    def he_stood_at_6_2_and_had_a_muscular_build(self):
        pass
    def he_normally_worked_as_a_construction_worker_but_he_also_moonlighted_as_a_mercenary_on_nights_like_this_one(self):
        self.Thomas_Watkins.occupation.append('construction worker')
        self.Thomas_Watkins.occupation.append('mercenary')
    def his_skills_were_in_high_demand_among_local_towns_that_needed_help_protecting_themselves_from_violent_criminals_or_people_that_wanted_to_invade_their_territory_or_business_interests(self):
        pass
    def thomas_was_armed_with_a_357_magnum_revolver_an_m_16_machine_gun_grenades_and_an_uzi_machine_pistol(self):
        pass
    def he_looked_over_at_his_young_partner_will_trenton_and_nodded_toward_the_main_street_of_town_in_front_of_them(self):
        self.Thomas_Watkins.relations['partner'] = 'Will_Trenton'
        self.Will_Trenton.relations['partner'] = 'Thomas_Watkins'
    def we_should_probably_start_taking_shifts(self):
        pass
    def he_let_out_a_frustrated_sigh(self):
        pass
    def there_s_no_way_we_re_going_to_get_any_sleep_tonight(self):
        pass
    def will_nodded_his_agreement(self):
        pass
    def okay(self):
        pass

## Create a world model state to track each character's appearance, personality, and relations with other characters.

